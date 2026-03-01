"""Tests for the multi-project registry, prompt integration, and tools."""

from __future__ import annotations

import re

import pytest

from geolab_kb_agent.agent.projects import (
    PROJECT_REGISTRY,
    ProjectInfo,
    get_all_boring_prefixes,
    get_project_by_name,
    get_project_names,
    get_projects_prompt_section,
)
from geolab_kb_agent.agent.system_prompt import get_system_prompt
from geolab_kb_agent.agent.tools import TOOLS


# ---------------------------------------------------------------------------
# TestProjectRegistry
# ---------------------------------------------------------------------------


class TestProjectRegistry:
    """PROJECT_REGISTRY structure and ProjectInfo behaviour."""

    def test_registry_has_two_entries(self):
        assert len(PROJECT_REGISTRY) == 2

    def test_entries_are_project_info(self):
        for p in PROJECT_REGISTRY:
            assert isinstance(p, ProjectInfo)

    @pytest.mark.parametrize(
        "field",
        ["name", "slug", "dam_type", "river", "county", "state"],
    )
    def test_required_fields_present(self, field: str):
        for p in PROJECT_REGISTRY:
            assert getattr(p, field), f"{p.name} missing {field}"

    def test_slugs_are_valid(self):
        slug_re = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        for p in PROJECT_REGISTRY:
            assert slug_re.match(p.slug), f"Invalid slug: {p.slug}"

    def test_package_id_property(self):
        for p in PROJECT_REGISTRY:
            assert p.package_id == f"project:{p.slug}"

    def test_get_project_by_name_found(self):
        result = get_project_by_name("Juniper Canyon Dam")
        assert result is not None
        assert result.slug == "juniper-canyon-dam"

    def test_get_project_by_name_case_insensitive(self):
        result = get_project_by_name("juniper canyon dam")
        assert result is not None
        assert result.name == "Juniper Canyon Dam"

    def test_get_project_by_name_not_found(self):
        assert get_project_by_name("Nonexistent Dam") is None

    def test_to_dict_round_trip(self):
        for p in PROJECT_REGISTRY:
            d = p.to_dict()
            assert d["name"] == p.name
            assert d["slug"] == p.slug
            assert d["package_id"] == p.package_id
            assert d["key_issues"] == list(p.key_issues)
            assert d["boring_prefixes"] == list(p.boring_prefixes)

    def test_get_project_names(self):
        names = get_project_names()
        assert "Juniper Canyon Dam" in names
        assert "Rimrock Diversion Dam" in names
        assert len(names) == 2


# ---------------------------------------------------------------------------
# TestProjectsPromptSection
# ---------------------------------------------------------------------------


class TestProjectsPromptSection:
    """get_projects_prompt_section() output."""

    def test_contains_both_project_names(self):
        section = get_projects_prompt_section()
        assert "Juniper Canyon Dam" in section
        assert "Rimrock Diversion Dam" in section

    def test_contains_doc_counts(self):
        section = get_projects_prompt_section()
        # Both projects have descriptions containing doc years
        assert "1959-2025" in section
        assert "1955-2025" in section

    def test_contains_dam_types(self):
        section = get_projects_prompt_section()
        assert "concrete gravity" in section
        assert "concrete thin arch" in section


# ---------------------------------------------------------------------------
# TestBoringPrefixes
# ---------------------------------------------------------------------------


class TestBoringPrefixes:
    """get_all_boring_prefixes() mapping."""

    def test_all_six_prefixes_present(self):
        prefixes = get_all_boring_prefixes()
        assert len(prefixes) == 6

    @pytest.mark.parametrize("prefix", ["BH-GS", "BH-LE", "BH-RE"])
    def test_juniper_canyon_prefixes(self, prefix: str):
        prefixes = get_all_boring_prefixes()
        assert prefixes[prefix] == "Juniper Canyon Dam"

    @pytest.mark.parametrize("prefix", ["BH-AS", "BH-RA", "BH-LA"])
    def test_rimrock_prefixes(self, prefix: str):
        prefixes = get_all_boring_prefixes()
        assert prefixes[prefix] == "Rimrock Diversion Dam"


# ---------------------------------------------------------------------------
# TestSystemPromptIntegration
# ---------------------------------------------------------------------------


class TestSystemPromptIntegration:
    """get_system_prompt() integrates project data correctly."""

    def test_contains_both_projects(self):
        blocks = get_system_prompt()
        text = blocks[0]["text"]
        assert "Juniper Canyon Dam" in text
        assert "Rimrock Diversion Dam" in text

    def test_contains_cross_project_section(self):
        blocks = get_system_prompt()
        text = blocks[0]["text"]
        assert "Cross-Project Queries" in text

    def test_contains_boring_prefix_guidance(self):
        blocks = get_system_prompt()
        text = blocks[0]["text"]
        assert "BH-GS" in text
        assert "BH-AS" in text

    def test_cache_control_preserved(self):
        blocks = get_system_prompt()
        assert blocks[0]["cache_control"] == {"type": "ephemeral"}

    def test_mode_instructions_still_work(self):
        for mode in ("concise", "educational", "report", "calculation", "review", "field"):
            blocks = get_system_prompt(mode=mode)
            text = blocks[0]["text"]
            assert f"Response Mode: {mode.capitalize()}" in text or "Response Mode:" in text


# ---------------------------------------------------------------------------
# TestListProjectsTool
# ---------------------------------------------------------------------------


class TestListProjectsTool:
    """list_projects tool definition in TOOLS list."""

    def _get_tool(self) -> dict:
        for t in TOOLS:
            if t["name"] == "list_projects":
                return t
        pytest.fail("list_projects tool not found in TOOLS")

    def test_tool_exists(self):
        self._get_tool()  # will fail via pytest.fail if missing

    def test_no_required_params(self):
        tool = self._get_tool()
        assert tool["input_schema"]["required"] == []

    def test_has_description(self):
        tool = self._get_tool()
        assert len(tool["description"]) > 0


# ---------------------------------------------------------------------------
# TestSearchKBProjectDescription
# ---------------------------------------------------------------------------


class TestSearchKBProjectDescription:
    """search_kb tool's project param lists all project names."""

    def _get_search_kb(self) -> dict:
        for t in TOOLS:
            if t["name"] == "search_kb":
                return t
        pytest.fail("search_kb tool not found in TOOLS")

    def test_project_description_lists_both_names(self):
        tool = self._get_search_kb()
        desc = tool["input_schema"]["properties"]["project"]["description"]
        assert "Juniper Canyon Dam" in desc
        assert "Rimrock Diversion Dam" in desc
