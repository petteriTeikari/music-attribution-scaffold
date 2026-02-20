"""Bridge PydanticAI domain tools to Pipecat function calling.

Registers the 4 existing domain tools (explain_confidence, search_attributions,
suggest_correction, submit_feedback) as Pipecat-compatible function schemas.
Tool handlers delegate to the existing PydanticAI tool logic — no business
logic duplication.

See Also
--------
music_attribution.chat.agent : Existing PydanticAI agent with domain tools.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def get_tool_schemas() -> list[dict]:
    """Return Pipecat-compatible function schemas for domain tools.

    Each schema defines the function name, description, and parameters
    in the format expected by Pipecat's ToolsSchema / FunctionSchema.

    Returns
    -------
    list[dict]
        List of function schema dictionaries.
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "explain_confidence",
                "description": "Explain the confidence score for an attribution record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_id": {
                            "type": "string",
                            "description": "UUID of the attribution record",
                        },
                    },
                    "required": ["work_id"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_attributions",
                "description": "Search attribution records by title, artist, or keyword",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query",
                        },
                    },
                    "required": ["query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "suggest_correction",
                "description": "Suggest a correction to an attribution record field",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_id": {"type": "string"},
                        "field": {"type": "string"},
                        "current_value": {"type": "string"},
                        "suggested_value": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["work_id", "field", "current_value", "suggested_value", "reason"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "submit_feedback",
                "description": "Submit structured feedback for an attribution record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_id": {"type": "string"},
                        "overall_assessment": {"type": "number"},
                        "free_text": {"type": "string"},
                    },
                    "required": ["work_id", "overall_assessment"],
                },
            },
        },
    ]
