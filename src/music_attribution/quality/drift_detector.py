"""Drift detection for pipeline quality monitoring.

Detects statistical drift from historical baselines at pipeline
boundaries. Flags anomalous batches for investigation.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime

from pydantic import BaseModel, Field

from music_attribution.schemas.batch import BatchMetadata

logger = logging.getLogger(__name__)

# Default drift thresholds
_CONFIDENCE_DRIFT_THRESHOLD = 2.0  # Standard deviations
_COVERAGE_DRIFT_THRESHOLD = 0.2  # Absolute difference
_SOURCE_DISTRIBUTION_THRESHOLD = 0.3  # Relative change threshold


class DriftReport(BaseModel):
    """Report on batch drift from baseline."""

    is_drifted: bool
    confidence_shift: float
    source_distribution_changed: bool
    identifier_coverage_delta: float
    details: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


class DriftDetector:
    """Detect statistical drift between batches.

    Compares current batch metadata against a baseline to detect
    significant changes in confidence distribution, source mix,
    and identifier coverage.
    """

    def __init__(
        self,
        confidence_threshold: float = _CONFIDENCE_DRIFT_THRESHOLD,
        coverage_threshold: float = _COVERAGE_DRIFT_THRESHOLD,
        source_threshold: float = _SOURCE_DISTRIBUTION_THRESHOLD,
    ) -> None:
        self._confidence_threshold = confidence_threshold
        self._coverage_threshold = coverage_threshold
        self._source_threshold = source_threshold

    def check(self, current: BatchMetadata, baseline: BatchMetadata) -> DriftReport:
        """Check for drift between current batch and baseline.

        Args:
            current: Current batch metadata.
            baseline: Historical baseline metadata.

        Returns:
            DriftReport with drift assessment.
        """
        # Confidence drift
        conf_shift = abs(
            current.confidence_stats.mean - baseline.confidence_stats.mean
        )
        baseline_std = max(baseline.confidence_stats.std, 0.01)
        conf_drifted = conf_shift > self._confidence_threshold * baseline_std

        # Source distribution drift
        source_changed = self._check_source_drift(current, baseline)

        # Identifier coverage drift
        coverage_delta = current.identifier_coverage - baseline.identifier_coverage
        coverage_drifted = abs(coverage_delta) > self._coverage_threshold

        is_drifted = conf_drifted or source_changed or coverage_drifted

        details_parts: list[str] = []
        if conf_drifted:
            details_parts.append(
                f"Confidence shifted by {conf_shift:.3f} "
                f"({conf_shift / baseline_std:.1f} std)"
            )
        if source_changed:
            details_parts.append("Source distribution changed significantly")
        if coverage_drifted:
            details_parts.append(
                f"Identifier coverage changed by {coverage_delta:+.3f}"
            )
        details = "; ".join(details_parts) if details_parts else "No drift detected"

        return DriftReport(
            is_drifted=is_drifted,
            confidence_shift=conf_shift,
            source_distribution_changed=source_changed,
            identifier_coverage_delta=coverage_delta,
            details=details,
        )

    def _check_source_drift(
        self, current: BatchMetadata, baseline: BatchMetadata,
    ) -> bool:
        """Check if source distribution has changed significantly."""
        all_sources = set(current.source_distribution) | set(baseline.source_distribution)
        current_total = max(sum(current.source_distribution.values()), 1)
        baseline_total = max(sum(baseline.source_distribution.values()), 1)

        for source in all_sources:
            curr_ratio = current.source_distribution.get(source, 0) / current_total
            base_ratio = baseline.source_distribution.get(source, 0) / baseline_total
            if abs(curr_ratio - base_ratio) > self._source_threshold:
                return True

        return False
