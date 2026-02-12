"""FastAPI application factory for attribution API."""

from __future__ import annotations

import logging
import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from music_attribution.api.routes.attribution import router as attribution_router
from music_attribution.api.routes.health import router as health_router
from music_attribution.api.routes.permissions import router as permissions_router
from music_attribution.chat.agui_endpoint import router as copilotkit_router
from music_attribution.db.engine import async_session_factory, create_async_engine_factory

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage async engine lifecycle: create on startup, dispose on shutdown."""
    try:
        database_url = os.environ["DATABASE_URL"]
    except KeyError:
        msg = (
            "DATABASE_URL environment variable is required. "
            "Set it to a PostgreSQL connection string, e.g.: "
            "postgresql+psycopg://user:pass@localhost:5432/music_attribution"  # pragma: allowlist secret
        )
        raise RuntimeError(msg) from None

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

    # CORS for frontend dev server
    app.add_middleware(
        CORSMiddleware,
        allow_origins=os.environ.get("CORS_ORIGINS", "http://localhost:3000").split(","),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Kept for backward compatibility with existing tests
    app.state.attributions = {}

    app.include_router(health_router)
    app.include_router(attribution_router, prefix="/api/v1")
    app.include_router(permissions_router, prefix="/api/v1")
    app.include_router(copilotkit_router, prefix="/api/v1")

    return app
