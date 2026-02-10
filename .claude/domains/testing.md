# Testing Domain

## Test Framework

- **Framework**: pytest
- **Config**: `pyproject.toml` [tool.pytest.ini_options]
- **Fixtures**: `tests/conftest.py`

## Test Categories

| Marker | Directory | Purpose |
|--------|-----------|---------|
| `@pytest.mark.unit` | `tests/unit/` | Pure function tests, no external deps |
| `@pytest.mark.integration` | `tests/integration/` | Tests with external services |
| `@pytest.mark.e2e` | `tests/e2e/` | End-to-end tests |
| `@pytest.mark.slow` | Any | Tests taking > 30 seconds |

## Test Structure

```python
"""Tests for module_name."""

from __future__ import annotations

import pytest


class TestFeatureName:
    """Tests for feature_name."""

    def test_expected_behavior_when_condition(self) -> None:
        """Should return expected result when condition is met."""
        # Arrange
        input_data = "test"

        # Act
        result = function_under_test(input_data)

        # Assert
        assert result == "expected"

    def test_raises_error_when_invalid_input(self) -> None:
        """Should raise ValueError when input is invalid."""
        with pytest.raises(ValueError, match="specific error"):
            function_under_test(None)
```

## Running Tests

```bash
# All tests
make test

# Unit tests only
uv run pytest tests/unit/ -m unit

# With coverage
make test-cov

# Single test file
uv run pytest tests/unit/test_module.py -v

# Single test
uv run pytest tests/unit/test_module.py::TestClass::test_method -v
```

## Coverage Requirements

- Minimum coverage: 80%
- Critical paths: 100%
- New code must have tests
