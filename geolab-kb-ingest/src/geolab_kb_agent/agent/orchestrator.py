"""Agent orchestrator: manages the Claude tool-use loop."""

from __future__ import annotations

import json
import logging
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from typing import Any

import anthropic
from sqlalchemy import Engine

from geolab_kb_ingest.embedder import Embedder

from geolab_kb_agent.confidence import ConfidenceLevel, ConfidenceScore, compute_confidence

from .provenance import ProvenanceCollector
from .system_prompt import get_system_prompt
from .temporal import TemporalIntent, detect_temporal_intent
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
                "IMPORTANT: Your confidence in this retrieval is moderate. "
                "Multiple sources scored similarly. Preface your answer with a brief note "
                "that you found relevant information but the user should verify critical values "
                "against the source documents.\n\n"
            )
        if confidence.level == ConfidenceLevel.LOW:
            return (
                "IMPORTANT: Your confidence in this retrieval is low. The sources may not "
                "directly address the question. Preface your answer with a clear statement "
                "that you have low confidence and recommend consulting source documents directly. "
                "Share what you found but flag uncertainty explicitly.\n\n"
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

    def _log_usage(self, response: anthropic.types.Message) -> None:
        """Log token usage including cache metrics."""
        u = response.usage
        cache_create = getattr(u, "cache_creation_input_tokens", 0) or 0
        cache_read = getattr(u, "cache_read_input_tokens", 0) or 0
        logger.debug(
            "API usage: in=%d out=%d cache_create=%d cache_read=%d",
            u.input_tokens,
            u.output_tokens,
            cache_create,
            cache_read,
        )

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
                except Exception as exc:
                    logger.exception("Tool %s failed", block.name)
                    result_content = json.dumps(
                        {"error": f"Tool execution failed: {exc}"}
                    )
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result_content,
                }
            )
        return tool_results, count

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

                # Append assistant reply to history for multi-turn
                messages.append({"role": "assistant", "content": final_text})

                sources = provenance.to_retrieved_chunks()
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
            sources=provenance.to_retrieved_chunks(),
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

            tool_use_blocks = [
                block for block in response.content if block.type == "tool_use"
            ]

            if not tool_use_blocks:
                # Final response detected — discard and break to re-stream
                final_found = True
                break

            # Append assistant + tool results for next iteration
            messages.append({"role": "assistant", "content": response.content})
            tool_results, count = await self._execute_tools(
                tool_use_blocks, provenance
            )
            tool_calls_made += count
            messages.append({"role": "user", "content": tool_results})

        if not final_found:
            yield {
                "error": (
                    "Unable to complete within allowed steps. "
                    "Try a more specific question."
                )
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
                    yield {"text": text_chunk}

                final_message = await stream.get_final_message()
                self._log_usage(final_message)

            final_text = "".join(full_text_parts)

            # Append to conversation history for multi-turn
            messages.append({"role": "assistant", "content": final_text})

            sources = provenance.to_retrieved_chunks()
            logger.info(
                "Stream response: %d chars, %d tool calls, %d sources, confidence=%s",
                len(final_text),
                tool_calls_made,
                len(sources),
                confidence.level.value,
            )

            yield {
                "done": True,
                "sources": sources,
                "confidence": confidence.model_dump(),
                "tool_calls_made": tool_calls_made,
            }

        except Exception as exc:
            logger.exception("Streaming failed")
            yield {"error": f"Streaming failed: {exc}"}
