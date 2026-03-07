"""Tests for the data export module."""

from __future__ import annotations

import time
from unittest.mock import patch

from geolab_kb_agent.exports import (
    ExportRegistry,
    ExportedFile,
    MAX_EXPORT_COLUMNS,
    MAX_EXPORT_ROWS,
    _coerce_value,
    create_export,
    generate_csv,
    generate_xlsx,
)


class TestCoerceValue:
    """_coerce_value preserves strings, converts obvious numbers."""

    def test_plain_int(self):
        assert _coerce_value("42") == 42

    def test_plain_float(self):
        assert _coerce_value("3.14") == 3.14

    def test_negative_int(self):
        assert _coerce_value("-7") == -7

    def test_preserves_leading_zeros(self):
        assert _coerce_value("007") == "007"

    def test_preserves_scientific_notation(self):
        assert _coerce_value("1e5") == "1e5"

    def test_preserves_text(self):
        assert _coerce_value("Dacite Tuff") == "Dacite Tuff"

    def test_preserves_empty(self):
        assert _coerce_value("") == ""

    def test_passthrough_none(self):
        assert _coerce_value(None) is None

    def test_passthrough_int(self):
        assert _coerce_value(42) == 42


class TestGenerateCSV:
    def test_basic(self):
        data = generate_csv(["A", "B"], [["1", "2"], ["3", "4"]])
        text = data.decode("utf-8-sig")
        assert "A,B" in text
        assert "1,2" in text

    def test_with_title(self):
        data = generate_csv(["X"], [["v"]], title="My Title")
        text = data.decode("utf-8-sig")
        assert "# My Title" in text


class TestGenerateXLSX:
    def test_basic(self):
        data = generate_xlsx(["Col1", "Col2"], [["a", "b"]])
        # XLSX files start with PK (zip format)
        assert data[:2] == b"PK"

    def test_with_title(self):
        data = generate_xlsx(["X"], [["v"]], title="Report")
        assert len(data) > 0


class TestCreateExport:
    def test_csv(self):
        ef = create_export(["A"], [["1"]], fmt="csv", filename="test")
        assert ef.filename == "test.csv"
        assert ef.format == "csv"
        assert ef.row_count == 1

    def test_xlsx(self):
        ef = create_export(["A"], [["1"]], fmt="xlsx", filename="test")
        assert ef.filename == "test.xlsx"
        assert ef.format == "xlsx"

    def test_sanitizes_filename(self):
        ef = create_export(["A"], [["1"]], fmt="csv", filename="../../etc/passwd")
        assert "/" not in ef.filename
        assert ".." not in ef.filename

    def test_row_limit(self):
        import pytest
        rows = [["x"]] * (MAX_EXPORT_ROWS + 1)
        with pytest.raises(ValueError, match="limited to"):
            create_export(["A"], rows, fmt="csv")

    def test_column_limit(self):
        import pytest
        cols = [f"c{i}" for i in range(MAX_EXPORT_COLUMNS + 1)]
        with pytest.raises(ValueError, match="limited to"):
            create_export(cols, [["x"] * len(cols)], fmt="csv")


class TestExportRegistry:
    def test_store_and_get(self):
        reg = ExportRegistry()
        ef = ExportedFile(
            file_id="abc", filename="f.csv", format="csv",
            content=b"data", created_at=time.time(),
        )
        reg.store(ef)
        assert reg.get("abc") is ef

    def test_missing_returns_none(self):
        reg = ExportRegistry()
        assert reg.get("nonexistent") is None

    def test_ttl_eviction(self):
        reg = ExportRegistry()
        ef = ExportedFile(
            file_id="old", filename="f.csv", format="csv",
            content=b"data", created_at=time.time() - 7200,  # 2 hours ago
        )
        reg._files["old"] = ef
        assert reg.get("old") is None  # evicted
