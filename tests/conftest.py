"""Pytest configuration and fixtures for Music Attribution Scaffold."""

from __future__ import annotations

import pytest


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Skip integration and e2e tests unless explicitly requested with -m."""
    run_markers = config.getoption("-m", default="")
    if "integration" in run_markers or "e2e" in run_markers:
        return

    skip_integration = pytest.mark.skip(reason="integration tests skipped by default (use -m integration)")
    skip_e2e = pytest.mark.skip(reason="e2e tests skipped by default (use -m e2e)")
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_integration)
        if "e2e" in item.keywords:
            item.add_marker(skip_e2e)


@pytest.fixture
def sample_data() -> dict[str, str]:
    """Provide sample data for tests.

    Returns:
        A dictionary with sample data.
    """
    return {"key": "value"}
