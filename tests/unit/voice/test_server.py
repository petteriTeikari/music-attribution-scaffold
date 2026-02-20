"""Tests for voice agent FastAPI router."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.testclient import TestClient

from music_attribution.voice.server import PIPECAT_AVAILABLE, create_voice_router


class TestVoiceRouter:
    """Tests for the voice agent router."""

    def test_router_creation(self) -> None:
        """Router is created without errors."""
        router = create_voice_router()
        assert router is not None

    def test_health_endpoint(self) -> None:
        """Voice health endpoint returns ok status."""
        app = FastAPI()
        app.include_router(create_voice_router())
        client = TestClient(app)
        response = client.get("/api/v1/voice/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["service"] == "voice-agent"

    def test_router_prefix(self) -> None:
        """Router uses /api/v1/voice prefix."""
        router = create_voice_router()
        assert router.prefix == "/api/v1/voice"

    def test_router_tags(self) -> None:
        """Router is tagged with 'voice'."""
        router = create_voice_router()
        assert "voice" in router.tags


class TestHealthEndpointDetails:
    """Tests for the extended voice health endpoint."""

    def test_health_includes_pipecat_status(self) -> None:
        """Health endpoint reports pipecat availability."""
        app = FastAPI()
        app.include_router(create_voice_router())
        client = TestClient(app)
        data = client.get("/api/v1/voice/health").json()
        assert "pipecat_available" in data
        assert isinstance(data["pipecat_available"], bool)

    def test_health_includes_connection_count(self) -> None:
        """Health endpoint reports active connection count."""
        app = FastAPI()
        app.include_router(create_voice_router())
        client = TestClient(app)
        data = client.get("/api/v1/voice/health").json()
        assert "active_connections" in data
        assert data["active_connections"] == 0


class TestWebSocketEndpoint:
    """Tests for the WebSocket voice endpoint."""

    def test_websocket_endpoint_exists(self) -> None:
        """WebSocket endpoint is registered on the router."""
        router = create_voice_router()
        ws_routes = [r for r in router.routes if hasattr(r, "path") and r.path.endswith("/ws")]
        assert len(ws_routes) == 1

    def test_websocket_graceful_without_pipecat(self) -> None:
        """WebSocket sends error JSON when pipecat not installed."""
        if PIPECAT_AVAILABLE:
            return  # Skip — this test is for non-pipecat environments

        app = FastAPI()
        app.include_router(create_voice_router())
        client = TestClient(app)
        with client.websocket_connect("/api/v1/voice/ws") as ws:
            data = ws.receive_json()
            assert "error" in data
            assert "pipecat-ai" in data["error"]
