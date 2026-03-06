"""Tool handler implementations wrapping geolab_kb_ingest modules."""

from __future__ import annotations

import asyncio
import json
import logging
from typing import Any, Callable, Awaitable

from sqlalchemy import Engine

from geolab_kb_ingest.db import KBChunk, ValidatedRetrieval, chunk_to_dict, get_session
from geolab_kb_ingest.embedder import Embedder
from geolab_kb_ingest.query import query_chunks

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

    def _apply_validation_boost(
        query_text: str, results: list[dict]
    ) -> list[dict]:
        """Boost the top validated chunk's score.

        Only the single highest-scoring validated chunk gets +0.15,
        which widens the gap between #1 and #2 and pushes confidence
        from MEDIUM to HIGH.

        Matches on chunk_id only (ignoring query_text) so the boost
        works even when the LLM reformulates the user's question.
        """
        if not results:
            return results
        result_ids = [r.get("id") for r in results if r.get("id")]
        if not result_ids:
            return results
        with get_session(engine) as session:
            validated = (
                session.query(ValidatedRetrieval.chunk_id)
                .filter(ValidatedRetrieval.chunk_id.in_(result_ids))
                .all()
            )
            validated_ids = {row[0] for row in validated}
        if not validated_ids:
            return results

        # Find the highest-scoring validated chunk and boost only that one
        best_idx = None
        best_score = -1.0
        for i, r in enumerate(results):
            if r.get("id") in validated_ids and r.get("score", 0) > best_score:
                best_score = r.get("score", 0)
                best_idx = i
        if best_idx is not None:
            results[best_idx]["score"] = min(results[best_idx].get("score", 0) + 0.15, 1.0)
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
        "list_projects": handle_list_projects,
    }
