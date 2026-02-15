"""Music Attribution Scaffold - chat module.

PydanticAI agent with AG-UI protocol support for CopilotKit integration.

This module implements the conversational interface to the attribution
scaffold, enabling natural-language queries about attribution records,
confidence explanations, correction suggestions, and structured feedback
submission.

Submodules
----------
agent
    PydanticAI agent factory and four domain tool definitions.
state
    Shared Pydantic state model synchronised between agent and frontend
    via AG-UI ``StateSnapshot`` events.
agui_endpoint
    FastAPI SSE endpoint that bridges PydanticAI agent responses to the
    CopilotKit frontend using the AG-UI protocol.
"""

from __future__ import annotations
