# Contributing to Music Attribution Scaffold

Thank you for your interest in contributing! This project is the companion code to an academic preprint ([SSRN No. 6109087](https://doi.org/10.2139/ssrn.6109087)), so contributions that improve reproducibility, documentation, and code quality are especially welcome.

## Getting Started

### Prerequisites

- **Docker** (for PostgreSQL + pgvector)
- **Python 3.13** with [uv](https://docs.astral.sh/uv/) package manager
- **Node.js 22+** (for the frontend)

### Setup

```bash
git clone https://github.com/petteriTeikari/music-attribution-scaffold.git
cd music-attribution-scaffold
make setup
```

This runs `scripts/setup.sh` which installs all dependencies, starts PostgreSQL, runs migrations, and seeds sample data.

## Development Workflow

### Package Manager

**uv only** — pip and conda are not supported. All Python dependencies are managed through `pyproject.toml` and `uv.lock`.

```bash
# Add a dependency
uv add <package>

# Sync environment
uv sync
```

### Code Style

This project uses **ruff** for linting and formatting, and **mypy** for type checking:

```bash
# Run all linters
make lint-local

# Format code
make format

# Type check
make typecheck
```

### Pre-commit Hooks

All commits must pass pre-commit hooks. Install them once:

```bash
pre-commit install
```

The hooks run automatically on `git commit`. To run manually:

```bash
pre-commit run --all-files
```

### Testing

```bash
# Backend tests (fast, local)
make test-local

# Backend tests (Docker, CI-parity)
make test

# Frontend tests
make test-frontend

# E2E tests (Playwright)
make test-e2e

# All tests
make test-all
```

All tests must pass before submitting a pull request.

## Pull Request Process

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feat/your-feature
   ```

2. **Write tests first** (TDD). Tests define the expected behavior.

3. **Implement the feature** — keep changes focused and minimal.

4. **Run the full verification suite**:
   ```bash
   pre-commit run --all-files
   make test-local
   make test-frontend
   ```

5. **Submit a PR** with a clear description of what and why.

### Branch Naming

| Prefix | Use |
|--------|-----|
| `feat/` | New features |
| `fix/` | Bug fixes |
| `chore/` | Maintenance, CI, tooling |
| `docs/` | Documentation only |
| `refactor/` | Code restructuring (no behavior change) |

## Code Conventions

- **Python**: Follow PEP 8 (enforced by ruff), use type hints, write docstrings
- **Imports**: Use `from __future__ import annotations` at the top of every Python file
- **Paths**: Use `pathlib.Path()`, never string concatenation
- **Encoding**: Always specify `encoding='utf-8'` for file operations
- **Timezone**: Always use `datetime.now(timezone.utc)`

## Reporting Issues

Please use the [issue templates](https://github.com/petteriTeikari/music-attribution-scaffold/issues/new/choose) when reporting bugs, requesting features, or asking research questions.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
