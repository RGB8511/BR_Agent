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

from .provenance import ProvenanceCollector
from .system_prompt import get_system_prompt
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


@dataclass
class KBAgent:
    """Orchestrates the Claude tool-use loop against the KB."""

    api_key: str
    model: str
    engine: Engine
    embedder: Embedder
    mode: str = "educational"
    _client: anthropic.AsyncAnthropic = field(init=False, repr=False)
    _handlers: dict[str, HandlerFn] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._client = anthropic.AsyncAnthropic(api_key=self.api_key)
        self._handlers = make_tool_handlers(self.engine, self.embedder)

    # ------------------------------------------------------------------
    # Shared helpers
    # ------------------------------------------------------------------

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
            handler = self._handlers.get(block.name)
            if handler is None:
                result_content = json.dumps(
                    {"error": f"Unknown tool: {block.name}"}
                )
            else:
                try:
                    result = await handler(block.input, provenance)
                    result_content = json.dumps(result, default=str)
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
        messages.append({"role": "user", "content": user_message})

        tool_calls_made = 0
        system = get_system_prompt(self.mode)

        for _iteration in range(MAX_ITERATIONS):
            response = await self._client.messages.create(
                model=self.model,
                max_tokens=4096,
                system=system,
                tools=TOOLS,
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

                # Append assistant reply to history for multi-turn
                messages.append({"role": "assistant", "content": final_text})

                return AgentResponse(
                    text=final_text,
                    sources=provenance.to_list(),
                    tool_calls_made=tool_calls_made,
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
            sources=provenance.to_list(),
            tool_calls_made=tool_calls_made,
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
        messages.append({"role": "user", "content": user_message})

        tool_calls_made = 0
        system = get_system_prompt(self.mode)

        # --- Tool-use loop (non-streaming) ---
        final_found = False
        for _iteration in range(MAX_ITERATIONS):
            response = await self._client.messages.create(
                model=self.model,
                max_tokens=4096,
                system=system,
                tools=TOOLS,
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

        # --- Re-issue as streaming call ---
        try:
            async with self._client.messages.stream(
                model=self.model,
                max_tokens=4096,
                system=system,
                tools=TOOLS,
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

            yield {
                "done": True,
                "sources": provenance.to_list(),
                "tool_calls_made": tool_calls_made,
            }

        except Exception as exc:
            logger.exception("Streaming failed")
            yield {"error": f"Streaming failed: {exc}"}
