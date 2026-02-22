"""Tests for voice pipeline Prometheus metrics.

Validates all 8 voice metric instruments:
- voice_stt_latency_seconds (histogram)
- voice_stt_requests_total (counter)
- voice_tts_latency_seconds (histogram)
- voice_tts_requests_total (counter)
- voice_vad_speech_segments_total (counter)
- voice_drift_score (histogram)
- voice_drift_events_total (counter)
- voice_active_connections (gauge)
"""

from __future__ import annotations

import pytest
from prometheus_client import CollectorRegistry

from music_attribution.observability.voice_metrics import VoiceMetrics, create_voice_metrics


@pytest.fixture()
def voice_metrics() -> VoiceMetrics:
    """Create isolated voice metrics for testing."""
    return create_voice_metrics(CollectorRegistry())


class TestVoiceMetrics:
    """Tests for observability.voice_metrics module."""

    def test_stt_latency_histogram_observes(self, voice_metrics: VoiceMetrics) -> None:
        """STT latency histogram records observations with model+device labels."""
        voice_metrics.stt_latency_seconds.labels(model="small", device="cuda").observe(0.42)
        assert voice_metrics.stt_latency_seconds.labels(model="small", device="cuda")._sum.get() == pytest.approx(0.42)

    def test_stt_requests_counter_increments(self, voice_metrics: VoiceMetrics) -> None:
        """STT requests counter increments with model+status labels."""
        voice_metrics.stt_requests_total.labels(model="small", status="success").inc()
        assert voice_metrics.stt_requests_total.labels(model="small", status="success")._value.get() == 1.0

    def test_tts_latency_histogram_observes(self, voice_metrics: VoiceMetrics) -> None:
        """TTS latency histogram records observations with provider label."""
        voice_metrics.tts_latency_seconds.labels(provider="piper").observe(0.085)
        assert voice_metrics.tts_latency_seconds.labels(provider="piper")._sum.get() == pytest.approx(0.085)

    def test_tts_requests_counter_increments(self, voice_metrics: VoiceMetrics) -> None:
        """TTS requests counter increments with provider+status labels."""
        voice_metrics.tts_requests_total.labels(provider="piper", status="success").inc()
        assert voice_metrics.tts_requests_total.labels(provider="piper", status="success")._value.get() == 1.0

    def test_vad_segments_counter_increments(self, voice_metrics: VoiceMetrics) -> None:
        """VAD speech segments counter increments (no labels)."""
        voice_metrics.vad_speech_segments_total.inc()
        voice_metrics.vad_speech_segments_total.inc()
        assert voice_metrics.vad_speech_segments_total._value.get() == 2.0

    def test_drift_score_histogram_observes(self, voice_metrics: VoiceMetrics) -> None:
        """Drift score histogram records observations with state label."""
        voice_metrics.voice_drift_score.labels(state="sync").observe(0.92)
        assert voice_metrics.voice_drift_score.labels(state="sync")._sum.get() == pytest.approx(0.92)

    def test_drift_events_counter_increments(self, voice_metrics: VoiceMetrics) -> None:
        """Drift events counter increments with state label."""
        voice_metrics.voice_drift_events_total.labels(state="desync").inc()
        assert voice_metrics.voice_drift_events_total.labels(state="desync")._value.get() == 1.0

    def test_active_connections_gauge(self, voice_metrics: VoiceMetrics) -> None:
        """Active connections gauge increments and decrements."""
        voice_metrics.voice_active_connections.inc()
        voice_metrics.voice_active_connections.inc()
        assert voice_metrics.voice_active_connections._value.get() == 2.0
        voice_metrics.voice_active_connections.dec()
        assert voice_metrics.voice_active_connections._value.get() == 1.0

    def test_isolated_registries_do_not_conflict(self) -> None:
        """Two VoiceMetrics instances with separate registries are independent."""
        vm1 = create_voice_metrics(CollectorRegistry())
        vm2 = create_voice_metrics(CollectorRegistry())
        vm1.stt_requests_total.labels(model="tiny", status="success").inc()
        assert vm2.stt_requests_total.labels(model="tiny", status="success")._value.get() == 0.0
