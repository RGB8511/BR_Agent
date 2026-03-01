"""Level 3 — Corpus health diagnostics.

Validates the KB data integrity without needing ground-truth questions.

Usage:
    DATABASE_URL="..." uv run pytest tests/eval/test_diagnostics.py -m eval -v
"""

from __future__ import annotations

import pytest
from sqlalchemy import Engine, text

from geolab_kb_ingest.db import get_session

PACKAGE_ID = "project:juniper-canyon-dam"
EXPECTED_CHUNK_COUNT = 267
EXPECTED_EMBEDDING_DIMS = 1024


@pytest.mark.eval
class TestCorpusHealth:
    """Verify KB data integrity for the Juniper Canyon Dam project."""

    def test_chunk_count(self, eval_engine: Engine) -> None:
        """Chunk count matches expected (~267)."""
        sql = text(
            "SELECT COUNT(*) AS cnt FROM kb_chunks WHERE package_id = :pkg"
        )
        with get_session(eval_engine) as session:
            count = session.execute(sql, {"pkg": PACKAGE_ID}).scalar()

        print(f"  Chunk count: {count} (expected ~{EXPECTED_CHUNK_COUNT})")
        assert count is not None and count > 0, "No chunks found"
        assert count == EXPECTED_CHUNK_COUNT, (
            f"Expected {EXPECTED_CHUNK_COUNT} chunks, got {count}"
        )

    def test_no_null_embeddings(self, eval_engine: Engine) -> None:
        """Every chunk must have an embedding vector."""
        sql = text("""
            SELECT COUNT(*) AS cnt FROM kb_chunks
            WHERE package_id = :pkg AND embedding IS NULL
        """)
        with get_session(eval_engine) as session:
            null_count = session.execute(sql, {"pkg": PACKAGE_ID}).scalar()

        assert null_count == 0, f"{null_count} chunks have NULL embeddings"

    def test_embedding_dimensions(self, eval_engine: Engine) -> None:
        """All embeddings must be 1024-dimensional."""
        sql = text("""
            SELECT id, vector_dims(embedding) AS dims
            FROM kb_chunks
            WHERE package_id = :pkg AND embedding IS NOT NULL
            LIMIT 1
        """)
        with get_session(eval_engine) as session:
            row = session.execute(sql, {"pkg": PACKAGE_ID}).first()

        assert row is not None, "No chunks with embeddings found"
        assert row.dims == EXPECTED_EMBEDDING_DIMS, (
            f"Expected {EXPECTED_EMBEDDING_DIMS} dims, got {row.dims}"
        )

    def test_no_duplicate_chunk_ids(self, eval_engine: Engine) -> None:
        """No duplicate chunk IDs within the project."""
        sql = text("""
            SELECT id, COUNT(*) AS cnt
            FROM kb_chunks
            WHERE package_id = :pkg
            GROUP BY id
            HAVING COUNT(*) > 1
        """)
        with get_session(eval_engine) as session:
            dupes = session.execute(sql, {"pkg": PACKAGE_ID}).fetchall()

        if dupes:
            dupe_list = [f"{row.id} (x{row.cnt})" for row in dupes]
            pytest.fail(f"Duplicate chunk IDs: {dupe_list}")

    def test_no_empty_content(self, eval_engine: Engine) -> None:
        """No chunks should have empty content."""
        sql = text("""
            SELECT COUNT(*) AS cnt FROM kb_chunks
            WHERE package_id = :pkg
              AND (content IS NULL OR TRIM(content) = '')
        """)
        with get_session(eval_engine) as session:
            empty_count = session.execute(sql, {"pkg": PACKAGE_ID}).scalar()

        assert empty_count == 0, f"{empty_count} chunks have empty content"

    def test_all_chunks_have_titles(self, eval_engine: Engine) -> None:
        """Every chunk should have a non-empty title."""
        sql = text("""
            SELECT COUNT(*) AS cnt FROM kb_chunks
            WHERE package_id = :pkg
              AND (title IS NULL OR TRIM(title) = '')
        """)
        with get_session(eval_engine) as session:
            no_title = session.execute(sql, {"pkg": PACKAGE_ID}).scalar()

        assert no_title == 0, f"{no_title} chunks have no title"
