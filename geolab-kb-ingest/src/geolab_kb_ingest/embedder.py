"""Voyage AI batched embedding client.

Uses direct HTTP calls instead of the voyageai SDK to avoid
Pydantic v1/v2 incompatibility on Python 3.14+.
"""

from __future__ import annotations

import logging
import time

import requests

logger = logging.getLogger(__name__)


class Embedder:
    _API_URL = "https://api.voyageai.com/v1/embeddings"

    def __init__(
        self,
        api_key: str,
        model: str = "voyage-3-large",
        batch_size: int = 128,
        dims: int = 1024,
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.batch_size = batch_size
        self.dims = dims

    def embed_texts(self, texts: list[str], input_type: str = "document") -> list[list[float]]:
        """Embed texts in batches. Retry once on failure per batch."""
        all_embeddings: list[list[float]] = []
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i : i + self.batch_size]
            embeddings = self._embed_batch(batch, input_type)
            all_embeddings.extend(embeddings)
        return all_embeddings

    def _embed_batch(self, batch: list[str], input_type: str) -> list[list[float]]:
        """Single batch API call with one retry."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "input": batch,
            "model": self.model,
            "input_type": input_type,
        }
        try:
            resp = requests.post(self._API_URL, json=payload, headers=headers, timeout=60)
            resp.raise_for_status()
            return [item["embedding"] for item in resp.json()["data"]]
        except Exception:
            logger.warning("Embedding failed, retrying once", exc_info=True)
            time.sleep(2)
            resp = requests.post(self._API_URL, json=payload, headers=headers, timeout=60)
            resp.raise_for_status()
            return [item["embedding"] for item in resp.json()["data"]]
