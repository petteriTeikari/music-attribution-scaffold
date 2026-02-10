"""Tests for centralized configuration (Pydantic Settings)."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest
from pydantic import ValidationError

from music_attribution.config import Settings


class TestSettings:
    """Tests for Settings configuration."""

    def test_default_config_valid(self) -> None:
        """Test that Settings loads with minimal required env vars."""
        env = {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost:5432/musicattr",
            "MUSICBRAINZ_USER_AGENT": "TestApp/1.0 (test@example.com)",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings()
            assert settings.musicbrainz_user_agent == "TestApp/1.0 (test@example.com)"
            assert settings.attribution_seed == 42
            assert settings.environment == "development"

    def test_config_from_env_vars(self) -> None:
        """Test that all settings can be configured via environment variables."""
        env = {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@db:5432/prod",
            "VALKEY_URL": "redis://valkey:6379/1",
            "MUSICBRAINZ_USER_AGENT": "ProdApp/2.0 (admin@example.com)",
            "DISCOGS_TOKEN": "secret-token-123",
            "LLM_PROVIDER": "openai",
            "LLM_MODEL": "gpt-4o",
            "ATTRIBUTION_SEED": "123",
            "LOG_LEVEL": "DEBUG",
            "ENVIRONMENT": "production",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings()
            assert settings.valkey_url == "redis://valkey:6379/1"
            assert settings.llm_provider == "openai"
            assert settings.llm_model == "gpt-4o"
            assert settings.attribution_seed == 123
            assert settings.log_level == "DEBUG"
            assert settings.environment == "production"

    def test_config_database_url_construction(self) -> None:
        """Test that database URL is properly validated."""
        env = {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost:5432/musicattr",
            "MUSICBRAINZ_USER_AGENT": "TestApp/1.0",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings()
            assert "postgresql" in str(settings.database_url)

    def test_config_seed_deterministic(self) -> None:
        """Test that same seed produces same Settings."""
        env = {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost:5432/musicattr",
            "MUSICBRAINZ_USER_AGENT": "TestApp/1.0",
            "ATTRIBUTION_SEED": "42",
        }
        with patch.dict(os.environ, env, clear=False):
            s1 = Settings()
            s2 = Settings()
            assert s1.attribution_seed == s2.attribution_seed == 42

    def test_config_sensitive_fields_excluded_from_repr(self) -> None:
        """Test that tokens and secrets are hidden in repr/str output."""
        env = {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost:5432/musicattr",
            "MUSICBRAINZ_USER_AGENT": "TestApp/1.0",
            "DISCOGS_TOKEN": "super-secret-token",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings()
            repr_str = repr(settings)
            assert "super-secret-token" not in repr_str
