"""Temporal intent detection and year extraction for queries.

Pure regex-based — no LLM calls. Detects temporal patterns in user
queries and extracts year references for scoped retrieval.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import StrEnum


class TemporalIntent(StrEnum):
    """Type of temporal query detected."""

    TREND = "trend"  # "how has X changed over time"
    COMPARISON = "comparison"  # "compare 2019 vs 2025"
    POINT_IN_TIME = "point_in_time"  # "what was X in 2020"
    RANGE = "range"  # "between 2010 and 2025"
    EVOLUTION = "evolution"  # "history of", "evolution of"
    NONE = "none"


@dataclass
class TemporalQuery:
    """Result of temporal intent detection."""

    is_temporal: bool = False
    intent: TemporalIntent = TemporalIntent.NONE
    years: list[int] = field(default_factory=list)
    year_min: int | None = None
    year_max: int | None = None
    base_query: str = ""  # query with temporal terms stripped

    @property
    def year_range(self) -> tuple[int, int] | None:
        """Return (min, max) year range if available."""
        if self.year_min is not None and self.year_max is not None:
            return (self.year_min, self.year_max)
        if self.years:
            return (min(self.years), max(self.years))
        return None


# --- Regex patterns ---

# Explicit year: 4 digits starting with 19 or 20
_YEAR_RE = re.compile(r"\b((?:19|20)\d{2})\b")

# Year range: "2010-2025", "2010 to 2025", "from 2010 to 2025"
_YEAR_RANGE_RE = re.compile(
    r"\b((?:19|20)\d{2})\s*[-–—]\s*((?:19|20)\d{2})\b"
    r"|\bfrom\s+((?:19|20)\d{2})\s+to\s+((?:19|20)\d{2})\b"
    r"|\bbetween\s+((?:19|20)\d{2})\s+and\s+((?:19|20)\d{2})\b",
    re.IGNORECASE,
)

# Comparison: "2019 vs 2025", "compare X and Y", "X compared to Y"
_COMPARISON_RE = re.compile(
    r"\b((?:19|20)\d{2})\s+(?:vs\.?|versus|compared?\s+(?:to|with))\s+((?:19|20)\d{2})\b"
    r"|\bcompar(?:e|ing|ison)\b",
    re.IGNORECASE,
)

# Trend / evolution / change over time
_TREND_RE = re.compile(
    r"\b(?:trend|trends|trending|over\s+time|changed?\s+over|"
    r"evolution|evolve[ds]?|history\s+of|historical|"
    r"how\s+has\b.*\bchanged|progression|progressed|"
    r"over\s+the\s+(?:years|decades|past)|"
    r"through\s+(?:the\s+)?years|"
    r"timeline)\b",
    re.IGNORECASE,
)

# Point in time: "in 2020", "in the 2019", "as of 2019", "during 2025"
_POINT_IN_TIME_RE = re.compile(
    r"\b(?:in|as\s+of|during|circa|around)\s+(?:the\s+)?((?:19|20)\d{2})\b",
    re.IGNORECASE,
)

# Temporal terms to strip from base query
_TEMPORAL_STRIP_RE = re.compile(
    r"\b(?:over\s+time|over\s+the\s+(?:years|decades|past)|"
    r"through\s+(?:the\s+)?years|timeline|"
    r"how\s+has\s+|how\s+have\s+|changed?\s+over\s+|"
    r"(?:19|20)\d{2}\s*[-–—]\s*(?:19|20)\d{2}|"
    r"from\s+(?:19|20)\d{2}\s+to\s+(?:19|20)\d{2}|"
    r"between\s+(?:19|20)\d{2}\s+and\s+(?:19|20)\d{2}|"
    r"(?:19|20)\d{2}\s+(?:vs\.?|versus|compared?\s+(?:to|with))\s+(?:19|20)\d{2}|"
    r"in\s+(?:19|20)\d{2}|as\s+of\s+(?:19|20)\d{2}|during\s+(?:19|20)\d{2}|"
    r"trend[s]?\s+(?:in|of|for)|"
    r"history\s+of|historical|evolution\s+of|"
    r"compare|comparison|comparing)\b",
    re.IGNORECASE,
)


def extract_years(text: str) -> list[int]:
    """Extract all 4-digit years (1900-2099) from text."""
    return sorted(set(int(m) for m in _YEAR_RE.findall(text)))


def detect_temporal_intent(query: str) -> TemporalQuery:
    """Detect temporal intent and extract year references from a query.

    Returns a TemporalQuery with:
    - is_temporal: True if the query has temporal aspects
    - intent: the type of temporal query
    - years: all years mentioned
    - year_min/year_max: explicit range boundaries
    - base_query: query with temporal terms removed (for semantic search)
    """
    years = extract_years(query)
    result = TemporalQuery(years=years)

    # Check for year range
    range_match = _YEAR_RANGE_RE.search(query)
    if range_match:
        groups = range_match.groups()
        # groups are in pairs: (g1,g2), (g3,g4), (g5,g6) for the three patterns
        for i in range(0, len(groups), 2):
            if groups[i] is not None and groups[i + 1] is not None:
                result.year_min = int(groups[i])
                result.year_max = int(groups[i + 1])
                break

    # Detect intent type (order matters — more specific first)
    if _COMPARISON_RE.search(query) and len(years) >= 2:
        result.intent = TemporalIntent.COMPARISON
        result.is_temporal = True
    elif result.year_min is not None:
        result.intent = TemporalIntent.RANGE
        result.is_temporal = True
    elif _TREND_RE.search(query):
        result.intent = TemporalIntent.TREND
        result.is_temporal = True
    elif _POINT_IN_TIME_RE.search(query) and len(years) == 1:
        result.intent = TemporalIntent.POINT_IN_TIME
        result.is_temporal = True
    elif len(years) >= 2:
        # Multiple years mentioned — likely a comparison or range
        result.intent = TemporalIntent.COMPARISON
        result.is_temporal = True
        if result.year_min is None:
            result.year_min = min(years)
            result.year_max = max(years)
    elif _TREND_RE.search(query) or query.lower().find("over time") >= 0:
        result.intent = TemporalIntent.EVOLUTION
        result.is_temporal = True

    if result.is_temporal:
        # Build base query by stripping temporal terms
        base = _TEMPORAL_STRIP_RE.sub(" ", query)
        base = re.sub(r"\s+", " ", base).strip()
        # Remove dangling prepositions
        base = re.sub(r"\b(?:from|to|between|and|vs\.?|versus)\s*$", "", base).strip()
        result.base_query = base if base else query
    else:
        result.base_query = query

    return result
