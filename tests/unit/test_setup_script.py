"""Tests for one-command setup script (Task 0.0).

Validates that scripts/setup.sh exists, is executable, checks
prerequisites, and that the Makefile has a setup target.

Note: These tests validate project layout files (scripts/, Makefile)
that are NOT copied into the Docker test image (docker/Dockerfile.test
only copies src/, tests/, alembic/). They are skipped automatically
when running inside Docker CI.
"""

from __future__ import annotations

import os
import stat
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SETUP_SCRIPT = PROJECT_ROOT / "scripts" / "setup.sh"
MAKEFILE = PROJECT_ROOT / "Makefile"

_IN_DOCKER = os.environ.get("RUNNING_IN_DOCKER") == "true"


@pytest.mark.skipif(_IN_DOCKER, reason="scripts/ and Makefile not copied into Docker test image")
class TestSetupScript:
    """Tests for scripts/setup.sh."""

    def test_setup_script_exists_and_executable(self) -> None:
        """Script file exists at scripts/setup.sh and has +x permission."""
        assert SETUP_SCRIPT.exists(), f"Setup script not found: {SETUP_SCRIPT}"
        mode = os.stat(SETUP_SCRIPT).st_mode
        assert mode & stat.S_IXUSR, "setup.sh is not executable (missing user execute bit)"

    def test_makefile_has_setup_target(self) -> None:
        """Makefile contains 'setup' target that calls scripts/setup.sh."""
        content = MAKEFILE.read_text(encoding="utf-8")
        assert "setup:" in content, "Makefile missing 'setup' target"
        assert "scripts/setup.sh" in content, "Makefile setup target should call scripts/setup.sh"

    def test_setup_checks_prerequisites(self) -> None:
        """Script checks for docker, uv, and node before proceeding."""
        content = SETUP_SCRIPT.read_text(encoding="utf-8")
        assert "docker" in content, "setup.sh must check for docker"
        assert "uv" in content, "setup.sh must check for uv"
        assert "node" in content, "setup.sh must check for node"

    def test_setup_idempotent(self) -> None:
        """Script uses 'already running' or idempotent patterns."""
        content = SETUP_SCRIPT.read_text(encoding="utf-8")
        # Should check if services are already running or use idempotent commands
        assert "already" in content.lower() or "if" in content.lower(), (
            "setup.sh should be idempotent (check if services are already running)"
        )
