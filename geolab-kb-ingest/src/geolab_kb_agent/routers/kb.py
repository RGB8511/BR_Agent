"""KB router — GET /api/v1/kb/topology."""

from __future__ import annotations

import logging
from collections import defaultdict
from typing import Any

from fastapi import APIRouter, Request
from sqlalchemy import text

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/kb", tags=["kb"])


@router.get("/topology")
async def kb_topology(request: Request) -> dict[str, Any]:
    """Return the KB tree structure grouped by discipline/package/chunk_type."""
    engine = request.app.state.engine

    query = text(
        "SELECT discipline, package_id, chunk_type, COUNT(*) AS cnt "
        "FROM kb_chunks GROUP BY discipline, package_id, chunk_type "
        "ORDER BY discipline, package_id, chunk_type"
    )

    with engine.connect() as conn:
        rows = conn.execute(query).fetchall()

    # Build nested structure: discipline -> package_id -> {chunk_types, count}
    disc_map: dict[str, dict[str, dict[str, Any]]] = defaultdict(
        lambda: defaultdict(lambda: {"chunk_types": defaultdict(int), "count": 0})
    )

    for row in rows:
        discipline = row[0] or "unknown"
        package_id = row[1] or "unknown"
        chunk_type = row[2] or "unknown"
        cnt = row[3]

        disc_map[discipline][package_id]["chunk_types"][chunk_type] += cnt
        disc_map[discipline][package_id]["count"] += cnt

    # Separate project packages from KB discipline packages
    project_children: list[dict[str, Any]] = []
    discipline_children: list[dict[str, Any]] = []

    for discipline, packages in sorted(disc_map.items()):
        disc_packages: list[dict[str, Any]] = []
        disc_total = 0

        for package_id, info in sorted(packages.items()):
            pkg_count = info["count"]
            disc_total += pkg_count

            if package_id.startswith("project:"):
                # Project packages go at the top level
                project_slug = package_id.removeprefix("project:")
                label = project_slug.replace("-", " ").title()
                project_children.append({
                    "id": package_id,
                    "label": label,
                    "project_slug": project_slug,
                    "chunk_count": pkg_count,
                    "chunk_types": dict(info["chunk_types"]),
                })
            else:
                # KB discipline packages
                # Extract short label from package_id (last segment)
                parts = package_id.split(".")
                short_label = parts[-1].replace("-", " ").title() if parts else package_id
                disc_packages.append({
                    "id": package_id,
                    "label": short_label,
                    "package_id": package_id,
                    "chunk_count": pkg_count,
                    "chunk_types": dict(info["chunk_types"]),
                })

        if disc_packages:
            discipline_children.append({
                "id": f"disc:{discipline}",
                "label": discipline.replace("-", " ").title(),
                "discipline": discipline,
                "chunk_count": disc_total,
                "children": disc_packages,
            })

    # Build final tree
    children: list[dict[str, Any]] = discipline_children + project_children

    tree = {
        "id": "router",
        "label": "GeoLab Routing Agent",
        "children": children,
    }

    return {"tree": tree}
