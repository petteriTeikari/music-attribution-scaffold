"""Observability subsystem: metrics and instrumentation.

Provides Prometheus application metrics for monitoring attribution
pipeline health, confidence distributions, and agent performance.

Submodules
----------
metrics
    Domain-specific Prometheus counters and histograms for attribution
    requests, confidence score distributions, agent tool latency,
    drift events, and center-bias detections. Includes a
    ``create_metrics`` factory for test isolation and a ``get_metrics``
    singleton for production use.

See Also
--------
music_attribution.quality.drift_detector : Produces ``drift_detected`` events.
music_attribution.chat.agent : Produces ``agent_latency`` observations.
"""

from __future__ import annotations
