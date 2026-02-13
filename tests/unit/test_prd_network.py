"""Tests for PRD decision network extensions (Task B4).

Validates that 4 new L3 nodes are added to the decision network
and that corresponding .decision.yaml files exist.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RUNNING_IN_DOCKER = not (PROJECT_ROOT / "pyproject.toml").exists()
pytestmark = pytest.mark.skipif(RUNNING_IN_DOCKER, reason="Project root files not available in Docker")


class TestNetworkExtensions:
    """Tests for _network.yaml additions (Task B4)."""

    @pytest.fixture(scope="class")
    def network(self) -> dict:
        """Load _network.yaml."""
        path = PROJECT_ROOT / "docs" / "prd" / "decisions" / "_network.yaml"
        return yaml.safe_load(path.read_text(encoding="utf-8"))

    def test_network_yaml_has_new_nodes(self, network: dict) -> None:
        """Verify _network.yaml contains all L3-components nodes."""
        node_ids = {n["id"] for n in network["nodes"]}
        expected = {
            "training_attribution_integration",
            "rights_management_scope",
            "provenance_verification",
            "external_registry_integration",
            "compliance_framework_mapping",
            "tdm_rights_reservation",
        }
        assert expected <= node_ids, f"Missing nodes: {expected - node_ids}"

    def test_new_decision_files_exist(self) -> None:
        """Verify all L3-components .decision.yaml files exist and are valid YAML."""
        decision_dir = PROJECT_ROOT / "docs" / "prd" / "decisions" / "L3-components"
        files = [
            "training-attribution-integration.decision.yaml",
            "rights-management-scope.decision.yaml",
            "provenance-verification.decision.yaml",
            "external-registry-integration.decision.yaml",
            "compliance-framework-mapping.decision.yaml",
            "tdm-rights-reservation.decision.yaml",
        ]
        for filename in files:
            path = decision_dir / filename
            assert path.exists(), f"Missing decision file: {filename}"
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            assert isinstance(data, dict), f"{filename} should parse as YAML mapping"

    def test_network_version_bumped(self, network: dict) -> None:
        """Verify network version is >= 2.0.0."""
        version = network["network"]["version"]
        parts = [int(x) for x in str(version).split(".")]
        assert parts >= [2, 0, 0], f"Expected version >= 2.0.0, got {version}"
