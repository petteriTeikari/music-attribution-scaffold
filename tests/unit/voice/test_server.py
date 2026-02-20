"""Tests for voice agent FastAPI router."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.testclient import TestClient

from music_attribution.voice.server import create_voice_router


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
