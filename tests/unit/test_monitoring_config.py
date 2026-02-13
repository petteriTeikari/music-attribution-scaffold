"""Tests for monitoring configuration (Grafana dashboard + Prometheus config).

Validates that pre-built monitoring configs exist for the Docker Compose
monitoring profile: Grafana dashboard, Prometheus scrape config, and
Grafana datasource provisioning.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RUNNING_IN_DOCKER = not (PROJECT_ROOT / "pyproject.toml").exists()
pytestmark = pytest.mark.skipif(RUNNING_IN_DOCKER, reason="Project root files not available in Docker")


class TestGrafanaDashboard:
    """Tests for the pre-built Grafana dashboard."""

    @pytest.fixture(scope="class")
    def dashboard(self) -> dict:
        """Load the attribution overview dashboard."""
        path = PROJECT_ROOT / "docker" / "grafana" / "dashboards" / "attribution-overview.json"
        assert path.exists(), "Missing Grafana dashboard JSON"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_grafana_dashboard_json_is_valid(self, dashboard: dict) -> None:
        """Dashboard JSON is parseable and has expected structure."""
        assert "panels" in dashboard, "Dashboard must have panels"
        assert "title" in dashboard, "Dashboard must have a title"

    def test_grafana_dashboard_has_expected_panels(self, dashboard: dict) -> None:
        """Dashboard includes panels for key metrics."""
        panel_titles = {p.get("title", "") for p in dashboard.get("panels", [])}
        # At least 4 of these should exist
        expected_keywords = {"request", "confidence", "latency", "drift", "bias"}
        found = sum(1 for kw in expected_keywords if any(kw.lower() in t.lower() for t in panel_titles))
        assert found >= 4, f"Expected >= 4 metric panels, found {found}. Panels: {panel_titles}"


class TestPrometheusConfig:
    """Tests for Prometheus scrape configuration."""

    def test_prometheus_config_targets_backend(self) -> None:
        """Prometheus config scrapes the backend /metrics endpoint."""
        path = PROJECT_ROOT / "docker" / "prometheus.yml"
        assert path.exists(), "Missing docker/prometheus.yml"
        config = yaml.safe_load(path.read_text(encoding="utf-8"))
        # Find scrape target
        targets_found = False
        for job in config.get("scrape_configs", []):
            for sc in job.get("static_configs", []):
                for target in sc.get("targets", []):
                    if "backend" in target or "8000" in str(target):
                        targets_found = True
        assert targets_found, "Prometheus must scrape backend:8000"


class TestGrafanaDatasource:
    """Tests for Grafana datasource provisioning."""

    def test_grafana_datasource_references_prometheus(self) -> None:
        """Grafana datasource config points to Prometheus."""
        path = PROJECT_ROOT / "docker" / "grafana" / "datasources" / "prometheus.yml"
        assert path.exists(), "Missing Grafana datasource config"
        config = yaml.safe_load(path.read_text(encoding="utf-8"))
        datasources = config.get("datasources", [])
        assert len(datasources) >= 1, "Must have at least 1 datasource"
        prom = datasources[0]
        assert prom.get("type") == "prometheus", "First datasource must be prometheus"


class TestDockerComposeMonitoring:
    """Tests for docker-compose.dev.yml monitoring profile."""

    def test_docker_compose_has_monitoring_profile(self) -> None:
        """docker-compose.dev.yml includes monitoring services with profile."""
        path = PROJECT_ROOT / "docker-compose.dev.yml"
        content = path.read_text(encoding="utf-8")
        assert "prometheus" in content, "docker-compose.dev.yml must include prometheus service"
        assert "grafana" in content, "docker-compose.dev.yml must include grafana service"
        assert "monitoring" in content, "docker-compose.dev.yml must reference monitoring profile"


class TestDashboardProvisioning:
    """Tests for Grafana dashboard provisioning config."""

    def test_dashboard_provisioning_exists(self) -> None:
        """Dashboard provisioning YAML exists."""
        path = PROJECT_ROOT / "docker" / "grafana" / "dashboards" / "dashboard.yml"
        assert path.exists(), "Missing dashboard provisioning config"
        config = yaml.safe_load(path.read_text(encoding="utf-8"))
        providers = config.get("apiVersion") or config.get("providers")
        assert providers is not None, "Dashboard provisioning must have apiVersion or providers"
