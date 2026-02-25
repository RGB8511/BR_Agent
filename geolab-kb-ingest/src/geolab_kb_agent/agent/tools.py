"""Tool definitions in Anthropic tool-use format."""

from __future__ import annotations

TOOLS: list[dict] = [
    {
        "name": "search_kb",
        "description": (
            "Semantic search across all knowledge-base chunks (theory, equations, "
            "tables, standards, manifests). Use this as the primary search tool "
            "for any geotechnical question."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Natural-language search query.",
                },
                "chunk_type": {
                    "type": "string",
                    "enum": ["theory", "equation", "table", "standard", "manifest"],
                    "description": "Optional filter to a specific chunk type.",
                },
                "discipline": {
                    "type": "string",
                    "description": (
                        "Optional filter by discipline (e.g. 'geotechnical', "
                        "'concrete', 'rock-mechanics', 'soil-mechanics')."
                    ),
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of results to return (default 5, max 20).",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "lookup_equation",
        "description": (
            "Look up a specific equation by its chunk ID, or search for equations "
            "matching a query. Use this when the user asks about a specific formula, "
            "equation, or calculation method."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "equation_id": {
                    "type": "string",
                    "description": "Exact chunk ID of the equation (e.g. 'soil-mechanics.consolidation.eq.cc-virgin-compression').",
                },
                "query": {
                    "type": "string",
                    "description": "Search query to find equations by content (used when equation_id is not known).",
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of results for query search (default 5).",
                },
            },
            "required": [],
        },
    },
    {
        "name": "lookup_table",
        "description": (
            "Look up a specific reference table by its chunk ID, or search for "
            "tables matching a query. Use this when the user asks about "
            "classification tables, reference values, or lookup data."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "table_id": {
                    "type": "string",
                    "description": "Exact chunk ID of the table (e.g. 'rock-mechanics.ucs-testing.tbl.isrm-strength-classification').",
                },
                "query": {
                    "type": "string",
                    "description": "Search query to find tables by content (used when table_id is not known).",
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of results for query search (default 5).",
                },
            },
            "required": [],
        },
    },
    {
        "name": "get_package_info",
        "description": (
            "List all knowledge-base packages (topics) or get the manifest for a "
            "specific package. Use this when the user asks what topics are available, "
            "or wants to browse the knowledge base structure."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "package_id": {
                    "type": "string",
                    "description": (
                        "Specific package ID to retrieve (e.g. 'soil-mechanics.consolidation'). "
                        "Omit to list all packages."
                    ),
                },
            },
            "required": [],
        },
        "cache_control": {"type": "ephemeral"},
    },
]
