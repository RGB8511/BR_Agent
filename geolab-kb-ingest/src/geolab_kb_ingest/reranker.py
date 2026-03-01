"""Voyage AI reranker client.

Uses direct HTTP calls (matching the pattern in embedder.py) to rerank
retrieved chunks by query-document relevance using a cross-encoder model.
"""

from __future__ import annotations

import logging
import time

import requests

logger = logging.getLogger(__name__)


class Reranker:
    _API_URL = "https://api.voyageai.com/v1/rerank"

    def __init__(
        self,
        api_key: str,
        model: str = "rerank-2.5",
    ) -> None:
        self.api_key = api_key
        self.model = model

    def rerank(
        self,
        query: str,
        documents: list[str],
        top_k: int | None = None,
    ) -> list[dict]:
        """Rerank documents by relevance to query.

        Args:
            query: The search query.
            documents: List of document texts to rerank.
            top_k: Number of top results to return (default: all).

        Returns:
            List of dicts with 'index' (original position) and
            'relevance_score', sorted by descending relevance.
        """
        if not documents:
            return []

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload: dict = {
            "query": query,
            "documents": documents,
            "model": self.model,
            "truncation": True,
        }
        if top_k is not None:
            payload["top_k"] = top_k

        try:
            resp = requests.post(
                self._API_URL, json=payload, headers=headers, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()["data"]
        except Exception:
            logger.warning("Rerank failed, retrying once", exc_info=True)
            time.sleep(2)
            resp = requests.post(
                self._API_URL, json=payload, headers=headers, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()["data"]
