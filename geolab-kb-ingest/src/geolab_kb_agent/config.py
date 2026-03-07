"""Application settings loaded from environment variables."""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="GEOLAB_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str = "postgresql://geolab:geolab@localhost:5432/geolab_kb"
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-sonnet-4-5-20250929"
    voyage_api_key: str = ""
    voyage_model: str = "voyage-3-large"
    embedding_dims: int = 1024
    host: str = "0.0.0.0"
    port: int = 8100
    dev_reload: bool = False
    cors_origins: str = "http://localhost:5173,http://localhost:5174,http://localhost:8100,http://localhost:8101"
    validation_password: str = "admin"


@lru_cache
def get_settings() -> Settings:
    return Settings()
