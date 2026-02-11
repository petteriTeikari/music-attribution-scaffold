"""Sync and async SQLAlchemy engine factories with pool hardening.

Pool hardening lessons from uad-copilot stochastic delay analysis:
- pool_pre_ping: detect stale/dead connections before use
- pool_size + max_overflow: prevent connection exhaustion
- pool_recycle: recycle connections hourly to prevent staleness
- statement_timeout: query-level timeout to prevent hangs
"""

from __future__ import annotations

import logging
from collections.abc import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

logger = logging.getLogger(__name__)

# Pool hardening defaults (from uad-copilot stochastic delay lessons)
DEFAULT_POOL_SIZE = 5
DEFAULT_MAX_OVERFLOW = 10
DEFAULT_POOL_RECYCLE = 3600  # 1 hour
DEFAULT_STATEMENT_TIMEOUT_MS = 30_000  # 30 seconds


def create_sync_engine(database_url: str) -> Engine:
    """Create a synchronous SQLAlchemy engine.

    Used by Alembic migrations (which require sync engines).

    Args:
        database_url: PostgreSQL connection string.

    Returns:
        SQLAlchemy Engine instance.
    """
    return create_engine(database_url, echo=False)


def create_async_engine_factory(
    database_url: str,
    *,
    pool_size: int = DEFAULT_POOL_SIZE,
    max_overflow: int = DEFAULT_MAX_OVERFLOW,
    pool_recycle: int = DEFAULT_POOL_RECYCLE,
    statement_timeout_ms: int = DEFAULT_STATEMENT_TIMEOUT_MS,
    echo: bool = False,
) -> AsyncEngine:
    """Create an async SQLAlchemy engine with pool hardening.

    Args:
        database_url: Database connection string.
            PostgreSQL: ``postgresql+psycopg://user:pass@host/db``
            SQLite (tests): ``sqlite+aiosqlite:///``
        pool_size: Maximum number of permanent connections.
        max_overflow: Extra connections allowed beyond pool_size.
        pool_recycle: Seconds before a connection is recycled.
        statement_timeout_ms: Query timeout in milliseconds.
        echo: Whether to log SQL statements.

    Returns:
        Configured AsyncEngine with pool hardening.
    """
    # Build connect_args for PostgreSQL statement timeout
    connect_args: dict[str, str] = {}
    is_postgresql = database_url.startswith("postgresql")
    if is_postgresql:
        connect_args["options"] = f"-c statement_timeout={statement_timeout_ms}"

    # SQLite doesn't support pool_size/max_overflow with StaticPool
    # so we conditionally pass pool params
    kwargs: dict[str, object] = {
        "echo": echo,
        "pool_pre_ping": True,
        "pool_recycle": pool_recycle,
    }

    if is_postgresql:
        kwargs["pool_size"] = pool_size
        kwargs["max_overflow"] = max_overflow
        kwargs["connect_args"] = connect_args

    engine = create_async_engine(database_url, **kwargs)

    logger.info(
        "Created async engine: pool_pre_ping=True, pool_recycle=%d",
        pool_recycle,
    )

    return engine


def async_session_factory(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    """Create an async session factory bound to an engine.

    Args:
        engine: AsyncEngine to bind sessions to.

    Returns:
        Configured async_sessionmaker.
    """
    return async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


async def get_async_session(
    factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    """Yield an async session and ensure cleanup.

    Usage as a FastAPI dependency::

        async for session in get_async_session(factory):
            await session.execute(...)

    Args:
        factory: Session factory to create sessions from.

    Yields:
        AsyncSession that is closed after use.
    """
    async with factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
