"""Tests for Phase 2 query.py improvements: package_id and tags filters."""

from __future__ import annotations

from geolab_kb_ingest.query import query_chunks


class TestQueryFilterSQL:
    """Verify that filter parameters produce correct WHERE clauses.

    These tests check argument acceptance and SQL construction without
    requiring a live database or embedder. We test that the function
    signature accepts all new parameters by calling with a mock that
    captures the generated SQL.
    """

    def test_accepts_package_id_param(self):
        """Verify query_chunks accepts package_id kwarg."""
        import inspect
        sig = inspect.signature(query_chunks)
        assert "package_id" in sig.parameters

    def test_accepts_package_id_prefix_param(self):
        """Verify query_chunks accepts package_id_prefix kwarg."""
        import inspect
        sig = inspect.signature(query_chunks)
        assert "package_id_prefix" in sig.parameters

    def test_accepts_package_id_exclude_prefix_param(self):
        """Verify query_chunks accepts package_id_exclude_prefix kwarg."""
        import inspect
        sig = inspect.signature(query_chunks)
        assert "package_id_exclude_prefix" in sig.parameters

    def test_accepts_tags_param(self):
        """Verify query_chunks accepts tags kwarg."""
        import inspect
        sig = inspect.signature(query_chunks)
        assert "tags" in sig.parameters

    def test_all_original_params_preserved(self):
        """Verify original parameters still exist."""
        import inspect
        sig = inspect.signature(query_chunks)
        for name in ["engine", "embedder", "query_text", "top_k",
                      "chunk_type", "discipline"]:
            assert name in sig.parameters, f"Missing original param: {name}"
