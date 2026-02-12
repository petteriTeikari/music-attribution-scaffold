"""Tests for database engine factory (async) with pool hardening."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker


class TestAsyncEngineFactory:
    """Tests for the async engine factory."""

    @pytest.mark.asyncio
    async def test_create_async_engine_returns_async_engine(self) -> None:
        """create_async_engine_factory returns an AsyncEngine instance."""
        from music_attribution.db.engine import create_async_engine_factory

        engine = create_async_engine_factory("sqlite+aiosqlite:///")
        assert isinstance(engine, AsyncEngine)
        await engine.dispose()

    def test_pool_pre_ping_enabled(self) -> None:
        """Pool pre-ping is enabled to detect stale connections.

        Verify by inspecting the creation keyword arguments since
        StaticPool (used by SQLite) doesn't expose pre_ping directly.
        """
        from music_attribution.db.engine import create_async_engine_factory

        engine = create_async_engine_factory("sqlite+aiosqlite:///")
        # The sync engine underneath carries the pool config
        sync_engine = engine.sync_engine
        # pool_pre_ping is stored on the engine itself
        assert sync_engine.pool._pre_ping is True
        engine.sync_engine.dispose()

    def test_pool_size_accepts_parameters(self) -> None:
        """Pool size and max overflow parameters are accepted."""
        from music_attribution.db.engine import create_async_engine_factory

        # Should not raise — verifies the factory signature accepts these
        engine = create_async_engine_factory(
            "sqlite+aiosqlite:///",
            pool_size=5,
            max_overflow=10,
        )
        assert isinstance(engine, AsyncEngine)
        engine.sync_engine.dispose()

    def test_pool_recycle_configured(self) -> None:
        """Pool recycle is set to provided value."""
        from music_attribution.db.engine import create_async_engine_factory

        engine = create_async_engine_factory(
            "sqlite+aiosqlite:///",
            pool_recycle=7200,
        )
        assert engine.sync_engine.pool._recycle == 7200
        engine.sync_engine.dispose()

    def test_default_pool_recycle_is_3600(self) -> None:
        """Default pool recycle is 3600 without explicit parameter."""
        from music_attribution.db.engine import create_async_engine_factory

        engine = create_async_engine_factory("sqlite+aiosqlite:///")
        assert engine.sync_engine.pool._recycle == 3600
        engine.sync_engine.dispose()

    def test_default_constants(self) -> None:
        """Verify module-level constants for pool hardening."""
        from music_attribution.db.engine import (
            DEFAULT_MAX_OVERFLOW,
            DEFAULT_POOL_RECYCLE,
            DEFAULT_POOL_SIZE,
            DEFAULT_STATEMENT_TIMEOUT_MS,
        )

        assert DEFAULT_POOL_SIZE == 5
        assert DEFAULT_MAX_OVERFLOW == 10
        assert DEFAULT_POOL_RECYCLE == 3600
        assert DEFAULT_STATEMENT_TIMEOUT_MS == 30_000


class TestAsyncSessionFactory:
    """Tests for async session factory and context manager."""

    def test_async_session_factory_creates_sessionmaker(self) -> None:
        """async_session_factory returns an async_sessionmaker."""
        from music_attribution.db.engine import (
            async_session_factory,
            create_async_engine_factory,
        )

        engine = create_async_engine_factory("sqlite+aiosqlite:///")
        factory = async_session_factory(engine)
        assert isinstance(factory, async_sessionmaker)
        engine.sync_engine.dispose()

    @pytest.mark.asyncio
    async def test_async_session_context_manager(self) -> None:
        """get_async_session yields an AsyncSession and cleans up."""
        from music_attribution.db.engine import (
            async_session_factory,
            create_async_engine_factory,
            get_async_session,
        )

        engine = create_async_engine_factory("sqlite+aiosqlite:///")
        factory = async_session_factory(engine)

        async for session in get_async_session(factory):
            assert isinstance(session, AsyncSession)

        await engine.dispose()
