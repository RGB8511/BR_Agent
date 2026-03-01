"""Level 2 — Full KBAgent pipeline evaluation.

Calls KBAgent.chat() with each golden question and checks:
- answer_keywords appear in the response (keyword coverage >= 50%)
- tool_calls_made > 0 (agent actually searched the KB)

Costs Anthropic API tokens per question. Use sparingly.

Usage:
    DATABASE_URL="..." VOYAGE_API_KEY="..." ANTHROPIC_API_KEY="..." \
      uv run pytest tests/eval/test_agent.py -m "eval and agent" -v
"""

from __future__ import annotations

import asyncio

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


def _run_async(coro):
    """Run an async coroutine synchronously for pytest."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        import concurrent.futures

        with concurrent.futures.ThreadPoolExecutor() as pool:
            return pool.submit(asyncio.run, coro).result()
    return asyncio.run(coro)


@pytest.mark.eval
@pytest.mark.agent
class TestAgentAnswers:
    """Evaluate full agent responses for golden questions."""

    def test_keyword_coverage(
        self,
        eval_agent: KBAgent,
        golden_questions: EvalDataset,
    ) -> None:
        """Agent responses must contain at least 50% of expected keywords."""
        failures: list[str] = []
        passes = 0

        for q in golden_questions.questions:
            response = _run_async(eval_agent.chat(q.question))

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

            print(
                f"  {q.id} | coverage={coverage:.0%} | "
                f"tools={'yes' if used_tools else 'NO'} | "
                f"{q.question[:50]}"
            )

        total = len(golden_questions.questions)
        print(f"\n  Agent: {passes}/{total} passed keyword coverage")

        if failures:
            msg = f"{len(failures)}/{total} below {MIN_KEYWORD_COVERAGE:.0%} coverage:\n"
            msg += "\n".join(f"  - {f}" for f in failures)
            pytest.fail(msg)

    def test_agent_uses_tools(
        self,
        eval_agent: KBAgent,
        golden_questions: EvalDataset,
    ) -> None:
        """Agent must make at least one tool call per question."""
        no_tools: list[str] = []

        for q in golden_questions.questions:
            response = _run_async(eval_agent.chat(q.question))

            if response.tool_calls_made == 0:
                no_tools.append(
                    f"{q.id}: No tool calls for: {q.question[:60]}"
                )

        if no_tools:
            msg = f"{len(no_tools)} questions got no tool calls:\n"
            msg += "\n".join(f"  - {f}" for f in no_tools)
            pytest.fail(msg)
