"""FastAPI application factory for the Music Attribution API.

Provides the ``create_app`` factory function and the ``lifespan`` async
context manager that boots the async database engine on startup and
disposes it on shutdown.  All route modules (attribution, permissions,
health, metrics, CopilotKit) are registered here.

The application follows the *attribution-by-design* philosophy described
in the companion paper (Teikari 2026, Section 4) — provenance metadata
is embedded at creation time rather than retrofitted post-hoc.

Notes
-----
CORS origins are read from ``Settings.cors_origins`` (comma-separated).
The database engine is stored on ``app.state`` so that route-level
dependencies can access it without global singletons.
"""

from __future__ import annotations

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from music_attribution.api.routes.attribution import router as attribution_router
from music_attribution.api.routes.health import router as health_router
from music_attribution.api.routes.metrics import router as metrics_router
from music_attribution.api.routes.permissions import router as permissions_router
from music_attribution.chat.agui_endpoint import router as copilotkit_router
from music_attribution.config import Settings
from music_attribution.db.engine import async_session_factory, create_async_engine_factory

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    """Manage the async database engine lifecycle.

    Creates the SQLAlchemy async engine and session factory on startup,
    attaches them to ``app.state``, and disposes the engine on shutdown.

    Parameters
    ----------
    app : FastAPI
        The FastAPI application instance whose ``state`` will be populated
        with ``async_engine``, ``async_session_factory``, and ``settings``.

    Yields
    ------
    None
        Control is yielded to the application between startup and shutdown.
    """
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

    Instantiates the FastAPI app with metadata, CORS middleware, and all
    route modules.  The ``lifespan`` context manager handles database
    engine startup and shutdown.

    Returns
    -------
    FastAPI
        Fully configured FastAPI application ready to serve.

    Notes
    -----
    Route prefixes:

    * ``/health`` — health check (no prefix)
    * ``/metrics`` — Prometheus metrics (no prefix)
    * ``/api/v1/attributions/`` — attribution CRUD
    * ``/api/v1/permissions/`` — permission checks
    * ``/api/v1/copilotkit`` — AG-UI / CopilotKit SSE endpoint

    Examples
    --------
    >>> from music_attribution.api.app import create_app
    >>> app = create_app()
    >>> app.title
    'Music Attribution API'
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
    app.include_router(metrics_router)
    app.include_router(attribution_router, prefix="/api/v1")
    app.include_router(permissions_router, prefix="/api/v1")
    app.include_router(copilotkit_router, prefix="/api/v1")

    return app
