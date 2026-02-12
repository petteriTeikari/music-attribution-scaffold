"""Pytest configuration and fixtures for Music Attribution Scaffold."""

from __future__ import annotations

import os

import pytest

# Ensure DATABASE_URL is set for any test that imports create_app().
# Unit tests use SQLite (fast, no Docker); integration tests override
# with real PostgreSQL via testcontainers.
os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite://")


@pytest.fixture
def sample_data() -> dict[str, str]:
    """Provide sample data for tests.

    Returns:
        A dictionary with sample data.
    """
    return {"key": "value"}
