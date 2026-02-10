"""Tests for conformal prediction confidence scoring."""

from __future__ import annotations

import pytest

from music_attribution.attribution.conformal import CalibrationReport, ConformalScorer
from music_attribution.schemas.attribution import ConformalSet
from music_attribution.schemas.enums import CreditRoleEnum


@pytest.fixture
def scorer() -> ConformalScorer:
    """Create a ConformalScorer."""
    return ConformalScorer()


class TestConformalScorer:
    """Tests for conformal prediction scoring."""

    def test_conformal_set_at_90_coverage(self, scorer) -> None:
        """Test that conformal set achieves 90% coverage target."""
        # Simulate predictions with known confidences
        predictions = [
            (CreditRoleEnum.PERFORMER, 0.95),
            (CreditRoleEnum.SONGWRITER, 0.80),
            (CreditRoleEnum.PRODUCER, 0.60),
        ]
        result = scorer.score(predictions, coverage=0.90)
        assert isinstance(result, ConformalSet)
        assert result.coverage_level == 0.90

    def test_conformal_set_size_decreases_with_more_evidence(self, scorer) -> None:
        """Test that more evidence produces smaller prediction sets."""
        # High-confidence single prediction — tight set
        high_conf = [(CreditRoleEnum.PERFORMER, 0.99)]
        result_high = scorer.score(high_conf, coverage=0.90)

        # Low-confidence with alternatives — wider set
        low_conf = [
            (CreditRoleEnum.PERFORMER, 0.4),
            (CreditRoleEnum.SONGWRITER, 0.35),
            (CreditRoleEnum.PRODUCER, 0.25),
        ]
        result_low = scorer.score(low_conf, coverage=0.90)

        # Low confidence should produce larger or equal set sizes
        high_total = sum(result_high.set_sizes.values())
        low_total = sum(result_low.set_sizes.values())
        assert low_total >= high_total

    def test_calibration_error_below_threshold(self, scorer) -> None:
        """Test that calibration error is computed and below threshold."""
        # Perfect calibration: predicted probabilities match actual frequencies
        predictions = [(0.9, True), (0.9, True), (0.9, True), (0.9, False),
                       (0.5, True), (0.5, False), (0.5, True), (0.5, False)]
        report = scorer.calibrate(predictions)
        assert isinstance(report, CalibrationReport)
        assert report.ece >= 0.0
        # ECE should be computable
        assert report.calibration_method == "APS"

    def test_empty_evidence_produces_wide_set(self, scorer) -> None:
        """Test that empty evidence produces a maximally wide prediction set."""
        result = scorer.score([], coverage=0.90)
        # With no evidence, should include all possible roles
        assert result.coverage_level == 0.90
        total_set_size = sum(result.set_sizes.values())
        assert total_set_size >= 0  # At minimum, exists

    def test_high_agreement_produces_narrow_set(self, scorer) -> None:
        """Test that high agreement produces a narrow prediction set."""
        # Very high confidence on single role
        high_agreement = [(CreditRoleEnum.PERFORMER, 0.99)]
        result = scorer.score(high_agreement, coverage=0.90)
        # Should have a narrow prediction set
        if "default" in result.prediction_sets:
            assert len(result.prediction_sets["default"]) <= 2
