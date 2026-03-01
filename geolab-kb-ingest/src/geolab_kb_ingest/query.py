"""Vector similarity search against the KB."""

from __future__ import annotations

import logging
import os
import re

from sqlalchemy import Engine, text

from .db import get_session
from .embedder import Embedder
from .reranker import Reranker

logger = logging.getLogger(__name__)

# Minimum cosine similarity score — chunks below this threshold are
# considered irrelevant and filtered out to reduce hallucination risk.
MIN_SIMILARITY_SCORE = 0.35


def query_chunks(
    engine: Engine,
    embedder: Embedder,
    query_text: str,
    top_k: int = 5,
    chunk_type: str | None = None,
    discipline: str | None = None,
    package_id: str | None = None,
    package_id_prefix: str | None = None,
    package_id_exclude_prefix: str | None = None,
    tags: list[str] | None = None,
    min_score: float = 0.35,
    expand: bool = False,
    reranker: Reranker | None = None,
    content_years: list[int] | None = None,
) -> list[dict]:
    """Embed query and perform cosine similarity search.

    Uses input_type='query' for Voyage AI asymmetric retrieval.
    Chunks with similarity score below MIN_SIMILARITY_SCORE are filtered out.

    Args:
        package_id: Exact match on package_id.
        package_id_prefix: LIKE prefix match (e.g. 'project:' to match all projects).
        package_id_exclude_prefix: Exclude packages matching this prefix.
        tags: PostgreSQL array containment — chunk must have ALL listed tags.
        expand: If True and ANTHROPIC_API_KEY is set, expand query with
            domain-specific synonyms via Claude Haiku before embedding.
        reranker: If provided, rerank the top-k results using Voyage
            cross-encoder before returning. Retrieves 3x top_k candidates
            for the reranker to choose from.
        content_years: If provided, post-filter results to only include chunks
            whose content contains at least one of the specified years.
            Retrieves extra candidates to compensate for filtering.
    """
    if expand:
        anthropic_key = os.environ.get("ANTHROPIC_API_KEY", "")
        if anthropic_key:
            from .query_expansion import expand_query

            query_text = expand_query(query_text, anthropic_key)
            logger.debug("Expanded query: %s", query_text)

    embeddings = embedder.embed_texts([query_text], input_type="query")
    query_vec = embeddings[0]

    # When reranking or year-filtering, retrieve more candidates.
    # 4x gives the reranker/filter a wide enough pool to find the best matches.
    retrieval_k = top_k
    if reranker:
        retrieval_k = top_k * 4
    if content_years:
        retrieval_k = max(retrieval_k, top_k * 4)

    # Build SQL with pgvector cosine distance operator
    where_clauses = []
    params: dict = {"vec": str(query_vec), "k": retrieval_k}

    if chunk_type:
        where_clauses.append("chunk_type = :chunk_type")
        params["chunk_type"] = chunk_type
    if discipline:
        where_clauses.append("discipline = :discipline")
        params["discipline"] = discipline
    if package_id:
        where_clauses.append("package_id = :package_id")
        params["package_id"] = package_id
    if package_id_prefix:
        where_clauses.append("package_id LIKE :pkg_prefix")
        params["pkg_prefix"] = f"{package_id_prefix}%"
    if package_id_exclude_prefix:
        where_clauses.append("package_id NOT LIKE :pkg_excl_prefix")
        params["pkg_excl_prefix"] = f"{package_id_exclude_prefix}%"
    if tags:
        where_clauses.append("tags @> CAST(:tags AS text[])")
        # Format as PostgreSQL array literal
        params["tags"] = "{" + ",".join(tags) + "}"

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
        if float(row.score) >= MIN_SIMILARITY_SCORE
    ]
    if min_score > 0:
        results = [r for r in results if r["score"] >= min_score]

    filtered_count = len(rows) - len(results)
    if filtered_count > 0:
        logger.debug(
            "Filtered %d/%d chunks below score threshold %.2f",
            filtered_count,
            len(rows),
            MIN_SIMILARITY_SCORE,
        )

    # Year-based content filtering
    if content_years and results:
        year_strs = [str(y) for y in content_years]
        before_count = len(results)
        results = [
            r for r in results
            if any(ys in r["content"] for ys in year_strs)
        ]
        year_filtered = before_count - len(results)
        if year_filtered > 0:
            logger.debug(
                "Year filter: kept %d/%d chunks matching years %s",
                len(results),
                before_count,
                year_strs,
            )

    # Rerank if a reranker is provided
    if reranker and results:
        documents = [r["content"] for r in results]
        reranked = reranker.rerank(
            query=query_text, documents=documents, top_k=top_k,
        )
        # Rebuild results in reranked order, replacing score with relevance
        reranked_results = []
        for item in reranked:
            r = results[item["index"]].copy()
            r["score"] = item["relevance_score"]
            reranked_results.append(r)
        return reranked_results

    return results
