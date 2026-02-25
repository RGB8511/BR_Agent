"""FastAPI application — GeoLab KB Agent demo server."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from geolab_kb_ingest.db import get_engine, init_db
from geolab_kb_ingest.embedder import Embedder

from .config import get_settings
from .routers import chat

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

STATIC_DIR = Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()

    # Initialize database engine + tables
    engine = None
    try:
        logger.info("Connecting to database: %s", settings.database_url[:40] + "...")
        engine = get_engine(settings.database_url)
        init_db(engine)
        logger.info("Database connected.")
    except Exception as exc:
        logger.warning("Database init failed (will retry on first request): %s", exc)
        if engine is None:
            engine = get_engine(settings.database_url)
    app.state.engine = engine

    # Initialize embedder (deferred — Voyage client validates key on construction)
    embedder = None
    if settings.voyage_api_key:
        try:
            logger.info("Initializing Voyage AI embedder: %s", settings.voyage_model)
            embedder = Embedder(
                api_key=settings.voyage_api_key,
                model=settings.voyage_model,
                dims=settings.embedding_dims,
            )
        except Exception as exc:
            logger.warning("Embedder init failed: %s", exc)
    else:
        logger.warning("GEOLAB_VOYAGE_API_KEY not set — embedder unavailable.")
    app.state.embedder = embedder

    logger.info("KB Agent ready on port %d", settings.port)
    yield

    # Cleanup
    engine.dispose()
    logger.info("Engine disposed.")


def create_app() -> FastAPI:
    app = FastAPI(
        title="GeoLab KB Agent",
        description="RAG agent over the geotechnical knowledge base",
        version="0.1.0",
        lifespan=lifespan,
    )

    # CORS — open for demo
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(chat.router)

    # Health
    @app.get("/health")
    async def health():
        return {"status": "ok", "service": "geolab-kb-agent"}

    # Static files for demo UI
    if STATIC_DIR.exists():
        app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")

    return app


app = create_app()


def main() -> None:
    """Entry point for `geolab-kb-agent` console script."""
    import uvicorn

    settings = get_settings()
    uvicorn.run(
        "geolab_kb_agent.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
