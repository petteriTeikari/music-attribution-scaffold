"""Tests for PRD network expansion — 7 new xOps decision nodes.

Validates that the PRD network is expanded from v1.8.0 (37 nodes)
to v1.9.0 (44 nodes) with proper DAG acyclicity, edge integrity,
and decision files.
"""

from __future__ import annotations

from collections import defaultdict, deque
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RUNNING_IN_DOCKER = not (PROJECT_ROOT / "pyproject.toml").exists()
pytestmark = pytest.mark.skipif(RUNNING_IN_DOCKER, reason="Project root files not available in Docker")

NEW_L4_NODES = {"orchestrator_choice", "cd_strategy"}
NEW_L5_NODES = {"ml_monitoring", "documentation_tooling", "policy_as_code", "finops_strategy", "ethics_governance"}
ALL_NEW_NODES = NEW_L4_NODES | NEW_L5_NODES


class TestNetworkExpansion:
    """Tests for _network.yaml xOps expansion."""

    @pytest.fixture(scope="class")
    def network(self) -> dict:
        """Load _network.yaml."""
        path = PROJECT_ROOT / "docs" / "prd" / "decisions" / "_network.yaml"
        return yaml.safe_load(path.read_text(encoding="utf-8"))

    def test_network_version_is_1_9_0(self, network: dict) -> None:
        """Network version bumped to 1.9.0."""
        version = str(network["network"]["version"])
        parts = [int(x) for x in version.split(".")]
        assert parts >= [1, 9, 0], f"Expected version >= 1.9.0, got {version}"

    def test_network_has_at_least_46_nodes(self, network: dict) -> None:
        """Network has at least 46 nodes (may grow as new decision areas are added)."""
        node_count = len(network["nodes"])
        assert node_count >= 46, f"Expected >= 46 nodes, got {node_count}"

    def test_new_l4_nodes_exist(self, network: dict) -> None:
        """New L4 deployment nodes are present."""
        node_ids = {n["id"] for n in network["nodes"]}
        assert node_ids >= NEW_L4_NODES, f"Missing L4 nodes: {NEW_L4_NODES - node_ids}"

    def test_new_l5_nodes_exist(self, network: dict) -> None:
        """New L5 operations nodes are present."""
        node_ids = {n["id"] for n in network["nodes"]}
        assert node_ids >= NEW_L5_NODES, f"Missing L5 nodes: {NEW_L5_NODES - node_ids}"

    def test_decision_files_exist_and_valid(self) -> None:
        """All 7 new .decision.yaml files exist and parse as valid YAML."""
        decisions_dir = PROJECT_ROOT / "docs" / "prd" / "decisions"
        expected_files = {
            "L4-deployment/orchestrator-choice.decision.yaml",
            "L4-deployment/cd-strategy.decision.yaml",
            "L5-operations/ml-monitoring.decision.yaml",
            "L5-operations/documentation-tooling.decision.yaml",
            "L5-operations/policy-as-code.decision.yaml",
            "L5-operations/finops-strategy.decision.yaml",
            "L5-operations/ethics-governance.decision.yaml",
        }
        for rel_path in expected_files:
            path = decisions_dir / rel_path
            assert path.exists(), f"Missing decision file: {rel_path}"
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            assert isinstance(data, dict), f"{rel_path} should parse as YAML mapping"

    def test_network_dag_is_acyclic(self, network: dict) -> None:
        """Network DAG has no cycles (Kahn's algorithm)."""
        node_ids = {n["id"] for n in network["nodes"]}
        in_degree: dict[str, int] = defaultdict(int)
        adjacency: dict[str, list[str]] = defaultdict(list)

        for nid in node_ids:
            in_degree.setdefault(nid, 0)

        for edge in network.get("edges", []):
            src = edge["from"]
            dst = edge["to"]
            assert src in node_ids, f"Edge source '{src}' not in nodes"
            assert dst in node_ids, f"Edge target '{dst}' not in nodes"
            adjacency[src].append(dst)
            in_degree[dst] += 1

        queue: deque[str] = deque(nid for nid in node_ids if in_degree[nid] == 0)
        visited = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for child in adjacency[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        assert visited == len(node_ids), f"DAG has cycle: visited {visited}/{len(node_ids)} nodes"

    def test_iac_tooling_has_opentofu_option(self) -> None:
        """iac_tooling decision file includes opentofu option."""
        path = PROJECT_ROOT / "docs" / "prd" / "decisions" / "L4-deployment" / "iac-tooling.decision.yaml"
        content = path.read_text(encoding="utf-8")
        assert "opentofu" in content.lower(), "iac_tooling must have opentofu option"

    def test_new_edges_reference_valid_nodes(self, network: dict) -> None:
        """All edges reference nodes that exist in the network."""
        node_ids = {n["id"] for n in network["nodes"]}
        for edge in network.get("edges", []):
            assert edge["from"] in node_ids, f"Edge from '{edge['from']}' references unknown node"
            assert edge["to"] in node_ids, f"Edge to '{edge['to']}' references unknown node"
