"""Async SQLAlchemy engine factory with connection pool hardening.

Provides factory functions for creating hardened async database engines
and session factories. Pool hardening parameters are derived from
production experience (uad-copilot stochastic delay analysis):

- ``pool_pre_ping``: detect stale/dead connections before checkout
- ``pool_size`` + ``max_overflow``: prevent connection exhaustion
  under load
- ``pool_recycle``: recycle connections hourly to prevent staleness
  (important behind PgBouncer or cloud proxies)
- ``statement_timeout``: per-query timeout to prevent long-running
  queries from blocking the pool

The module supports both PostgreSQL (production) and SQLite with
aiosqlite (unit tests). SQLite-specific pool parameters are
automatically skipped.

Functions
---------
create_async_engine_factory
    Create an ``AsyncEngine`` with pool hardening.
async_session_factory
    Create an ``async_sessionmaker`` bound to an engine.
get_async_session
    Async generator yielding sessions with automatic cleanup.

See Also
--------
music_attribution.config.Settings.database_url : Connection string source.
music_attribution.db.models : ORM models using these sessions.
"""

from __future__ import annotations

import logging
from collections.abc import AsyncGenerator

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


def create_async_engine_factory(
    database_url: str,
    *,
    pool_size: int = DEFAULT_POOL_SIZE,
    max_overflow: int = DEFAULT_MAX_OVERFLOW,
    pool_recycle: int = DEFAULT_POOL_RECYCLE,
    statement_timeout_ms: int = DEFAULT_STATEMENT_TIMEOUT_MS,
    echo: bool = False,
) -> AsyncEngine:
    """Create an async SQLAlchemy engine with connection pool hardening.

    Configures the engine with production-grade pool settings. For
    PostgreSQL, sets a per-connection ``statement_timeout`` via
    ``connect_args``. For SQLite (used in tests), pool size parameters
    are omitted since SQLite uses ``StaticPool``.

    Parameters
    ----------
    database_url : str
        Database connection string. Supported formats:

        - PostgreSQL: ``postgresql+psycopg://user:pass@host/db``
        - SQLite (tests): ``sqlite+aiosqlite:///``
    pool_size : int, optional
        Maximum number of permanent connections in the pool.
        Default is 5.
    max_overflow : int, optional
        Maximum extra connections allowed beyond ``pool_size`` during
        traffic spikes. Default is 10.
    pool_recycle : int, optional
        Seconds before a connection is recycled (returned to pool
        and replaced). Default is 3600 (1 hour).
    statement_timeout_ms : int, optional
        Per-query timeout in milliseconds (PostgreSQL only). Prevents
        long-running queries from exhausting the pool. Default is 30000.
    echo : bool, optional
        If ``True``, log all SQL statements via the ``sqlalchemy.engine``
        logger. Default is ``False``.

    Returns
    -------
    AsyncEngine
        Configured SQLAlchemy async engine with pool hardening.
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

    Sessions created by this factory have ``expire_on_commit=False``
    to allow accessing ORM attributes after commit without triggering
    lazy loads (important for async usage where implicit I/O is banned).

    Parameters
    ----------
    engine : AsyncEngine
        SQLAlchemy async engine to bind sessions to.

    Returns
    -------
    async_sessionmaker[AsyncSession]
        Configured session factory that yields ``AsyncSession`` instances.
    """
    return async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


async def get_async_session(
    factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession]:
    """Yield an async session and ensure automatic cleanup.

    Designed for use as a FastAPI dependency. The session is
    automatically rolled back on exception and closed after use.

    Usage as a FastAPI dependency::

        async for session in get_async_session(factory):
            await session.execute(...)

    Parameters
    ----------
    factory : async_sessionmaker[AsyncSession]
        Session factory to create sessions from.

    Yields
    ------
    AsyncSession
        Active database session. Rolled back on exception, closed
        after the generator exits.
    """
    async with factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
