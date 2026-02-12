"""Tests for centralized configuration (Pydantic Settings)."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

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

    def test_settings_defaults(self) -> None:
        """Verify all default values match spec."""
        env = {
            "DATABASE_URL": "postgresql+psycopg://u:p@localhost/db",  # pragma: allowlist secret
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings()
            assert settings.cors_origins == "http://localhost:3000"
            assert settings.attribution_agent_model == "anthropic:claude-haiku-4-5"
            assert settings.api_host == "0.0.0.0"
            assert settings.api_port == 8000
            assert settings.valkey_url == "redis://localhost:6379"
            assert settings.llm_provider == "anthropic"
            assert settings.llm_model == "claude-haiku-4-5"
            assert settings.attribution_seed == 42
            assert settings.log_level == "INFO"
            assert settings.environment == "development"

    def test_cors_origins_field(self) -> None:
        """Verify cors_origins field exists and accepts custom value."""
        env = {
            "DATABASE_URL": "postgresql+psycopg://u:p@localhost/db",  # pragma: allowlist secret
            "CORS_ORIGINS": "http://localhost:3000,https://app.example.com",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings()
            assert settings.cors_origins == "http://localhost:3000,https://app.example.com"

    def test_agent_model_field(self) -> None:
        """Verify attribution_agent_model field exists and accepts custom value."""
        env = {
            "DATABASE_URL": "postgresql+psycopg://u:p@localhost/db",  # pragma: allowlist secret
            "ATTRIBUTION_AGENT_MODEL": "openai:gpt-4o",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings()
            assert settings.attribution_agent_model == "openai:gpt-4o"

    def test_settings_ignores_extra(self) -> None:
        """Extra env vars don't cause errors."""
        env = {
            "DATABASE_URL": "postgresql+psycopg://u:p@localhost/db",  # pragma: allowlist secret
            "TOTALLY_UNKNOWN_VAR": "some-value",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings()
            assert settings.database_url is not None

    def test_musicbrainz_user_agent_optional(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """musicbrainz_user_agent has a None default (not yet used in codebase)."""
        monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://u:p@localhost/db")
        monkeypatch.delenv("MUSICBRAINZ_USER_AGENT", raising=False)
        settings = Settings()
        assert settings.musicbrainz_user_agent is None
