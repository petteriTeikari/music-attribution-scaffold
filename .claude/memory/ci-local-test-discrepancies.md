# CI vs Local Test Discrepancies — Metalearning

## Root Cause Pattern

Tests pass locally but fail in GitHub Actions Docker CI when they depend
on **project layout files** that are not copied into the Docker test image.

### Dockerfile.test copies ONLY:
```
pyproject.toml, uv.lock, README.md  (deps layer)
src/                                 (source)
tests/                               (tests)
alembic/, alembic.ini                (migrations)
```

### NOT copied (intentionally, to keep image small):
- `scripts/` — setup scripts, security checks
- `Makefile` — build targets
- `frontend/` — Node.js frontend
- `docker/` — Docker configs
- `docs/` — documentation
- `.github/` — CI workflows
- `.claude/` — AI assistant config
- `CLAUDE.md` — AI rules

## Detection Signal

- **Docker env var**: `RUNNING_IN_DOCKER=true` (set in Dockerfile.test)
- **CI env var**: `CI=true` (set in both Dockerfile.test and GitHub Actions)
- **Path resolution**: `Path(__file__).resolve().parents[N]` resolves to `/app/` in Docker

## Fix Pattern

For tests that validate project structure files not in Docker:

```python
import os
import pytest

_IN_DOCKER = os.environ.get("RUNNING_IN_DOCKER") == "true"

@pytest.mark.skipif(_IN_DOCKER, reason="file not copied into Docker test image")
class TestProjectLayout:
    ...
```

## Incidents

| Date | Test File | Root Cause | Fix |
|------|-----------|------------|-----|
| 2026-02-11 | `test_setup_script.py` (4 tests) | `scripts/setup.sh` and `Makefile` not in Docker image | Added `@pytest.mark.skipif(_IN_DOCKER)` |

## Prevention Checklist

When writing tests that read project files outside `src/` or `tests/`:

1. Check if the file is in `Dockerfile.test` COPY list
2. If not, add `skipif(RUNNING_IN_DOCKER)` guard
3. Or: add the file to Dockerfile.test COPY (only if needed for actual logic tests)

## When to COPY vs Skip

- **COPY into Docker**: Files needed for runtime logic (migrations, config)
- **Skip in Docker**: Files testing project structure (setup scripts, Makefile targets, docs presence)

## Alternative: Copy Everything

Could change Dockerfile.test to `COPY . .` but this:
- Bloats the test image with docs, frontend, .git
- Breaks Docker layer caching
- Doesn't match CI philosophy of testing only Python code

The selective-skip approach is better.
