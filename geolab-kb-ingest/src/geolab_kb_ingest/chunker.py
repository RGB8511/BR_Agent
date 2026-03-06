"""Chunking strategies for GeoLab knowledge packages.

Each package contains 5 files: _manifest.json, theory.md, equations.json,
tables.json, and standards.md.  This module converts them into Chunk objects
ready for embedding and storage.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from .db import count_tokens as _count_tokens


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------
@dataclass
class Chunk:
    id: str
    package_id: str
    chunk_type: str  # "theory"|"equation"|"table"|"standard"|"manifest"
    title: str
    content: str  # rendered text for embedding
    metadata: dict = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    discipline: str = ""
    level: int = 0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _slugify(text: str) -> str:
    """Convert a heading to a URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")



# ---------------------------------------------------------------------------
# Manifest chunking
# ---------------------------------------------------------------------------
def chunk_manifest(manifest: dict) -> Chunk:
    """Render the manifest as a searchable summary text."""
    pkg_id = manifest["id"]
    lines = [
        f"Package: {manifest['name']}",
        f"ID: {pkg_id}",
        f"Discipline: {manifest.get('discipline', '')}",
        f"Level: {manifest.get('level', 0)} ({manifest.get('textbook_level', '')})",
    ]
    if manifest.get("dependencies"):
        lines.append(f"Dependencies: {', '.join(manifest['dependencies'])}")
    if manifest.get("tags"):
        lines.append(f"Tags: {', '.join(manifest['tags'])}")
    if manifest.get("standards"):
        lines.append(f"Standards: {', '.join(manifest['standards'])}")
    if manifest.get("key_references"):
        lines.append("Key References:")
        for ref in manifest["key_references"]:
            lines.append(f"  - {ref}")
    lines.append(
        f"Content: {manifest.get('equation_count', 0)} equations, "
        f"{manifest.get('table_count', 0)} tables, "
        f"{manifest.get('concept_count', 0)} concepts"
    )
    content = "\n".join(lines)
    return Chunk(
        id=f"{pkg_id}.manifest",
        package_id=pkg_id,
        chunk_type="manifest",
        title=manifest["name"],
        content=content,
        metadata={k: v for k, v in manifest.items() if k not in ("tags",)},
        tags=manifest.get("tags", []),
        discipline=manifest.get("discipline", ""),
        level=manifest.get("level", 0),
    )


# ---------------------------------------------------------------------------
# Theory chunking
# ---------------------------------------------------------------------------
def chunk_theory(text: str, manifest: dict, max_tokens: int) -> list[Chunk]:
    """Split theory.md on H2 headings, sub-split long sections on H3."""
    pkg_id = manifest["id"]
    tags = manifest.get("tags", [])
    discipline = manifest.get("discipline", "")
    level = manifest.get("level", 0)

    # Split on H2 — keep delimiter with lookahead
    sections = re.split(r"(?=^## )", text, flags=re.MULTILINE)
    chunks: list[Chunk] = []

    for section in sections:
        section = section.strip()
        if not section:
            continue

        # Extract heading
        first_line = section.split("\n", 1)[0]
        heading = re.sub(r"^#+\s*", "", first_line).strip()
        if not heading:
            heading = manifest.get("name", "Introduction")

        if _count_tokens(section) <= max_tokens:
            slug = _slugify(heading)
            chunks.append(Chunk(
                id=f"{pkg_id}.theory.{slug}",
                package_id=pkg_id,
                chunk_type="theory",
                title=heading,
                content=section,
                tags=tags,
                discipline=discipline,
                level=level,
            ))
        else:
            # Sub-split on H3
            sub_sections = re.split(r"(?=^### )", section, flags=re.MULTILINE)
            h2_heading = heading
            for sub in sub_sections:
                sub = sub.strip()
                if not sub:
                    continue
                sub_first = sub.split("\n", 1)[0]
                sub_heading = re.sub(r"^#+\s*", "", sub_first).strip()
                if not sub_heading:
                    sub_heading = h2_heading

                # Prepend H2 heading if this is an H3 sub-chunk
                if sub.startswith("### "):
                    sub = f"## {h2_heading}\n\n{sub}"
                    title = f"{h2_heading} > {sub_heading}"
                else:
                    title = sub_heading

                slug = _slugify(title)
                chunks.append(Chunk(
                    id=f"{pkg_id}.theory.{slug}",
                    package_id=pkg_id,
                    chunk_type="theory",
                    title=title,
                    content=sub,
                    tags=tags,
                    discipline=discipline,
                    level=level,
                ))

    return chunks


# ---------------------------------------------------------------------------
# Equation chunking
# ---------------------------------------------------------------------------
def chunk_equations(equations: list[dict], manifest: dict) -> list[Chunk]:
    """One chunk per equation, rendered as prose."""
    pkg_id = manifest["id"]
    tags = manifest.get("tags", [])
    discipline = manifest.get("discipline", "")
    level = manifest.get("level", 0)

    chunks: list[Chunk] = []
    for eq in equations:
        # Some entries are reference data (have "data" instead of "equation")
        if "equation" not in eq:
            # Render as a reference-data chunk
            import json as _json
            data_text = _json.dumps(eq.get("data", {}), indent=2, ensure_ascii=False)
            parts = [f"{eq['title']}", f"Data:\n{data_text}"]
            if eq.get("source"):
                parts.append(f"Source: {eq['source']}")
            content = "\n".join(parts)
            eq_id = eq.get("id", f"{pkg_id}.eq-unknown")
            chunks.append(Chunk(
                id=eq_id,
                package_id=pkg_id,
                chunk_type="equation",
                title=eq["title"],
                content=content,
                metadata=eq,
                tags=tags,
                discipline=discipline,
                level=level,
            ))
            continue

        parts = [f"{eq['title']}: {eq['equation']}"]

        # Variables
        if eq.get("variables"):
            var_parts = []
            for var_name, info in eq["variables"].items():
                desc = info.get("description", "")
                units = info.get("units", "")
                var_parts.append(f"{var_name}: {desc} ({units})")
            parts.append(f"Variables: {', '.join(var_parts)}")

        # Optional fields
        if eq.get("applicability"):
            parts.append(f"Applicability: {eq['applicability']}")
        if eq.get("alt_form"):
            parts.append(f"Alternative form: {eq['alt_form']}")
        if eq.get("criteria"):
            criteria_parts = [f"{k}: {v}" for k, v in eq["criteria"].items()]
            parts.append(f"Criteria: {'; '.join(criteria_parts)}")

        parts.append(f"Source: {eq.get('source', 'N/A')}")

        content = "\n".join(parts)
        eq_id = eq.get("id", f"{pkg_id}.eq-unknown")

        chunks.append(Chunk(
            id=eq_id,
            package_id=pkg_id,
            chunk_type="equation",
            title=eq["title"],
            content=content,
            metadata=eq,
            tags=tags,
            discipline=discipline,
            level=level,
        ))

    return chunks


# ---------------------------------------------------------------------------
# Table chunking
# ---------------------------------------------------------------------------
def chunk_tables(tables: list[dict], manifest: dict) -> list[Chunk]:
    """One chunk per table, rendered as markdown table."""
    pkg_id = manifest["id"]
    tags = manifest.get("tags", [])
    discipline = manifest.get("discipline", "")
    level = manifest.get("level", 0)

    chunks: list[Chunk] = []
    for tbl in tables:
        data = tbl.get("data", {})
        headers = data.get("headers", [])
        rows = data.get("rows", [])

        # Render
        lines = [f"{tbl['title']} ({tbl.get('type', 'reference')})"]
        if headers:
            lines.append("| " + " | ".join(headers) + " |")
            lines.append("| " + " | ".join("---" for _ in headers) + " |")
        for row in rows:
            lines.append("| " + " | ".join(str(c) for c in row) + " |")
        lines.append(f"Source: {tbl.get('source', 'N/A')}")

        content = "\n".join(lines)
        tbl_id = tbl.get("id", f"{pkg_id}.tbl-unknown")

        chunks.append(Chunk(
            id=tbl_id,
            package_id=pkg_id,
            chunk_type="table",
            title=tbl["title"],
            content=content,
            metadata=tbl,
            tags=tags,
            discipline=discipline,
            level=level,
        ))

    return chunks


# ---------------------------------------------------------------------------
# Standards chunking
# ---------------------------------------------------------------------------
def chunk_standards(text: str, manifest: dict) -> list[Chunk]:
    """Split standards.md on H2 headers."""
    pkg_id = manifest["id"]
    tags = manifest.get("tags", [])
    discipline = manifest.get("discipline", "")
    level = manifest.get("level", 0)

    sections = re.split(r"(?=^## )", text, flags=re.MULTILINE)
    chunks: list[Chunk] = []

    for section in sections:
        section = section.strip()
        if not section:
            continue

        first_line = section.split("\n", 1)[0]
        heading = re.sub(r"^#+\s*", "", first_line).strip()
        if not heading:
            heading = "Standards Overview"

        slug = _slugify(heading)
        chunks.append(Chunk(
            id=f"{pkg_id}.std.{slug}",
            package_id=pkg_id,
            chunk_type="standard",
            title=heading,
            content=section,
            tags=tags,
            discipline=discipline,
            level=level,
        ))

    return chunks


# ---------------------------------------------------------------------------
# Package-level entry point
# ---------------------------------------------------------------------------
def chunk_package(package_dir: Path, max_tokens: int = 1500) -> list[Chunk]:
    """Read all 5 files from a package directory and return combined chunks."""
    manifest_path = package_dir / "_manifest.json"
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    chunks: list[Chunk] = []

    # Manifest
    chunks.append(chunk_manifest(manifest))

    # Theory
    theory_path = package_dir / "theory.md"
    if theory_path.exists():
        theory_text = theory_path.read_text(encoding="utf-8")
        chunks.extend(chunk_theory(theory_text, manifest, max_tokens))

    # Equations
    eq_path = package_dir / "equations.json"
    if eq_path.exists():
        with open(eq_path, encoding="utf-8") as f:
            equations = json.load(f)
        chunks.extend(chunk_equations(equations, manifest))

    # Tables
    tbl_path = package_dir / "tables.json"
    if tbl_path.exists():
        with open(tbl_path, encoding="utf-8") as f:
            tables = json.load(f)
        chunks.extend(chunk_tables(tables, manifest))

    # Standards
    std_path = package_dir / "standards.md"
    if std_path.exists():
        std_text = std_path.read_text(encoding="utf-8")
        chunks.extend(chunk_standards(std_text, manifest))

    return chunks
