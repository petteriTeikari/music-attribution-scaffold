"""Tests for PRD network expansion — xOps + Discussion ecosystem nodes.

Validates that the PRD network is expanded with proper DAG acyclicity,
edge integrity, and decision files. Covers:
- v1.9.0: 7 xOps nodes (orchestrator, CD, ML monitoring, etc.)
- v3.0.0: 28 ecosystem integration nodes (platform strategy, partnerships, etc.)
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

    def test_network_has_at_least_78_nodes(self, network: dict) -> None:
        """Network has at least 78 nodes (v3.0.0: 50 core + 28 ecosystem expansion)."""
        node_count = len(network["nodes"])
        assert node_count >= 78, f"Expected >= 78 nodes, got {node_count}"

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


# --- v3.0.0 Discussion Expansion Tests ---

ECOSYSTEM_L2_NODES = {"platform_strategy", "partnership_model"}
ECOSYSTEM_L3_CATEGORY_NODES = {
    "tda_provider_integration",
    "cmo_licensing_integration",
    "content_id_system",
    "ai_music_platform_connector",
    "metadata_registry_integration",
    "watermark_detection",
    "agent_interop_protocol",
    "edge_inference_strategy",
    "attribution_eval_framework",
    "agent_observability_otel",
    "agentic_commerce_protocol",
    "knowledge_graph_backend",
}
ECOSYSTEM_L3_COMPANY_NODES = {
    "musical_ai_partnership",
    "sureel_ai_partnership",
    "stim_cmo_pilot",
    "soundexchange_registry",
    "fairly_trained_certification",
    "suno_udio_licensing",
}
ECOSYSTEM_L4_NODES = {
    "compliance_reporting_pipeline",
    "training_data_provenance_store",
    "golden_dataset_management",
    "edge_deployment_target",
}
ECOSYSTEM_L5_NODES = {
    "regulatory_monitoring",
    "market_intelligence",
    "attribution_accuracy_monitoring",
    "partnership_health_metrics",
}
ALL_ECOSYSTEM_NODES = (
    ECOSYSTEM_L2_NODES
    | ECOSYSTEM_L3_CATEGORY_NODES
    | ECOSYSTEM_L3_COMPANY_NODES
    | ECOSYSTEM_L4_NODES
    | ECOSYSTEM_L5_NODES
)


class TestEcosystemExpansion:
    """Tests for v3.0.0 Discussion expansion — 28 ecosystem integration nodes."""

    @pytest.fixture(scope="class")
    def network(self) -> dict:
        """Load _network.yaml."""
        path = PROJECT_ROOT / "docs" / "prd" / "decisions" / "_network.yaml"
        return yaml.safe_load(path.read_text(encoding="utf-8"))

    def test_network_version_is_3_0_0(self, network: dict) -> None:
        """Network version bumped to 3.0.0."""
        version = str(network["network"]["version"])
        parts = [int(x) for x in version.split(".")]
        assert parts >= [3, 0, 0], f"Expected version >= 3.0.0, got {version}"

    def test_all_28_ecosystem_nodes_exist(self, network: dict) -> None:
        """All 28 ecosystem expansion nodes are present."""
        node_ids = {n["id"] for n in network["nodes"]}
        missing = ALL_ECOSYSTEM_NODES - node_ids
        assert not missing, f"Missing ecosystem nodes: {missing}"

    def test_ecosystem_l2_nodes(self, network: dict) -> None:
        """L2 architecture ecosystem nodes are present."""
        node_ids = {n["id"] for n in network["nodes"]}
        assert node_ids >= ECOSYSTEM_L2_NODES

    def test_ecosystem_l3_category_nodes(self, network: dict) -> None:
        """L3 category ecosystem nodes are present."""
        node_ids = {n["id"] for n in network["nodes"]}
        assert node_ids >= ECOSYSTEM_L3_CATEGORY_NODES

    def test_ecosystem_l3_company_nodes(self, network: dict) -> None:
        """L3 company ecosystem nodes are present."""
        node_ids = {n["id"] for n in network["nodes"]}
        assert node_ids >= ECOSYSTEM_L3_COMPANY_NODES

    def test_ecosystem_decision_files_exist(self) -> None:
        """All 28 ecosystem .decision.yaml files exist and parse as valid YAML."""
        decisions_dir = PROJECT_ROOT / "docs" / "prd" / "decisions"
        expected_files = {
            # L2
            "L2-architecture/platform-strategy.decision.yaml",
            "L2-architecture/partnership-model.decision.yaml",
            # L3 category
            "L3-components/tda-provider-integration.decision.yaml",
            "L3-components/cmo-licensing-integration.decision.yaml",
            "L3-components/content-id-system.decision.yaml",
            "L3-components/ai-music-platform-connector.decision.yaml",
            "L3-components/metadata-registry-integration.decision.yaml",
            "L3-components/watermark-detection.decision.yaml",
            "L3-components/agent-interop-protocol.decision.yaml",
            "L3-components/edge-inference-strategy.decision.yaml",
            "L3-components/attribution-eval-framework.decision.yaml",
            "L3-components/agent-observability-otel.decision.yaml",
            "L3-components/agentic-commerce-protocol.decision.yaml",
            "L3-components/knowledge-graph-backend.decision.yaml",
            # L3 company
            "L3-components/musical-ai-partnership.decision.yaml",
            "L3-components/sureel-ai-partnership.decision.yaml",
            "L3-components/stim-cmo-pilot.decision.yaml",
            "L3-components/soundexchange-registry.decision.yaml",
            "L3-components/fairly-trained-certification.decision.yaml",
            "L3-components/suno-udio-licensing.decision.yaml",
            # L4
            "L4-deployment/compliance-reporting-pipeline.decision.yaml",
            "L4-deployment/training-data-provenance-store.decision.yaml",
            "L4-deployment/golden-dataset-management.decision.yaml",
            "L4-deployment/edge-deployment-target.decision.yaml",
            # L5
            "L5-operations/regulatory-monitoring.decision.yaml",
            "L5-operations/market-intelligence.decision.yaml",
            "L5-operations/attribution-accuracy-monitoring.decision.yaml",
            "L5-operations/partnership-health-metrics.decision.yaml",
        }
        for rel_path in expected_files:
            path = decisions_dir / rel_path
            assert path.exists(), f"Missing decision file: {rel_path}"
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            assert isinstance(data, dict), f"{rel_path} should parse as YAML mapping"

    def test_ecosystem_nodes_have_discussion_tag(self) -> None:
        """All ecosystem decision files include 'discussion-expansion' tag."""
        decisions_dir = PROJECT_ROOT / "docs" / "prd" / "decisions"
        for level_dir in ["L2-architecture", "L3-components", "L4-deployment", "L5-operations"]:
            dir_path = decisions_dir / level_dir
            for yaml_file in dir_path.glob("*.decision.yaml"):
                data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
                if data.get("decision_id") in ALL_ECOSYSTEM_NODES:
                    tags = data.get("tags", [])
                    assert "discussion-expansion" in tags, (
                        f"{yaml_file.name}: ecosystem node missing 'discussion-expansion' tag"
                    )

    def test_ecosystem_probabilities_sum_to_one(self) -> None:
        """All ecosystem decision files have option probabilities summing to 1.0."""
        decisions_dir = PROJECT_ROOT / "docs" / "prd" / "decisions"
        for level_dir in ["L2-architecture", "L3-components", "L4-deployment", "L5-operations"]:
            dir_path = decisions_dir / level_dir
            for yaml_file in dir_path.glob("*.decision.yaml"):
                data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
                if data.get("decision_id") in ALL_ECOSYSTEM_NODES:
                    options = data.get("options", [])
                    total = sum(o.get("prior_probability", 0) for o in options)
                    assert abs(total - 1.0) < 0.01, f"{yaml_file.name}: probabilities sum to {total}, expected 1.0"
