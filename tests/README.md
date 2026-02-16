# Tests

Testing infrastructure for the Music Attribution Scaffold. The project follows a testing pyramid with fast unit tests at the base, Docker-backed integration tests in the middle, and frontend component + E2E tests alongside.

## Test Counts

| Layer | Count | Speed | Docker Required |
|---|---|---|---|
| Unit (backend) | 351 | Fast (< 30s) | No |
| Integration (backend) | 42 | Medium (< 2min) | Yes (testcontainers) |
| Frontend (Vitest) | 265 | Fast (< 20s) | No |
| E2E (Playwright) | varies | Slow | Yes (full stack) |

## How to Run

```bash
# Unit tests only (fast, no Docker)
.venv/bin/python -m pytest tests/unit/ -x -q

# All backend tests locally (unit + integration, needs Docker daemon)
make test-local

# Backend tests in Docker (CI-parity)
make test

# Full CI simulation (lint + typecheck + tests)
make test-all

# Frontend tests
make test-frontend

# Coverage report
make test-cov
```

**Important**: Always use `.venv/bin/python -m pytest` rather than bare `pytest` to avoid VIRTUAL_ENV mismatches.

## Directory Structure

```
tests/
├── conftest.py              # Root fixtures (DATABASE_URL default, sample_data)
├── unit/
│   ├── conftest.py          # Unit-specific fixtures
│   ├── test_schemas_*.py    # Boundary object validation
│   ├── test_etl_*.py        # ETL connector transforms
│   ├── test_resolution_*.py # Entity resolution strategies
│   ├── test_attribution_*.py # Aggregation + conformal scoring
│   ├── test_api_*.py        # FastAPI route tests
│   ├── test_chat_*.py       # Agent + AG-UI endpoint
│   ├── test_mcp_*.py        # MCP server tools
│   ├── test_search_*.py     # Hybrid search
│   ├── test_pipeline_*.py   # DAG runner
│   └── ...
├── integration/
│   ├── conftest.py          # PostgreSQL via testcontainers
│   ├── test_db_*.py         # Database round-trips
│   ├── test_seed_*.py       # Seed data loading
│   └── ...
├── e2e/                     # End-to-end tests
└── smoke/                   # Smoke tests
```

## Unit Tests

Unit tests are fast, deterministic, and mock all external dependencies:

- **No network calls**: ETL connectors are tested by feeding raw API response dicts to `transform_*` methods.
- **No database**: Use in-memory repositories (`AttributionRecordRepository`).
- **No Docker**: Can run anywhere with just Python.
- **Isolated**: Each test class is self-contained with its own fixtures.

Pattern:

```python
class TestFeatureName:
    """Tests for feature_name."""

    def test_expected_behavior(self) -> None:
        """Test description following Arrange-Act-Assert."""
        # Arrange
        record = build_test_record(confidence=0.8)

        # Act
        result = function_under_test(record)

        # Assert
        assert result.confidence >= 0.75
```

## Integration Tests

Integration tests verify real database behavior using testcontainers:

- **Real PostgreSQL**: Each test session spins up a PostgreSQL container via testcontainers-python.
- **pgvector extension**: `CREATE EXTENSION vector` runs before table creation.
- **Alembic migrations**: Tables are created via migration scripts, not `create_all()`.
- **Docker daemon required**: Tests skip gracefully if Docker is not available.

The integration `conftest.py` provides a `db_session` fixture that manages container lifecycle.

## Frontend Tests

Frontend tests live in `frontend/src/__tests__/` and use:

- **Vitest** as the test runner (Jest-compatible API).
- **React Testing Library** for component rendering and interaction.
- **vitest-axe** for component-level WCAG 2.1 AA accessibility checks.
- **jsdom** as the browser environment.

Run with `make test-frontend` or `cd frontend && npm run test`.

## Naming Conventions

- Test files: `test_<module_name>.py`
- Test classes: `Test<FeatureName>`
- Test methods: `test_<expected_behavior>` (e.g., `test_rejects_empty_canonical_name`)
- Fixtures: Descriptive nouns (e.g., `sample_normalized_record`, `db_session`)

## conftest Structure

| File | Scope | Provides |
|---|---|---|
| `tests/conftest.py` | Session | `DATABASE_URL` env default, `sample_data` fixture |
| `tests/unit/conftest.py` | Unit tests | Test builder functions, mock factories |
| `tests/integration/conftest.py` | Integration tests | Testcontainers PostgreSQL session, migration runner |

## CI vs Local Discrepancies

The Docker test image (`docker/Dockerfile.test`) only copies `src/`, `tests/`, and `alembic/`. Tests that read files outside those directories (e.g., `Makefile`, `scripts/`) must use `skipif(RUNNING_IN_DOCKER)` to avoid failures in CI.

## Visual Documentation

![Testing pyramid showing unit tests at the base, integration in the middle, and E2E at the top](docs/figures/repo-figures/assets/fig-repo-10-testing-pyramid.jpg)
*Testing pyramid -- 351 unit, 42 integration (testcontainers), 265 frontend (Vitest), and Playwright E2E.*

![Agent testing strategy showing mock agent injection, endpoint tests, and state sync verification](docs/figures/repo-figures/assets/fig-agent-10-testing-strategy.jpg)
*Agent testing strategy -- mock agent pattern with AG-UI endpoint tests and state synchronization checks.*
