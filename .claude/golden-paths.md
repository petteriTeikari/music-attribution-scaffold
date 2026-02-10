# Golden Paths - Approved Implementation Patterns

This document defines the approved patterns for common development tasks.

## Adding a New Feature

1. Create feature branch: `git checkout -b feature/feature-name`
2. Write tests first (TDD): `tests/unit/test_feature.py`
3. Implement in `src/music_attribution/`
4. Run tests: `make test`
5. Run linting: `make lint`
6. Create PR

## Adding a New Dependency

```bash
# Add production dependency
uv add package-name

# Add development dependency
uv add --group dev package-name

# Add test dependency
uv add --group test package-name
```

NEVER use `pip install`.

## Running Tests

```bash
# All tests
make test

# Unit tests only
make test-unit

# Integration tests
make test-integration

# With coverage
make test-cov
```

## Code Analysis (APPROVED PATTERN)

```python
import ast
from pathlib import Path

def analyze_module(path: Path) -> list[str]:
    """Extract function names from a Python module."""
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return functions
```

NEVER use grep/sed/awk/regex to parse Python code.

## File Operations (APPROVED PATTERN)

```python
from pathlib import Path

def read_config(path: Path) -> str:
    """Read configuration file."""
    return path.read_text(encoding="utf-8")

def write_output(path: Path, content: str) -> None:
    """Write output file."""
    path.write_text(content, encoding="utf-8")
```

Always specify encoding. Always use Path.

## Datetime (APPROVED PATTERN)

```python
from datetime import datetime, timezone

def get_timestamp() -> datetime:
    """Get current UTC timestamp."""
    return datetime.now(timezone.utc)
```

NEVER use `datetime.now()` without timezone.
