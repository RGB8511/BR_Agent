"""Tests for Phase 2 tools.py and doc_ingestor.py changes."""

from __future__ import annotations

from geolab_kb_agent.agent.tools import TOOLS
from geolab_kb_ingest.doc_ingestor import _DOC_TYPE_MAP, _slugify_project


class TestSearchKBToolDefinition:
    """Verify the search_kb tool has the new parameters."""

    def _get_search_kb(self):
        return next(t for t in TOOLS if t["name"] == "search_kb")

    def test_has_source_param(self):
        tool = self._get_search_kb()
        props = tool["input_schema"]["properties"]
        assert "source" in props
        assert props["source"]["enum"] == ["kb", "project"]

    def test_has_project_param(self):
        tool = self._get_search_kb()
        props = tool["input_schema"]["properties"]
        assert "project" in props

    def test_chunk_type_includes_narrative(self):
        tool = self._get_search_kb()
        enum = tool["input_schema"]["properties"]["chunk_type"]["enum"]
        assert "narrative" in enum
        assert "csv_data" in enum

    def test_original_chunk_types_preserved(self):
        tool = self._get_search_kb()
        enum = tool["input_schema"]["properties"]["chunk_type"]["enum"]
        for ct in ["theory", "equation", "table", "standard", "manifest"]:
            assert ct in enum

    def test_query_still_required(self):
        tool = self._get_search_kb()
        assert "query" in tool["input_schema"]["required"]


class TestDocTypeMap:
    """Verify the doc_type mapping covers all project document files."""

    def test_juniper_has_20_entries(self):
        jc = {k: v for k, v in _DOC_TYPE_MAP.items() if k.startswith("doc") and k.endswith(".pdf")}
        # 20 Juniper-unique + 12 Rimrock-unique PDFs (8 shared filenames overlap)
        assert len(jc) >= 20

    def test_rimrock_csvs(self):
        csvs = {k for k in _DOC_TYPE_MAP if k.startswith("data_")}
        assert len(csvs) == 7

    def test_total_entries(self):
        assert len(_DOC_TYPE_MAP) == 39

    def test_all_values_are_valid_types(self):
        valid_types = {
            "construction_report", "boring_logs", "first_filling",
            "safety_inspection", "part_12d", "geotechnical",
            "instrumentation", "concrete", "drain_evaluation",
            "stability", "seepage", "seismic", "remediation",
            "mix_design", "corrosion", "eap", "spillway_erosion",
        }
        for filename, doc_type in _DOC_TYPE_MAP.items():
            assert doc_type in valid_types, (
                f"{filename} has unknown doc_type: {doc_type}"
            )

    def test_filenames_are_pdfs_or_csvs(self):
        for filename in _DOC_TYPE_MAP:
            assert filename.endswith(".pdf") or filename.endswith(".csv"), (
                f"{filename} is not a PDF or CSV"
            )

    def test_doc01_is_construction(self):
        assert _DOC_TYPE_MAP["doc01_wsrb_1963_construction_report.pdf"] == "construction_report"

    def test_doc20_is_eap(self):
        assert _DOC_TYPE_MAP["doc20_jbid_2025_eap_update.pdf"] == "eap"


class TestSlugifyProject:
    def test_basic(self):
        assert _slugify_project("Juniper Canyon Dam") == "project:juniper-canyon-dam"

    def test_extra_spaces(self):
        assert _slugify_project("  My Project  ") == "project:my-project"

    def test_special_chars(self):
        result = _slugify_project("Dam #1 — Phase (2)")
        assert result.startswith("project:")
        assert "#" not in result
