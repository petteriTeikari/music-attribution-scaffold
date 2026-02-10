"""Async SQLAlchemy engine factory."""

from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def create_sync_engine(database_url: str) -> Engine:
    """Create a synchronous SQLAlchemy engine.

    Used by Alembic migrations (which require sync engines).

    Args:
        database_url: PostgreSQL connection string.

    Returns:
        SQLAlchemy Engine instance.
    """
    return create_engine(database_url, echo=False)
