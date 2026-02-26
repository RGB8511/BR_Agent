"""Citation and provenance tracking for agent responses."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Citation:
    """A single data-provenance citation."""

    source_table: str
    record_id: str
    field_name: str | None = None
    value: str | None = None
    snippet: str | None = None

    def to_dict(self) -> dict:
        d: dict = {"source_table": self.source_table, "record_id": self.record_id}
        if self.field_name is not None:
            d["field_name"] = self.field_name
        if self.value is not None:
            d["value"] = self.value
        if self.snippet is not None:
            d["snippet"] = self.snippet
        return d


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
    ) -> None:
        self.citations.append(
            Citation(
                source_table=source_table,
                record_id=record_id,
                field_name=field_name,
                value=value,
                snippet=snippet,
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
            )

    def to_list(self) -> list[dict]:
        # De-duplicate by (source_table, record_id)
        seen: set[tuple[str, str]] = set()
        unique: list[dict] = []
        for c in self.citations:
            key = (c.source_table, c.record_id)
            if key not in seen:
                seen.add(key)
                unique.append(c.to_dict())
        return unique
