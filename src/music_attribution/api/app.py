"""FastAPI application factory for attribution API."""

from __future__ import annotations

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from music_attribution.api.routes.attribution import router as attribution_router
from music_attribution.api.routes.health import router as health_router
from music_attribution.api.routes.permissions import router as permissions_router
from music_attribution.chat.agui_endpoint import router as copilotkit_router
from music_attribution.config import Settings
from music_attribution.db.engine import async_session_factory, create_async_engine_factory

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    """Manage async engine lifecycle: create on startup, dispose on shutdown."""
    settings = Settings()  # type: ignore[call-arg]

    engine = create_async_engine_factory(settings.database_url)
    factory = async_session_factory(engine)

    app.state.async_engine = engine
    app.state.async_session_factory = factory
    app.state.settings = settings

    db_host = settings.database_url.split("@")[-1] if "@" in settings.database_url else "unknown"
    logger.info("Database engine created: %s", db_host)

    yield

    await engine.dispose()
    logger.info("Database engine disposed")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        Configured FastAPI application.
    """
    settings = Settings()  # type: ignore[call-arg]

    app = FastAPI(
        title="Music Attribution API",
        description="REST API for querying music attribution records",
        version="0.1.0",
        lifespan=lifespan,
    )

    # CORS for frontend dev server
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins.split(","),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_router)
    app.include_router(attribution_router, prefix="/api/v1")
    app.include_router(permissions_router, prefix="/api/v1")
    app.include_router(copilotkit_router, prefix="/api/v1")

    return app
