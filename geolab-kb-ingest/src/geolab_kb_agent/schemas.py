"""Request / response schemas — mirrors geolab-platform patterns."""

from __future__ import annotations

from typing import Any, Generic, Literal, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None
    mode: Literal["concise", "educational", "report", "calculation", "review", "field"] | None = None


class ChatResponse(BaseModel):
    response: str
    sources: list[dict[str, Any]]
    conversation_id: str


class Envelope(BaseModel, Generic[T]):
    data: T
    meta: dict[str, Any] = {}
