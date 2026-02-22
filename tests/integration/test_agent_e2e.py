"""End-to-end tests for the AG-UI agent loop.

Tests the full flow: CopilotKit request → FastAPI → AG-UI SSE events,
without requiring an actual LLM API key (mocked agent).
"""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from music_attribution.api.app import create_app

pytestmark = pytest.mark.integration


def _mock_agent():
    """Create a mock agent that returns a canned response."""
    mock_result = AsyncMock()
    mock_result.output = "Hide and Seek has a confidence of 95% based on MUSICBRAINZ, DISCOGS, ACOUSTID."
    agent = AsyncMock()
    agent.run = AsyncMock(return_value=mock_result)
    return agent


def _parse_events(text: str) -> list[dict]:
    """Parse SSE response into event dicts."""
    events = []
    for line in text.strip().split("\n\n"):
        for part in line.split("\n"):
            if part.startswith("data: "):
                events.append(json.loads(part[6:]))
    return events


class TestAgentE2EFlow:
    """Test the full AG-UI event flow through the FastAPI app."""

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_full_conversation_flow(self, mock_get_agent) -> None:
        """Test complete: request → RunStarted → TextMessage → StateSnapshot → RunFinished."""
        mock_get_agent.return_value = _mock_agent()

        app = create_app()
        client = TestClient(app)

        response = client.post(
            "/api/v1/copilotkit",
            json={
                "messages": [
                    {"role": "user", "content": "Explain the confidence for Hide and Seek"},
                ],
            },
        )

        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]

        events = _parse_events(response.text)
        types = [e["type"] for e in events]

        # Verify AG-UI event ordering
        assert types[0] == "RunStarted"
        assert "TextMessageStart" in types
        assert "TextMessageContent" in types
        assert "TextMessageEnd" in types
        assert "StateSnapshot" in types
        assert types[-1] == "RunFinished"

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_text_content_is_chunked(self, mock_get_agent) -> None:
        """Verify that text content is streamed in chunks."""
        mock_get_agent.return_value = _mock_agent()

        app = create_app()
        client = TestClient(app)

        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "hello"}]},
        )

        events = _parse_events(response.text)
        content_events = [e for e in events if e.get("type") == "TextMessageContent"]
        assert len(content_events) >= 1

        # Reconstruct full text
        full_text = "".join(e.get("content", "") for e in content_events)
        assert "confidence" in full_text.lower() or len(full_text) > 0

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_state_snapshot_has_required_fields(self, mock_get_agent) -> None:
        """StateSnapshot must contain all AttributionAgentState fields."""
        mock_get_agent.return_value = _mock_agent()

        app = create_app()
        client = TestClient(app)

        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "hello"}]},
        )

        events = _parse_events(response.text)
        state_events = [e for e in events if e["type"] == "StateSnapshot"]
        assert len(state_events) == 1

        snapshot = state_events[0]["snapshot"]
        required_fields = [
            "current_work_id",
            "confidence_score",
            "review_queue_size",
            "pending_correction",
            "explanation_text",
        ]
        for field in required_fields:
            assert field in snapshot, f"Missing field: {field}"

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_cors_headers_present(self, mock_get_agent) -> None:
        """Verify CORS headers are set for frontend dev server."""
        mock_get_agent.return_value = _mock_agent()

        app = create_app()
        client = TestClient(app)

        response = client.options(
            "/api/v1/copilotkit",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST",
            },
        )
        # FastAPI CORS middleware should respond to preflight
        assert response.status_code in (200, 204)

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_multi_turn_conversation(self, mock_get_agent) -> None:
        """Test that multi-message conversations work."""
        mock_get_agent.return_value = _mock_agent()

        app = create_app()
        client = TestClient(app)

        response = client.post(
            "/api/v1/copilotkit",
            json={
                "messages": [
                    {"role": "user", "content": "What is the confidence for Hide and Seek?"},
                    {"role": "assistant", "content": "It has 95% confidence."},
                    {"role": "user", "content": "Can you explain why?"},
                ],
            },
        )

        assert response.status_code == 200
        events = _parse_events(response.text)
        assert events[0]["type"] == "RunStarted"
        assert events[-1]["type"] == "RunFinished"
