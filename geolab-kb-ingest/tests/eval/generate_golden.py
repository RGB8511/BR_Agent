"""Generate golden evaluation questions spanning all KB packages.

Reads non-project chunks from the database, samples representative chunks
per package, sends them to Claude Haiku to generate targeted questions,
validates each question via vector retrieval, and merges with existing
project questions into a unified dataset.

Usage:
    DATABASE_URL="..." VOYAGE_API_KEY="..." ANTHROPIC_API_KEY="..." \
      uv run python -m tests.eval.generate_golden \
        --target 400 --validate --output tests/eval/golden/questions.json
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import os
import sys
from pathlib import Path

import anthropic
from sqlalchemy import Engine, text

from geolab_kb_ingest.db import get_engine, get_session
from geolab_kb_ingest.embedder import Embedder
from geolab_kb_ingest.query import query_chunks

logger = logging.getLogger(__name__)

EVAL_DIR = Path(__file__).resolve().parent
GOLDEN_DIR = EVAL_DIR / "golden"
QUESTIONS_FILE = GOLDEN_DIR / "questions.json"
PARTIAL_FILE = GOLDEN_DIR / ".partial.json"

# Categories that Claude can assign (superset of existing + new)
VALID_CATEGORIES = {
    "factual_lookup",
    "numerical_data",
    "table_query",
    "equation_query",
    "technical_detail",
    "definition",
    "procedural",
    "geotechnical",
    "instrumentation",
    "safety",
    "temporal",
    "cross_document",
}
VALID_DIFFICULTIES = {"easy", "medium", "hard"}

# Max content tokens per chunk sent to Claude (rough char estimate: 1 token ~ 4 chars)
MAX_CHUNK_CHARS = 3200  # ~800 tokens


# ---------------------------------------------------------------------------
# Stage 1 — Inventory
# ---------------------------------------------------------------------------
def get_package_inventory(engine: Engine) -> dict[str, list[dict]]:
    """Query DB for all non-project chunks grouped by package_id.

    Excludes packages starting with 'project:' or 'projects:'
    (already covered by existing questions / synthetic data).

    Returns:
        {package_id: [{"id", "chunk_type", "title", "content", "token_count", "discipline"}, ...]}
    """
    sql = text("""
        SELECT id, package_id, chunk_type, title, content, token_count, discipline
        FROM kb_chunks
        WHERE package_id NOT LIKE 'project:%'
          AND package_id NOT LIKE 'projects.%'
        ORDER BY package_id, id
    """)

    packages: dict[str, list[dict]] = {}
    with get_session(engine) as session:
        rows = session.execute(sql).fetchall()

    for row in rows:
        chunk = {
            "id": row.id,
            "chunk_type": row.chunk_type,
            "title": row.title,
            "content": row.content,
            "token_count": row.token_count,
            "discipline": row.discipline,
        }
        packages.setdefault(row.package_id, []).append(chunk)

    return packages


# ---------------------------------------------------------------------------
# Stage 2 — Sample
# ---------------------------------------------------------------------------
def sample_chunks_for_package(
    chunks: list[dict], target_questions: int,
) -> list[dict]:
    """Sample representative chunks from a package for question generation.

    Sends ~2x target chunks to Claude. Guarantees at least one per chunk_type
    present (equation, table, narrative). Fills rest by diversity/length.
    Caps at 15 chunks per call.
    """
    max_send = min(15, target_questions * 2)

    # Group by chunk_type
    by_type: dict[str, list[dict]] = {}
    for c in chunks:
        by_type.setdefault(c["chunk_type"], []).append(c)

    selected: list[dict] = []
    selected_ids: set[str] = set()

    # Guarantee at least one per chunk_type
    for ctype, type_chunks in sorted(by_type.items()):
        if not type_chunks:
            continue
        # Pick the longest chunk of this type (more content = better question)
        best = max(type_chunks, key=lambda c: c["token_count"])
        if best["id"] not in selected_ids:
            selected.append(best)
            selected_ids.add(best["id"])

    # Fill rest by token_count descending (longer chunks are richer)
    remaining = [c for c in chunks if c["id"] not in selected_ids]
    remaining.sort(key=lambda c: c["token_count"], reverse=True)

    for c in remaining:
        if len(selected) >= max_send:
            break
        selected.append(c)
        selected_ids.add(c["id"])

    return selected


def compute_target_per_package(
    chunk_count: int, total_packages: int, global_target: int,
) -> int:
    """Compute how many questions to request for a package.

    Formula: max(3, min(10, ceil(chunk_count / 5)))
    Then scale to approximate global target.
    """
    base = max(3, min(10, math.ceil(chunk_count / 5)))
    return base


# ---------------------------------------------------------------------------
# Stage 3 — Generate (Claude Haiku)
# ---------------------------------------------------------------------------
GENERATION_PROMPT = """\
You are generating evaluation questions for a knowledge base retrieval system.
Below are chunks from the "{package_id}" package (discipline: {discipline}).
Each chunk has an ID, type, title, and content.

Generate exactly {target} questions that:
1. Can be answered using ONLY the information in one specific chunk
2. Are natural questions an engineer or researcher would ask
3. Cover a mix of difficulties (easy, medium, hard)
4. Cover a mix of categories from: factual_lookup, numerical_data, table_query, \
equation_query, technical_detail, definition, procedural, geotechnical, \
instrumentation, safety, temporal
5. Use the appropriate category based on the chunk content (e.g. table_query \
for table chunks, equation_query for equation chunks)

CHUNKS:
{chunks_text}

Return a JSON array (no markdown fences, no extra text) with exactly {target} items:
[
  {{
    "question": "A clear, specific question",
    "category": "one of the valid categories",
    "difficulty": "easy|medium|hard",
    "target_chunk_id": "the exact chunk ID that answers this question",
    "expected_answer": "concise answer from the chunk",
    "answer_keywords": ["keyword1", "keyword2"],
    "tags": ["topic_tag"]
  }}
]

Important:
- target_chunk_id MUST be one of the chunk IDs provided above
- Questions should be specific enough that only the target chunk answers them
- expected_answer must come directly from the chunk content
- answer_keywords should be 2-4 distinctive terms from the answer
- Vary question phrasing: use who/what/when/where/how/why and both short and long forms
"""


def format_chunks_for_prompt(chunks: list[dict]) -> str:
    """Format sampled chunks for inclusion in the Claude prompt."""
    parts = []
    for c in chunks:
        content = c["content"]
        if len(content) > MAX_CHUNK_CHARS:
            content = content[:MAX_CHUNK_CHARS] + "..."
        parts.append(
            f"--- CHUNK ---\n"
            f"ID: {c['id']}\n"
            f"Type: {c['chunk_type']}\n"
            f"Title: {c['title']}\n"
            f"Content:\n{content}\n"
        )
    return "\n".join(parts)


def generate_questions_for_package(
    client: anthropic.Anthropic,
    model: str,
    package_id: str,
    discipline: str,
    sampled_chunks: list[dict],
    target: int,
) -> list[dict]:
    """Call Claude to generate questions for one package.

    Returns list of raw question dicts from Claude's response.
    """
    chunks_text = format_chunks_for_prompt(sampled_chunks)

    prompt = GENERATION_PROMPT.format(
        package_id=package_id,
        discipline=discipline,
        target=target,
        chunks_text=chunks_text,
    )

    try:
        message = client.messages.create(
            model=model,
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        raw_text = message.content[0].text.strip()

        # Handle potential markdown fences
        if raw_text.startswith("```"):
            lines = raw_text.split("\n")
            # Remove first and last fence lines
            lines = [l for l in lines if not l.strip().startswith("```")]
            raw_text = "\n".join(lines)

        questions = json.loads(raw_text)
        if not isinstance(questions, list):
            logger.warning("Package %s: Claude returned non-list, skipping", package_id)
            return []

        return questions

    except json.JSONDecodeError as exc:
        logger.warning(
            "Package %s: JSON parse error: %s\nRaw: %s",
            package_id, exc, raw_text[:500],
        )
        return []
    except Exception:
        logger.warning(
            "Package %s: Claude API error", package_id, exc_info=True,
        )
        return []


def validate_generated_question(q: dict, valid_chunk_ids: set[str]) -> dict | None:
    """Validate and normalize a single generated question.

    Returns normalized dict or None if invalid.
    """
    # Required fields
    for field in ("question", "category", "target_chunk_id", "expected_answer"):
        if field not in q or not q[field]:
            return None

    # Validate target_chunk_id exists in the sampled set
    if q["target_chunk_id"] not in valid_chunk_ids:
        logger.debug("Chunk ID %s not in valid set", q["target_chunk_id"])
        return None

    # Normalize category
    category = q.get("category", "").strip().lower()
    if category not in VALID_CATEGORIES:
        category = "technical_detail"  # safe fallback

    # Normalize difficulty
    difficulty = q.get("difficulty", "").strip().lower()
    if difficulty not in VALID_DIFFICULTIES:
        difficulty = "medium"

    return {
        "question": q["question"].strip(),
        "category": category,
        "difficulty": difficulty,
        "target_chunk_id": q["target_chunk_id"].strip(),
        "expected_answer": q["expected_answer"].strip(),
        "answer_keywords": q.get("answer_keywords", []),
        "tags": q.get("tags", []),
    }


# ---------------------------------------------------------------------------
# Stage 4 — Validate via retrieval
# ---------------------------------------------------------------------------
def validate_question_retrieval(
    engine: Engine,
    embedder: Embedder,
    question: dict,
) -> dict | None:
    """Validate that the target chunk is retrievable for this question.

    Calls query_chunks with top_k=5, min_score=0.0.
    - Rank 1-3: Accept with min_acceptable_rank=3
    - Rank 4-5: Accept with min_acceptable_rank=5
    - Not found: Discard

    Returns enriched question dict or None if validation fails.
    """
    try:
        results = query_chunks(
            engine=engine,
            embedder=embedder,
            query_text=question["question"],
            top_k=5,
            min_score=0.0,
        )
    except Exception:
        logger.warning(
            "Retrieval failed for question: %s",
            question["question"][:60],
            exc_info=True,
        )
        return None

    target_id = question["target_chunk_id"]
    found_rank = None
    for i, r in enumerate(results):
        if r["id"] == target_id:
            found_rank = i + 1  # 1-based
            break

    if found_rank is None:
        logger.debug(
            "Target chunk %s not in top-5 for: %s",
            target_id, question["question"][:60],
        )
        return None

    # Set min_acceptable_rank based on where it landed
    if found_rank <= 3:
        min_acceptable_rank = 3
    else:
        min_acceptable_rank = 5

    # Collect all top-5 chunk IDs as expected_chunk_ids
    expected_chunk_ids = [r["id"] for r in results]

    return {
        **question,
        "expected_chunk_ids": expected_chunk_ids,
        "expected_chunk_id_primary": target_id,
        "min_acceptable_rank": min_acceptable_rank,
        "expected_top_k": 5,
        "source_doc": target_id.rsplit(".", 2)[0] if "." in target_id else target_id,
    }


# ---------------------------------------------------------------------------
# Stage 5 — Merge & Save
# ---------------------------------------------------------------------------
def load_existing_questions() -> list[dict]:
    """Load existing project questions from questions.json."""
    if not QUESTIONS_FILE.exists():
        return []
    with open(QUESTIONS_FILE, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("questions", [])


def save_dataset(
    questions: list[dict],
    output_path: Path,
    version: str = "2.0",
) -> None:
    """Save the merged dataset."""
    dataset = {
        "version": version,
        "project": "GeoLab KB",
        "package_id": "all",
        "questions": questions,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    logger.info("Saved %d questions to %s", len(questions), output_path)


def load_partial_results() -> dict[str, list[dict]]:
    """Load partial results from previous run."""
    if not PARTIAL_FILE.exists():
        return {}
    with open(PARTIAL_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_partial_results(partial: dict[str, list[dict]]) -> None:
    """Save partial results for resumability."""
    with open(PARTIAL_FILE, "w", encoding="utf-8") as f:
        json.dump(partial, f, indent=2, ensure_ascii=False)


def print_summary(all_new_questions: list[dict], validated_count: int, discarded_count: int) -> None:
    """Print generation summary."""
    print(f"\n{'=' * 60}")
    print("GENERATION SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Total new questions generated: {len(all_new_questions)}")
    print(f"  Validated (retrieval pass):    {validated_count}")
    print(f"  Discarded (retrieval fail):    {discarded_count}")

    # By category
    cats: dict[str, int] = {}
    diffs: dict[str, int] = {}
    for q in all_new_questions:
        cats[q["category"]] = cats.get(q["category"], 0) + 1
        diffs[q["difficulty"]] = diffs.get(q["difficulty"], 0) + 1

    if cats:
        print(f"\n  By Category:")
        for cat in sorted(cats):
            print(f"    {cat:<20} {cats[cat]:>4}")

    if diffs:
        print(f"\n  By Difficulty:")
        for diff in sorted(diffs):
            print(f"    {diff:<20} {diffs[diff]:>4}")

    print(f"{'=' * 60}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate golden evaluation questions for the full KB",
    )
    parser.add_argument(
        "--target", type=int, default=400,
        help="Target number of new questions to generate (default: 400)",
    )
    parser.add_argument(
        "--model", type=str, default="claude-haiku-4-5-20251001",
        help="Anthropic model ID for generation (default: claude-haiku-4-5-20251001)",
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Output path for merged dataset (default: tests/eval/golden/questions.json)",
    )
    parser.add_argument(
        "--validate", action="store_true", default=True,
        help="Validate questions via vector retrieval (default: True)",
    )
    parser.add_argument(
        "--no-validate", dest="validate", action="store_false",
        help="Skip retrieval validation",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be generated without calling APIs",
    )
    parser.add_argument(
        "--resume", action="store_true",
        help="Resume from partial results of a previous run",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    # Environment
    db_url = os.environ.get(
        "DATABASE_URL",
        "postgresql://geolab:geolab@localhost:5432/geolab_kb",
    )
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY", "")
    voyage_key = os.environ.get("VOYAGE_API_KEY", "")

    if not args.dry_run and not anthropic_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    if not args.dry_run and args.validate and not voyage_key:
        print("ERROR: VOYAGE_API_KEY not set (required for --validate)", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output) if args.output else QUESTIONS_FILE

    # Setup clients
    engine = get_engine(db_url)
    client = anthropic.Anthropic(api_key=anthropic_key) if not args.dry_run else None
    embedder = Embedder(api_key=voyage_key) if (args.validate and not args.dry_run) else None

    # Stage 1 — Inventory
    print("Stage 1: Querying chunk inventory...")
    packages = get_package_inventory(engine)
    total_chunks = sum(len(v) for v in packages.values())
    print(f"  Found {total_chunks} chunks across {len(packages)} packages")

    if not packages:
        print("ERROR: No non-project packages found in DB", file=sys.stderr)
        sys.exit(1)

    # Load partial results if resuming
    partial: dict[str, list[dict]] = {}
    if args.resume:
        partial = load_partial_results()
        if partial:
            print(f"  Resuming: {len(partial)} packages already completed")

    # Stage 2 — Sample & compute targets
    print("\nStage 2: Computing targets and sampling chunks...")
    package_plan: list[tuple[str, int, list[dict]]] = []
    total_target = 0

    for pkg_id, chunks in sorted(packages.items()):
        if pkg_id in partial:
            continue  # Already done in previous run

        target = compute_target_per_package(len(chunks), len(packages), args.target)
        sampled = sample_chunks_for_package(chunks, target)
        package_plan.append((pkg_id, target, sampled))
        total_target += target

        # Get discipline from first chunk
        disc = chunks[0]["discipline"] if chunks else "unknown"
        print(
            f"  {pkg_id}: {len(chunks)} chunks, "
            f"target={target} Qs, sending={len(sampled)} chunks "
            f"[{disc}]"
        )

    print(f"\n  Total target (new packages): {total_target} questions")

    if args.dry_run:
        print("\n[DRY RUN] Would generate questions for the above packages.")
        print("Exiting without API calls.")
        return

    # Stage 3 — Generate
    print("\nStage 3: Generating questions via Claude...")
    all_raw_questions: list[dict] = []

    # Include questions from partial results
    for pkg_id, qs in partial.items():
        all_raw_questions.extend(qs)
        print(f"  [CACHED] {pkg_id}: {len(qs)} questions from previous run")

    for i, (pkg_id, target, sampled) in enumerate(package_plan, 1):
        discipline = sampled[0]["discipline"] if sampled else "unknown"
        print(f"  [{i}/{len(package_plan)}] {pkg_id} (target={target})...", end=" ", flush=True)

        raw_qs = generate_questions_for_package(
            client=client,
            model=args.model,
            package_id=pkg_id,
            discipline=discipline,
            sampled_chunks=sampled,
            target=target,
        )

        # Validate raw questions against the chunk IDs we sent
        valid_ids = {c["id"] for c in sampled}
        validated_qs = []
        for q in raw_qs:
            normalized = validate_generated_question(q, valid_ids)
            if normalized:
                validated_qs.append(normalized)

        print(f"{len(validated_qs)}/{len(raw_qs)} valid")
        all_raw_questions.extend(validated_qs)

        # Save partial progress
        partial[pkg_id] = validated_qs
        save_partial_results(partial)

    print(f"\n  Total raw questions (all packages): {len(all_raw_questions)}")

    # Stage 4 — Validate via retrieval
    validated_questions: list[dict] = []
    discarded = 0

    if args.validate and embedder is not None:
        print("\nStage 4: Validating questions via vector retrieval...")
        for i, q in enumerate(all_raw_questions, 1):
            if i % 50 == 0 or i == len(all_raw_questions):
                print(f"  Validating {i}/{len(all_raw_questions)}...", flush=True)

            enriched = validate_question_retrieval(engine, embedder, q)
            if enriched:
                validated_questions.append(enriched)
            else:
                discarded += 1

        print(f"  Validated: {len(validated_questions)}, Discarded: {discarded}")
    else:
        # No validation — use raw questions with placeholder fields
        print("\nStage 4: Skipped (--no-validate)")
        for q in all_raw_questions:
            validated_questions.append({
                **q,
                "expected_chunk_ids": [q["target_chunk_id"]],
                "expected_chunk_id_primary": q["target_chunk_id"],
                "min_acceptable_rank": 3,
                "expected_top_k": 5,
                "source_doc": (
                    q["target_chunk_id"].rsplit(".", 2)[0]
                    if "." in q["target_chunk_id"]
                    else q["target_chunk_id"]
                ),
            })

    # Stage 5 — Merge & Save
    print("\nStage 5: Merging with existing questions...")
    existing = load_existing_questions()
    print(f"  Existing project questions: {len(existing)}")
    print(f"  New KB questions: {len(validated_questions)}")

    # Renumber new questions from Q101+
    next_num = 101
    for q in validated_questions:
        q["id"] = f"Q{next_num:03d}"
        # Remove the intermediate target_chunk_id field (not in schema)
        q.pop("target_chunk_id", None)
        # Ensure acceptable_primary_ids exists
        q.setdefault("acceptable_primary_ids", [])
        next_num += 1

    merged = existing + validated_questions
    print(f"  Total merged: {len(merged)}")

    # Save merged dataset
    save_dataset(merged, output_path, version="2.0")
    print(f"  Saved merged dataset: {output_path}")

    # Also save KB-only dataset
    kb_only_path = output_path.parent / "questions_kb.json"
    save_dataset(validated_questions, kb_only_path, version="2.0")
    print(f"  Saved KB-only dataset: {kb_only_path}")

    # Clean up partial file
    if PARTIAL_FILE.exists():
        PARTIAL_FILE.unlink()
        print("  Cleaned up .partial.json")

    print_summary(validated_questions, len(validated_questions), discarded)


if __name__ == "__main__":
    main()
