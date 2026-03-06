"""Audit verification tests — validates fixes from the pre-demo security & quality audit."""

from __future__ import annotations

import time
from pathlib import Path
from unittest.mock import patch

from geolab_kb_agent.confidence import ConfidenceLevel, compute_confidence
from geolab_kb_agent.config import Settings
from geolab_kb_agent.memory import Conversation, ConversationStore
from geolab_kb_agent.schemas import Envelope, FeedbackRequest
from geolab_kb_ingest.db import ValidatedRetrieval


class TestEnvelopeMetaIsolation:
    """Fix 3: Mutable default — two instances must not share meta."""

    def test_meta_isolation(self):
        a = Envelope(data="x")
        b = Envelope(data="y")
        a.meta["key"] = "value"
        assert "key" not in b.meta


class TestMemorySlidingWindow:
    """Memory sliding window caps at 100 messages, first is role=user."""

    def test_window_cap(self):
        conv = Conversation(id="test")
        for i in range(150):
            if i % 2 == 0:
                conv.add_user_message(f"msg-{i}")
            else:
                conv.add_assistant_message(f"msg-{i}")
        assert len(conv.messages) <= 100
        assert conv.messages[0]["role"] == "user"


class TestMemoryTTLEviction:
    """Memory TTL eviction removes expired conversations."""

    def test_ttl_eviction(self):
        store = ConversationStore(ttl=1.0)
        conv = store.get_or_create("session-1")
        conv.add_user_message("hello")

        # Advance time past TTL
        with patch("geolab_kb_agent.memory.time") as mock_time:
            mock_time.monotonic.return_value = time.monotonic() + 2.0
            result = store.get_or_create("session-1")
            # Should be a fresh conversation (old one evicted)
            assert len(result.messages) == 0


class TestValidatedRetrievalModel:
    """ValidatedRetrieval table name, columns, and indexed columns."""

    def test_table_name(self):
        assert ValidatedRetrieval.__tablename__ == "validated_retrieval"

    def test_columns(self):
        col_names = {c.name for c in ValidatedRetrieval.__table__.columns}
        assert col_names == {"id", "query_text", "chunk_id", "original_score", "created_at"}

    def test_indexed_columns(self):
        indexed = {
            idx.columns.keys()[0]
            for idx in ValidatedRetrieval.__table__.indexes
        }
        assert "query_text" in indexed
        assert "chunk_id" in indexed


class TestFeedbackRequestValidation:
    """FeedbackRequest optional fields accept None and values."""

    def test_minimal(self):
        req = FeedbackRequest(
            conversation_id="c1", message_index=0, sentiment="up",
        )
        assert req.query_text is None
        assert req.chunk_ids is None
        assert req.scores is None
        assert req.password is None

    def test_with_values(self):
        req = FeedbackRequest(
            conversation_id="c1",
            message_index=1,
            sentiment="down",
            query_text="test query",
            chunk_ids=["a", "b"],
            scores=[0.9, 0.8],
            password="secret",
        )
        assert req.query_text == "test query"
        assert req.chunk_ids == ["a", "b"]


class TestConfidenceThresholds:
    """Confidence thresholds: HIGH requires top >= 0.65 and gap > 0.10."""

    def test_high_confidence(self):
        result = compute_confidence([0.85, 0.70])
        assert result.level == ConfidenceLevel.HIGH
        assert result.score >= 0.65
        assert result.top_gap > 0.10

    def test_low_below_threshold(self):
        result = compute_confidence([0.60, 0.55])
        assert result.level == ConfidenceLevel.LOW

    def test_medium_small_gap(self):
        result = compute_confidence([0.80, 0.72])
        assert result.level == ConfidenceLevel.MEDIUM


class TestDevReloadDefault:
    """Settings().dev_reload defaults to False."""

    def test_default(self):
        settings = Settings()
        assert settings.dev_reload is False


class TestCORSOriginsParsing:
    """CORS origins string is comma-split correctly."""

    def test_split(self):
        settings = Settings()
        origins = [o.strip() for o in settings.cors_origins.split(",") if o.strip()]
        assert origins == ["http://localhost:5173", "http://localhost:8100"]


class TestErrorMessageGeneric:
    """Fix 2: Error response must not leak exception details."""

    def test_no_fstring_exc_in_error(self):
        src = Path(__file__).resolve().parent.parent / "src" / "geolab_kb_agent" / "agent" / "orchestrator.py"
        content = src.read_text(encoding="utf-8")
        # The error dict should use a generic message, not interpolate exc
        assert '"Tool execution failed: {exc}"' not in content
        assert "Tool execution failed" in content


class TestDOMPurifyPresent:
    """Fix 1: index.html must include DOMPurify for XSS protection."""

    def test_dompurify_in_html(self):
        src = Path(__file__).resolve().parent.parent / "src" / "geolab_kb_agent" / "static" / "index.html"
        content = src.read_text(encoding="utf-8")
        assert "DOMPurify" in content
        assert "DOMPurify.sanitize" in content
