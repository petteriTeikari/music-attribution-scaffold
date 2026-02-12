"""Tests for FastAPI app factory config wiring."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest


class TestCreateAppUsesSettings:
    """Verify create_app reads config from Settings, not raw os.environ."""

    def test_cors_from_settings(self) -> None:
        """CORS origins are read from Settings.cors_origins, not os.environ directly."""
        env = {
            "DATABASE_URL": "sqlite+aiosqlite://",
            "CORS_ORIGINS": "https://custom.example.com,https://other.example.com",
        }
        with patch.dict(os.environ, env, clear=False):
            from music_attribution.api.app import create_app

            app = create_app()

        # Check that CORS middleware was configured with the custom origins
        cors_middleware = None
        for middleware in app.user_middleware:
            if middleware.cls.__name__ == "CORSMiddleware":
                cors_middleware = middleware
                break

        assert cors_middleware is not None
        origins = cors_middleware.kwargs["allow_origins"]
        assert "https://custom.example.com" in origins
        assert "https://other.example.com" in origins

    def test_missing_database_url_raises(self) -> None:
        """Settings validation raises when DATABASE_URL is missing."""
        from pydantic import ValidationError

        env_without_db = {k: v for k, v in os.environ.items() if k != "DATABASE_URL"}
        with patch.dict(os.environ, env_without_db, clear=True):
            from music_attribution.api.app import create_app

            with pytest.raises(ValidationError):
                create_app()

    def test_no_os_environ_in_create_app(self) -> None:
        """create_app body should not call os.environ directly for CORS."""
        import ast
        from pathlib import Path

        app_path = Path("src/music_attribution/api/app.py")
        source = app_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        # Find the create_app function
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "create_app":
                # Check that no os.environ.get calls exist inside create_app
                for child in ast.walk(node):
                    if (
                        isinstance(child, ast.Attribute)
                        and isinstance(child.value, ast.Attribute)
                        and isinstance(child.value.value, ast.Name)
                        and child.value.value.id == "os"
                        and child.value.attr == "environ"
                    ):
                        pytest.fail("create_app still uses os.environ directly")
