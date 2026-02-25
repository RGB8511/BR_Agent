"""Voyage AI batched embedding client."""

from __future__ import annotations

import time

import voyageai


class Embedder:
    def __init__(
        self,
        api_key: str,
        model: str = "voyage-3-large",
        batch_size: int = 128,
        dims: int = 1024,
    ) -> None:
        self.client = voyageai.Client(api_key=api_key)
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
        try:
            result = self.client.embed(
                batch,
                model=self.model,
                input_type=input_type,
            )
            return result.embeddings
        except Exception:
            time.sleep(2)
            result = self.client.embed(
                batch,
                model=self.model,
                input_type=input_type,
            )
            return result.embeddings
