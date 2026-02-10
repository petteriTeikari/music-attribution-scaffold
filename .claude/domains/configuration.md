# Configuration Domain

## Package Management (uv)

### Adding Dependencies

```bash
# Production dependency
uv add package-name

# Development dependency
uv add --group dev package-name

# Test dependency
uv add --group test package-name

# With version constraint
uv add "package-name>=1.0.0,<2.0.0"
```

### Syncing Dependencies

```bash
# Install all dependencies
uv sync

# Production only
uv sync --no-dev
```

### NEVER DO

```bash
pip install  # BANNED
conda        # BANNED
requirements.txt  # BANNED
```

## pyproject.toml Structure

```toml
[project]
name = "music-attribution"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [...]

[dependency-groups]
dev = [...]
test = [...]

[tool.ruff]
# Linting and formatting config

[tool.pytest.ini_options]
# Test configuration

[tool.mypy]
# Type checking config

[tool.coverage.run]
# Coverage config
```

## Pre-commit Configuration

Located in `.pre-commit-config.yaml`:
- `pre-commit-hooks`: Basic checks
- `uv-pre-commit`: Lock file validation
- `ruff-pre-commit`: Linting and formatting
- `mypy`: Type checking

## Environment Variables

- Store in `.env` (never commit)
- Use `python-dotenv` to load
- Document required variables in README
