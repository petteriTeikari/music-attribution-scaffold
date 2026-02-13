"""Tests for production Dockerfile (P2-6).

Validates that docker/Dockerfile.prod exists and follows production
best practices: multi-stage build, non-root user, HEALTHCHECK, and
Python version matching pyproject.toml.
"""

from __future__ import annotations

from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RUNNING_IN_DOCKER = not (PROJECT_ROOT / "pyproject.toml").exists()
pytestmark = pytest.mark.skipif(RUNNING_IN_DOCKER, reason="Project root files not available in Docker")


class TestProductionDockerfile:
    """Tests for docker/Dockerfile.prod."""

    @pytest.fixture(scope="class")
    def dockerfile_content(self) -> str:
        """Load Dockerfile.prod content."""
        path = PROJECT_ROOT / "docker" / "Dockerfile.prod"
        assert path.exists(), "docker/Dockerfile.prod must exist"
        return path.read_text(encoding="utf-8")

    def test_dockerfile_prod_exists(self) -> None:
        """Verify docker/Dockerfile.prod exists."""
        path = PROJECT_ROOT / "docker" / "Dockerfile.prod"
        assert path.exists(), "Missing docker/Dockerfile.prod"

    def test_dockerfile_has_multi_stage_build(self, dockerfile_content: str) -> None:
        """Production Dockerfile uses multi-stage build (builder + runtime)."""
        from_count = sum(1 for line in dockerfile_content.splitlines() if line.strip().startswith("FROM "))
        assert from_count >= 2, f"Expected >= 2 FROM stages, found {from_count}"

    def test_dockerfile_has_non_root_user(self, dockerfile_content: str) -> None:
        """Production Dockerfile creates and switches to a non-root user."""
        lines_lower = dockerfile_content.lower()
        assert "user " in lines_lower or "useradd" in lines_lower or "adduser" in lines_lower, (
            "Dockerfile.prod must create a non-root user"
        )

    def test_dockerfile_has_healthcheck(self, dockerfile_content: str) -> None:
        """Production Dockerfile includes a HEALTHCHECK instruction."""
        assert "HEALTHCHECK" in dockerfile_content, "Dockerfile.prod must have a HEALTHCHECK instruction"

    def test_dockerfile_python_version_matches_pyproject(self, dockerfile_content: str) -> None:
        """Python version ARG matches pyproject.toml requires-python."""
        import tomllib

        pyproject_path = PROJECT_ROOT / "pyproject.toml"
        with pyproject_path.open("rb") as f:
            pyproject = tomllib.load(f)

        requires_python = pyproject.get("project", {}).get("requires-python", "")
        # Extract major.minor from requires-python (e.g., ">=3.13,<3.14" → "3.13")
        import re

        match = re.search(r"(\d+\.\d+)", requires_python)
        assert match, f"Cannot parse Python version from requires-python: {requires_python}"
        version = match.group(1)
        assert version in dockerfile_content, (
            f"Dockerfile.prod must reference Python {version} (from pyproject.toml requires-python)"
        )

    def test_dockerfile_has_ssrn_label(self, dockerfile_content: str) -> None:
        """Production Dockerfile includes SSRN DOI label for provenance."""
        assert "LABEL" in dockerfile_content, "Dockerfile.prod must have LABEL metadata"
        assert "6109087" in dockerfile_content, "Dockerfile.prod must reference SSRN paper ID 6109087"

    def test_dockerfile_uses_uv_no_dev(self, dockerfile_content: str) -> None:
        """Production Dockerfile installs without dev dependencies."""
        assert "--no-dev" in dockerfile_content, "Dockerfile.prod must use --no-dev for production deps"
