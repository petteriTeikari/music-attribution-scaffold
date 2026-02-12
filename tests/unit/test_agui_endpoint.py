"""Tests for AG-UI FastAPI endpoint."""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from music_attribution.chat.agui_endpoint import router


@pytest.fixture()
def app() -> FastAPI:
    """Create test FastAPI app with copilotkit router (no in-memory dict)."""
    app = FastAPI()
    app.include_router(router, prefix="/api/v1")
    return app


@pytest.fixture()
def client(app: FastAPI) -> TestClient:
    return TestClient(app)


def _mock_agent_run():
    """Create mock for the agent run method."""
    mock_result = AsyncMock()
    mock_result.data = "This is a test response from the attribution agent."
    mock_agent = AsyncMock()
    mock_agent.run = AsyncMock(return_value=mock_result)
    return mock_agent


class TestCopilotKitEndpoint:
    """Tests for the /api/v1/copilotkit SSE endpoint."""

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_endpoint_returns_sse(self, mock_get_agent, client: TestClient) -> None:
        mock_get_agent.return_value = _mock_agent_run()
        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "Hello"}]},
        )
        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_endpoint_returns_run_events(self, mock_get_agent, client: TestClient) -> None:
        mock_get_agent.return_value = _mock_agent_run()
        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "Hello"}]},
        )
        events = _parse_sse_events(response.text)
        event_types = [e.get("type") for e in events]
        assert "RunStarted" in event_types
        assert "RunFinished" in event_types

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_endpoint_returns_text_message_events(self, mock_get_agent, client: TestClient) -> None:
        mock_get_agent.return_value = _mock_agent_run()
        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "Hello"}]},
        )
        events = _parse_sse_events(response.text)
        event_types = [e.get("type") for e in events]
        assert "TextMessageStart" in event_types
        assert "TextMessageContent" in event_types
        assert "TextMessageEnd" in event_types

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_endpoint_returns_state_snapshot(self, mock_get_agent, client: TestClient) -> None:
        mock_get_agent.return_value = _mock_agent_run()
        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "Hello"}]},
        )
        events = _parse_sse_events(response.text)
        state_events = [e for e in events if e.get("type") == "StateSnapshot"]
        assert len(state_events) == 1
        snapshot = state_events[0].get("snapshot", {})
        assert "review_queue_size" in snapshot

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_endpoint_handles_empty_messages(self, mock_get_agent, client: TestClient) -> None:
        mock_get_agent.return_value = _mock_agent_run()
        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": []},
        )
        assert response.status_code == 200

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_endpoint_works_without_session_factory(self, mock_get_agent) -> None:
        """Test endpoint works when no async_session_factory is set."""
        mock_get_agent.return_value = _mock_agent_run()
        app = FastAPI()
        app.include_router(router, prefix="/api/v1")
        client = TestClient(app)
        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "search something"}]},
        )
        assert response.status_code == 200

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_event_ordering(self, mock_get_agent, client: TestClient) -> None:
        """RunStarted must come first, RunFinished last."""
        mock_get_agent.return_value = _mock_agent_run()
        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "Hi"}]},
        )
        events = _parse_sse_events(response.text)
        assert events[0]["type"] == "RunStarted"
        assert events[-1]["type"] == "RunFinished"

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_agent_error_handled_gracefully(self, mock_get_agent, client: TestClient) -> None:
        """Test that agent errors produce a friendly error message."""
        mock_agent = AsyncMock()
        mock_agent.run = AsyncMock(side_effect=RuntimeError("LLM unavailable"))
        mock_get_agent.return_value = mock_agent
        response = client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "Hello"}]},
        )
        assert response.status_code == 200
        events = _parse_sse_events(response.text)
        content_events = [e for e in events if e.get("type") == "TextMessageContent"]
        full_text = "".join(e.get("content", "") for e in content_events)
        assert "error" in full_text.lower()


class TestEndpointSessionFactory:
    """Tests that endpoint passes session_factory to AgentDeps."""

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_endpoint_passes_session_factory(self, mock_get_agent) -> None:
        """When app.state.async_session_factory exists, it's passed to AgentDeps."""
        mock_get_agent.return_value = _mock_agent_run()
        mock_factory = AsyncMock()

        test_app = FastAPI()
        test_app.state.async_session_factory = mock_factory
        test_app.include_router(router, prefix="/api/v1")
        test_client = TestClient(test_app)

        # Capture the deps passed to agent.run
        captured_deps = []
        original_run = mock_get_agent.return_value.run

        async def capture_run(msg, *, deps=None, **kwargs):
            captured_deps.append(deps)
            return await original_run(msg, deps=deps, **kwargs)

        mock_get_agent.return_value.run = capture_run

        test_client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "Hello"}]},
        )

        assert len(captured_deps) == 1
        assert captured_deps[0].session_factory is mock_factory

    @patch("music_attribution.chat.agui_endpoint._get_agent")
    def test_endpoint_session_factory_none_without_db(self, mock_get_agent) -> None:
        """When app.state has no async_session_factory, deps.session_factory is None."""
        mock_get_agent.return_value = _mock_agent_run()

        test_app = FastAPI()
        test_app.include_router(router, prefix="/api/v1")
        test_client = TestClient(test_app)

        captured_deps = []
        original_run = mock_get_agent.return_value.run

        async def capture_run(msg, *, deps=None, **kwargs):
            captured_deps.append(deps)
            return await original_run(msg, deps=deps, **kwargs)

        mock_get_agent.return_value.run = capture_run

        test_client.post(
            "/api/v1/copilotkit",
            json={"messages": [{"role": "user", "content": "Hello"}]},
        )

        assert len(captured_deps) == 1
        assert captured_deps[0].session_factory is None


def _parse_sse_events(text: str) -> list[dict]:
    """Parse SSE text into list of event dicts."""
    events = []
    for line in text.strip().split("\n\n"):
        for part in line.split("\n"):
            if part.startswith("data: "):
                data = part[6:]
                events.append(json.loads(data))
    return events
