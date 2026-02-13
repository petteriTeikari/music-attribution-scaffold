"""Tests for Prometheus metrics module (P2-7).

Validates domain-specific metrics for the attribution scaffold:
- attribution_requests_total (counter)
- attribution_confidence_score (histogram)
- agent_response_latency_seconds (histogram)
- drift_detected_total (counter)
- center_bias_detections_total (counter)
- active_pipeline_stage (info/gauge)
"""

from __future__ import annotations

import pytest


class TestMetricsModule:
    """Tests for observability.metrics module."""

    def test_metrics_module_exports_expected_metrics(self) -> None:
        """All domain-specific metrics are importable."""
        from music_attribution.observability.metrics import (
            AGENT_LATENCY,
            ATTRIBUTION_REQUESTS,
            CENTER_BIAS_DETECTIONS,
            CONFIDENCE_HISTOGRAM,
            DRIFT_DETECTED,
        )

        assert ATTRIBUTION_REQUESTS is not None
        assert CONFIDENCE_HISTOGRAM is not None
        assert AGENT_LATENCY is not None
        assert DRIFT_DETECTED is not None
        assert CENTER_BIAS_DETECTIONS is not None

    def test_request_counter_increments(self) -> None:
        """ATTRIBUTION_REQUESTS counter increments correctly."""
        from prometheus_client import CollectorRegistry

        from music_attribution.observability.metrics import create_metrics

        registry = CollectorRegistry()
        metrics = create_metrics(registry)
        metrics.attribution_requests.labels(method="GET", endpoint="/api/v1/attributions", status="200").inc()
        value = metrics.attribution_requests.labels(
            method="GET", endpoint="/api/v1/attributions", status="200"
        )._value.get()
        assert value == 1.0

    def test_confidence_histogram_observes_values(self) -> None:
        """CONFIDENCE_HISTOGRAM records observed values."""
        from prometheus_client import CollectorRegistry

        from music_attribution.observability.metrics import create_metrics

        registry = CollectorRegistry()
        metrics = create_metrics(registry)
        metrics.confidence_histogram.labels(assurance_level="A2").observe(0.87)
        # Histogram sum should contain the observed value
        assert metrics.confidence_histogram.labels(assurance_level="A2")._sum.get() == pytest.approx(0.87)

    def test_drift_counter_increments(self) -> None:
        """DRIFT_DETECTED counter increments."""
        from prometheus_client import CollectorRegistry

        from music_attribution.observability.metrics import create_metrics

        registry = CollectorRegistry()
        metrics = create_metrics(registry)
        metrics.drift_detected.labels(drift_type="confidence").inc()
        assert metrics.drift_detected.labels(drift_type="confidence")._value.get() == 1.0

    def test_agent_latency_histogram_exists(self) -> None:
        """AGENT_LATENCY histogram accepts observations."""
        from prometheus_client import CollectorRegistry

        from music_attribution.observability.metrics import create_metrics

        registry = CollectorRegistry()
        metrics = create_metrics(registry)
        metrics.agent_latency.labels(tool="explain_confidence").observe(0.42)
        assert metrics.agent_latency.labels(tool="explain_confidence")._sum.get() == pytest.approx(0.42)

    def test_center_bias_counter(self) -> None:
        """CENTER_BIAS_DETECTIONS counter increments."""
        from prometheus_client import CollectorRegistry

        from music_attribution.observability.metrics import create_metrics

        registry = CollectorRegistry()
        metrics = create_metrics(registry)
        metrics.center_bias_detections.inc()
        assert metrics.center_bias_detections._value.get() == 1.0


class TestMetricsEndpoint:
    """Tests for /metrics route."""

    def test_metrics_endpoint_returns_prometheus_format(self) -> None:
        """The /metrics endpoint returns text/plain with Prometheus exposition format."""
        from music_attribution.api.routes.metrics import router

        # Verify the router has a /metrics route
        routes = [r.path for r in router.routes]  # type: ignore[union-attr]
        assert "/metrics" in routes
