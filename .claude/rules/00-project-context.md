# Project Context Rules

## Project Information

- **Name**: Music Attribution Scaffold
- **Type**: library
- **Python Version**: 3.13
- **Package Manager**: uv (ONLY)
- **Linter**: ruff
- **Formatter**: ruff
- **Type Checker**: mypy
- **Test Framework**: pytest

## Directory Structure

```
music-attribution-scaffold/
├── src/music_attribution/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/
└── .claude/
```

## Coding Standards

- Follow PEP 8 (enforced by ruff)
- Use type hints for all public functions
- Write docstrings for all modules, classes, and public functions
- Use `from __future__ import annotations` at the top of every Python file
- Maximum line length: 120 characters
