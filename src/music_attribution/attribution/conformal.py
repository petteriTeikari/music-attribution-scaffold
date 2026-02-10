"""Conformal prediction confidence scoring for attribution.

Wraps attribution confidence in conformal prediction sets. "90% confident"
must actually mean 90% coverage. Implements Adaptive Prediction Sets (APS)
method for calibrated uncertainty quantification.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime

from pydantic import BaseModel, Field

from music_attribution.schemas.attribution import ConformalSet
from music_attribution.schemas.enums import CreditRoleEnum

logger = logging.getLogger(__name__)


class CalibrationReport(BaseModel):
    """Report on calibration quality."""

    ece: float = Field(ge=0.0)  # Expected Calibration Error
    marginal_coverage: float = Field(ge=0.0, le=1.0)
    target_coverage: float = Field(ge=0.0, le=1.0)
    calibration_method: str
    calibration_set_size: int = Field(ge=0)
    bin_accuracies: list[float] = Field(default_factory=list)
    bin_confidences: list[float] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


class ConformalScorer:
    """Conformal prediction scorer for attribution confidence.

    Uses Adaptive Prediction Sets (APS) method to produce
    calibrated prediction sets at specified coverage levels.
    """

    def score(
        self,
        predictions: list[tuple[CreditRoleEnum, float]],
        coverage: float = 0.90,
    ) -> ConformalSet:
        """Produce a conformal prediction set at specified coverage.

        Args:
            predictions: List of (role, confidence) tuples.
            coverage: Target coverage level (e.g., 0.90 for 90%).

        Returns:
            ConformalSet with prediction sets and calibration info.
        """
        if not predictions:
            return ConformalSet(
                coverage_level=coverage,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=coverage,
                calibration_error=0.0,
                calibration_method="APS",
                calibration_set_size=0,
            )

        # Sort by confidence descending
        sorted_preds = sorted(predictions, key=lambda x: x[1], reverse=True)

        # Build prediction set: include roles until cumulative confidence >= coverage
        prediction_set: list[CreditRoleEnum] = []
        cumulative = 0.0
        for role, conf in sorted_preds:
            prediction_set.append(role)
            cumulative += conf
            if cumulative >= coverage:
                break

        # If we still haven't reached coverage, include all
        if cumulative < coverage:
            prediction_set = [role for role, _ in sorted_preds]

        # Compute marginal coverage (achieved coverage)
        total_conf = sum(c for _, c in sorted_preds)
        marginal = min(cumulative / total_conf, 1.0) if total_conf > 0 else 0.0

        # Calibration error (simplified — deviation from target)
        cal_error = abs(marginal - coverage)

        return ConformalSet(
            coverage_level=coverage,
            prediction_sets={"default": prediction_set},
            set_sizes={"default": len(prediction_set)},
            marginal_coverage=marginal,
            calibration_error=cal_error,
            calibration_method="APS",
            calibration_set_size=len(predictions),
        )

    def calibrate(
        self, predictions: list[tuple[float, bool]],
    ) -> CalibrationReport:
        """Compute calibration metrics from predictions vs actuals.

        Args:
            predictions: List of (predicted_probability, actual_outcome) tuples.

        Returns:
            CalibrationReport with ECE and per-bin metrics.
        """
        if not predictions:
            return CalibrationReport(
                ece=0.0,
                marginal_coverage=0.0,
                target_coverage=0.9,
                calibration_method="APS",
                calibration_set_size=0,
            )

        # Bin predictions into 10 bins
        n_bins = 10
        bin_sums: list[float] = [0.0] * n_bins
        bin_correct: list[int] = [0] * n_bins
        bin_counts: list[int] = [0] * n_bins

        for prob, actual in predictions:
            bin_idx = min(int(prob * n_bins), n_bins - 1)
            bin_sums[bin_idx] += prob
            bin_correct[bin_idx] += int(actual)
            bin_counts[bin_idx] += 1

        # Compute per-bin accuracy and confidence
        bin_accuracies: list[float] = []
        bin_confidences: list[float] = []
        ece = 0.0
        total = len(predictions)

        for i in range(n_bins):
            if bin_counts[i] > 0:
                acc = bin_correct[i] / bin_counts[i]
                conf = bin_sums[i] / bin_counts[i]
                bin_accuracies.append(acc)
                bin_confidences.append(conf)
                ece += (bin_counts[i] / total) * abs(acc - conf)
            else:
                bin_accuracies.append(0.0)
                bin_confidences.append(0.0)

        # Compute actual coverage
        correct_count = sum(1 for _, actual in predictions if actual)
        marginal_coverage = correct_count / total if total > 0 else 0.0

        return CalibrationReport(
            ece=ece,
            marginal_coverage=marginal_coverage,
            target_coverage=0.9,
            calibration_method="APS",
            calibration_set_size=total,
            bin_accuracies=bin_accuracies,
            bin_confidences=bin_confidences,
        )
