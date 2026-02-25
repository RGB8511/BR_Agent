"""In-memory conversation store with TTL eviction."""

from __future__ import annotations

import secrets
import time
from dataclasses import dataclass, field
from typing import Any

DEFAULT_TTL = 3600  # 1 hour


@dataclass
class Conversation:
    """A single conversation's message history in Anthropic API format."""

    id: str
    messages: list[dict[str, Any]] = field(default_factory=list)
    created_at: float = field(default_factory=time.monotonic)
    last_active: float = field(default_factory=time.monotonic)

    def add_user_message(self, content: str) -> None:
        self.messages.append({"role": "user", "content": content})
        self.last_active = time.monotonic()

    def add_assistant_message(self, content: str) -> None:
        self.messages.append({"role": "assistant", "content": content})
        self.last_active = time.monotonic()

    def add_tool_results(self, results: list[dict[str, Any]]) -> None:
        self.messages.append({"role": "user", "content": results})
        self.last_active = time.monotonic()


class ConversationStore:
    """Dict-backed store with lazy TTL eviction."""

    def __init__(self, ttl: float = DEFAULT_TTL) -> None:
        self._convos: dict[str, Conversation] = {}
        self._ttl = ttl

    def get_or_create(self, conversation_id: str | None = None) -> Conversation:
        """Return existing conversation or create a new one."""
        self._evict()

        if conversation_id and conversation_id in self._convos:
            conv = self._convos[conversation_id]
            conv.last_active = time.monotonic()
            return conv

        new_id = conversation_id or secrets.token_hex(8)
        conv = Conversation(id=new_id)
        self._convos[new_id] = conv
        return conv

    def _evict(self) -> None:
        """Remove conversations that have exceeded the TTL."""
        now = time.monotonic()
        expired = [
            cid
            for cid, conv in self._convos.items()
            if now - conv.last_active > self._ttl
        ]
        for cid in expired:
            del self._convos[cid]
