"""Shared database session helper for route modules.

Provides ``get_session`` which extracts the ``async_sessionmaker`` from
``request.app.state`` and returns a new ``AsyncSession``.  This module
is the **single source of truth** for obtaining a database session in
API route handlers — no route module should define its own session helper.

The session factory is created in the ``lifespan`` context manager
(see ``music_attribution.api.app``) and stored on ``app.state``.
"""

from __future__ import annotations

import logging

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

logger = logging.getLogger(__name__)


def get_session(request: Request) -> AsyncSession:
    """Get an async session from the application's session factory.

    Parameters
    ----------
    request : Request
        FastAPI request object with access to ``app.state``.

    Returns
    -------
    AsyncSession
        A new async database session. Caller must use it as a context
        manager (``async with``) to ensure proper cleanup.
    """
    factory: async_sessionmaker[AsyncSession] = request.app.state.async_session_factory
    return factory()
