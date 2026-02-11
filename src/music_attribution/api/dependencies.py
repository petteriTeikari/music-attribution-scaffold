"""FastAPI dependency injection for database sessions."""

from __future__ import annotations

import logging
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

logger = logging.getLogger(__name__)


async def get_db_session(
    factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    """Yield an async database session for a single request.

    Intended as a FastAPI dependency. The session is automatically
    closed when the request completes, with rollback on errors.

    Args:
        factory: Session factory bound to an async engine.

    Yields:
        AsyncSession for use within a single request scope.
    """
    async with factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
