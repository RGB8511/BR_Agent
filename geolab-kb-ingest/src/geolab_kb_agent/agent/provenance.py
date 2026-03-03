"""Citation and provenance tracking for agent responses."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

# ---------------------------------------------------------------------------
# Citation formatting helpers
# ---------------------------------------------------------------------------

# 4-digit year in a date metadata field (1900-2099)
_DATE_YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")

# Year from filename pattern: docNN_abbr_YYYY_...
_FILENAME_YEAR_RE = re.compile(r"^doc\d+_[a-z]+_(\d{4})_")

# Firm abbreviation from filename: docNN_ABBR_...
_FILENAME_FIRM_RE = re.compile(r"^doc\d+_([a-z]+)_")

# Maps abbreviations to full firm / agency names
_FIRM_ABBR: dict[str, str] = {
    "idse": "Intermountain Dam Safety Engineers, LLC",
    "wsrb": "Washington State Reclamation Board",
    "fhsc": "FH Stoltze Consulting",
    "sdwr": "State Division of Water Resources",
    "jbid": "Joint Board of Irrigation Districts",
    "rvic": "Rimrock Valley Irrigation Company",
}


def _extract_year(meta: dict[str, Any]) -> str | None:
    """Try date field for a valid year, then filename pattern, else None."""
    date_val = meta.get("date", "")
    if date_val:
        m = _DATE_YEAR_RE.search(str(date_val))
        if m:
            return m.group(0)
    filename = meta.get("filename", "")
    if filename:
        m = _FILENAME_YEAR_RE.match(filename.lower())
        if m:
            return m.group(1)
    return None


def _extract_author(meta: dict[str, Any]) -> str | None:
    """Try author field, then firm abbreviation lookup, else None."""
    author = meta.get("author", "")
    if author and author.strip():
        return author.strip()
    filename = meta.get("filename", "")
    if filename:
        m = _FILENAME_FIRM_RE.match(filename.lower())
        if m:
            return _FIRM_ABBR.get(m.group(1))
    return None


def _title_case(text: str) -> str:
    """Convert ALL-CAPS OCR text to title case; leave mixed-case alone."""
    if text.isupper():
        return text.title()
    return text


def _clean_csv_title(title: str) -> str:
    """Normalise CSV-derived titles.

    Example: "Data I1 Ucs Dacite Tuff" -> "UCS Test Data — Dacite Tuff"
    """
    if not title:
        return title
    # Strip leading "Data XX " prefix
    cleaned = re.sub(r"^Data\s+[A-Za-z0-9]+\s+", "", title, flags=re.IGNORECASE)
    # Uppercase known acronyms
    acronyms = {"ucs", "pls", "bts", "xrd", "xrf", "spt", "cpt", "uscs"}
    words = cleaned.split()
    normalised = []
    for w in words:
        if w.lower() in acronyms:
            normalised.append(w.upper())
        else:
            normalised.append(_title_case(w))
    cleaned = " ".join(normalised)
    # If the first word is an acronym, append " Test Data"
    if normalised and normalised[0].isupper() and normalised[0].lower() in acronyms:
        first = normalised[0]
        rest = " ".join(normalised[1:])
        cleaned = f"{first} Test Data" + (f" \u2014 {rest}" if rest else "")
    return cleaned


# --- Per-type formatters ---------------------------------------------------

def _format_pdf_citation(
    meta: dict[str, Any], package_id: str | None, title: str | None,
) -> str:
    author = _extract_author(meta)
    year = _extract_year(meta)
    doc_title = title or meta.get("title", "")
    if doc_title:
        doc_title = _title_case(doc_title)
    project = meta.get("project", "")
    discipline = meta.get("discipline", "")

    parts: list[str] = []
    # Author (Year).
    if author and year:
        parts.append(f"{author} ({year}).")
    elif author:
        parts.append(f"{author} (n.d.).")
    elif year:
        parts.append(f"({year}).")

    # Title.
    if doc_title:
        parts.append(f"{doc_title}.")

    # Project.
    if project:
        parts.append(f"{project}.")

    # [Discipline] tag
    if discipline:
        parts.append(f"[{_title_case(discipline)}]")

    return " ".join(parts) if parts else ""


def _format_csv_citation(
    meta: dict[str, Any], package_id: str | None, title: str | None,
) -> str:
    raw_title = title or meta.get("title", "")
    cleaned = _clean_csv_title(raw_title) if raw_title else ""
    project = meta.get("project", "")

    parts: list[str] = []
    if cleaned:
        parts.append(f"{cleaned}.")
    if project:
        parts.append(f"{project}.")
    parts.append("[Laboratory Data]")
    return " ".join(parts)


def _format_kb_citation(
    meta: dict[str, Any], package_id: str | None, title: str | None,
) -> str:
    doc_title = title or meta.get("title", "")
    if doc_title:
        doc_title = _title_case(doc_title)
    standard = meta.get("standard", "")

    parts: list[str] = []
    if doc_title:
        parts.append(f"{doc_title}.")
    if standard:
        parts.append(f"{standard}.")
    parts.append("[Reference KB]")
    return " ".join(parts)


def format_citation(
    metadata: dict[str, Any] | None,
    chunk_type: str | None,
    package_id: str | None,
    title: str | None,
) -> str:
    """Build a scientific-style citation string from chunk metadata."""
    meta = metadata or {}
    ct = (chunk_type or "").lower()

    if ct == "csv" or ct == "lab":
        return _format_csv_citation(meta, package_id, title)
    if ct in ("kb", "reference", "knowledge_base"):
        return _format_kb_citation(meta, package_id, title)
    # Default: PDF / project document
    return _format_pdf_citation(meta, package_id, title)


@dataclass
class Citation:
    """A single data-provenance citation with full chunk metadata."""

    source_table: str
    record_id: str
    field_name: str | None = None
    value: str | None = None
    snippet: str | None = None
    score: float | None = None
    chunk_type: str | None = None
    package_id: str | None = None
    discipline: str | None = None
    metadata: dict[str, Any] | None = None

    def to_dict(self) -> dict:
        d: dict = {"source_table": self.source_table, "record_id": self.record_id}
        if self.field_name is not None:
            d["field_name"] = self.field_name
        if self.value is not None:
            d["value"] = self.value
        if self.snippet is not None:
            d["snippet"] = self.snippet
        if self.score is not None:
            d["score"] = self.score
        if self.chunk_type is not None:
            d["chunk_type"] = self.chunk_type
        if self.package_id is not None:
            d["package_id"] = self.package_id
        if self.discipline is not None:
            d["discipline"] = self.discipline
        if self.metadata is not None:
            d["metadata"] = self.metadata
        return d

    def to_retrieved_chunk(self, source_number: int) -> dict:
        """Convert to RetrievedChunk-compatible dict for API response."""
        # Extract document_name from package_id or metadata
        doc_name = ""
        section = None
        page_number = None

        if self.metadata:
            doc_name = self.metadata.get("source_file", "")
            section = self.metadata.get("section")
            page_number = self.metadata.get("page_number")
            if page_number is not None:
                try:
                    page_number = int(page_number)
                except (ValueError, TypeError):
                    page_number = None

        if not doc_name and self.package_id:
            doc_name = self.package_id

        return {
            "chunk_id": self.record_id,
            "document_name": doc_name,
            "section": section or self.value,
            "page_number": page_number,
            "chunk_text": self.snippet or "",
            "similarity_score": self.score or 0.0,
            "chunk_type": self.chunk_type,
            "metadata": self.metadata,
        }


@dataclass
class ProvenanceCollector:
    """Accumulates citations during an agent tool-use cycle."""

    citations: list[Citation] = field(default_factory=list)

    def add(
        self,
        source_table: str,
        record_id: str,
        field_name: str | None = None,
        value: str | None = None,
        snippet: str | None = None,
        score: float | None = None,
        chunk_type: str | None = None,
        package_id: str | None = None,
        discipline: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        self.citations.append(
            Citation(
                source_table=source_table,
                record_id=record_id,
                field_name=field_name,
                value=value,
                snippet=snippet,
                score=score,
                chunk_type=chunk_type,
                package_id=package_id,
                discipline=discipline,
                metadata=metadata,
            )
        )

    def add_kb_results(self, results: list[dict]) -> None:
        """Add a citation for each KB search result."""
        for row in results:
            content = str(row.get("content", ""))
            snippet = content[:200].rstrip() + ("..." if len(content) > 200 else "")
            self.add(
                source_table="kb_chunks",
                record_id=str(row.get("id", "unknown")),
                field_name="title",
                value=str(row.get("title", "")),
                snippet=snippet,
                score=row.get("score"),
                chunk_type=row.get("chunk_type"),
                package_id=row.get("package_id"),
                discipline=row.get("discipline"),
                metadata=row.get("metadata"),
            )

    def to_list(self) -> list[dict]:
        """Return deduplicated citations as dicts (legacy format)."""
        seen: set[tuple[str, str]] = set()
        unique: list[dict] = []
        for c in self.citations:
            key = (c.source_table, c.record_id)
            if key not in seen:
                seen.add(key)
                unique.append(c.to_dict())
        return unique

    def to_retrieved_chunks(self) -> list[dict]:
        """Return deduplicated citations as RetrievedChunk-compatible dicts."""
        seen: set[tuple[str, str]] = set()
        unique: list[dict] = []
        n = 0
        for c in self.citations:
            key = (c.source_table, c.record_id)
            if key not in seen:
                seen.add(key)
                n += 1
                unique.append(c.to_retrieved_chunk(n))
        return unique

    def to_grouped_chunks(self) -> list[dict]:
        """Return citations grouped by source document.

        Each group: {
            "doc_number": 1,
            "document_name": "doc06_idse_2025_geotech_arch.pdf",
            "project": "Rimrock Diversion Dam",
            "sub_refs": [
                {"letter": "a", "section": "...", "page_number": 3, ...},
                {"letter": "b", ...},
            ]
        }
        """
        seen: set[tuple[str, str]] = set()
        doc_groups: dict[str, dict] = {}   # keyed by document_name
        doc_order: list[str] = []          # preserves first-appearance order

        for c in self.citations:
            key = (c.source_table, c.record_id)
            if key in seen:
                continue
            seen.add(key)

            doc_name = ""
            section = None
            page_number = None
            project = None
            if c.metadata:
                doc_name = c.metadata.get("filename", "")
                section = c.metadata.get("section")
                page_number = c.metadata.get("page_number")
                project = c.metadata.get("project")
            if not doc_name:
                doc_name = c.package_id or c.record_id

            if doc_name not in doc_groups:
                doc_order.append(doc_name)
                citation = format_citation(
                    metadata=c.metadata,
                    chunk_type=c.chunk_type,
                    package_id=c.package_id,
                    title=c.value,
                )
                doc_groups[doc_name] = {
                    "document_name": doc_name,
                    "project": project,
                    "display_citation": citation,
                    "sub_refs": [],
                }

            idx = len(doc_groups[doc_name]["sub_refs"])
            letter = chr(ord("a") + idx) if idx < 26 else str(idx + 1)

            if page_number is not None:
                try:
                    page_number = int(page_number)
                except (ValueError, TypeError):
                    page_number = None

            doc_groups[doc_name]["sub_refs"].append({
                "letter": letter,
                "chunk_id": c.record_id,
                "section": section or c.value,
                "page_number": page_number,
                "chunk_text": c.snippet or "",
                "similarity_score": c.score or 0.0,
                "chunk_type": c.chunk_type,
                "metadata": c.metadata,
            })

        result = []
        for i, doc_name in enumerate(doc_order):
            group = doc_groups[doc_name]
            group["doc_number"] = i + 1
            result.append(group)
        return result
