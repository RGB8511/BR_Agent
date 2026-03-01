"""CLI runner for KB RAG evaluation with metrics reporting.

Runs Level 1 retrieval evaluation and produces a JSON report with:
- Recall@k, Precision@1, MRR, mean cosine similarity, pass rate
- Breakdowns by category and difficulty

Usage:
    DATABASE_URL="..." VOYAGE_API_KEY="..." \
      uv run python -m tests.eval.runner --output eval_results.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from geolab_kb_ingest.db import get_engine
from geolab_kb_ingest.embedder import Embedder
from geolab_kb_ingest.query import query_chunks
from geolab_kb_ingest.reranker import Reranker

from .golden.schema import (
    CategoryMetrics,
    EvalDataset,
    EvalQuestion,
    EvalReport,
    RetrievalResult,
    RetrievedChunk,
)

QUESTIONS_FILE = Path(__file__).resolve().parent / "golden" / "questions.json"


def load_dataset() -> EvalDataset:
    """Load the golden question dataset."""
    if not QUESTIONS_FILE.exists():
        print(f"ERROR: Golden dataset not found: {QUESTIONS_FILE}", file=sys.stderr)
        sys.exit(1)

    with open(QUESTIONS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    dataset = EvalDataset.model_validate(data)
    if not dataset.questions:
        print("ERROR: Golden dataset has no questions", file=sys.stderr)
        sys.exit(1)

    return dataset


def evaluate_question(
    engine,
    embedder: Embedder,
    q: EvalQuestion,
    reranker: Reranker | None = None,
) -> RetrievalResult:
    """Evaluate a single question's retrieval quality."""
    try:
        results = query_chunks(
            engine=engine,
            embedder=embedder,
            query_text=q.question,
            top_k=q.expected_top_k,
            min_score=0.0,
            reranker=reranker,
        )
    except Exception as exc:
        return RetrievalResult(
            question_id=q.id,
            question=q.question,
            category=q.category,
            difficulty=q.difficulty,
            expected_primary_chunk=q.expected_chunk_id_primary,
            error=str(exc),
        )

    chunks = [
        RetrievedChunk(
            rank=i + 1,
            chunk_id=r["id"],
            title=r["title"],
            score=r["score"],
        )
        for i, r in enumerate(results)
    ]

    # Find primary chunk rank — check both primary and acceptable IDs
    acceptable_ids = {q.expected_chunk_id_primary}
    if q.acceptable_primary_ids:
        acceptable_ids.update(q.acceptable_primary_ids)

    primary_rank = None
    primary_score = None
    for c in chunks:
        if c.chunk_id in acceptable_ids:
            primary_rank = c.rank
            primary_score = c.score
            break

    passed = primary_rank is not None and primary_rank <= q.min_acceptable_rank

    return RetrievalResult(
        question_id=q.id,
        question=q.question,
        category=q.category,
        difficulty=q.difficulty,
        expected_primary_chunk=q.expected_chunk_id_primary,
        actual_chunks=chunks,
        primary_chunk_rank=primary_rank,
        primary_chunk_score=primary_score,
        passed=passed,
    )


def compute_slice_metrics(results: list[RetrievalResult]) -> CategoryMetrics:
    """Compute metrics for a slice of results."""
    n = len(results)
    if n == 0:
        return CategoryMetrics()

    recall_hits = sum(1 for r in results if r.primary_chunk_rank is not None)
    precision_hits = sum(
        1 for r in results if r.primary_chunk_rank == 1
    )
    pass_hits = sum(1 for r in results if r.passed)

    reciprocal_ranks = []
    for r in results:
        if r.primary_chunk_rank is not None:
            reciprocal_ranks.append(1.0 / r.primary_chunk_rank)
        else:
            reciprocal_ranks.append(0.0)

    return CategoryMetrics(
        count=n,
        recall_at_k=recall_hits / n,
        precision_at_1=precision_hits / n,
        mrr=sum(reciprocal_ranks) / n,
        pass_rate=pass_hits / n,
    )


def compute_report(results: list[RetrievalResult]) -> EvalReport:
    """Compute aggregate metrics from individual results."""
    n = len(results)
    if n == 0:
        return EvalReport()

    # Overall metrics
    overall = compute_slice_metrics(results)

    # Mean cosine similarity (of found primary chunks only)
    scores = [
        r.primary_chunk_score
        for r in results
        if r.primary_chunk_score is not None
    ]
    mean_sim = sum(scores) / len(scores) if scores else 0.0

    # By category
    by_category: dict[str, CategoryMetrics] = {}
    categories = {r.category for r in results}
    for cat in sorted(categories):
        cat_results = [r for r in results if r.category == cat]
        by_category[cat] = compute_slice_metrics(cat_results)

    # By difficulty
    by_difficulty: dict[str, CategoryMetrics] = {}
    difficulties = {r.difficulty for r in results}
    for diff in sorted(difficulties):
        diff_results = [r for r in results if r.difficulty == diff]
        by_difficulty[diff] = compute_slice_metrics(diff_results)

    return EvalReport(
        total_questions=n,
        recall_at_k=overall.recall_at_k,
        precision_at_1=overall.precision_at_1,
        mrr=overall.mrr,
        mean_cosine_similarity=mean_sim,
        pass_rate=overall.pass_rate,
        by_category=by_category,
        by_difficulty=by_difficulty,
        results=results,
    )


def print_report(report: EvalReport) -> None:
    """Print a human-readable evaluation report."""
    print("\n" + "=" * 70)
    print("KB RAG EVALUATION REPORT")
    print("=" * 70)

    print(f"\n  Total questions:       {report.total_questions}")
    print(f"  Recall@k:              {report.recall_at_k:.1%}")
    print(f"  Precision@1:           {report.precision_at_1:.1%}")
    print(f"  MRR:                   {report.mrr:.4f}")
    print(f"  Mean cosine sim:       {report.mean_cosine_similarity:.4f}")
    print(f"  Pass rate:             {report.pass_rate:.1%}")

    if report.by_category:
        print("\n  By Category:")
        print(f"  {'Category':<20} {'Count':>5} {'Recall':>8} {'P@1':>8} {'MRR':>8} {'Pass':>8}")
        print("  " + "-" * 58)
        for cat, m in sorted(report.by_category.items()):
            print(
                f"  {cat:<20} {m.count:>5} {m.recall_at_k:>7.1%} "
                f"{m.precision_at_1:>7.1%} {m.mrr:>7.4f} {m.pass_rate:>7.1%}"
            )

    if report.by_difficulty:
        print("\n  By Difficulty:")
        print(f"  {'Difficulty':<20} {'Count':>5} {'Recall':>8} {'P@1':>8} {'MRR':>8} {'Pass':>8}")
        print("  " + "-" * 58)
        for diff, m in sorted(report.by_difficulty.items()):
            print(
                f"  {diff:<20} {m.count:>5} {m.recall_at_k:>7.1%} "
                f"{m.precision_at_1:>7.1%} {m.mrr:>7.4f} {m.pass_rate:>7.1%}"
            )

    # Print failures
    failures = [r for r in report.results if not r.passed]
    if failures:
        print(f"\n  FAILURES ({len(failures)}):")
        for r in failures:
            rank_str = str(r.primary_chunk_rank) if r.primary_chunk_rank else "MISS"
            score_str = f"{r.primary_chunk_score:.4f}" if r.primary_chunk_score else "N/A"
            print(
                f"    {r.question_id}: rank={rank_str} score={score_str} "
                f"| {r.question[:55]}"
            )
            if r.error:
                print(f"      ERROR: {r.error}")

    print("\n" + "=" * 70)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run KB RAG retrieval evaluation"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Path to write JSON report (default: stdout only)",
    )
    parser.add_argument(
        "--rerank",
        action="store_true",
        help="Enable Voyage reranker (off by default, adds cost/latency)",
    )
    args = parser.parse_args()

    # Setup
    db_url = os.environ.get(
        "DATABASE_URL",
        "postgresql://geolab:geolab@localhost:5432/geolab_kb",
    )
    voyage_key = os.environ.get("VOYAGE_API_KEY", "")
    if not voyage_key:
        print("ERROR: VOYAGE_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    engine = get_engine(db_url)
    embedder = Embedder(api_key=voyage_key)
    reranker = Reranker(api_key=voyage_key) if args.rerank else None
    dataset = load_dataset()

    mode = "vector + rerank" if args.rerank else "vector only"
    print(f"Evaluating {len(dataset.questions)} questions ({mode})...")

    # Run evaluations
    results: list[RetrievalResult] = []
    for i, q in enumerate(dataset.questions, 1):
        result = evaluate_question(engine, embedder, q, reranker)
        results.append(result)

        status = "PASS" if result.passed else "FAIL"
        rank_str = str(result.primary_chunk_rank) if result.primary_chunk_rank else "MISS"
        print(f"  [{i:>3}/{len(dataset.questions)}] [{status}] {q.id} rank={rank_str}")

    # Compute and display report
    report = compute_report(results)
    print_report(report)

    # Write JSON output
    if args.output:
        output_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "dataset_version": dataset.version,
            "project": dataset.project,
            **report.model_dump(),
        }
        output_path = Path(args.output)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, default=str)
        print(f"\nJSON report written to: {output_path}")


if __name__ == "__main__":
    main()
