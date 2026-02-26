"""Vector similarity search against the KB."""

from __future__ import annotations

from sqlalchemy import Engine, text

from .db import get_session
from .embedder import Embedder


def query_chunks(
    engine: Engine,
    embedder: Embedder,
    query_text: str,
    top_k: int = 5,
    chunk_type: str | None = None,
    discipline: str | None = None,
    min_score: float = 0.35,
) -> list[dict]:
    """Embed query and perform cosine similarity search.

    Uses input_type='query' for Voyage AI asymmetric retrieval.
    """
    embeddings = embedder.embed_texts([query_text], input_type="query")
    query_vec = embeddings[0]

    # Build SQL with pgvector cosine distance operator
    where_clauses = []
    params: dict = {"vec": str(query_vec), "k": top_k}

    if chunk_type:
        where_clauses.append("chunk_type = :chunk_type")
        params["chunk_type"] = chunk_type
    if discipline:
        where_clauses.append("discipline = :discipline")
        params["discipline"] = discipline

    where_sql = ""
    if where_clauses:
        where_sql = "WHERE " + " AND ".join(where_clauses)

    sql = text(f"""
        SELECT id, title, content, chunk_type, package_id, discipline,
               1 - (embedding <=> CAST(:vec AS vector)) AS score
        FROM kb_chunks
        {where_sql}
        ORDER BY embedding <=> CAST(:vec AS vector)
        LIMIT :k
    """)

    with get_session(engine) as session:
        rows = session.execute(sql, params).fetchall()

    results = [
        {
            "id": row.id,
            "title": row.title,
            "content": row.content,
            "chunk_type": row.chunk_type,
            "package_id": row.package_id,
            "discipline": row.discipline,
            "score": float(row.score),
        }
        for row in rows
    ]
    if min_score > 0:
        results = [r for r in results if r["score"] >= min_score]
    return results
