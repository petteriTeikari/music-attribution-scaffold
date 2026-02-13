"""FastAPI dependency injection for database sessions.

Provides the ``get_db_session`` async generator dependency that yields
a scoped ``AsyncSession`` per HTTP request.  The session is automatically
rolled back on unhandled exceptions and closed when the request
completes.

Notes
-----
This module is imported by route modules via ``Depends(get_db_session)``.
The session factory itself is created in the ``lifespan`` context manager
(see ``music_attribution.api.app``) and stored on ``app.state``.
"""

from __future__ import annotations

import logging
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

logger = logging.getLogger(__name__)


async def get_db_session(
    factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession]:
    """Yield an async database session scoped to a single HTTP request.

    Intended as a FastAPI dependency.  The session is automatically
    closed when the request completes, with an explicit rollback on
    unhandled exceptions to prevent partial writes.

    Parameters
    ----------
    factory : async_sessionmaker[AsyncSession]
        Session factory bound to the application's async engine.  Typically
        retrieved from ``request.app.state.async_session_factory``.

    Yields
    ------
    AsyncSession
        An async SQLAlchemy session for use within a single request scope.

    Raises
    ------
    Exception
        Re-raises the original exception after rolling back the session.

    Examples
    --------
    Used as a FastAPI dependency::

        @router.get("/items")
        async def list_items(
            session: AsyncSession = Depends(get_db_session),
        ) -> list[dict]: ...
    """
    async with factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
