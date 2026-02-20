"""FastAPI router for voice agent WebSocket endpoint.

Provides a WebSocket endpoint for voice agent interaction during development.
For production, swap to Daily WebRTC transport via config. The server creates
a fresh Pipecat pipeline per WebSocket connection and manages the lifecycle.

The voice router can be mounted on the existing FastAPI app::

    from music_attribution.voice.server import create_voice_router

    app.include_router(create_voice_router())

See Also
--------
music_attribution.api.app : Main FastAPI application factory.
music_attribution.voice.pipeline : Pipeline factory.
"""

from __future__ import annotations

import logging

from fastapi import APIRouter, WebSocket

logger = logging.getLogger(__name__)

# Conditional Pipecat imports
try:
    from pipecat.pipeline.runner import PipelineRunner
    from pipecat.transports.websocket.fastapi import (
        FastAPIWebsocketParams,
        FastAPIWebsocketTransport,
    )

    PIPECAT_AVAILABLE = True
except ImportError:
    PIPECAT_AVAILABLE = False

# Track active connections for health monitoring
_active_connections: int = 0


def create_voice_router() -> APIRouter:
    """Create FastAPI router with voice WebSocket and health endpoints.

    Returns
    -------
    APIRouter
        Router with:
        - ``GET /api/v1/voice/health`` — health check
        - ``WS /api/v1/voice/ws`` — WebSocket voice endpoint
    """
    router = APIRouter(prefix="/api/v1/voice", tags=["voice"])

    @router.get("/health")
    async def voice_health() -> dict:
        """Voice agent health check."""
        return {
            "status": "ok",
            "service": "voice-agent",
            "pipecat_available": PIPECAT_AVAILABLE,
            "active_connections": _active_connections,
        }

    @router.websocket("/ws")
    async def voice_websocket(websocket: WebSocket) -> None:
        """WebSocket endpoint for real-time voice interaction.

        Creates a fresh Pipecat pipeline per connection, streams audio
        frames bidirectionally, and cleans up on disconnect.

        The transport expects 16kHz 16-bit PCM audio frames.
        """
        global _active_connections  # noqa: PLW0603

        if not PIPECAT_AVAILABLE:
            await websocket.accept()
            await websocket.send_json({"error": "Voice agent requires pipecat-ai. Install with: uv sync --group voice"})
            await websocket.close()
            return

        _active_connections += 1
        logger.info("Voice WebSocket connected (active: %d)", _active_connections)

        try:
            from music_attribution.voice.config import VoiceConfig
            from music_attribution.voice.pipeline import build_pipecat_pipeline

            config = VoiceConfig()

            # Create WebSocket transport for this connection
            transport = FastAPIWebsocketTransport(
                websocket=websocket,
                params=FastAPIWebsocketParams(
                    audio_in_enabled=True,
                    audio_out_enabled=True,
                ),
            )

            # Build pipeline with transport
            pipeline, task = build_pipecat_pipeline(config, transport=transport)

            # Run pipeline until disconnect
            runner = PipelineRunner(handle_sigint=False)
            await runner.run(task)

        except Exception:
            logger.exception("Voice WebSocket error")
        finally:
            _active_connections -= 1
            logger.info("Voice WebSocket disconnected (active: %d)", _active_connections)

    return router
