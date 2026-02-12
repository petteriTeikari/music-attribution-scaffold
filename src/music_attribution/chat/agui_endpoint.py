"""AG-UI protocol endpoint for CopilotKit integration.

Provides SSE streaming via FastAPI for the attribution agent.
CopilotKit connects to this endpoint and receives AG-UI events
(TextMessageStart, TextMessageContent, TextMessageEnd, etc.).
"""

from __future__ import annotations

import json
import logging
from collections.abc import AsyncGenerator
from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from music_attribution.chat.agent import AgentDeps, create_attribution_agent
from music_attribution.chat.state import AttributionAgentState

logger = logging.getLogger(__name__)

router = APIRouter()

# Lazy singleton agent instance
_agent = None


def _get_agent():
    """Get or create the singleton agent instance."""
    global _agent  # noqa: PLW0603
    if _agent is None:
        _agent = create_attribution_agent()
    return _agent


async def _generate_sse_events(
    messages: list[dict],
    state: AttributionAgentState,
    session_factory: Any = None,
) -> AsyncGenerator[str]:
    """Generate SSE events from the agent response.

    This is a simplified AG-UI adapter that streams text message events.
    In production, PydanticAI's AGUIAdapter would be used for full
    protocol compliance with all 31 event types.

    Args:
        messages: Conversation messages from CopilotKit.
        state: Current agent state.
        session_factory: Async session factory for database access.

    Yields:
        SSE-formatted event strings.
    """
    import uuid

    run_id = str(uuid.uuid4())
    message_id = str(uuid.uuid4())

    # Emit RunStarted
    yield _sse_event("RunStarted", {"runId": run_id})

    # Emit TextMessageStart
    yield _sse_event(
        "TextMessageStart",
        {
            "messageId": message_id,
            "role": "assistant",
        },
    )

    # Extract user message
    user_message = ""
    for msg in reversed(messages):
        if msg.get("role") == "user":
            content = msg.get("content", "")
            if isinstance(content, str):
                user_message = content
            elif isinstance(content, list):
                user_message = " ".join(part.get("text", "") for part in content if part.get("type") == "text")
            break

    if not user_message:
        user_message = "Hello"

    # Run agent (simplified — in production would stream token by token)
    deps = AgentDeps(state=state, session_factory=session_factory)
    agent = _get_agent()

    try:
        result = await agent.run(user_message, deps=deps)
        response_text = result.data if isinstance(result.data, str) else str(result.data)
    except Exception:
        logger.exception("Agent error")
        response_text = "I encountered an error processing your request. Please try again."

    # Emit TextMessageContent (chunked for streaming feel)
    chunk_size = 50
    for i in range(0, len(response_text), chunk_size):
        chunk = response_text[i : i + chunk_size]
        yield _sse_event("TextMessageContent", {"content": chunk})

    # Emit TextMessageEnd
    yield _sse_event("TextMessageEnd", {})

    # Emit state snapshot
    yield _sse_event(
        "StateSnapshot",
        {
            "snapshot": state.model_dump(mode="json"),
        },
    )

    # Emit RunFinished
    yield _sse_event("RunFinished", {"runId": run_id})


def _sse_event(event_type: str, data: dict) -> str:
    """Format a single SSE event.

    Args:
        event_type: AG-UI event type name.
        data: Event payload.

    Returns:
        SSE-formatted string with event type and JSON data.
    """
    payload = {"type": event_type, **data}
    return f"data: {json.dumps(payload)}\n\n"


@router.post("/copilotkit")
async def copilotkit_endpoint(request: Request) -> StreamingResponse:
    """CopilotKit AG-UI endpoint.

    Receives conversation messages from CopilotKit and streams
    AG-UI events back via SSE.

    Args:
        request: FastAPI request with CopilotKit payload.

    Returns:
        SSE StreamingResponse with AG-UI events.
    """
    body = await request.json()
    messages = body.get("messages", [])

    # Get or create state
    state = AttributionAgentState()

    # Extract async session factory for DB access
    session_factory: Any = getattr(request.app.state, "async_session_factory", None)

    return StreamingResponse(
        _generate_sse_events(messages, state, session_factory),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
