"""Query expansion using Claude Haiku for domain-specific synonyms.

Bridges the vocabulary gap between natural-language user queries
("What is the dam height?") and technical chunk content
("crest elevation 5,195 ft").
"""

from __future__ import annotations

import logging

import anthropic

logger = logging.getLogger(__name__)

_EXPANSION_PROMPT = (
    "Add 3-5 technical synonyms and related terms for this dam engineering "
    "query. Return only the expanded query, no explanation: {query}"
)


def expand_query(query: str, api_key: str) -> str:
    """Expand a query with domain-specific synonyms via Claude Haiku.

    Returns the original query + expansion as a single string for embedding.
    Falls back to the original query on any failure.

    Cost: ~$0.001 per query.
    """
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            messages=[
                {
                    "role": "user",
                    "content": _EXPANSION_PROMPT.format(query=query),
                }
            ],
        )
        expanded = message.content[0].text.strip()
        if expanded:
            return f"{query} {expanded}"
    except Exception:
        logger.warning("Query expansion failed, using original query", exc_info=True)

    return query
