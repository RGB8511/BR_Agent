"""Level 2 — Full KBAgent pipeline evaluation.

Calls KBAgent.chat() with each golden question and checks:
- answer_keywords appear in the response (keyword coverage >= 50%)
- tool_calls_made > 0 (agent actually searched the KB)

Costs Anthropic API tokens per question. Use sparingly.

Usage:
    DATABASE_URL="..." VOYAGE_API_KEY="..." ANTHROPIC_API_KEY="..." \
      uv run pytest tests/eval/test_agent.py -m "eval and agent" -v -s
"""

from __future__ import annotations

import asyncio
from collections.abc import Callable

import pytest

from geolab_kb_agent.agent.orchestrator import KBAgent

from .golden.schema import EvalDataset, EvalQuestion

MIN_KEYWORD_COVERAGE = 0.50


def _keyword_coverage(response_text: str, keywords: list[str]) -> float:
    """Fraction of keywords found in the response (case-insensitive)."""
    if not keywords:
        return 1.0
    lower = response_text.lower()
    hits = sum(1 for kw in keywords if kw.lower() in lower)
    return hits / len(keywords)


def _safe_print(msg: str) -> None:
    """Print with Unicode fallback for Windows consoles."""
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"), flush=True)


@pytest.mark.eval
@pytest.mark.agent
class TestAgentAnswers:
    """Evaluate full agent responses for golden questions."""

    def test_keyword_coverage(
        self,
        eval_agent_factory: Callable[[], KBAgent],
        golden_questions: EvalDataset,
    ) -> None:
        """Agent responses must contain at least 50% of expected keywords."""

        async def _run():
            agent = eval_agent_factory()
            failures: list[str] = []
            passes = 0
            total = len(golden_questions.questions)

            for i, q in enumerate(golden_questions.questions, 1):
                response = await agent.chat(q.question)

                coverage = _keyword_coverage(
                    response.text, q.answer_keywords
                )
                used_tools = response.tool_calls_made > 0

                if coverage < MIN_KEYWORD_COVERAGE:
                    missing = [
                        kw
                        for kw in q.answer_keywords
                        if kw.lower() not in response.text.lower()
                    ]
                    failures.append(
                        f"{q.id}: coverage={coverage:.0%} "
                        f"(need {MIN_KEYWORD_COVERAGE:.0%}), "
                        f"missing={missing}, tools={used_tools}"
                    )
                else:
                    passes += 1

                status = "PASS" if coverage >= MIN_KEYWORD_COVERAGE else "FAIL"
                _safe_print(
                    f"  [{i:>3}/{total}] [{status}] {q.id} | "
                    f"cov={coverage:.0%} | tools={response.tool_calls_made} | "
                    f"{q.question[:50]}"
                )

            return passes, total, failures

        passes, total, failures = asyncio.run(_run())
        _safe_print(f"\n  Agent: {passes}/{total} passed keyword coverage")

        if failures:
            msg = f"{len(failures)}/{total} below {MIN_KEYWORD_COVERAGE:.0%} coverage:\n"
            msg += "\n".join(f"  - {f}" for f in failures)
            pytest.fail(msg)

    def test_agent_uses_tools(
        self,
        eval_agent_factory: Callable[[], KBAgent],
        golden_questions: EvalDataset,
    ) -> None:
        """Agent must make at least one tool call per question."""

        async def _run():
            agent = eval_agent_factory()
            no_tools: list[str] = []

            for q in golden_questions.questions:
                response = await agent.chat(q.question)

                if response.tool_calls_made == 0:
                    no_tools.append(
                        f"{q.id}: No tool calls for: {q.question[:60]}"
                    )

            return no_tools

        no_tools = asyncio.run(_run())

        if no_tools:
            msg = f"{len(no_tools)} questions got no tool calls:\n"
            msg += "\n".join(f"  - {f}" for f in no_tools)
            pytest.fail(msg)
