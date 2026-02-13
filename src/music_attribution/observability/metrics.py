"""Prometheus application metrics for the attribution scaffold.

Domain-specific metrics that teach what matters in a music attribution
system: confidence distributions, source agreement rates, drift events,
agent latency, and center-bias detections.

Usage:
    from music_attribution.observability.metrics import get_metrics
    metrics = get_metrics()
    metrics.attribution_requests.labels(method="GET", endpoint="/api/v1/attributions", status="200").inc()
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from prometheus_client import CollectorRegistry, Counter, Histogram

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

# Histogram buckets tuned for API latency (seconds)
_LATENCY_BUCKETS = (0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0)

# Confidence score buckets (0.0 to 1.0 in 0.05 increments)
_CONFIDENCE_BUCKETS = tuple(i / 20 for i in range(21))


@dataclass(frozen=True)
class AppMetrics:
    """Container for all application Prometheus metrics.

    Using a dataclass rather than module-level globals allows
    isolated registries in tests and prevents collector conflicts.
    """

    attribution_requests: Counter
    confidence_histogram: Histogram
    agent_latency: Histogram
    drift_detected: Counter
    center_bias_detections: Counter


def create_metrics(registry: CollectorRegistry | None = None) -> AppMetrics:
    """Create a fresh set of application metrics.

    Args:
        registry: Prometheus CollectorRegistry. Uses a new registry if
                  None is provided (useful for testing).

    Returns:
        AppMetrics dataclass with all metric instruments.
    """
    if registry is None:
        registry = CollectorRegistry()

    return AppMetrics(
        attribution_requests=Counter(
            "attribution_requests_total",
            "Total HTTP requests to attribution endpoints",
            labelnames=["method", "endpoint", "status"],
            registry=registry,
        ),
        confidence_histogram=Histogram(
            "attribution_confidence_score",
            "Distribution of attribution confidence scores",
            labelnames=["assurance_level"],
            buckets=_CONFIDENCE_BUCKETS,
            registry=registry,
        ),
        agent_latency=Histogram(
            "agent_response_latency_seconds",
            "Agent tool call response latency in seconds",
            labelnames=["tool"],
            buckets=_LATENCY_BUCKETS,
            registry=registry,
        ),
        drift_detected=Counter(
            "drift_detected_total",
            "Number of drift events detected by DriftDetector",
            labelnames=["drift_type"],
            registry=registry,
        ),
        center_bias_detections=Counter(
            "center_bias_detections_total",
            "Number of center-bias flags raised in feedback cards",
            registry=registry,
        ),
    )


# --- Module-level singletons for convenience imports ---
# These use the default global registry for production use.
# Tests should use create_metrics(CollectorRegistry()) for isolation.

_default_metrics: AppMetrics | None = None


def get_metrics() -> AppMetrics:
    """Get or create the default application metrics singleton.

    Returns:
        AppMetrics instance using the default Prometheus registry.
    """
    global _default_metrics  # noqa: PLW0603
    if _default_metrics is None:
        from prometheus_client import REGISTRY

        _default_metrics = create_metrics(REGISTRY)
    return _default_metrics


# Convenience exports for direct import
ATTRIBUTION_REQUESTS = "attribution_requests_total"
CONFIDENCE_HISTOGRAM = "attribution_confidence_score"
AGENT_LATENCY = "agent_response_latency_seconds"
DRIFT_DETECTED = "drift_detected_total"
CENTER_BIAS_DETECTIONS = "center_bias_detections_total"
