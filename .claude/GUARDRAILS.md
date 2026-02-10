# Guardrails - Safety Rules

## Code Modification Guardrails

### AIDEV-IMMUTABLE Sections
Lines or blocks marked with `# AIDEV-IMMUTABLE` MUST NOT be modified by AI.

```python
# AIDEV-IMMUTABLE - Do not modify this function
def critical_function():
    pass
```

### Protected Files
These files require human approval before modification:
- `pyproject.toml` (dependency changes)
- Database migrations
- API contracts/schemas
- Security-related code

## Execution Guardrails

### Allowed Commands
```bash
uv sync
uv run pytest
uv run ruff
uv run mypy
git status
git diff
make test
make lint
```

### Denied Commands
```bash
rm -rf /
git push --force
pip install
conda
rm -rf .git
```

## Data Guardrails

### Never Commit
- `.env` files
- API keys or secrets
- Credentials
- Private keys
- Database passwords

### Always Validate
- User input at boundaries
- External API responses
- File paths (no traversal)
