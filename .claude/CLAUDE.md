# Music Attribution Scaffold - Claude Behavior Contract

This file defines the complete behavior contract for AI assistants working on this project.

## Quick Reference

| Category | Rule |
|----------|------|
| **Package Management** | uv ONLY (pip/conda BANNED) |
| **Code Analysis** | AST ONLY (grep/sed/awk BANNED for parsing) |
| **File Operations** | Always use `encoding='utf-8'` and `Path()` |
| **Datetime** | Always use `datetime.now(timezone.utc)` |
| **Pre-commit** | MUST pass before any commit |
| **Markers** | NEVER modify `# AIDEV-IMMUTABLE` sections |
| **Quality** | NEVER say "should work" - verify locally first |

## Forbidden Actions

### Package Management
- NEVER use `pip install` - use `uv add` or `uv sync`
- NEVER use `conda` - TOTAL BAN
- NEVER create `requirements.txt` - use `pyproject.toml`

### Code Analysis
- NEVER use `grep`, `sed`, or `awk` to parse Python code
- NEVER use regex to extract imports, classes, or functions
- ALWAYS use `ast.parse()` and `ast.walk()` for code analysis

### File Operations
- ALWAYS specify `encoding='utf-8'` when opening files
- ALWAYS use `pathlib.Path()` for file paths
- NEVER hardcode paths as strings
- NEVER use os.path string concatenation

### Datetime
- ALWAYS use `datetime.now(timezone.utc)` for current time
- NEVER use `datetime.now()` without timezone

### Protected Content
- NEVER modify code marked with `# AIDEV-IMMUTABLE`
- NEVER modify API contracts without explicit approval
- NEVER alter database migrations after they've been applied

### Quality and Verification
- NEVER use speculative language like "should work", "should pass", "should fix"
- ALWAYS verify changes locally before claiming they work
- ALWAYS run `make ci-docker` before pushing CI-related changes
- NEVER push untested changes to CI - test locally first
- If local verification is not possible, explicitly state what was NOT verified

## Required Patterns

### Python File Template
```python
"""Module docstring."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

logger = logging.getLogger(__name__)


def function_name(arg: str) -> str:
    """Function docstring.

    Args:
        arg: Description.

    Returns:
        Description.
    """
    return arg
```

### Test Template
```python
"""Tests for module_name."""

from __future__ import annotations

import pytest


class TestFeatureName:
    """Tests for feature_name."""

    def test_expected_behavior(self) -> None:
        """Test description."""
        # Arrange
        # Act
        # Assert
        assert True
```

## Context Loading

| Trigger | Files to Load |
|---------|---------------|
| Any file | `.claude/CLAUDE.md`, `CLAUDE.md` |
| `tests/**` | `.claude/domains/testing.md` |
| `pyproject.toml` | `.claude/domains/configuration.md` |
| `frontend/**` | `.claude/rules/10-frontend-design-system.md`, `.claude/rules/11-ux-first-philosophy.md` |
| `frontend/src/components/**` | `.claude/rules/10-frontend-design-system.md` |
| `frontend/src/app/**` | `.claude/rules/11-ux-first-philosophy.md` |

## Frontend Quick Commands

```bash
# Development server
make dev-frontend

# Run frontend tests
make test-frontend

# Lint frontend
make lint-frontend

# Production build
make build-frontend
```

## Frontend Rules

- **Zero hardcoded hex** in `.tsx` files — use CSS custom property tokens only
- **CSS custom properties** for all theme values in `globals.css`
- **Vitest + React Testing Library** for component tests
- **`vitest-axe`** for component-level WCAG checks
- **Jotai** for client state (theme, role mode)
- **App Router** (Next.js 15) — all pages in `frontend/src/app/`

## Mode System

Current mode: maintenance

| Mode | Risk Tolerance | Max Files | Max Lines |
|------|----------------|-----------|-----------|
| creation | high | 20 | 1000 |
| maintenance | low | 3 | 200 |
| debug | medium | 10 | 500 |
