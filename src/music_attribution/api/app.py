"""FastAPI application factory for attribution API."""

from __future__ import annotations

import uuid

from fastapi import FastAPI

from music_attribution.api.routes.attribution import router as attribution_router
from music_attribution.api.routes.health import router as health_router
from music_attribution.schemas.attribution import AttributionRecord


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        Configured FastAPI application.
    """
    app = FastAPI(
        title="Music Attribution API",
        description="REST API for querying music attribution records",
        version="0.1.0",
    )

    # In-memory storage for development/testing
    app.state.attributions = {}  # dict[uuid.UUID, AttributionRecord]

    app.include_router(health_router)
    app.include_router(attribution_router, prefix="/api/v1")

    return app
