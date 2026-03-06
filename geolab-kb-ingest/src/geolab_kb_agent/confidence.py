"""Deterministic confidence scoring based on retrieval similarity scores.

No LLM calls — pure math on the similarity score distribution.
"""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel


class ConfidenceLevel(StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class ConfidenceScore(BaseModel):
    """Confidence assessment for a retrieval result set."""

    level: ConfidenceLevel
    score: float  # top chunk similarity
    top_gap: float  # gap between rank 1 and rank 2
    reasoning: str  # human-readable explanation


def compute_confidence(similarity_scores: list[float]) -> ConfidenceScore:
    """Compute confidence from a list of retrieval similarity scores.

    Thresholds:
    - top score < 0.65 → LOW regardless of gap
    - gap > 0.10 → HIGH (clear best match)
    - gap > 0.05 → MEDIUM (good match, similar alternatives)
    - gap <= 0.05 → LOW (ambiguous, multiple close results)
    """
    if not similarity_scores:
        return ConfidenceScore(
            level=ConfidenceLevel.LOW,
            score=0.0,
            top_gap=0.0,
            reasoning="No relevant chunks found in the knowledge base.",
        )

    scores = sorted(similarity_scores, reverse=True)
    top = scores[0]

    # Single result
    if len(scores) == 1:
        if top >= 0.80:
            level = ConfidenceLevel.HIGH
            reasoning = f"Single strong match ({top:.2f})."
        elif top >= 0.65:
            level = ConfidenceLevel.MEDIUM
            reasoning = f"Single moderate match ({top:.2f}). Limited corroboration."
        else:
            level = ConfidenceLevel.LOW
            reasoning = f"Single weak match ({top:.2f}). May not be relevant."
        return ConfidenceScore(
            level=level, score=top, top_gap=0.0, reasoning=reasoning,
        )

    gap = scores[0] - scores[1]

    if top < 0.65:
        level = ConfidenceLevel.LOW
        reasoning = f"Best match ({top:.2f}) below relevance threshold."
    elif gap > 0.10:
        level = ConfidenceLevel.HIGH
        reasoning = f"Clear best match ({top:.2f}) with strong separation from next result."
    elif gap > 0.05:
        level = ConfidenceLevel.MEDIUM
        reasoning = f"Good match ({top:.2f}) but similar alternatives exist (gap: {gap:.2f})."
    else:
        level = ConfidenceLevel.LOW
        reasoning = (
            f"Multiple similarly-ranked results ({top:.2f} vs {scores[1]:.2f}). "
            "Answer may draw from wrong source."
        )

    return ConfidenceScore(
        level=level, score=top, top_gap=gap, reasoning=reasoning,
    )
