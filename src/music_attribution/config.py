"""Centralized application configuration using Pydantic Settings.

All configuration is loaded from environment variables with sensible
defaults for local development. A ``.env`` file in the project root
is automatically read if present.

The ``Settings`` class is the single source of truth for all runtime
configuration. It is instantiated lazily (e.g. in ``_get_agent_model``)
to avoid requiring environment variables at import time.

Environment Variables
---------------------
DATABASE_URL : str
    PostgreSQL async connection string
    (e.g. ``postgresql+psycopg://…@localhost/db``).  # pragma: allowlist secret
VALKEY_URL : str
    Valkey/Redis connection URL (default ``redis://localhost:6379``).
API_HOST : str
    API server bind address (default ``0.0.0.0``).
API_PORT : int
    API server port (default ``8000``).
CORS_ORIGINS : str
    Comma-separated CORS origins (default ``http://localhost:3000``).
ANTHROPIC_API_KEY : str
    Anthropic API key (set externally, not in Settings).
ATTRIBUTION_AGENT_MODEL : str
    PydanticAI model string (default ``anthropic:claude-haiku-4-5``).
LOG_LEVEL : str
    Python logging level (default ``INFO``).
ENVIRONMENT : str
    Runtime environment name (default ``development``).

See Also
--------
music_attribution.chat.agent._get_agent_model : Lazy Settings consumer.
music_attribution.db.engine : Uses ``database_url`` for engine creation.
"""

from __future__ import annotations

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables.

    Uses Pydantic Settings to load and validate configuration from
    environment variables and ``.env`` files. All settings except
    ``database_url`` have sensible defaults for local development.

    The ``model_config`` enables case-insensitive matching,
    UTF-8 ``.env`` file reading, and ignoring extra environment
    variables.

    Attributes
    ----------
    database_url : str
        PostgreSQL connection string with asyncpg driver
        (e.g. ``postgresql+psycopg://…@localhost/db``).
    valkey_url : str
        Valkey/Redis connection URL for caching and pub/sub.
    api_host : str
        Network interface to bind the API server to.
    api_port : int
        TCP port for the API server.
    cors_origins : str
        Comma-separated CORS origin allowlist.
    musicbrainz_user_agent : str | None
        User-Agent header for MusicBrainz API rate-limiting compliance.
    discogs_token : SecretStr | None
        Discogs API personal access token (stored as SecretStr to
        prevent accidental logging).
    llm_provider : str
        LLM provider name for routing (e.g. ``"anthropic"``).
    llm_model : str
        LLM model identifier (e.g. ``"claude-haiku-4-5"``).
    attribution_agent_model : str
        PydanticAI model string for the attribution agent, combining
        provider and model (e.g. ``"anthropic:claude-haiku-4-5"``).
    attribution_seed : int
        Random seed for reproducible entity resolution and experiments.
    log_level : str
        Python logging level string (``DEBUG``, ``INFO``, etc.).
    environment : str
        Runtime environment (``development``, ``staging``, ``production``).
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
