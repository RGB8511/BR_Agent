"""Dump all KB chunks for a project to JSON for question authoring.

Usage:
    DATABASE_URL="postgresql://geolab:geolab@localhost:5432/geolab_kb" \
      uv run python -m tests.eval.inspect_chunks
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from sqlalchemy import text

from geolab_kb_ingest.db import get_engine, get_session

PACKAGE_ID = "project:juniper-canyon-dam"
OUTPUT_FILE = Path(__file__).resolve().parent / "golden" / "chunks_inventory.json"


def dump_chunks() -> None:
    """Query all chunks for the project and write to chunks_inventory.json."""
    url = os.environ.get(
        "DATABASE_URL",
        "postgresql://geolab:geolab@localhost:5432/geolab_kb",
    )
    engine = get_engine(url)

    sql = text("""
        SELECT id, title, chunk_type, content, token_count
        FROM kb_chunks
        WHERE package_id = :pkg
        ORDER BY id
    """)

    with get_session(engine) as session:
        rows = session.execute(sql, {"pkg": PACKAGE_ID}).fetchall()

    chunks = [
        {
            "id": row.id,
            "title": row.title,
            "chunk_type": row.chunk_type,
            "content": row.content,
            "token_count": row.token_count,
        }
        for row in rows
    ]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Dumped {len(chunks)} chunks to {OUTPUT_FILE}")


if __name__ == "__main__":
    dump_chunks()
