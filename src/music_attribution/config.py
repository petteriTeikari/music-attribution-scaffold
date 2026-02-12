"""Centralized configuration using Pydantic Settings.

All configuration is loaded from environment variables with sensible
defaults. Supports .env files for local development.
"""

from __future__ import annotations

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables.

    Required environment variables:
        DATABASE_URL: PostgreSQL connection string

    All other settings have sensible defaults for local development.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Database
    database_url: str = Field(description="PostgreSQL async connection string")
    valkey_url: str = Field(default="redis://localhost:6379", description="Valkey/Redis connection URL")

    # API
    api_host: str = Field(default="0.0.0.0", description="API server host")
    api_port: int = Field(default=8000, description="API server port")
    cors_origins: str = Field(default="http://localhost:3000", description="Comma-separated CORS origins")

    # External APIs
    musicbrainz_user_agent: str | None = Field(default=None, description="User-Agent for MusicBrainz API")
    discogs_token: SecretStr | None = Field(default=None, description="Discogs API token")

    # LLM / Agent
    llm_provider: str = Field(default="anthropic", description="LLM provider name")
    llm_model: str = Field(default="claude-haiku-4-5", description="LLM model identifier")
    attribution_agent_model: str = Field(
        default="anthropic:claude-haiku-4-5", description="PydanticAI model string for attribution agent"
    )

    # Reproducibility
    attribution_seed: int = Field(default=42, description="Random seed for reproducible experiments")

    # Runtime
    log_level: str = Field(default="INFO", description="Logging level")
    environment: str = Field(default="development", description="Runtime environment")
