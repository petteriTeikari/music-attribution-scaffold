# Environment Specification

This document specifies the exact environment for reproducible builds.

## Quick Start

```bash
# Option 1: Local development (may differ from CI)
make install-dev
make test

# Option 2: Docker-based testing (RECOMMENDED - mirrors CI exactly)
make ci-docker
```

## The Reproducibility Stack

```
┌────────────────────────────────────────────────────────────┐
│  Your Python Code                                          │  ← VISIBLE
├────────────────────────────────────────────────────────────┤
│  Python Packages (uv.lock)                                 │  ← LOCKED
│  - loguru, pytest, ruff, mypy, etc.                        │
├────────────────────────────────────────────────────────────┤
│  System Libraries                                          │  ← DOCUMENTED
│  - git, curl (for CI/testing)                              │
├────────────────────────────────────────────────────────────┤
│  Python Runtime                                            │  ← PINNED
│  - Python 3.11 or 3.13                                     │
├────────────────────────────────────────────────────────────┤
│  OS + Kernel                                               │  ← SPECIFIED
│  - Ubuntu (via GitHub Actions / Docker)                    │
└────────────────────────────────────────────────────────────┘
```

## Verified Configurations

### GitHub Actions CI

| Component | Version |
|-----------|---------|
| OS | Ubuntu Latest (ubuntu-latest) |
| Python | 3.11, 3.13 (matrix) |
| Package Manager | uv (astral-sh/setup-uv@v4) |
| Lockfile | `uv.lock` (frozen) |

### Docker-based Local Testing

| Component | Version |
|-----------|---------|
| Base Image | `python:3.13-slim` / `python:3.11-slim` |
| Package Manager | uv (ghcr.io/astral-sh/uv:latest) |
| Lockfile | `uv.lock` (frozen) |
| System Packages | git, curl |

## Dependency Management

### Lockfile (`uv.lock`)

The `uv.lock` file is the source of truth for Python dependencies:

- **MUST be tracked in git** (not gitignored)
- Contains exact versions of ALL packages (including transitive)
- Contains SHA-256 hashes for verification

### Dependency Groups

| Group | Purpose | Contents |
|-------|---------|----------|
| (default) | Production | loguru |
| `dev` | Development | pre-commit, ruff, mypy |
| `test` | Testing | pytest, pytest-cov, pytest-timeout, pytest-asyncio |

### Installation Commands

```bash
# Install production only
uv sync

# Install with dev tools
uv sync --group dev

# Install with test tools
uv sync --group test

# Install everything (recommended for development)
uv sync --group dev --group test

# Install from frozen lockfile (CI/Docker - deterministic)
uv sync --frozen --group dev --group test
```

## CI/Local Parity

### The Problem

"Works on my machine" failures occur when local and CI environments differ:
- Different Python versions
- Different system libraries
- Different package versions (if lockfile not used)

### The Solution

1. **Frozen lockfile**: Both CI and Docker use `--frozen`
2. **Matrix testing**: CI tests both Python 3.11 and 3.13
3. **Docker mirror**: Local Docker exactly replicates CI environment
4. **Parallel validation**: CI-Docker workflow validates parity

### Commands Comparison

| Check | Local (fast) | Docker (CI-equivalent) |
|-------|--------------|------------------------|
| All tests | `make test` | `make test-docker` |
| Linting | `make lint` | `make lint-docker` |
| Full CI | `make ci-local` | `make ci-docker` |
| Python 3.11 | N/A | `make test-docker-py311` |

## Adding Dependencies

```bash
# Add production dependency
uv add package-name

# Add development dependency
uv add --group dev package-name

# Add test dependency
uv add --group test package-name

# After adding, uv.lock is auto-updated
# Commit both pyproject.toml AND uv.lock
```

## Troubleshooting

### "pytest not found" in CI

**Cause**: CI running `uv sync` without `--group test`

**Fix**: Ensure CI uses `uv sync --frozen --group dev --group test`

### "Different results locally vs CI"

**Solution**: Use `make ci-docker` to run tests in CI-equivalent environment

### "Docker build fails"

**Check**: Is `uv.lock` committed? Run `git ls-files uv.lock`

## References

- [Why uv?](https://docs.astral.sh/uv/) - Package management done right
- [Docker is NOT Enough](https://arxiv.org/abs/2601.12811) - Why lockfiles matter
- [System Dependencies: The Hidden Iceberg](../docs/knowledge-base/) - Document all layers
