"""Chat router — POST /api/v1/chat/completions + POST /api/v1/chat/stream."""

from __future__ import annotations

import json
import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse

from geolab_kb_agent.agent.orchestrator import KBAgent
from geolab_kb_agent.config import get_settings
from geolab_kb_agent.memory import ConversationStore
from geolab_kb_agent.schemas import ChatRequest, ChatResponse, Envelope, FeedbackRequest, GroupedSource
from geolab_kb_ingest.db import ChatFeedback, ValidatedRetrieval

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/chat", tags=["chat"])

store = ConversationStore()


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
    except Exception:
        logger.exception("Agent chat failed")
        raise HTTPException(status_code=500, detail="Agent processing failed.")

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
        except Exception:
            logger.exception("Stream error")
            yield _sse({"type": "error", "error": "An internal error occurred. Please try again."})

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
            if body.password != settings.validation_password:
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


def _sse(data: dict) -> str:
    """Format a dict as an SSE data line."""
    return f"data: {json.dumps(data)}\n\n"
