"""Level 1 — Retrieval-only evaluation.

Embeds each golden question via Voyage AI and checks that the expected
primary chunk appears in the top-k results within the acceptable rank.

Fast and cheap (~$0.01 per 100 questions via Voyage embedding API).

Usage:
    DATABASE_URL="..." VOYAGE_API_KEY="..." \
      uv run pytest tests/eval/test_retrieval.py -m eval -v
"""

from __future__ import annotations

import pytest
from sqlalchemy import Engine

from geolab_kb_ingest.embedder import Embedder
from geolab_kb_ingest.query import query_chunks
from geolab_kb_ingest.reranker import Reranker

from .golden.schema import EvalDataset, EvalQuestion


def _retrieve_for_question(
    engine: Engine,
    embedder: Embedder,
    q: EvalQuestion,
    reranker: Reranker | None = None,
) -> list[dict]:
    """Run retrieval with min_score=0.0 so we see all ranks."""
    return query_chunks(
        engine=engine,
        embedder=embedder,
        query_text=q.question,
        top_k=q.expected_top_k,
        package_id=q.expected_chunk_ids[0].rsplit(".", 2)[0]
        if q.expected_chunk_ids
        else None,
        min_score=0.0,
        reranker=reranker,
    )


def _find_primary_rank(
    results: list[dict],
    primary_chunk_id: str,
    acceptable_ids: list[str] | None = None,
) -> tuple[int | None, float | None]:
    """Return (1-based rank, score) of the primary chunk, or (None, None).

    Checks against both the single primary ID and any acceptable alternates.
    """
    all_ids = {primary_chunk_id}
    if acceptable_ids:
        all_ids.update(acceptable_ids)

    for i, r in enumerate(results, 1):
        if r["id"] in all_ids:
            return i, r["score"]
    return None, None


# ---------------------------------------------------------------------------
# Parametrized test — one case per golden question
# ---------------------------------------------------------------------------
def _question_ids(dataset: EvalDataset) -> list[str]:
    return [q.id for q in dataset.questions]


@pytest.mark.eval
class TestRetrieval:
    """Evaluate retrieval quality for every golden question."""

    def test_primary_chunk_in_top_k(
        self,
        eval_engine: Engine,
        eval_embedder: Embedder,
        eval_reranker: Reranker | None,
        golden_questions: EvalDataset,
        request: pytest.FixtureRequest,
    ) -> None:
        """Each question's primary chunk must appear in top-k."""
        failures: list[str] = []

        for q in golden_questions.questions:
            results = _retrieve_for_question(
                eval_engine, eval_embedder, q, eval_reranker,
            )
            rank, score = _find_primary_rank(
                results,
                q.expected_chunk_id_primary,
                q.acceptable_primary_ids,
            )

            if rank is None:
                actual_ids = [r["id"] for r in results]
                failures.append(
                    f"{q.id}: Primary chunk '{q.expected_chunk_id_primary}' "
                    f"NOT in top-{q.expected_top_k}. "
                    f"Got: {actual_ids}"
                )
            elif rank > q.min_acceptable_rank:
                failures.append(
                    f"{q.id}: Primary chunk at rank {rank} "
                    f"(max acceptable: {q.min_acceptable_rank}, "
                    f"score: {score:.4f})"
                )

        if failures:
            msg = f"{len(failures)}/{len(golden_questions.questions)} failed:\n"
            msg += "\n".join(f"  - {f}" for f in failures)
            pytest.fail(msg)

    def test_per_question_retrieval(
        self,
        eval_engine: Engine,
        eval_embedder: Embedder,
        eval_reranker: Reranker | None,
        golden_questions: EvalDataset,
    ) -> None:
        """Detailed per-question report (always passes, prints diagnostics)."""
        for q in golden_questions.questions:
            results = _retrieve_for_question(
                eval_engine, eval_embedder, q, eval_reranker,
            )
            rank, score = _find_primary_rank(
                results,
                q.expected_chunk_id_primary,
                q.acceptable_primary_ids,
            )

            status = "PASS" if (rank and rank <= q.min_acceptable_rank) else "FAIL"
            rank_str = str(rank) if rank else "MISS"
            score_str = f"{score:.4f}" if score else "N/A"

            print(
                f"  [{status}] {q.id} | rank={rank_str} | "
                f"score={score_str} | {q.category}/{q.difficulty} | "
                f"{q.question[:60]}"
            )
