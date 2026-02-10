# Source of Truth Rules

## Configuration Source of Truth

| Configuration | Source of Truth |
|--------------|-----------------|
| Dependencies | `pyproject.toml` |
| Python version | `pyproject.toml` |
| Linting rules | `pyproject.toml` [tool.ruff] |
| Test config | `pyproject.toml` [tool.pytest] |
| Type checking | `pyproject.toml` [tool.mypy] |
| Pre-commit hooks | `.pre-commit-config.yaml` |
| Claude rules | `.claude/CLAUDE.md` |

## Code Source of Truth

| Information | Source |
|-------------|--------|
| Project version | `src/music_attribution/__init__.py` |
| API contracts | Type definitions in source |
| Database schema | Migration files |

## Documentation Source of Truth

| Documentation | Source |
|--------------|--------|
| Project overview | `README.md` |
| AI rules | `CLAUDE.md`, `.claude/CLAUDE.md` |
| API docs | Docstrings in source code |

## Rules

1. Never duplicate information that exists in source of truth
2. Reference the source of truth, don't copy it
3. When in doubt, check the source of truth
4. Keep sources of truth in sync
