"""Chunk enrichment for improved embedding quality.

Constructs enriched embedding text with targeted improvements:
- OCR title cleanup for garbled boring log documents
- Table section context (concise, no full metadata prefix)
- Leaves narrative content unchanged to preserve content signal

Design principle: minimal intervention. Only enrich where there's a
clear information deficit (garbled titles, contextless tables).
Avoid blanket metadata prefixes that dilute the content signal.
"""

from __future__ import annotations

import re

from .db import KBChunk


# ---------------------------------------------------------------------------
# OCR title overrides
# ---------------------------------------------------------------------------
TITLE_OVERRIDES: dict[str, str] = {
    "doc02_wsrb_1959_boring_logs": "WSRB 1959 Boring Logs — Juniper Canyon Dam",
    "doc08_idse_2025_boring_logs": "IDSE 2025 Boring Logs — Juniper Canyon Dam",
}

# Lines injected by doc_chunker that should be stripped before table parsing
_CONTEXT_LINE_RE = re.compile(r"^\[(?:Section|Source|TABLE):")


def clean_title(chunk: KBChunk) -> str:
    """Return a corrected title if the chunk's source doc has OCR issues."""
    filename = (chunk.metadata_ or {}).get("filename", "")
    for prefix, clean in TITLE_OVERRIDES.items():
        if filename.startswith(prefix):
            return clean
    return chunk.title


# ---------------------------------------------------------------------------
# Table context
# ---------------------------------------------------------------------------
def _strip_context_lines(text: str) -> str:
    """Remove [Section:...] and [Source:...] context lines from table content."""
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if _CONTEXT_LINE_RE.match(stripped):
            continue
        lines.append(line)
    return "\n".join(lines)


def _build_table_context(chunk: KBChunk) -> str:
    """Build a brief context line for table chunks from the section title.

    Only adds the section name as a natural-language lead-in, which helps
    the embedding model understand what data the table contains without
    the noise of a full metadata prefix.
    """
    section = (chunk.metadata_ or {}).get("section", "")
    if section:
        return f"This table presents {section}."
    return ""


# ---------------------------------------------------------------------------
# Enrichment functions
# ---------------------------------------------------------------------------
def enrich_narrative_chunk(chunk: KBChunk) -> str:
    """Return content as-is for narrative chunks.

    Narrative content already has strong semantic signal.
    Adding metadata prefixes consistently dilutes it.
    """
    return chunk.content


def enrich_table_chunk(chunk: KBChunk) -> str:
    """Return section context + cleaned table content.

    Tables embed poorly because pipe-delimited format lacks semantic
    signal. A brief section-title lead-in helps the embedding model
    understand the table's topic.
    """
    table_ctx = _build_table_context(chunk)
    cleaned = _strip_context_lines(chunk.content).strip()

    if table_ctx:
        return table_ctx + "\n" + chunk.content
    return chunk.content


def enrich_chunk(chunk: KBChunk) -> str:
    """Dispatch to the appropriate enrichment function based on chunk_type."""
    if chunk.chunk_type == "table":
        return enrich_table_chunk(chunk)
    return enrich_narrative_chunk(chunk)
