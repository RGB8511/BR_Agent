"""Citation and provenance tracking for agent responses."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


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
                doc_groups[doc_name] = {
                    "document_name": doc_name,
                    "project": project,
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
