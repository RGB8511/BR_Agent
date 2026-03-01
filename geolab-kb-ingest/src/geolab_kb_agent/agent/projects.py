"""Project registry — metadata for all managed dam projects."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ProjectInfo:
    """Metadata for a single project (dam)."""

    name: str
    slug: str
    dam_type: str
    river: str
    county: str
    state: str
    key_issues: list[str] = field(default_factory=list)
    doc_count: int = 0
    doc_years: str = ""
    boring_prefixes: list[str] = field(default_factory=list)
    description: str = ""

    @property
    def package_id(self) -> str:
        """Return the KB package_id for this project."""
        return f"project:{self.slug}"

    def to_dict(self) -> dict:
        """Serialize to a plain dict (excludes package_id property)."""
        return {
            "name": self.name,
            "slug": self.slug,
            "dam_type": self.dam_type,
            "river": self.river,
            "county": self.county,
            "state": self.state,
            "key_issues": list(self.key_issues),
            "doc_count": self.doc_count,
            "doc_years": self.doc_years,
            "boring_prefixes": list(self.boring_prefixes),
            "description": self.description,
            "package_id": self.package_id,
        }


PROJECT_REGISTRY: list[ProjectInfo] = [
    ProjectInfo(
        name="Juniper Canyon Dam",
        slug="juniper-canyon-dam",
        dam_type="concrete gravity",
        river="Snake River",
        county="Owyhee County",
        state="Idaho",
        key_issues=[
            "gravity sliding",
            "shear zone seepage",
            "ASR + freeze-thaw",
            "spillway gate corrosion",
        ],
        doc_count=20,
        doc_years="1959-2025",
        boring_prefixes=["BH-GS", "BH-LE", "BH-RE"],
        description=(
            "20 documents (1959-2025): construction, boring logs, first filling, "
            "inspections, 2025 PSR assessments (geotechnical, concrete, drains, "
            "stability, seepage, instrumentation, seismic, remediation, corrosion, EAP)"
        ),
    ),
    ProjectInfo(
        name="Rimrock Diversion Dam",
        slug="rimrock-diversion-dam",
        dam_type="concrete thin arch",
        river="Middle Fork Boise River",
        county="Elmore County",
        state="Idaho",
        key_issues=[
            "right abutment foundation softening",
            "lacustrine interbed seepage",
            "freeze-thaw deterioration",
            "spillway plunge pool erosion",
        ],
        doc_count=20,
        doc_years="1955-2025",
        boring_prefixes=["BH-AS", "BH-RA", "BH-LA"],
        description=(
            "20 documents (1955-2025): construction, boring logs, first filling, "
            "inspections, 2025 PSR assessments (geotechnical, concrete, drains, "
            "stability, seepage, instrumentation, seismic, remediation, corrosion, EAP)"
        ),
    ),
]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def get_project_names() -> list[str]:
    """Return the display names of all registered projects."""
    return [p.name for p in PROJECT_REGISTRY]


def get_project_by_name(name: str) -> ProjectInfo | None:
    """Look up a project by display name (case-insensitive)."""
    name_lower = name.lower()
    for p in PROJECT_REGISTRY:
        if p.name.lower() == name_lower:
            return p
    return None


def get_projects_prompt_section() -> str:
    """Build a markdown section listing all projects for the system prompt."""
    lines: list[str] = ["Available projects:"]
    for p in PROJECT_REGISTRY:
        lines.append(
            f"- **{p.name}** ({p.dam_type}, {p.river}, {p.county}, {p.state}) "
            f"— {p.description}"
        )
    return "\n".join(lines)


def get_all_boring_prefixes() -> dict[str, str]:
    """Return a mapping of boring-ID prefix → project name."""
    mapping: dict[str, str] = {}
    for p in PROJECT_REGISTRY:
        for prefix in p.boring_prefixes:
            mapping[prefix] = p.name
    return mapping
