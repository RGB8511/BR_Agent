"""Request / response schemas — mirrors geolab-platform patterns."""

from __future__ import annotations

from typing import Any, Generic, Literal, TypeVar

from pydantic import BaseModel, Field

from geolab_kb_agent.confidence import ConfidenceScore

T = TypeVar("T")


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None
    mode: Literal["concise", "educational", "report", "calculation", "review", "field"] | None = None


class SubRef(BaseModel):
    """A single chunk sub-reference within a grouped document."""

    letter: str
    chunk_id: str
    section: str | None = None
    page_number: int | None = None
    chunk_text: str = ""
    similarity_score: float = 0.0
    chunk_type: str | None = None
    metadata: dict[str, Any] | None = None


class GroupedSource(BaseModel):
    """Citations grouped by source document."""

    doc_number: int
    document_name: str
    project: str | None = None
    display_citation: str = ""
    sub_refs: list[SubRef] = Field(default_factory=list)


# Keep the old model for backwards compatibility if needed
class RetrievedChunk(BaseModel):
    """A single chunk returned by the retrieval pipeline with provenance."""

    chunk_id: str
    document_name: str
    section: str | None = None
    page_number: int | None = None
    chunk_text: str
    similarity_score: float
    chunk_type: str | None = None
    metadata: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    response: str
    sources: list[GroupedSource] = Field(default_factory=list)
    confidence: ConfidenceScore | None = None
    conversation_id: str


class FeedbackRequest(BaseModel):
    conversation_id: str
    message_index: int
    sentiment: Literal["up", "down"]
    query_text: str | None = None
    chunk_ids: list[str] | None = None
    scores: list[float] | None = None
    password: str | None = None


class Envelope(BaseModel, Generic[T]):
    data: T
    meta: dict[str, Any] = {}
