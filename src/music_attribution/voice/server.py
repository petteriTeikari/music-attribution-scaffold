"""FastAPI router for voice agent WebSocket endpoint.

Provides a WebSocket endpoint for voice agent interaction during development.
For production, swap to Daily WebRTC transport via config.

See Also
--------
music_attribution.api.app : Main FastAPI application factory.
"""

from __future__ import annotations

import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)


def create_voice_router() -> APIRouter:
    """Create FastAPI router with voice WebSocket endpoint.

    Returns
    -------
    APIRouter
        Router with ``/api/v1/voice/ws`` WebSocket endpoint.
    """
    router = APIRouter(prefix="/api/v1/voice", tags=["voice"])

    @router.get("/health")
    async def voice_health() -> dict:
        """Voice agent health check."""
        return {"status": "ok", "service": "voice-agent"}

    return router
