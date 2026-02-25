"""Application settings loaded from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass, field


@dataclass
class Settings:
    database_url: str = field(default="")
    voyage_api_key: str = field(default="")
    voyage_model: str = "voyage-3-large"
    voyage_batch_size: int = 128
    embedding_dims: int = 1024
    chunk_max_tokens: int = 1500


def get_settings() -> Settings:
    """Build settings from environment variables with sensible defaults."""
    return Settings(
        database_url=os.environ.get(
            "DATABASE_URL",
            "postgresql://geolab:geolab@localhost:5432/geolab_kb",
        ),
        voyage_api_key=os.environ.get("VOYAGE_API_KEY", ""),
        voyage_model=os.environ.get("VOYAGE_MODEL", "voyage-3-large"),
        voyage_batch_size=int(os.environ.get("VOYAGE_BATCH_SIZE", "128")),
        embedding_dims=int(os.environ.get("EMBEDDING_DIMS", "1024")),
        chunk_max_tokens=int(os.environ.get("CHUNK_MAX_TOKENS", "1500")),
    )
