"""AG-UI protocol endpoint for CopilotKit integration.

Implements a simplified AG-UI (Agent-GUI) protocol adapter that streams
Server-Sent Events (SSE) from the PydanticAI attribution agent to the
CopilotKit frontend. The AG-UI protocol defines 31 event types; this
adapter implements the subset needed for text-based conversation:

- ``RunStarted`` / ``RunFinished`` -- lifecycle bookends
- ``TextMessageStart`` / ``TextMessageContent`` / ``TextMessageEnd`` --
  streamed assistant response
- ``StateSnapshot`` -- full agent state for frontend synchronisation

In production, PydanticAI's ``AGUIAdapter`` would replace this
simplified implementation to support the full event catalogue
(tool calls, state deltas, action requests, etc.).

The endpoint is mounted at ``/api/v1/copilotkit`` and accepts POST
requests with the CopilotKit message payload.

Notes
-----
The agent instance is a lazy singleton (``_get_agent``) to avoid
requiring an Anthropic API key at import time. Tests mock this
function to inject a test agent.

See Also
--------
music_attribution.chat.agent : Agent factory and tool definitions.
music_attribution.chat.state : Shared state model.
"""

from __future__ import annotations

import json
import logging
import threading
from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from music_attribution.chat.agent import AgentDeps, create_attribution_agent
from music_attribution.chat.state import AttributionAgentState

if TYPE_CHECKING:
    from pydantic_ai import Agent

    from music_attribution.chat.agent import AgentDeps as _AgentDeps

logger = logging.getLogger(__name__)

router = APIRouter()

# Lazy singleton agent instance — guarded by _agent_lock for thread safety.
_agent: Agent[_AgentDeps, str] | None = None
_agent_lock = threading.Lock()


def _get_agent() -> Agent[AgentDeps, str]:
    """Get or create the singleton PydanticAI agent instance.

    Uses a module-level global guarded by a threading lock to ensure
    exactly one agent is created per process, even under concurrent
    requests. The lazy initialisation avoids requiring environment
    variables (e.g. ``ANTHROPIC_API_KEY``) at import time.

    Returns
    -------
    Agent[AgentDeps, str]
        The singleton attribution agent.
    """
    global _agent  # noqa: PLW0603
    if _agent is None:
        with _agent_lock:
            if _agent is None:
                _agent = create_attribution_agent()
    return _agent  # narrowed by double-check above


async def _generate_sse_events(
    messages: list[dict],
    state: AttributionAgentState,
    session_factory: Any = None,
) -> AsyncGenerator[str]:
    """Generate AG-UI Server-Sent Events from the agent response.

    Implements a simplified AG-UI event stream for text-based
    conversation. The response text is chunked into 50-character
    segments to simulate token-by-token streaming in the frontend.

    Event sequence per request::

        RunStarted -> TextMessageStart -> TextMessageContent* ->
        TextMessageEnd -> StateSnapshot -> RunFinished

    Parameters
    ----------
    messages : list[dict]
        Conversation messages from the CopilotKit payload. Each dict
        has ``role`` (``"user"`` / ``"assistant"``) and ``content``
        (string or list of content parts).
    state : AttributionAgentState
        Mutable agent state that is updated by tool calls during the
        run and serialised as a ``StateSnapshot`` event at the end.
    session_factory : Any, optional
        SQLAlchemy ``async_sessionmaker`` for database access. Passed
        to ``AgentDeps`` for tool calls. ``None`` in tests.

    Yields
    ------
    str
        SSE-formatted event strings (``data: {json}\\n\\n``).
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
        response_text = result.output if isinstance(result.output, str) else str(result.output)
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
    """Format a single Server-Sent Event in AG-UI protocol format.

    The AG-UI protocol encodes the event type in the JSON payload
    (as ``type``) rather than using the SSE ``event:`` field, so all
    events use the default ``data:`` field.

    Parameters
    ----------
    event_type : str
        AG-UI event type name (e.g. ``"TextMessageStart"``,
        ``"StateSnapshot"``, ``"RunFinished"``).
    data : dict
        Event-specific payload fields.

    Returns
    -------
    str
        SSE-formatted string: ``data: {"type": ..., ...}\\n\\n``.
    """
    payload = {"type": event_type, **data}
    return f"data: {json.dumps(payload)}\n\n"


@router.post("/copilotkit")
async def copilotkit_endpoint(request: Request) -> StreamingResponse:
    """CopilotKit AG-UI endpoint for agent conversation.

    Receives a CopilotKit message payload via POST, extracts the
    conversation history, and returns an SSE stream of AG-UI events
    generated by the PydanticAI attribution agent.

    The endpoint extracts the ``async_session_factory`` from
    ``request.app.state`` (set during FastAPI startup) to give agent
    tools database access.

    SSE response headers disable caching and buffering to ensure
    low-latency event delivery to the frontend.

    Parameters
    ----------
    request : Request
        FastAPI request containing a JSON body with ``messages``
        (list of ``{role, content}`` dicts) from CopilotKit.

    Returns
    -------
    StreamingResponse
        SSE stream (``text/event-stream``) with AG-UI events.
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
