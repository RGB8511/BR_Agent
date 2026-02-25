"""Tool handler implementations wrapping geolab_kb_ingest modules."""

from __future__ import annotations

import asyncio
import json
import logging
from typing import Any, Callable, Awaitable

from sqlalchemy import Engine

from geolab_kb_ingest.db import KBChunk, get_session
from geolab_kb_ingest.embedder import Embedder
from geolab_kb_ingest.query import query_chunks

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

        results = await asyncio.to_thread(
            query_chunks,
            engine=engine,
            embedder=embedder,
            query_text=query,
            top_k=top_k,
            chunk_type=chunk_type,
            discipline=discipline,
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

    def _get_chunk_by_id(chunk_id: str) -> dict | None:
        """Direct lookup of a chunk by primary key."""
        with get_session(engine) as session:
            chunk = session.get(KBChunk, chunk_id)
            if chunk is None:
                return None
            return _chunk_to_dict(chunk)

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
            return _chunk_to_dict(chunk)

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

    def _chunk_to_dict(chunk: KBChunk) -> dict:
        """Convert a KBChunk ORM object to a plain dict."""
        return {
            "id": chunk.id,
            "title": chunk.title,
            "content": chunk.content,
            "chunk_type": chunk.chunk_type,
            "package_id": chunk.package_id,
            "discipline": chunk.discipline,
            "tags": chunk.tags,
            "metadata": chunk.metadata_,
        }

    return {
        "search_kb": handle_search_kb,
        "lookup_equation": handle_lookup_equation,
        "lookup_table": handle_lookup_table,
        "get_package_info": handle_get_package_info,
    }
