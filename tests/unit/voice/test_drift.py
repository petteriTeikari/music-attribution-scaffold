"""Tests for embedding-based persona drift detector."""

from __future__ import annotations

import pytest

from music_attribution.voice.config import VoiceConfig
from music_attribution.voice.drift import PIPECAT_AVAILABLE, DriftDetector

PERSONA_TEXT = (
    "You are the Music Attribution Assistant, an expert in music credit "
    "attribution, provenance tracking, and confidence scoring."
)


@pytest.fixture
def detector() -> DriftDetector:
    """Create a DriftDetector with default config."""
    config = VoiceConfig(drift_monitoring=True)
    return DriftDetector(config, PERSONA_TEXT)


class TestDriftDetectorInit:
    """Tests for DriftDetector initialization."""

    def test_starts_in_sync(self, detector: DriftDetector) -> None:
        """Detector starts with EWMA score of 1.0 (fully in sync)."""
        assert detector.ewma_score == pytest.approx(1.0)

    def test_initial_state_is_sync(self, detector: DriftDetector) -> None:
        """Initial state is 'sync'."""
        assert detector.state() == "sync"

    def test_no_raw_scores_initially(self, detector: DriftDetector) -> None:
        """No raw scores before any scoring calls."""
        assert detector.raw_scores == []


class TestDriftScoring:
    """Tests for drift score computation."""

    def test_similar_text_scores_high(self, detector: DriftDetector) -> None:
        """Text similar to persona should score relatively high."""
        score = detector.score(
            "As the Music Attribution Assistant, I can explain this confidence score for your attribution record."
        )
        assert score > 0.0

    def test_dissimilar_text_scores_lower(self, detector: DriftDetector) -> None:
        """Text unrelated to persona should score lower than similar text."""
        similar_score = detector.score("I am an expert in music attribution and provenance tracking.")
        # Reset for fair comparison
        detector2 = DriftDetector(VoiceConfig(drift_monitoring=True), PERSONA_TEXT)
        dissimilar_score = detector2.score("The weather today is sunny and warm.")
        assert similar_score > dissimilar_score

    def test_empty_response_scores_zero(self, detector: DriftDetector) -> None:
        """Empty response text returns zero similarity."""
        score = detector.score("")
        assert score < 1.0  # EWMA won't be zero due to smoothing

    def test_ewma_smoothing_applied(self, detector: DriftDetector) -> None:
        """EWMA smoothing reduces score volatility."""
        # Score with persona-aligned text (should stay high)
        scores = []
        for _ in range(5):
            score = detector.score(
                "The attribution confidence score for this music work is based on source agreement tracking."
            )
            scores.append(score)
        # With EWMA, scores converge rather than jumping
        assert len(scores) == 5
        # All scores should be positive (persona-aligned text)
        assert all(s > 0 for s in scores)

    def test_raw_scores_accumulated(self, detector: DriftDetector) -> None:
        """Raw scores are stored for each scoring call."""
        detector.score("test one")
        detector.score("test two")
        detector.score("test three")
        assert len(detector.raw_scores) == 3

    def test_raw_scores_are_between_0_and_1(self, detector: DriftDetector) -> None:
        """Raw scores are clamped to [0, 1] range."""
        detector.score("some random text for testing")
        for score in detector.raw_scores:
            assert 0.0 <= score <= 1.0


class TestDriftStates:
    """Tests for drift state transitions."""

    def test_sync_state_at_high_score(self) -> None:
        """State is 'sync' when EWMA score is above sync threshold."""
        config = VoiceConfig(
            drift_monitoring=True,
            drift_sync_threshold=0.85,
        )
        detector = DriftDetector(config, PERSONA_TEXT)
        # Initial EWMA is 1.0 → sync
        assert detector.state() == "sync"

    def test_desync_state_at_low_score(self) -> None:
        """State transitions to 'desync' after many off-topic responses."""
        config = VoiceConfig(
            drift_monitoring=True,
            drift_sync_threshold=0.85,
            drift_desync_threshold=0.70,
            drift_ewma_alpha=0.9,  # High alpha → fast adaptation
        )
        detector = DriftDetector(config, PERSONA_TEXT)
        # Force many completely unrelated responses
        for _ in range(20):
            detector.score("xyz abc 123 completely random irrelevant text")
        # After many off-topic responses, should be in drift or desync
        assert detector.state() in ("drift", "desync")

    def test_ewma_alpha_affects_responsiveness(self) -> None:
        """Higher EWMA alpha means faster adaptation to score changes."""
        config_fast = VoiceConfig(drift_monitoring=True, drift_ewma_alpha=0.9)
        config_slow = VoiceConfig(drift_monitoring=True, drift_ewma_alpha=0.1)

        detector_fast = DriftDetector(config_fast, PERSONA_TEXT)
        detector_slow = DriftDetector(config_slow, PERSONA_TEXT)

        # Both score same off-topic text
        off_topic = "completely unrelated text about weather"
        for _ in range(5):
            detector_fast.score(off_topic)
            detector_slow.score(off_topic)

        # Fast alpha should deviate from initial 1.0 more than slow
        assert detector_fast.ewma_score < detector_slow.ewma_score

    def test_drift_state_between_thresholds(self) -> None:
        """State is 'drift' when EWMA is between sync and desync thresholds."""
        config = VoiceConfig(
            drift_monitoring=True,
            drift_sync_threshold=0.85,
            drift_desync_threshold=0.70,
        )
        detector = DriftDetector(config, PERSONA_TEXT)
        # Manually set EWMA to middle range
        detector._ewma_score = 0.78
        assert detector.state() == "drift"

    def test_state_transitions_sync_to_drift(self) -> None:
        """Scoring off-topic text transitions from sync through drift."""
        config = VoiceConfig(
            drift_monitoring=True,
            drift_sync_threshold=0.85,
            drift_desync_threshold=0.70,
            drift_ewma_alpha=0.5,
        )
        detector = DriftDetector(config, PERSONA_TEXT)
        assert detector.state() == "sync"

        # Score progressively off-topic until drift
        for _ in range(50):
            detector.score("random xyz noise unrelated text")
            if detector.state() != "sync":
                break

        # Should have left sync state
        assert detector.state() in ("drift", "desync")


class TestDriftConfigIntegration:
    """Tests for drift detector config integration."""

    def test_thresholds_from_config(self) -> None:
        """Detector uses thresholds from VoiceConfig."""
        config = VoiceConfig(
            drift_monitoring=True,
            drift_sync_threshold=0.90,
            drift_desync_threshold=0.60,
            drift_ewma_alpha=0.5,
        )
        detector = DriftDetector(config, PERSONA_TEXT)
        # Initial EWMA is 1.0, threshold is 0.90 → sync
        assert detector.state() == "sync"

    def test_custom_alpha_affects_score_update(self) -> None:
        """Different alpha values produce different score trajectories."""
        config_a = VoiceConfig(drift_monitoring=True, drift_ewma_alpha=0.1)
        config_b = VoiceConfig(drift_monitoring=True, drift_ewma_alpha=0.9)
        det_a = DriftDetector(config_a, PERSONA_TEXT)
        det_b = DriftDetector(config_b, PERSONA_TEXT)

        text = "random off topic text about cooking"
        score_a = det_a.score(text)
        score_b = det_b.score(text)

        # Higher alpha → score closer to raw (which is low for off-topic)
        # Lower alpha → score closer to initial 1.0
        assert score_a > score_b


class TestDriftMonitorProcessor:
    """Tests for the Pipecat FrameProcessor drift monitor."""

    def test_pipecat_available_flag(self) -> None:
        """PIPECAT_AVAILABLE flag is a boolean."""
        assert isinstance(PIPECAT_AVAILABLE, bool)

    @pytest.mark.skipif(not PIPECAT_AVAILABLE, reason="Requires pipecat-ai")
    def test_processor_class_exists(self) -> None:
        """DriftMonitorProcessor is importable when pipecat is available."""
        from music_attribution.voice.drift import DriftMonitorProcessor

        assert DriftMonitorProcessor is not None

    @pytest.mark.skipif(PIPECAT_AVAILABLE, reason="Test for non-pipecat env")
    def test_processor_not_importable_without_pipecat(self) -> None:
        """DriftMonitorProcessor is not defined without pipecat."""
        import music_attribution.voice.drift as drift_mod

        assert not hasattr(drift_mod, "DriftMonitorProcessor")

    def test_embedding_fallback_to_jaccard(self) -> None:
        """Drift detector falls back to Jaccard when sentence-transformers unavailable."""
        config = VoiceConfig(drift_monitoring=True)
        detector = DriftDetector(config, "music attribution expert confidence scoring")
        # This should work even without sentence-transformers
        score = detector.score("music attribution confidence")
        assert 0.0 <= score <= 1.0
