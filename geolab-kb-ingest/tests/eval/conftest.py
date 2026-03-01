"""Pytest fixtures for KB RAG evaluation tests."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest
from sqlalchemy import Engine

from geolab_kb_ingest.db import get_engine
from geolab_kb_ingest.embedder import Embedder
from geolab_kb_ingest.reranker import Reranker

from .golden.schema import EvalDataset

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
EVAL_DIR = Path(__file__).resolve().parent
GOLDEN_DIR = EVAL_DIR / "golden"
QUESTIONS_FILE = GOLDEN_DIR / "questions.json"


# ---------------------------------------------------------------------------
# Markers
# ---------------------------------------------------------------------------
def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "eval: KB RAG evaluation tests")
    config.addinivalue_line("markers", "agent: tests requiring Anthropic API")


# ---------------------------------------------------------------------------
# Session-scoped fixtures
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def eval_engine() -> Engine:
    """Live database engine for evaluation.

    Requires DATABASE_URL env var (defaults to local geolab_kb).
    """
    url = os.environ.get(
        "DATABASE_URL",
        "postgresql://geolab:geolab@localhost:5432/geolab_kb",
    )
    return get_engine(url)


@pytest.fixture(scope="session")
def eval_embedder() -> Embedder:
    """Voyage AI embedder for query embedding.

    Requires VOYAGE_API_KEY env var.
    """
    api_key = os.environ.get("VOYAGE_API_KEY", "")
    if not api_key:
        pytest.skip("VOYAGE_API_KEY not set")
    return Embedder(api_key=api_key)


@pytest.fixture(scope="session")
def eval_reranker() -> Reranker | None:
    """Voyage AI reranker for result reranking.

    Uses the same VOYAGE_API_KEY as the embedder.
    Returns None if VOYAGE_API_KEY is not set (reranking disabled).
    """
    api_key = os.environ.get("VOYAGE_API_KEY", "")
    if not api_key:
        return None
    return Reranker(api_key=api_key)


@pytest.fixture(scope="session")
def eval_agent_factory(eval_engine: Engine, eval_embedder: Embedder):
    """Factory that creates a KBAgent inside an async context.

    Returns a callable so the KBAgent (and its AsyncAnthropic client) can be
    created inside ``asyncio.run()``, avoiding event-loop mismatch on Windows.

    Requires ANTHROPIC_API_KEY env var.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        pytest.skip("ANTHROPIC_API_KEY not set")

    from geolab_kb_agent.agent.orchestrator import KBAgent

    def _create() -> KBAgent:
        return KBAgent(
            api_key=api_key,
            model=os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250929"),
            engine=eval_engine,
            embedder=eval_embedder,
            mode="concise",
        )

    return _create


@pytest.fixture(scope="session")
def golden_questions() -> EvalDataset:
    """Load the golden question dataset.

    Skips the test if questions.json doesn't exist or is empty.
    """
    if not QUESTIONS_FILE.exists():
        pytest.skip(f"Golden dataset not found: {QUESTIONS_FILE}")

    with open(QUESTIONS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    dataset = EvalDataset.model_validate(data)
    if not dataset.questions:
        pytest.skip("Golden dataset has no questions")

    return dataset
