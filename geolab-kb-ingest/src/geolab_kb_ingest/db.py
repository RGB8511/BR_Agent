"""Database model, engine, session, and bulk operations."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Iterator

from pgvector.sqlalchemy import Vector
from sqlalchemy import (
    ARRAY,
    DateTime,
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


class KBChunk(Base):
    __tablename__ = "kb_chunks"

    id: Mapped[str] = mapped_column(Text, primary_key=True)
    package_id: Mapped[str] = mapped_column(Text, index=True)
    chunk_type: Mapped[str] = mapped_column(Text, index=True)
    title: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
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
