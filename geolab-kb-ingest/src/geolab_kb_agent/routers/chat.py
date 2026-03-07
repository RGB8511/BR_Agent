"""Chat router — POST /api/v1/chat/completions + POST /api/v1/chat/stream."""

from __future__ import annotations

import json
import logging
import secrets
from typing import Any

import anthropic
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response, StreamingResponse

from geolab_kb_agent.agent.orchestrator import KBAgent
from geolab_kb_agent.config import get_settings
from geolab_kb_agent.exports import export_registry
from geolab_kb_agent.memory import ConversationStore
from geolab_kb_agent.schemas import (
    ChatRequest,
    ChatResponse,
    Envelope,
    FeedbackRequest,
    GroupedSource,
)
from geolab_kb_ingest.db import ChatFeedback, ValidatedRetrieval

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/chat", tags=["chat"])

store = ConversationStore()


def _classify_error(exc: Exception) -> tuple[int, str]:
    """Map known exceptions to (status_code, user_message)."""
    if isinstance(exc, anthropic.AuthenticationError):
        return 401, "Anthropic API key is invalid or revoked. Check GEOLAB_ANTHROPIC_API_KEY."
    if isinstance(exc, anthropic.RateLimitError):
        return 429, "Anthropic API rate limit reached. Please wait a moment and try again."
    if isinstance(exc, anthropic.BadRequestError):
        msg = str(exc)
        if "usage limit" in msg.lower():
            return 429, "Anthropic API usage limit reached. Check your plan limits at console.anthropic.com."
        return 400, f"Anthropic API rejected the request: {msg}"
    if isinstance(exc, anthropic.APIConnectionError):
        return 502, "Cannot reach the Anthropic API. Check your network connection."
    if isinstance(exc, anthropic.APIStatusError):
        return 502, f"Anthropic API error (HTTP {exc.status_code}). Please try again."
    return 500, "An internal error occurred. Please try again."


def _require_deps(request: Request) -> tuple:
    """Validate API key, engine, and embedder; return (settings, engine, embedder)."""
    settings = get_settings()

    if not settings.anthropic_api_key:
        raise HTTPException(
            status_code=503,
            detail="Anthropic API key not configured. Set GEOLAB_ANTHROPIC_API_KEY.",
        )

    engine = request.app.state.engine
    embedder = request.app.state.embedder

    if embedder is None:
        raise HTTPException(
            status_code=503,
            detail="Voyage embedder not configured. Set GEOLAB_VOYAGE_API_KEY.",
        )

    return settings, engine, embedder


@router.get("/health")
async def chat_health() -> dict[str, str]:
    settings = get_settings()
    has_key = bool(settings.anthropic_api_key)
    return {"status": "ok", "api_key_configured": str(has_key).lower()}


@router.post("/completions", response_model=Envelope[ChatResponse])
async def chat_completions(
    body: ChatRequest,
    request: Request,
) -> dict[str, Any]:
    settings, engine, embedder = _require_deps(request)

    conv = store.get_or_create(body.conversation_id)

    agent = KBAgent(
        api_key=settings.anthropic_api_key,
        model=settings.anthropic_model,
        engine=engine,
        embedder=embedder,
        mode=body.mode or "educational",
    )

    try:
        result = await agent.chat(body.message, messages=conv.messages)
    except Exception as exc:
        logger.exception("Agent chat failed")
        status, detail = _classify_error(exc)
        raise HTTPException(status_code=status, detail=detail)

    sources = [GroupedSource(**s) for s in result.sources]
    return {
        "data": ChatResponse(
            response=result.text,
            sources=sources,
            confidence=result.confidence,
            conversation_id=conv.id,
        ),
        "meta": {"tool_calls_made": result.tool_calls_made},
    }


@router.post("/stream")
async def chat_stream(
    body: ChatRequest,
    request: Request,
) -> StreamingResponse:
    settings, engine, embedder = _require_deps(request)

    conv = store.get_or_create(body.conversation_id)

    agent = KBAgent(
        api_key=settings.anthropic_api_key,
        model=settings.anthropic_model,
        engine=engine,
        embedder=embedder,
        mode=body.mode or "educational",
    )

    async def event_generator():
        # First event: conversation_id
        yield _sse({"conversation_id": conv.id})

        try:
            async for event in agent.chat_stream(
                body.message, messages=conv.messages
            ):
                yield _sse(event)
        except Exception as exc:
            logger.exception("Stream error")
            _, detail = _classify_error(exc)
            yield _sse({"type": "error", "error": detail})

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.post("/feedback")
async def submit_feedback(body: FeedbackRequest, request: Request) -> dict:
    engine = request.app.state.engine
    feedback = ChatFeedback(
        conversation_id=body.conversation_id,
        message_index=body.message_index,
        sentiment=body.sentiment,
    )
    from sqlalchemy.orm import sessionmaker

    factory = sessionmaker(bind=engine)
    session = factory()
    try:
        session.add(feedback)

        # If this is a validation request (thumbs-up with password + chunk context)
        validated = False
        if (
            body.sentiment == "up"
            and body.password
            and body.query_text
            and body.chunk_ids
        ):
            settings = get_settings()
            if not secrets.compare_digest(body.password, settings.validation_password):
                session.rollback()
                raise HTTPException(status_code=403, detail="Invalid validation password")

            scores = body.scores or [0.0] * len(body.chunk_ids)
            for chunk_id, score in zip(body.chunk_ids, scores):
                session.add(
                    ValidatedRetrieval(
                        query_text=body.query_text,
                        chunk_id=chunk_id,
                        original_score=score,
                    )
                )
            validated = True

        session.commit()
    except HTTPException:
        raise
    except Exception:
        session.rollback()
        logger.exception("Failed to store feedback")
        raise HTTPException(status_code=500, detail="Failed to store feedback")
    finally:
        session.close()
    return {"status": "ok", "validated": validated}


@router.delete("/validations")
async def clear_validations(request: Request) -> dict:
    """Clear all validated retrievals — used for demo reset."""
    engine = request.app.state.engine
    from sqlalchemy.orm import sessionmaker

    factory = sessionmaker(bind=engine)
    session = factory()
    try:
        count = session.query(ValidatedRetrieval).delete()
        session.commit()
    except Exception:
        session.rollback()
        logger.exception("Failed to clear validations")
        raise HTTPException(status_code=500, detail="Failed to clear validations")
    finally:
        session.close()
    return {"status": "ok", "deleted": count}


@router.get("/conversations/{conversation_id}/export")
async def export_conversation(conversation_id: str) -> dict:
    """Export a conversation as markdown for sharing/archival."""
    conv = store.get(conversation_id)
    if conv is None:
        raise HTTPException(status_code=404, detail="Conversation not found.")

    lines: list[str] = []
    lines.append("# BR Agent Conversation\n")
    for msg in conv.messages:
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        if isinstance(content, list):
            # Tool results — skip in export
            continue
        if isinstance(content, str) and content.startswith("[System:"):
            # Internal orchestrator instructions — skip
            continue
        if role == "user":
            # Strip temporal hints appended by orchestrator
            clean = content.split("\n\n[Temporal context:")[0] if isinstance(content, str) else content
            lines.append(f"## Question\n\n{clean}\n")
        elif role == "assistant":
            lines.append(f"## Response\n\n{content}\n")

    return {"conversation_id": conversation_id, "markdown": "\n".join(lines)}


@router.delete("/conversations/{conversation_id}")
async def reset_conversation(conversation_id: str, request: Request) -> dict:
    """Reset a conversation and optionally clear its validated retrievals."""
    deleted_validations = 0

    # Clear validated retrievals for this conversation
    engine = request.app.state.engine
    from sqlalchemy.orm import sessionmaker

    factory = sessionmaker(bind=engine)
    session = factory()
    try:
        deleted_validations = (
            session.query(ChatFeedback)
            .filter(ChatFeedback.conversation_id == conversation_id)
            .delete()
        )
        session.commit()
    except Exception:
        session.rollback()
        logger.warning("Failed to clear feedback for conversation %s", conversation_id)
    finally:
        session.close()

    # Remove from in-memory store
    store.delete(conversation_id)

    return {
        "status": "ok",
        "conversation_id": conversation_id,
        "deleted_feedback": deleted_validations,
    }


@router.get("/downloads/{file_id}")
async def download_file(file_id: str) -> Response:
    """Serve an exported data file (CSV or XLSX)."""
    ef = export_registry.get(file_id)
    if ef is None:
        raise HTTPException(status_code=404, detail="File not found or expired.")

    media_types = {
        "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "csv": "text/csv",
    }
    media_type = media_types.get(ef.format, "application/octet-stream")

    return Response(
        content=ef.content,
        media_type=media_type,
        headers={
            "Content-Disposition": f'attachment; filename="{ef.filename}"',
        },
    )


def _sse(data: dict) -> str:
    """Format a dict as an SSE data line."""
    return f"data: {json.dumps(data)}\n\n"
