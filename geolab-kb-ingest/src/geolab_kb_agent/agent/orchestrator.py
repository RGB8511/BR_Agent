"""Agent orchestrator: manages the Claude tool-use loop."""

from __future__ import annotations

import json
import logging
import re
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from typing import Any

import anthropic
from sqlalchemy import Engine

from geolab_kb_agent.confidence import ConfidenceLevel, ConfidenceScore, compute_confidence
from geolab_kb_ingest.embedder import Embedder

from .provenance import ProvenanceCollector
from .system_prompt import get_system_prompt
from .temporal import detect_temporal_intent
from .tool_handlers import HandlerFn, make_tool_handlers
from .tools import TOOLS

logger = logging.getLogger(__name__)

MAX_ITERATIONS = 10


@dataclass
class AgentResponse:
    """Final response from the agent."""

    text: str
    sources: list[dict]
    tool_calls_made: int = 0
    confidence: ConfidenceScore | None = None


@dataclass
class KBAgent:
    """Orchestrates the Claude tool-use loop against the KB.

    Supports injecting extra tools (e.g. project database queries) via
    ``extra_tools`` / ``extra_handlers`` so the host application can extend
    the agent's capabilities without modifying this package.
    """

    api_key: str
    model: str
    engine: Engine
    embedder: Embedder
    mode: str = "educational"
    extra_tools: list[dict] = field(default_factory=list)
    extra_handlers: dict[str, HandlerFn] = field(default_factory=dict)
    _client: anthropic.AsyncAnthropic = field(init=False, repr=False)
    _handlers: dict[str, HandlerFn] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._client = anthropic.AsyncAnthropic(api_key=self.api_key)
        self._handlers = make_tool_handlers(self.engine, self.embedder)
        # Merge any extra handlers provided by the host application
        if self.extra_handlers:
            self._handlers.update(self.extra_handlers)

    # ------------------------------------------------------------------
    # Shared helpers
    # ------------------------------------------------------------------

    def _all_tools(self) -> list[dict]:
        """Return merged KB tools + any extra tools."""
        if self.extra_tools:
            return TOOLS + self.extra_tools
        return TOOLS

    @staticmethod
    def _compute_confidence(provenance: ProvenanceCollector) -> ConfidenceScore:
        """Compute confidence from provenance similarity scores."""
        scores = [
            c.score for c in provenance.citations if c.score is not None
        ]
        return compute_confidence(scores)

    @staticmethod
    def _uncertainty_prefix(confidence: ConfidenceScore) -> str:
        """Return an uncertainty instruction to inject before the final LLM call."""
        if confidence.level == ConfidenceLevel.MEDIUM:
            return (
                "This response draws from multiple sources. "
                "Note any areas of uncertainty.\n\n"
            )
        if confidence.level == ConfidenceLevel.LOW:
            return (
                "This response synthesizes across several documents. "
                "Encourage the user to verify against cited sources.\n\n"
            )
        return ""

    @staticmethod
    def _temporal_hint(user_message: str) -> str | None:
        """Detect temporal intent and return a hint string, or None."""
        tq = detect_temporal_intent(user_message)
        if not tq.is_temporal:
            return None

        parts = [f"[Temporal context: intent={tq.intent.value}"]
        if tq.year_range:
            parts.append(f"year_range={tq.year_range[0]}-{tq.year_range[1]}")
        elif tq.years:
            parts.append(f"years={','.join(str(y) for y in tq.years)}")
        parts_str = ", ".join(parts) + ". Use year_min/year_max filters in search_kb.]"
        logger.info("Temporal query detected: %s", parts_str)
        return parts_str

    @staticmethod
    def _extract_usage(response: anthropic.types.Message) -> dict:
        """Extract token usage dict from an API response."""
        u = response.usage
        return {
            "input_tokens": u.input_tokens,
            "output_tokens": u.output_tokens,
            "cache_creation_input_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
            "cache_read_input_tokens": getattr(u, "cache_read_input_tokens", 0) or 0,
        }

    def _log_usage(self, response: anthropic.types.Message) -> None:
        """Log token usage including cache metrics."""
        u = self._extract_usage(response)
        logger.debug(
            "API usage: in=%d out=%d cache_create=%d cache_read=%d",
            u["input_tokens"],
            u["output_tokens"],
            u["cache_creation_input_tokens"],
            u["cache_read_input_tokens"],
        )

    @staticmethod
    def _build_references(
        text: str, provenance: ProvenanceCollector,
    ) -> tuple[str, str]:
        """Rewrite inline citations and build a grouped references section.

        Returns (rewritten_text, references_block).
        - Chunks from the same document share a number: [1a], [1b], …
        - Single-chunk documents use plain [1].
        """

        def _clean(val: str) -> str:
            return " ".join(val.split()) if val else ""

        # Filename format: doc{NN}_{author}_{year}_{desc}.pdf
        _FILENAME_RE = re.compile(
            r"^doc\d+_([a-z]+)_(\d{4})_(.+)\.pdf$", re.IGNORECASE,
        )

        # Author abbreviations found in filenames
        _AUTHOR_MAP: dict[str, str] = {
            "wsrb": "Western States Reclamation Bureau",
            "idse": "Intermountain Dam Safety Engineers, LLC",
            "fhsc": "Cascade Dam Safety Consultants",
            "sdwr": "State Division of Water Resources",
            "jbid": "Juniper Basin Irrigation District",
        }

        def _parse_filename(fn: str) -> tuple[str, str, str]:
            """Extract (author, year, title) from a structured filename.

            Returns empty strings for any field that cannot be parsed.
            """
            m = _FILENAME_RE.match(fn)
            if not m:
                return "", "", ""
            abbrev, year, desc = m.group(1), m.group(2), m.group(3)
            author = _AUTHOR_MAP.get(abbrev.lower(), "")
            title = desc.replace("_", " ").title()
            return author, year, title

        def _is_garbled(val: str) -> bool:
            """Heuristic: detect garbled interleaved-text titles."""
            if not val:
                return False
            # Only examine alphabetic characters to avoid dilution
            # from spaces, commas, digits etc.
            alpha = [c for c in val if c.isalpha()]
            if len(alpha) < 6:
                return False
            switches = sum(
                1 for a, b in zip(alpha, alpha[1:])
                if (a.isupper() and b.islower()) or (a.islower() and b.isupper())
            )
            ratio = switches / max(len(alpha) - 1, 1)
            return ratio > 0.3

        def _is_bad_date(val: str) -> bool:
            """Detect non-date values like 'Idaho 8362' or 'Clear\\n5195'."""
            if not val:
                return True
            # Good dates contain month names or just a year
            val_lower = val.lower()
            if re.match(r"^\d{4}$", val.strip()):
                return False
            months = {
                "jan", "feb", "mar", "apr", "may", "jun",
                "jul", "aug", "sep", "oct", "nov", "dec",
            }
            return not any(m in val_lower for m in months)

        def _project_citation(meta: dict, fallback_title: str) -> str:
            """Build a clean citation string for a project document."""
            filename = _clean(meta.get("filename", ""))
            fn_author, fn_year, fn_title = _parse_filename(filename)

            raw_title = _clean(meta.get("title", fallback_title))
            raw_author = _clean(meta.get("author", ""))
            raw_date = _clean(meta.get("date", ""))
            project = _clean(meta.get("project", ""))
            pages = _clean(meta.get("page_range", ""))

            # Use filename-derived values when metadata is garbled
            title = fn_title if _is_garbled(raw_title) else raw_title
            author = raw_author if raw_author else fn_author
            date = raw_date if not _is_bad_date(raw_date) else fn_year

            parts: list[str] = []
            if author:
                parts.append(f"{author},")
            if title:
                parts.append(f'"{title},"')
            if project:
                parts.append(f"{project},")
            if date:
                parts.append(f"{date}.")
            if pages:
                parts.append(f"pp. {pages}.")
            if filename:
                parts.append(f"({filename})")
            return " ".join(parts) if parts else filename or "Unknown source"

        # Accept both [Source N] and [N] from the model
        cited = sorted(
            set(int(m) for m in re.findall(r"\[(?:Source\s+)?(\d+)\]", text))
        )
        if not cited:
            return text, ""

        # Deduplicate provenance into ordered list (1-based index = source N)
        seen: set[tuple[str, str]] = set()
        ordered: list = []
        for c in provenance.citations:
            key = (c.source_table, c.record_id)
            if key not in seen:
                seen.add(key)
                ordered.append(c)

        # --- Group cited chunks by document ---
        # Preserves first-seen order of documents.
        from collections import OrderedDict

        # doc_key -> list of (old_source_num, citation)
        doc_chunks: OrderedDict[str, list[tuple[int, Any]]] = OrderedDict()
        for n in cited:
            idx = n - 1
            if idx < 0 or idx >= len(ordered):
                continue
            c = ordered[idx]
            meta = c.metadata or {}
            filename = meta.get("filename", meta.get("source_file", ""))
            doc_key = filename if filename else f"{c.package_id}|{_clean(c.value or '')}"
            doc_chunks.setdefault(doc_key, []).append((n, c))

        if not doc_chunks:
            return text, ""

        # --- Assign new labels ---
        # old_num -> new_label  (e.g. 3 -> "1b")
        label_map: dict[int, str] = {}
        # For building the references section
        doc_entries: list[tuple[str, Any, list[tuple[str, Any]]]] = []

        doc_num = 0
        for _doc_key, chunk_list in doc_chunks.items():
            doc_num += 1
            multi = len(chunk_list) > 1
            sub_items: list[tuple[str, Any]] = []
            for i, (old_num, c) in enumerate(chunk_list):
                if multi:
                    letter = chr(ord("a") + i) if i < 26 else str(i + 1)
                    new_label = f"{doc_num}{letter}"
                else:
                    new_label = str(doc_num)
                label_map[old_num] = new_label
                sub_items.append((new_label, c))
            # Use the first citation's metadata for the document-level entry
            doc_entries.append((str(doc_num), chunk_list[0][1], sub_items))

        # --- Rewrite inline citations in text ---
        def _replace_cite(m: re.Match) -> str:
            n = int(m.group(1))
            new = label_map.get(n)
            return f"[{new}]" if new else m.group(0)

        rewritten = re.sub(r"\[(?:Source\s+)?(\d+)\]", _replace_cite, text)

        # --- Build references block ---
        lines = ["\n\n---\n\n## References\n"]
        for doc_label, rep_citation, sub_items in doc_entries:
            meta = rep_citation.metadata or {}

            if rep_citation.package_id and rep_citation.package_id.startswith("project:"):
                ref_text = _project_citation(meta, rep_citation.value or "")
            else:
                title = _clean(rep_citation.value or "")
                pkg = rep_citation.package_id or ""
                disc = rep_citation.discipline or ""
                ctype = rep_citation.chunk_type or ""
                parts = []
                if title:
                    parts.append(f'"{title},"')
                if pkg:
                    parts.append(f"*{pkg}*,")
                if disc:
                    parts.append(f"{disc.capitalize()}.")
                if ctype:
                    parts.append(f"({ctype}: `{rep_citation.record_id}`)")
                ref_text = " ".join(parts) if parts else rep_citation.record_id

            lines.append(f"**[{doc_label}]** {ref_text}")

            # Sub-items (only when multiple chunks from same doc)
            if len(sub_items) > 1:
                for sub_label, sc in sub_items:
                    sm = sc.metadata or {}
                    chunk_title = _clean(sc.value or "")
                    section = _clean(sm.get("section", ""))
                    ctype = sc.chunk_type or ""
                    doc_title = _clean(meta.get("title", ""))

                    # Build a concise sub-description
                    desc = ""
                    if ctype == "table" and section and not _is_garbled(section):
                        desc = f"Table: {section}"
                    elif ctype == "table":
                        desc = "Table"
                    elif ctype == "equation" and section:
                        desc = f"Eq: {section}"
                    elif section and not _is_garbled(section):
                        desc = section
                    elif chunk_title and chunk_title != doc_title and not _is_garbled(chunk_title):
                        desc = chunk_title
                    else:
                        # Use first ~80 chars of snippet as fallback, but
                        # only if it's not garbled
                        snippet = _clean(sc.snippet or "")[:80]
                        if snippet and not _is_garbled(snippet):
                            desc = f'"{snippet}..."'
                        else:
                            # Fall back to chunk type + index from chunk ID
                            chunk_suffix = sc.record_id.rsplit(".", 1)[-1] if sc.record_id else ""
                            desc = f"{ctype or 'section'} {chunk_suffix}".strip()
                    lines.append(f"  - [{sub_label}] {desc}")

            lines.append("")  # blank line between entries

        return rewritten, "\n".join(lines)

    async def _execute_tools(
        self,
        tool_use_blocks: list,
        provenance: ProvenanceCollector,
    ) -> tuple[list[dict[str, Any]], int]:
        """Execute tool calls and return (tool_results, count)."""
        tool_results: list[dict[str, Any]] = []
        count = 0
        for block in tool_use_blocks:
            count += 1
            logger.info(
                "Tool call: %s | args=%s",
                block.name,
                json.dumps(block.input, default=str)[:500],
            )
            handler = self._handlers.get(block.name)
            if handler is None:
                result_content = json.dumps(
                    {"error": f"Unknown tool: {block.name}"}
                )
            else:
                try:
                    result = await handler(block.input, provenance)
                    result_content = json.dumps(result, default=str)
                    # Log result summary for debugging
                    result_count = result.get("count", "?") if isinstance(result, dict) else "?"
                    logger.info(
                        "Tool result: %s | count=%s | size=%d chars",
                        block.name,
                        result_count,
                        len(result_content),
                    )
                except Exception:
                    logger.exception("Tool %s failed", block.name)
                    result_content = json.dumps(
                        {"error": "Tool execution failed"}
                    )
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result_content,
                }
            )
        return tool_results, count

    @staticmethod
    def _summarize_tool_result(tool_name: str, result: dict) -> list[dict]:
        """Extract chunk summaries from a tool result for SSE events."""
        if not isinstance(result, dict):
            return []

        # search_kb returns {"results": [...]}, lookup_* return {"result": {...}}
        chunks: list[dict] = []
        if "results" in result:
            chunks = result["results"]
        elif "result" in result and isinstance(result["result"], dict):
            chunks = [result["result"]]

        if not chunks:
            return []

        return [
            {
                "id": c.get("id", ""),
                "title": c.get("title", ""),
                "package_id": c.get("package_id", ""),
                "discipline": c.get("discipline", ""),
                "chunk_type": c.get("chunk_type", ""),
                "score": round(c.get("score", 0), 4),
                "snippet": (c.get("content", "") or "")[:150],
            }
            for c in chunks[:10]
        ]

    # ------------------------------------------------------------------
    # Non-streaming chat (backwards compatible)
    # ------------------------------------------------------------------

    async def chat(
        self,
        user_message: str,
        messages: list[dict[str, Any]] | None = None,
    ) -> AgentResponse:
        """Run the agent loop and return a final text response with citations."""
        provenance = ProvenanceCollector()

        if messages is None:
            messages = []

        # Detect temporal intent and augment the user message
        temporal_hint = self._temporal_hint(user_message)
        if temporal_hint:
            messages.append({
                "role": "user",
                "content": f"{user_message}\n\n{temporal_hint}",
            })
        else:
            messages.append({"role": "user", "content": user_message})
        logger.info("Agent chat: %s", user_message[:200])

        tool_calls_made = 0
        system = get_system_prompt(self.mode)
        all_tools = self._all_tools()

        for _iteration in range(MAX_ITERATIONS):
            response = await self._client.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=0.0,
                system=system,
                tools=all_tools,
                messages=messages,
            )
            self._log_usage(response)

            tool_use_blocks = [
                block for block in response.content if block.type == "tool_use"
            ]

            if not tool_use_blocks:
                # Final text response
                text_parts = [
                    block.text
                    for block in response.content
                    if block.type == "text"
                ]
                final_text = "\n".join(text_parts)

                if tool_calls_made == 0:
                    final_text = (
                        "> **Note:** This response was generated without searching the "
                        "knowledge base and may not be accurate.\n\n" + final_text
                    )

                # Rewrite citations and append references section
                final_text, refs = self._build_references(final_text, provenance)
                final_text += refs

                # Append assistant reply to history for multi-turn
                messages.append({"role": "assistant", "content": final_text})

                sources = provenance.to_grouped_chunks()
                confidence = self._compute_confidence(provenance)
                logger.info(
                    "Agent response: %d chars, %d tool calls, %d sources, confidence=%s",
                    len(final_text),
                    tool_calls_made,
                    len(sources),
                    confidence.level.value,
                )

                return AgentResponse(
                    text=final_text,
                    sources=sources,
                    tool_calls_made=tool_calls_made,
                    confidence=confidence,
                )

            # Append assistant message with tool_use blocks
            messages.append({"role": "assistant", "content": response.content})

            # Execute tools
            tool_results, count = await self._execute_tools(
                tool_use_blocks, provenance
            )
            tool_calls_made += count
            messages.append({"role": "user", "content": tool_results})

        # Exceeded max iterations
        fallback = (
            "I was unable to complete your request within the allowed "
            "number of steps. Please try a more specific question."
        )
        messages.append({"role": "assistant", "content": fallback})
        return AgentResponse(
            text=fallback,
            sources=provenance.to_grouped_chunks(),
            tool_calls_made=tool_calls_made,
            confidence=self._compute_confidence(provenance),
        )

    # ------------------------------------------------------------------
    # Streaming chat (SSE)
    # ------------------------------------------------------------------

    async def chat_stream(
        self,
        user_message: str,
        messages: list[dict[str, Any]] | None = None,
    ) -> AsyncIterator[dict[str, Any]]:
        """Async generator that yields SSE-ready dicts.

        Strategy:
        1. Run tool iterations with non-streaming messages.create()
        2. When the final (no tool_use) response is detected, discard it
        3. Re-issue the same call via messages.stream() for text chunks
        4. Yield text chunks as they arrive
        """
        provenance = ProvenanceCollector()

        if messages is None:
            messages = []

        # Detect temporal intent and augment the user message
        temporal_hint = self._temporal_hint(user_message)
        if temporal_hint:
            messages.append({
                "role": "user",
                "content": f"{user_message}\n\n{temporal_hint}",
            })
        else:
            messages.append({"role": "user", "content": user_message})
        logger.info("Agent chat_stream: %s", user_message[:200])

        tool_calls_made = 0
        system = get_system_prompt(self.mode)
        all_tools = self._all_tools()
        token_steps: list[dict] = []

        yield {"type": "routing_started"}

        # --- Tool-use loop (non-streaming) ---
        final_found = False
        for _iteration in range(MAX_ITERATIONS):
            response = await self._client.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=0.0,
                system=system,
                tools=all_tools,
                messages=messages,
            )
            self._log_usage(response)
            step_usage = self._extract_usage(response)
            step_usage["step"] = f"tool_loop_{_iteration + 1}"
            token_steps.append(step_usage)

            tool_use_blocks = [
                block for block in response.content if block.type == "tool_use"
            ]

            if not tool_use_blocks:
                # Final response detected — discard and break to re-stream
                final_found = True
                break

            # Append assistant message
            messages.append({"role": "assistant", "content": response.content})

            # Execute tools inline with events (instead of _execute_tools)
            tool_results = []
            for block in tool_use_blocks:
                tool_calls_made += 1
                yield {
                    "type": "tool_call",
                    "tool_name": block.name,
                    "arguments": block.input,
                }

                handler = self._handlers.get(block.name)
                if handler is None:
                    result_content = json.dumps({"error": f"Unknown tool: {block.name}"})
                    yield {"type": "tool_result", "tool_name": block.name, "chunks": []}
                else:
                    try:
                        result = await handler(block.input, provenance)
                        result_content = json.dumps(result, default=str)
                        chunks = self._summarize_tool_result(block.name, result)
                        yield {"type": "tool_result", "tool_name": block.name, "chunks": chunks}
                    except Exception:
                        logger.exception("Tool %s failed", block.name)
                        result_content = json.dumps({"error": "Tool execution failed"})
                        yield {
                            "type": "tool_result",
                            "tool_name": block.name,
                            "chunks": [],
                            "error": "Tool execution failed",
                        }

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result_content,
                })
            messages.append({"role": "user", "content": tool_results})

        if not final_found:
            yield {
                "type": "error",
                "error": (
                    "Unable to complete within allowed steps. "
                    "Try a more specific question."
                ),
            }
            return

        # --- Compute confidence from retrieval scores ---
        confidence = self._compute_confidence(provenance)

        # --- Inject disclaimer if no tools were called ---
        if tool_calls_made == 0:
            messages.append({
                "role": "user",
                "content": (
                    "[System: You did not search the knowledge base. Remind the user "
                    "that this answer is from general knowledge, not the KB. Preface "
                    "your response with a disclaimer.]"
                ),
            })
        else:
            # Inject uncertainty prefix for MEDIUM/LOW confidence
            prefix = self._uncertainty_prefix(confidence)
            if prefix:
                messages.append({
                    "role": "user",
                    "content": f"[System: {prefix}]",
                })

        # --- Re-issue as streaming call ---
        yield {"type": "synthesis_started", "confidence": confidence.model_dump()}

        try:
            async with self._client.messages.stream(
                model=self.model,
                max_tokens=4096,
                temperature=0.0,
                system=system,
                tools=all_tools,
                messages=messages,
            ) as stream:
                full_text_parts: list[str] = []
                async for text_chunk in stream.text_stream:
                    full_text_parts.append(text_chunk)
                    yield {"type": "text", "text": text_chunk}

                final_message = await stream.get_final_message()
                self._log_usage(final_message)
                synth_usage = self._extract_usage(final_message)
                synth_usage["step"] = "synthesis"
                token_steps.append(synth_usage)

            raw_text = "".join(full_text_parts)

            # Rewrite citations and build references section
            final_text, refs = self._build_references(raw_text, provenance)

            # Emit the rewritten text as a replacement + refs
            # Since we already streamed the original text, emit a
            # special event with the full rewritten text + refs so
            # the frontend can replace the content.
            if final_text != raw_text or refs:
                yield {"type": "rewrite", "rewrite": final_text + refs}

            final_text += refs

            # Append to conversation history for multi-turn
            messages.append({"role": "assistant", "content": final_text})

            sources = provenance.to_grouped_chunks()
            logger.info(
                "Stream response: %d chars, %d tool calls, %d sources, confidence=%s",
                len(final_text),
                tool_calls_made,
                len(sources),
                confidence.level.value,
            )

            yield {
                "type": "done",
                "done": True,
                "sources": sources,
                "confidence": confidence.model_dump(),
                "tool_calls_made": tool_calls_made,
                "token_usage": {
                    "steps": token_steps,
                    "model": self.model,
                },
            }

        except Exception:
            logger.exception("Streaming failed")
            yield {"type": "error", "error": "Streaming failed. Please try again."}
