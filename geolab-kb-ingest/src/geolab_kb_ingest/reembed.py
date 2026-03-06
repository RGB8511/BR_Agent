"""Re-embed all chunks with enriched embedding text.

Updates embeddings in-place without re-extracting PDFs:
1. Loads all chunks from DB for a given package_id
2. Generates enriched embedding_text via chunk_enrichment
3. Batch-embeds via Voyage API
4. Updates each row's embedding_text and embedding columns

Usage:
    DATABASE_URL="..." VOYAGE_API_KEY="..." \
      uv run python -m geolab_kb_ingest.reembed
"""

from __future__ import annotations

import os
import sys

from .chunk_enrichment import clean_title, enrich_chunk
from .db import KBChunk, get_engine, get_session
from .embedder import Embedder

DEFAULT_PACKAGE_ID = "project:juniper-canyon-dam"


def reembed(
    db_url: str,
    voyage_key: str,
    package_id: str = DEFAULT_PACKAGE_ID,
) -> None:
    """Re-embed all chunks for a package with enriched text."""
    engine = get_engine(db_url)
    embedder = Embedder(api_key=voyage_key)

    # Load all chunks
    with get_session(engine) as session:
        chunks: list[KBChunk] = (
            session.query(KBChunk)
            .filter(KBChunk.package_id == package_id)
            .order_by(KBChunk.id)
            .all()
        )
        # Detach from session so we can work with them
        session.expunge_all()

    total = len(chunks)
    if total == 0:
        print(f"No chunks found for package_id='{package_id}'")
        return

    print(f"Loaded {total} chunks for package_id='{package_id}'")

    # Generate enriched embedding text
    enriched_texts: list[str] = []
    title_changes: list[str] = []
    type_counts: dict[str, int] = {}

    for chunk in chunks:
        enriched = enrich_chunk(chunk)
        enriched_texts.append(enriched)

        # Track type distribution
        ct = chunk.chunk_type or "unknown"
        type_counts[ct] = type_counts.get(ct, 0) + 1

        # Track title changes
        cleaned = clean_title(chunk)
        if cleaned != chunk.title:
            title_changes.append(f"  {chunk.id}: '{chunk.title}' -> '{cleaned}'")

    # Print pre-embed stats
    print("\nChunk type distribution:")
    for ct, count in sorted(type_counts.items()):
        print(f"  {ct}: {count}")

    if title_changes:
        print(f"\nTitle overrides applied ({len(title_changes)}):")
        for tc in title_changes[:10]:
            print(tc)
        if len(title_changes) > 10:
            print(f"  ... and {len(title_changes) - 10} more")

    avg_original = sum(len(c.content) for c in chunks) / total
    avg_enriched = sum(len(t) for t in enriched_texts) / total
    print(f"\nAvg content length:        {avg_original:.0f} chars")
    print(f"Avg enriched text length:  {avg_enriched:.0f} chars")
    print(f"Avg enrichment overhead:   {avg_enriched - avg_original:.0f} chars")

    # Batch embed
    print(f"\nEmbedding {total} enriched texts via Voyage API...")
    embeddings = embedder.embed_texts(enriched_texts, input_type="document")
    print(f"Got {len(embeddings)} embeddings (dims={len(embeddings[0])})")

    # Update DB
    print("Updating database...")
    with get_session(engine) as session:
        for chunk, enriched, embedding in zip(chunks, enriched_texts, embeddings):
            session.query(KBChunk).filter(KBChunk.id == chunk.id).update({
                KBChunk.embedding_text: enriched,
                KBChunk.embedding: embedding,
            })

    print(f"Updated {total} chunks successfully.")


def main() -> None:
    db_url = os.environ.get(
        "DATABASE_URL",
        "postgresql://geolab:geolab@localhost:5432/geolab_kb",
    )
    voyage_key = os.environ.get("VOYAGE_API_KEY", "")
    if not voyage_key:
        print("ERROR: VOYAGE_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    package_id = os.environ.get("REEMBED_PACKAGE_ID", DEFAULT_PACKAGE_ID)
    reembed(db_url, voyage_key, package_id)


if __name__ == "__main__":
    main()
