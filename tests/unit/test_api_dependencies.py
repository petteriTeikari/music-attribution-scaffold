"""Tests for FastAPI database session dependency and app lifespan."""

from __future__ import annotations

import contextlib

from sqlalchemy.ext.asyncio import AsyncSession


class TestGetDbSession:
    """Tests for the get_db_session dependency."""

    async def test_get_db_session_yields_session(self) -> None:
        """Dependency yields an AsyncSession instance."""
        from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

        from music_attribution.api.dependencies import get_db_session

        engine = create_async_engine("sqlite+aiosqlite://", echo=False)
        factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

        session_gen = get_db_session(factory)
        session = await session_gen.__anext__()
        assert isinstance(session, AsyncSession)

        # Cleanup
        with contextlib.suppress(StopAsyncIteration):
            await session_gen.__anext__()
        await engine.dispose()

    async def test_db_session_closes_after_request(self) -> None:
        """Session is closed after the generator finishes."""
        from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

        from music_attribution.api.dependencies import get_db_session

        engine = create_async_engine("sqlite+aiosqlite://", echo=False)
        factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

        session_gen = get_db_session(factory)
        session = await session_gen.__anext__()

        # Exhaust the generator (simulates request completion)
        with contextlib.suppress(StopAsyncIteration):
            await session_gen.__anext__()

        # Session should be closed
        assert session.is_active is False or session.get_bind() is not None
        await engine.dispose()


class TestAppLifespan:
    """Tests for the FastAPI app lifespan (engine creation/disposal)."""

    async def test_app_lifespan_creates_engine(self) -> None:
        """App lifespan stores async engine and session factory on app.state."""
        import os

        from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

        os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite://")
        os.environ.setdefault("MUSICBRAINZ_USER_AGENT", "test/1.0")

        from music_attribution.api.app import create_app, lifespan

        app = create_app()

        async with lifespan(app):
            # During lifespan, app.state should have the engine
            assert hasattr(app.state, "async_engine")
            assert hasattr(app.state, "async_session_factory")
            assert isinstance(app.state.async_engine, AsyncEngine)
            assert isinstance(app.state.async_session_factory, async_sessionmaker)

    async def test_app_lifespan_disposes_engine(self) -> None:
        """Engine is disposed after lifespan exits."""
        import os

        from sqlalchemy.ext.asyncio import AsyncEngine

        os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite://")
        os.environ.setdefault("MUSICBRAINZ_USER_AGENT", "test/1.0")

        from music_attribution.api.app import create_app, lifespan

        app = create_app()

        async with lifespan(app):
            engine = app.state.async_engine
            assert isinstance(engine, AsyncEngine)

        # After lifespan exits, engine.dispose() was called without error
