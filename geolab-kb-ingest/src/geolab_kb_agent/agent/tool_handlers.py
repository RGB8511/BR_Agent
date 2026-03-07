"""Tool handler implementations wrapping geolab_kb_ingest modules."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable
from typing import Any

from sqlalchemy import Engine

from geolab_kb_ingest.db import KBChunk, ValidatedRetrieval, chunk_to_dict, get_session
from geolab_kb_ingest.embedder import Embedder
from geolab_kb_ingest.query import query_chunks

from geolab_kb_agent.exports import create_export

from .projects import PROJECT_REGISTRY
from .provenance import ProvenanceCollector

logger = logging.getLogger(__name__)

# Type alias for handler functions
HandlerFn = Callable[[dict[str, Any], ProvenanceCollector], Awaitable[dict[str, Any]]]


def make_tool_handlers(engine: Engine, embedder: Embedder) -> dict[str, HandlerFn]:
    """Create tool handlers bound to the given engine and embedder."""

    async def handle_search_kb(
        args: dict[str, Any], provenance: ProvenanceCollector
    ) -> dict[str, Any]:
        query = args.get("query", "")
        chunk_type = args.get("chunk_type")
        discipline = args.get("discipline")
        top_k = min(args.get("top_k", 5), 20)
        source = args.get("source")
        project = args.get("project")
        year_min = args.get("year_min")
        year_max = args.get("year_max")

        # Build package_id filters from source / project params
        package_id: str | None = None
        package_id_prefix: str | None = None
        package_id_exclude_prefix: str | None = None

        if source == "project":
            package_id_prefix = "project:"
            if project:
                # Convert project name to package_id slug
                import re
                slug = project.lower().strip()
                slug = re.sub(r"[^\w\s-]", "", slug)
                slug = re.sub(r"[\s_]+", "-", slug)
                package_id = f"project:{slug.strip('-')}"
                package_id_prefix = None  # exact match takes precedence
        elif source == "kb":
            package_id_exclude_prefix = "project:"

        # Build content_years list from year_min/year_max
        content_years: list[int] | None = None
        if year_min is not None or year_max is not None:
            y_lo = year_min or 1900
            y_hi = year_max or 2099
            content_years = list(range(y_lo, y_hi + 1))

        results = await asyncio.to_thread(
            query_chunks,
            engine=engine,
            embedder=embedder,
            query_text=query,
            top_k=top_k,
            chunk_type=chunk_type,
            discipline=discipline,
            package_id=package_id,
            package_id_prefix=package_id_prefix,
            package_id_exclude_prefix=package_id_exclude_prefix,
            content_years=content_years,
        )

        # Apply validation boost: if this exact query was validated,
        # boost matching chunk scores by +0.15 (capped at 1.0)
        results = await asyncio.to_thread(
            _apply_validation_boost, query, results
        )

        provenance.add_kb_results(results)
        return {"results": results, "count": len(results)}

    async def handle_lookup_equation(
        args: dict[str, Any], provenance: ProvenanceCollector
    ) -> dict[str, Any]:
        equation_id = args.get("equation_id")

        # Direct ID lookup
        if equation_id:
            row = await asyncio.to_thread(_get_chunk_by_id, equation_id)
            if row:
                provenance.add_kb_results([row])
                return {"result": row}
            return {"error": f"Equation '{equation_id}' not found."}

        # Fallback to vector search filtered to equations
        query = args.get("query", "")
        if not query:
            return {"error": "Provide either equation_id or query."}

        top_k = min(args.get("top_k", 5), 20)
        results = await asyncio.to_thread(
            query_chunks,
            engine=engine,
            embedder=embedder,
            query_text=query,
            top_k=top_k,
            chunk_type="equation",
        )
        provenance.add_kb_results(results)
        return {"results": results, "count": len(results)}

    async def handle_lookup_table(
        args: dict[str, Any], provenance: ProvenanceCollector
    ) -> dict[str, Any]:
        table_id = args.get("table_id")

        # Direct ID lookup
        if table_id:
            row = await asyncio.to_thread(_get_chunk_by_id, table_id)
            if row:
                provenance.add_kb_results([row])
                return {"result": row}
            return {"error": f"Table '{table_id}' not found."}

        # Fallback to vector search filtered to tables
        query = args.get("query", "")
        if not query:
            return {"error": "Provide either table_id or query."}

        top_k = min(args.get("top_k", 5), 20)
        results = await asyncio.to_thread(
            query_chunks,
            engine=engine,
            embedder=embedder,
            query_text=query,
            top_k=top_k,
            chunk_type="table",
        )
        provenance.add_kb_results(results)
        return {"results": results, "count": len(results)}

    async def handle_get_package_info(
        args: dict[str, Any], provenance: ProvenanceCollector
    ) -> dict[str, Any]:
        package_id = args.get("package_id")

        if package_id:
            # Get manifest chunk for a specific package
            row = await asyncio.to_thread(_get_package_manifest, package_id)
            if row:
                provenance.add_kb_results([row])
                return {"result": row}
            return {"error": f"Package '{package_id}' not found."}

        # List all packages (distinct package_ids with their manifest info)
        packages = await asyncio.to_thread(_list_all_packages)
        return {"packages": packages, "count": len(packages)}

    _STOPWORDS = frozenset({
        "a", "an", "the", "is", "are", "was", "were", "what", "which",
        "who", "how", "when", "where", "why", "do", "does", "did", "can",
        "could", "would", "should", "will", "shall", "be", "been", "being",
        "have", "has", "had", "of", "in", "on", "at", "to", "for", "with",
        "from", "by", "about", "into", "and", "or", "not", "no", "it",
        "its", "this", "that", "these", "those", "my", "your", "me", "i",
        "show", "tell", "give", "find", "get", "list", "describe", "explain",
    })

    def _normalize_query(q: str) -> str:
        """Lowercase, collapse whitespace, strip punctuation for fuzzy matching."""
        import re
        q = q.lower().strip()
        q = re.sub(r"[^\w\s]", " ", q)
        return re.sub(r"\s+", " ", q).strip()

    def _content_words(q: str) -> set[str]:
        """Extract meaningful words (no stopwords) for overlap comparison."""
        return {w for w in _normalize_query(q).split() if w not in _STOPWORDS}

    def _apply_validation_boost(
        query_text: str, results: list[dict]
    ) -> list[dict]:
        """Boost validated chunks with query-aware scoring.

        - Exact query match (normalized): +0.15 per validated chunk
        - Chunk-only match (validated for a different query): +0.05
        - Re-sorts results after boosting so validated chunks float up
        """
        if not results:
            return results
        result_ids = [r.get("id") for r in results if r.get("id")]
        if not result_ids:
            return results

        normalized = _normalize_query(query_text)

        with get_session(engine) as session:
            validated = (
                session.query(
                    ValidatedRetrieval.chunk_id,
                    ValidatedRetrieval.query_text,
                )
                .filter(ValidatedRetrieval.chunk_id.in_(result_ids))
                .all()
            )
        if not validated:
            return results

        # Build boost map: chunk_id -> best boost level
        # Exact normalized match: +0.15
        # High keyword overlap (>50% content words): +0.10
        # Chunk-only match (low overlap): +0.05
        query_words = _content_words(query_text)

        boost_map: dict[str, float] = {}
        for chunk_id, validated_query in validated:
            norm_validated = _normalize_query(validated_query)
            if norm_validated == normalized:
                boost = 0.15
            else:
                validated_words = _content_words(validated_query)
                if query_words and validated_words:
                    overlap = len(query_words & validated_words) / max(len(query_words), len(validated_words))
                    boost = 0.10 if overlap > 0.5 else 0.05
                else:
                    boost = 0.05
            boost_map[chunk_id] = max(boost_map.get(chunk_id, 0), boost)

        # Apply boosts
        boosted = 0
        for r in results:
            rid = r.get("id")
            if rid in boost_map:
                old = r.get("score", 0)
                r["score"] = min(old + boost_map[rid], 1.0)
                r["validation_boosted"] = True
                boosted += 1

        if boosted:
            results.sort(key=lambda r: r.get("score", 0), reverse=True)
            logger.info(
                "Validation boost: %d chunks boosted for query '%s'",
                boosted, query_text[:80],
            )

        return results

    def _get_chunk_by_id(chunk_id: str) -> dict | None:
        """Direct lookup of a chunk by primary key."""
        with get_session(engine) as session:
            chunk = session.get(KBChunk, chunk_id)
            if chunk is None:
                return None
            return chunk_to_dict(chunk)

    def _get_package_manifest(package_id: str) -> dict | None:
        """Get the manifest chunk for a package."""
        with get_session(engine) as session:
            chunk = (
                session.query(KBChunk)
                .filter(
                    KBChunk.package_id == package_id,
                    KBChunk.chunk_type == "manifest",
                )
                .first()
            )
            if chunk is None:
                return None
            return chunk_to_dict(chunk)

    def _list_all_packages() -> list[dict]:
        """List all distinct packages with summary info."""
        with get_session(engine) as session:
            manifests = (
                session.query(KBChunk)
                .filter(KBChunk.chunk_type == "manifest")
                .order_by(KBChunk.package_id)
                .all()
            )
            return [
                {
                    "package_id": m.package_id,
                    "title": m.title,
                    "discipline": m.discipline,
                    "level": m.level,
                    "tags": m.tags,
                }
                for m in manifests
            ]

    async def handle_export_data(
        args: dict[str, Any], provenance: ProvenanceCollector
    ) -> dict[str, Any]:
        columns = args.get("columns", [])
        rows = args.get("rows", [])
        fmt = args.get("format", "csv")
        filename = args.get("filename")
        title = args.get("title")

        if not columns or not rows:
            return {"error": "Columns and rows are required."}
        if not all(isinstance(c, str) for c in columns):
            return {"error": "All column headers must be strings."}
        if not all(isinstance(r, list) for r in rows):
            return {"error": "Each row must be a list of values."}

        try:
            ef = create_export(
                columns=columns,
                rows=rows,
                fmt=fmt,
                filename=filename,
                title=title,
            )
        except ValueError as exc:
            return {"error": str(exc)}
        return {
            "file_id": ef.file_id,
            "filename": ef.filename,
            "download_url": f"/api/v1/chat/downloads/{ef.file_id}",
            "rows_exported": ef.row_count,
            "format": ef.format,
        }

    async def handle_list_projects(
        args: dict[str, Any], provenance: ProvenanceCollector
    ) -> dict[str, Any]:
        return {
            "projects": [p.to_dict() for p in PROJECT_REGISTRY],
            "count": len(PROJECT_REGISTRY),
        }

    return {
        "search_kb": handle_search_kb,
        "lookup_equation": handle_lookup_equation,
        "lookup_table": handle_lookup_table,
        "get_package_info": handle_get_package_info,
        "export_data": handle_export_data,
        "list_projects": handle_list_projects,
    }
