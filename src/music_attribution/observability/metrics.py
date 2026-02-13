"""Prometheus application metrics for the attribution scaffold.

Defines domain-specific metrics that capture what matters in a music
attribution system: confidence distributions, source agreement rates,
drift events, agent tool latency, and center-bias detections.

The module provides two usage patterns:

1. **Production**: Use ``get_metrics()`` to obtain a singleton
   ``AppMetrics`` instance backed by the default Prometheus registry.
2. **Testing**: Use ``create_metrics(CollectorRegistry())`` to obtain
   an isolated instance that does not conflict with other tests.

Usage
-----
>>> from music_attribution.observability.metrics import get_metrics
>>> metrics = get_metrics()
>>> metrics.attribution_requests.labels(method="GET", endpoint="/api/v1/attributions", status="200").inc()

Metric Instruments
------------------
attribution_requests_total : Counter
    Total HTTP requests to attribution endpoints, labelled by
    method, endpoint, and status.
attribution_confidence_score : Histogram
    Distribution of attribution confidence scores (0.0--1.0 in
    0.05 increments), labelled by assurance level.
agent_response_latency_seconds : Histogram
    Agent tool call response latency, labelled by tool name.
drift_detected_total : Counter
    Number of drift events detected by ``DriftDetector``, labelled
    by drift type.
center_bias_detections_total : Counter
    Number of center-bias flags raised in feedback cards.

See Also
--------
music_attribution.quality.drift_detector : Increments ``drift_detected``.
music_attribution.chat.agent : Observed by ``agent_latency``.
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

    Using a frozen dataclass rather than module-level globals allows
    isolated registries in tests (preventing collector name conflicts)
    and makes the set of metrics explicit and type-safe.

    Attributes
    ----------
    attribution_requests : Counter
        Total HTTP requests to attribution endpoints. Labels:
        ``method``, ``endpoint``, ``status``.
    confidence_histogram : Histogram
        Distribution of attribution confidence scores. Labels:
        ``assurance_level``. Buckets: 0.0--1.0 in 0.05 steps.
    agent_latency : Histogram
        Agent tool call response latency in seconds. Labels: ``tool``.
        Buckets: 10ms to 10s (logarithmic).
    drift_detected : Counter
        Number of drift events detected. Labels: ``drift_type``.
    center_bias_detections : Counter
        Number of center-bias flags raised (no labels).
    """

    attribution_requests: Counter
    confidence_histogram: Histogram
    agent_latency: Histogram
    drift_detected: Counter
    center_bias_detections: Counter


def create_metrics(registry: CollectorRegistry | None = None) -> AppMetrics:
    """Create a fresh set of application Prometheus metrics.

    Each call creates new metric instruments registered with the
    given (or a new) ``CollectorRegistry``. For production, pass the
    default Prometheus ``REGISTRY``; for tests, pass a fresh
    ``CollectorRegistry()`` to avoid name collisions.

    Parameters
    ----------
    registry : CollectorRegistry | None, optional
        Prometheus collector registry to register metrics with.
        If ``None``, a new isolated registry is created (useful for
        testing).

    Returns
    -------
    AppMetrics
        Frozen dataclass containing all metric instruments.
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

    Uses module-level caching to ensure metrics are registered exactly
    once with the default Prometheus ``REGISTRY``. Subsequent calls
    return the same ``AppMetrics`` instance.

    Returns
    -------
    AppMetrics
        Singleton ``AppMetrics`` instance using the default Prometheus
        registry.
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
