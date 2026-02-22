"""Prometheus metrics for the voice pipeline.

Captures latency distributions, throughput counters, drift scores,
and active connection counts for the voice agent subsystem.

The module follows the same frozen-dataclass + singleton pattern as
:mod:`~music_attribution.observability.metrics`.

Usage
-----
>>> from music_attribution.observability.voice_metrics import get_voice_metrics
>>> vm = get_voice_metrics()
>>> vm.stt_latency_seconds.labels(model="small", device="cuda").observe(0.42)

Metric Instruments
------------------
voice_stt_latency_seconds : Histogram
    STT inference latency (seconds), labelled by model size and device.
voice_stt_requests_total : Counter
    Total STT requests, labelled by model and status.
voice_tts_latency_seconds : Histogram
    TTS synthesis latency (seconds), labelled by provider.
voice_tts_requests_total : Counter
    Total TTS requests, labelled by provider and status.
voice_vad_speech_segments_total : Counter
    Total VAD speech segments detected (no labels).
voice_drift_score : Histogram
    Distribution of persona drift EWMA scores, labelled by state.
voice_drift_events_total : Counter
    Number of drift/desync events, labelled by state.
voice_active_connections : Gauge
    Current number of active voice WebSocket connections (no labels).

See Also
--------
music_attribution.observability.metrics : Application-level metrics.
music_attribution.voice.drift : Emits drift score and event metrics.
music_attribution.voice.server : Emits connection gauge metrics.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from prometheus_client import CollectorRegistry, Counter, Gauge, Histogram

logger = logging.getLogger(__name__)

# STT buckets — CPU Whisper can be very slow (up to 30s for large audio)
_STT_LATENCY_BUCKETS = (0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0)

# TTS buckets — typically fast (Piper is sub-second)
_TTS_LATENCY_BUCKETS = (0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5)

# Drift score buckets — reuse confidence-style 0.0-1.0 in 0.05 steps
_DRIFT_SCORE_BUCKETS = tuple(i / 20 for i in range(21))


@dataclass(frozen=True)
class VoiceMetrics:
    """Container for all voice pipeline Prometheus metrics.

    Using a frozen dataclass rather than module-level globals allows
    isolated registries in tests (preventing collector name conflicts)
    and makes the set of metrics explicit and type-safe.

    Attributes
    ----------
    stt_latency_seconds : Histogram
        STT inference latency in seconds. Labels: ``model``, ``device``.
    stt_requests_total : Counter
        Total STT inference requests. Labels: ``model``, ``status``.
    tts_latency_seconds : Histogram
        TTS synthesis latency in seconds. Labels: ``provider``.
    tts_requests_total : Counter
        Total TTS synthesis requests. Labels: ``provider``, ``status``.
    vad_speech_segments_total : Counter
        Total VAD speech segments detected (no labels).
    voice_drift_score : Histogram
        Distribution of persona drift EWMA scores. Labels: ``state``.
    voice_drift_events_total : Counter
        Number of drift or desync events. Labels: ``state``.
    voice_active_connections : Gauge
        Current number of active voice WebSocket connections (no labels).
    """

    stt_latency_seconds: Histogram
    stt_requests_total: Counter
    tts_latency_seconds: Histogram
    tts_requests_total: Counter
    vad_speech_segments_total: Counter
    voice_drift_score: Histogram
    voice_drift_events_total: Counter
    voice_active_connections: Gauge


def create_voice_metrics(registry: CollectorRegistry | None = None) -> VoiceMetrics:
    """Create a fresh set of voice pipeline Prometheus metrics.

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
    VoiceMetrics
        Frozen dataclass containing all voice metric instruments.
    """
    if registry is None:
        registry = CollectorRegistry()

    return VoiceMetrics(
        stt_latency_seconds=Histogram(
            "voice_stt_latency_seconds",
            "STT inference latency in seconds",
            labelnames=["model", "device"],
            buckets=_STT_LATENCY_BUCKETS,
            registry=registry,
        ),
        stt_requests_total=Counter(
            "voice_stt_requests_total",
            "Total STT inference requests",
            labelnames=["model", "status"],
            registry=registry,
        ),
        tts_latency_seconds=Histogram(
            "voice_tts_latency_seconds",
            "TTS synthesis latency in seconds",
            labelnames=["provider"],
            buckets=_TTS_LATENCY_BUCKETS,
            registry=registry,
        ),
        tts_requests_total=Counter(
            "voice_tts_requests_total",
            "Total TTS synthesis requests",
            labelnames=["provider", "status"],
            registry=registry,
        ),
        vad_speech_segments_total=Counter(
            "voice_vad_speech_segments_total",
            "Total VAD speech segments detected",
            registry=registry,
        ),
        voice_drift_score=Histogram(
            "voice_drift_score",
            "Distribution of persona drift EWMA scores",
            labelnames=["state"],
            buckets=_DRIFT_SCORE_BUCKETS,
            registry=registry,
        ),
        voice_drift_events_total=Counter(
            "voice_drift_events_total",
            "Number of drift or desync events",
            labelnames=["state"],
            registry=registry,
        ),
        voice_active_connections=Gauge(
            "voice_active_connections",
            "Current number of active voice WebSocket connections",
            registry=registry,
        ),
    )


# --- Module-level singletons for convenience imports ---

_default_voice_metrics: VoiceMetrics | None = None


def get_voice_metrics() -> VoiceMetrics:
    """Get or create the default voice metrics singleton.

    Uses module-level caching to ensure metrics are registered exactly
    once with the default Prometheus ``REGISTRY``. Subsequent calls
    return the same ``VoiceMetrics`` instance.

    Returns
    -------
    VoiceMetrics
        Singleton ``VoiceMetrics`` instance using the default Prometheus
        registry.
    """
    global _default_voice_metrics  # noqa: PLW0603
    if _default_voice_metrics is None:
        from prometheus_client import REGISTRY

        _default_voice_metrics = create_voice_metrics(REGISTRY)
    return _default_voice_metrics
