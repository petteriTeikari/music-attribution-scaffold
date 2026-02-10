"""Pytest configuration and fixtures for Music Attribution Scaffold."""

from __future__ import annotations

import pytest


@pytest.fixture
def sample_data() -> dict[str, str]:
    """Provide sample data for tests.

    Returns:
        A dictionary with sample data.
    """
    return {"key": "value"}
