"""FastAPI application factory for attribution API."""

from __future__ import annotations

import logging
import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from music_attribution.api.routes.attribution import router as attribution_router
from music_attribution.api.routes.health import router as health_router
from music_attribution.api.routes.permissions import router as permissions_router
from music_attribution.db.engine import async_session_factory, create_async_engine_factory

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage async engine lifecycle: create on startup, dispose on shutdown."""
    database_url = os.environ.get("DATABASE_URL", "sqlite+aiosqlite://")

    engine = create_async_engine_factory(database_url)
    factory = async_session_factory(engine)

    app.state.async_engine = engine
    app.state.async_session_factory = factory

    logger.info("Database engine created: %s", database_url.split("@")[-1] if "@" in database_url else "in-memory")

    yield

    await engine.dispose()
    logger.info("Database engine disposed")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        Configured FastAPI application.
    """
    app = FastAPI(
        title="Music Attribution API",
        description="REST API for querying music attribution records",
        version="0.1.0",
        lifespan=lifespan,
    )

    # Kept for backward compatibility with existing tests
    app.state.attributions = {}

    app.include_router(health_router)
    app.include_router(attribution_router, prefix="/api/v1")
    app.include_router(permissions_router, prefix="/api/v1")

    return app
