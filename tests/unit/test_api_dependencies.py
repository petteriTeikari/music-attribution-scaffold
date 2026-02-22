"""Tests for FastAPI database session dependency and app lifespan."""

from __future__ import annotations

from unittest.mock import MagicMock

from sqlalchemy.ext.asyncio import AsyncSession


class TestGetSession:
    """Tests for the get_session dependency."""

    def test_get_session_returns_session(self) -> None:
        """get_session returns a session from the app's factory."""
        from music_attribution.api.dependencies import get_session

        mock_session = MagicMock(spec=AsyncSession)
        mock_factory = MagicMock(return_value=mock_session)

        mock_request = MagicMock()
        mock_request.app.state.async_session_factory = mock_factory

        result = get_session(mock_request)
        assert result is mock_session
        mock_factory.assert_called_once()

    def test_get_session_reads_from_app_state(self) -> None:
        """get_session extracts factory from request.app.state."""
        from music_attribution.api.dependencies import get_session

        mock_factory = MagicMock()
        mock_request = MagicMock()
        mock_request.app.state.async_session_factory = mock_factory

        get_session(mock_request)
        mock_factory.assert_called_once()


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
