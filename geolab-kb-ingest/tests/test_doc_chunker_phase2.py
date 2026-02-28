"""Tests for Phase 2 doc_chunker improvements: section context and source prefix."""

from __future__ import annotations

from geolab_kb_ingest.doc_chunker import (
    _split_table_and_narrative,
    chunk_document,
)


class TestSplitTableAndNarrative:
    """Tests for the updated _split_table_and_narrative with section parsing."""

    def test_narrative_only(self):
        segments = _split_table_and_narrative("Just some text here.")
        assert len(segments) == 1
        assert segments[0][0] == "narrative"
        assert segments[0][2] is None  # no section

    def test_table_with_section(self):
        text = "Intro text.\n[TABLE:4.2 — Lab Results]\nA | B\n1 | 2\n[/TABLE]\nMore text."
        segments = _split_table_and_narrative(text)
        assert len(segments) == 3
        # First segment: narrative
        assert segments[0][0] == "narrative"
        # Second segment: table with section
        assert segments[1][0] == "table"
        assert segments[1][2] == "4.2 — Lab Results"
        assert "A | B" in segments[1][1]
        # Third segment: narrative
        assert segments[2][0] == "narrative"

    def test_table_without_section(self):
        text = "Before.\n[TABLE:]\nX | Y\n[/TABLE]\nAfter."
        segments = _split_table_and_narrative(text)
        table_seg = [s for s in segments if s[0] == "table"]
        assert len(table_seg) == 1
        assert table_seg[0][2] is None  # empty section -> None

    def test_multiple_tables(self):
        text = (
            "Intro.\n"
            "[TABLE:Section A]\nA1 | A2\n[/TABLE]\n"
            "Middle.\n"
            "[TABLE:Section B]\nB1 | B2\n[/TABLE]\n"
            "End."
        )
        segments = _split_table_and_narrative(text)
        tables = [s for s in segments if s[0] == "table"]
        assert len(tables) == 2
        assert tables[0][2] == "Section A"
        assert tables[1][2] == "Section B"


class TestChunkDocumentContextEnrichment:
    """Tests for section context on tables and source prefix on narratives."""

    def _make_meta(self, filename="test.pdf", title="Test Doc"):
        return {"filename": filename, "title": title}

    def test_first_narrative_has_source_prefix(self):
        text = "This is a narrative paragraph about testing."
        chunks = chunk_document(
            text, self._make_meta(), "pkg:test", max_tokens=512,
        )
        assert len(chunks) >= 1
        assert chunks[0].content.startswith("[Source: test.pdf, Test Doc]")

    def test_table_chunk_has_source_tag(self):
        text = "Intro.\n[TABLE:]\nA | B\n1 | 2\n[/TABLE]\nEnd."
        chunks = chunk_document(
            text, self._make_meta(), "pkg:test", max_tokens=512,
        )
        table_chunks = [c for c in chunks if c.chunk_type == "table"]
        assert len(table_chunks) == 1
        assert "[Source: test.pdf]" in table_chunks[0].content

    def test_table_chunk_has_section_tag(self):
        text = "Intro.\n[TABLE:4.2 — UCS Results]\nA | B\n1 | 2\n[/TABLE]\nEnd."
        chunks = chunk_document(
            text, self._make_meta(), "pkg:test", max_tokens=512,
        )
        table_chunks = [c for c in chunks if c.chunk_type == "table"]
        assert len(table_chunks) == 1
        assert "[Section: 4.2 — UCS Results]" in table_chunks[0].content
        assert "[Source: test.pdf]" in table_chunks[0].content

    def test_table_section_stored_in_metadata(self):
        text = "Intro.\n[TABLE:Section 3]\nX | Y\n[/TABLE]\nEnd."
        chunks = chunk_document(
            text, self._make_meta(), "pkg:test", max_tokens=512,
        )
        table_chunks = [c for c in chunks if c.chunk_type == "table"]
        assert table_chunks[0].metadata.get("section") == "Section 3"

    def test_csv_chunk_unaffected(self):
        text = "A | B\n---\n1 | 2"
        chunks = chunk_document(
            text, self._make_meta(), "pkg:test", is_csv=True,
        )
        assert len(chunks) == 1
        assert chunks[0].chunk_type == "csv_data"
        # CSV chunks should not get source prefix
        assert not chunks[0].content.startswith("[Source:")

    def test_all_chunk_ids_unique(self):
        text = (
            "Paragraph one about geology.\n"
            "[TABLE:Table 1]\nA | B\n[/TABLE]\n"
            "Paragraph two about strength.\n"
            "[TABLE:Table 2]\nC | D\n[/TABLE]\n"
            "Final paragraph."
        )
        chunks = chunk_document(
            text, self._make_meta(), "pkg:test", max_tokens=512,
        )
        ids = [c.id for c in chunks]
        assert len(ids) == len(set(ids)), f"Duplicate IDs: {ids}"
