"""Fixtures for voice persona evaluation tests.

These tests require DeepEval and an LLM API key. They are marked with
``@pytest.mark.persona_eval`` and excluded from regular CI runs.
"""

from __future__ import annotations

import pytest

# Check if deepeval is available
try:
    import deepeval  # noqa: F401

    DEEPEVAL_AVAILABLE = True
except ImportError:
    DEEPEVAL_AVAILABLE = False


def pytest_configure(config: pytest.Config) -> None:
    """Register custom markers."""
    config.addinivalue_line(
        "markers",
        "persona_eval: marks tests as persona evaluation (requires LLM API)",
    )


@pytest.fixture
def skip_without_deepeval() -> None:
    """Skip test if deepeval is not installed."""
    if not DEEPEVAL_AVAILABLE:
        pytest.skip("deepeval not installed")
