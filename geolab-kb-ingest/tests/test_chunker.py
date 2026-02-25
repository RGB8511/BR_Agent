"""Tests for the chunker module using real package data."""

from __future__ import annotations

import json
from pathlib import Path

from geolab_kb_ingest.chunker import (
    Chunk,
    _count_tokens,
    _slugify,
    chunk_equations,
    chunk_manifest,
    chunk_package,
    chunk_standards,
    chunk_tables,
    chunk_theory,
)


# ---------------------------------------------------------------------------
# Helper tests
# ---------------------------------------------------------------------------
class TestSlugify:
    def test_basic(self):
        assert _slugify("Hello World") == "hello-world"

    def test_special_chars(self):
        result = _slugify("ASTM D2487 — Standard Practice")
        assert result == "astm-d2487-standard-practice"

    def test_leading_trailing(self):
        assert _slugify("  foo  ") == "foo"


class TestCountTokens:
    def test_nonempty(self):
        count = _count_tokens("Hello, world!")
        assert count > 0

    def test_empty(self):
        assert _count_tokens("") == 0


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
class TestChunkManifest:
    def test_produces_one_chunk(self, sample_manifest):
        chunk = chunk_manifest(sample_manifest)
        assert isinstance(chunk, Chunk)
        assert chunk.chunk_type == "manifest"
        assert chunk.package_id == sample_manifest["id"]
        assert chunk.id.endswith(".manifest")

    def test_content_includes_name(self, sample_manifest):
        chunk = chunk_manifest(sample_manifest)
        assert sample_manifest["name"] in chunk.content

    def test_tags_propagated(self, sample_manifest):
        chunk = chunk_manifest(sample_manifest)
        assert chunk.tags == sample_manifest["tags"]


# ---------------------------------------------------------------------------
# Theory
# ---------------------------------------------------------------------------
class TestChunkTheory:
    def test_splits_on_h2(self, sample_package, sample_manifest):
        text = (sample_package / "theory.md").read_text(encoding="utf-8")
        chunks = chunk_theory(text, sample_manifest, max_tokens=1500)
        assert len(chunks) >= 2  # At least overview + one H2 section
        for c in chunks:
            assert c.chunk_type == "theory"
            assert c.package_id == sample_manifest["id"]

    def test_ids_are_unique(self, sample_package, sample_manifest):
        text = (sample_package / "theory.md").read_text(encoding="utf-8")
        chunks = chunk_theory(text, sample_manifest, max_tokens=1500)
        ids = [c.id for c in chunks]
        assert len(ids) == len(set(ids))

    def test_small_max_tokens_triggers_subsplit(self, sample_package, sample_manifest):
        text = (sample_package / "theory.md").read_text(encoding="utf-8")
        # Very small max to force H3 sub-splitting
        chunks_small = chunk_theory(text, sample_manifest, max_tokens=100)
        chunks_large = chunk_theory(text, sample_manifest, max_tokens=10000)
        assert len(chunks_small) >= len(chunks_large)


# ---------------------------------------------------------------------------
# Equations
# ---------------------------------------------------------------------------
class TestChunkEquations:
    def test_one_per_equation(self, sample_package, sample_manifest):
        with open(sample_package / "equations.json", encoding="utf-8") as f:
            eqs = json.load(f)
        chunks = chunk_equations(eqs, sample_manifest)
        assert len(chunks) == len(eqs)
        for c in chunks:
            assert c.chunk_type == "equation"

    def test_content_has_equation_text(self, sample_package, sample_manifest):
        with open(sample_package / "equations.json", encoding="utf-8") as f:
            eqs = json.load(f)
        chunks = chunk_equations(eqs, sample_manifest)
        for chunk, eq in zip(chunks, eqs):
            assert eq["equation"] in chunk.content
            assert eq["title"] in chunk.content

    def test_criteria_rendered(self, sample_package, sample_manifest):
        """soil-classification has criteria field on eq-001."""
        with open(sample_package / "equations.json", encoding="utf-8") as f:
            eqs = json.load(f)
        eq_with_criteria = [e for e in eqs if e.get("criteria")]
        if eq_with_criteria:
            chunks = chunk_equations(eq_with_criteria, sample_manifest)
            assert "Criteria:" in chunks[0].content


# ---------------------------------------------------------------------------
# Tables
# ---------------------------------------------------------------------------
class TestChunkTables:
    def test_one_per_table(self, sample_package, sample_manifest):
        with open(sample_package / "tables.json", encoding="utf-8") as f:
            tables = json.load(f)
        chunks = chunk_tables(tables, sample_manifest)
        assert len(chunks) == len(tables)
        for c in chunks:
            assert c.chunk_type == "table"

    def test_markdown_table_format(self, sample_package, sample_manifest):
        with open(sample_package / "tables.json", encoding="utf-8") as f:
            tables = json.load(f)
        chunks = chunk_tables(tables, sample_manifest)
        for c in chunks:
            assert "| " in c.content
            assert "---" in c.content


# ---------------------------------------------------------------------------
# Standards
# ---------------------------------------------------------------------------
class TestChunkStandards:
    def test_splits_on_h2(self, sample_package, sample_manifest):
        text = (sample_package / "standards.md").read_text(encoding="utf-8")
        chunks = chunk_standards(text, sample_manifest)
        assert len(chunks) >= 1
        for c in chunks:
            assert c.chunk_type == "standard"

    def test_ids_have_std_prefix(self, sample_package, sample_manifest):
        text = (sample_package / "standards.md").read_text(encoding="utf-8")
        chunks = chunk_standards(text, sample_manifest)
        for c in chunks:
            assert ".std." in c.id


# ---------------------------------------------------------------------------
# Full package
# ---------------------------------------------------------------------------
class TestChunkPackage:
    def test_produces_all_types(self, sample_package):
        chunks = chunk_package(sample_package)
        types = {c.chunk_type for c in chunks}
        assert "manifest" in types
        assert "theory" in types
        assert "equation" in types
        assert "table" in types
        assert "standard" in types

    def test_all_ids_unique(self, sample_package):
        chunks = chunk_package(sample_package)
        ids = [c.id for c in chunks]
        assert len(ids) == len(set(ids)), f"Duplicate IDs: {[x for x in ids if ids.count(x) > 1]}"

    def test_consolidation_chunk_count(self, consolidation_package):
        """Consolidation package should produce a reasonable number of chunks."""
        chunks = chunk_package(consolidation_package)
        # Should have: 1 manifest + N theory + 18 eq + 4 table + N standards
        assert len(chunks) >= 25
        eq_chunks = [c for c in chunks if c.chunk_type == "equation"]
        tbl_chunks = [c for c in chunks if c.chunk_type == "table"]
        assert len(eq_chunks) == 18
        assert len(tbl_chunks) == 4
