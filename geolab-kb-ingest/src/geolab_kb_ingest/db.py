"""Database model, engine, session, and bulk operations."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Iterator

from pgvector.sqlalchemy import Vector
from sqlalchemy import (
    ARRAY,
    DateTime,
    Float,
    Integer,
    Text,
    create_engine,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    sessionmaker,
)
from sqlalchemy import Engine


# ---------------------------------------------------------------------------
# Declarative base
# ---------------------------------------------------------------------------
class Base(DeclarativeBase):
    pass


class ChatFeedback(Base):
    __tablename__ = "chat_feedback"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    conversation_id: Mapped[str] = mapped_column(Text, index=True)
    message_index: Mapped[int] = mapped_column(Integer)
    sentiment: Mapped[str] = mapped_column(Text)  # "up" | "down"
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class ValidatedRetrieval(Base):
    __tablename__ = "validated_retrieval"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    query_text: Mapped[str] = mapped_column(Text, index=True)
    chunk_id: Mapped[str] = mapped_column(Text, index=True)
    original_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class KBChunk(Base):
    __tablename__ = "kb_chunks"

    id: Mapped[str] = mapped_column(Text, primary_key=True)
    package_id: Mapped[str] = mapped_column(Text, index=True)
    chunk_type: Mapped[str] = mapped_column(Text, index=True)
    title: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    embedding_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    embedding = mapped_column(Vector(1024))
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict)
    tags: Mapped[list[str]] = mapped_column(ARRAY(Text), default=list)
    discipline: Mapped[str] = mapped_column(Text, index=True)
    level: Mapped[int] = mapped_column(Integer)
    token_count: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


# ---------------------------------------------------------------------------
# Engine / Session
# ---------------------------------------------------------------------------
def get_engine(url: str) -> Engine:
    return create_engine(url, pool_pre_ping=True)


@contextmanager
def get_session(engine: Engine) -> Iterator[Session]:
    factory = sessionmaker(bind=engine)
    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


# ---------------------------------------------------------------------------
# DDL helpers
# ---------------------------------------------------------------------------
def init_db(engine: Engine) -> None:
    """Create pgvector extension, tables, and indexes."""
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    Base.metadata.create_all(engine)


def delete_package_chunks(session: Session, package_id: str) -> int:
    """Delete all chunks for a package. Returns deleted count."""
    count = session.query(KBChunk).filter(KBChunk.package_id == package_id).delete()
    return count


def bulk_insert_chunks(session: Session, chunks: list[KBChunk]) -> None:
    """Bulk-insert a list of KBChunk objects."""
    session.add_all(chunks)


# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------
def count_tokens(text: str) -> int:
    """Count tokens using cl100k_base encoding."""
    import tiktoken

    _enc = tiktoken.get_encoding("cl100k_base")
    return len(_enc.encode(text))


def chunk_to_dict(chunk: KBChunk) -> dict:
    """Convert a KBChunk ORM object to a plain dict."""
    return {
        "id": chunk.id,
        "title": chunk.title,
        "content": chunk.content,
        "chunk_type": chunk.chunk_type,
        "package_id": chunk.package_id,
        "discipline": chunk.discipline,
        "tags": chunk.tags,
        "metadata": chunk.metadata_,
    }
