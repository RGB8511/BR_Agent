"""Tool definitions in Anthropic tool-use format."""

from __future__ import annotations

from .projects import get_project_names

TOOLS: list[dict] = [
    {
        "name": "search_kb",
        "description": (
            "Semantic search across knowledge-base chunks (theory, equations, "
            "tables, standards, manifests) AND project documents (narratives, "
            "tables, CSV data). Use this as the primary search tool for any "
            "geotechnical question, whether about reference material or "
            "project-specific data."
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
                    "enum": [
                        "theory", "equation", "table", "standard",
                        "manifest", "narrative", "csv_data",
                    ],
                    "description": (
                        "Optional filter to a specific chunk type. Use 'narrative' "
                        "or 'table' for project documents, 'csv_data' for ingested "
                        "CSV data files."
                    ),
                },
                "discipline": {
                    "type": "string",
                    "description": (
                        "Optional filter by discipline (e.g. 'geotechnical', "
                        "'concrete', 'rock-mechanics', 'soil-mechanics')."
                    ),
                },
                "source": {
                    "type": "string",
                    "enum": ["kb", "project"],
                    "description": (
                        "Filter to knowledge base packages ('kb') or project "
                        "documents ('project'). Omit to search all."
                    ),
                },
                "project": {
                    "type": "string",
                    "description": (
                        "Filter to a specific project. Available: "
                        + ", ".join(f"'{n}'" for n in get_project_names())
                        + ". Only applies when source='project'."
                    ),
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of results to return (default 5, max 20).",
                },
                "year_min": {
                    "type": "integer",
                    "description": (
                        "Filter results to chunks containing years >= this value. "
                        "Use for temporal queries like 'what happened after 2010'."
                    ),
                },
                "year_max": {
                    "type": "integer",
                    "description": (
                        "Filter results to chunks containing years <= this value. "
                        "Use for temporal queries like 'data before 2020'."
                    ),
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
    {
        "name": "list_projects",
        "description": (
            "List all available projects with metadata (dam type, location, key "
            "issues, document counts). Use when the user asks about available "
            "projects or to disambiguate which project a query refers to."
        ),
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
]
