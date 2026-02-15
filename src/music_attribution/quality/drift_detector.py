"""Drift detection for pipeline quality monitoring.

Detects statistical drift from historical baselines at pipeline
boundaries. Flags anomalous batches for investigation by comparing
three dimensions:

1. **Confidence drift** -- mean confidence shift measured in standard
   deviations of the baseline distribution.
2. **Source distribution drift** -- relative change in the proportion
   of records from each data source.
3. **Identifier coverage drift** -- absolute change in the fraction
   of records with standard identifiers (ISRC, ISWC, ISNI).

Default thresholds are conservative to minimise false positives in
early pipeline runs. They can be tuned per deployment via the
``DriftDetector`` constructor.

Classes
-------
DriftReport
    Pydantic model summarising drift assessment for a batch pair.
DriftDetector
    Stateless detector comparing current vs. baseline ``BatchMetadata``.

See Also
--------
music_attribution.schemas.batch.BatchMetadata : Input to drift checks.
music_attribution.observability.metrics : ``drift_detected`` counter.
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
    """Report on batch drift from baseline.

    Summarises the drift assessment across three dimensions
    (confidence, source distribution, identifier coverage) with
    a boolean ``is_drifted`` flag and human-readable details.

    Attributes
    ----------
    is_drifted : bool
        ``True`` if any dimension exceeds its threshold.
    confidence_shift : float
        Absolute difference in mean confidence between current
        and baseline batches.
    source_distribution_changed : bool
        ``True`` if the source mix changed beyond the threshold.
    identifier_coverage_delta : float
        Signed difference in identifier coverage (current - baseline).
    details : str
        Human-readable summary of detected drift dimensions.
        ``"No drift detected"`` if ``is_drifted`` is ``False``.
    timestamp : datetime
        UTC timestamp when the report was generated.
    """

    is_drifted: bool
    confidence_shift: float
    source_distribution_changed: bool
    identifier_coverage_delta: float
    details: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


class DriftDetector:
    """Detect statistical drift between batches at pipeline boundaries.

    Compares current batch metadata against a historical baseline to
    detect significant changes in confidence distribution, source mix,
    and identifier coverage. Designed to be run at the end of each
    pipeline batch to catch data quality regressions early.

    The detector is stateless -- thresholds are set at construction
    time and each ``check()`` call is independent.

    Attributes
    ----------
    _confidence_threshold : float
        Maximum allowed confidence shift in standard deviations.
    _coverage_threshold : float
        Maximum allowed absolute change in identifier coverage.
    _source_threshold : float
        Maximum allowed relative change in any source's proportion.
    """

    def __init__(
        self,
        confidence_threshold: float = _CONFIDENCE_DRIFT_THRESHOLD,
        coverage_threshold: float = _COVERAGE_DRIFT_THRESHOLD,
        source_threshold: float = _SOURCE_DISTRIBUTION_THRESHOLD,
    ) -> None:
        """Initialise the drift detector with configurable thresholds.

        Parameters
        ----------
        confidence_threshold : float, optional
            Maximum confidence shift in standard deviations of the
            baseline before flagging drift. Default is 2.0.
        coverage_threshold : float, optional
            Maximum absolute change in identifier coverage fraction.
            Default is 0.2.
        source_threshold : float, optional
            Maximum relative change in any individual source's
            proportion. Default is 0.3.
        """
        self._confidence_threshold = confidence_threshold
        self._coverage_threshold = coverage_threshold
        self._source_threshold = source_threshold

    def check(self, current: BatchMetadata, baseline: BatchMetadata) -> DriftReport:
        """Check for drift between the current batch and a baseline.

        Compares three dimensions independently and aggregates the
        results into a ``DriftReport``. Any single dimension exceeding
        its threshold sets ``is_drifted=True``.

        Parameters
        ----------
        current : BatchMetadata
            Metadata from the current pipeline batch.
        baseline : BatchMetadata
            Historical baseline metadata (e.g. rolling average of
            recent batches or the initial seed batch).

        Returns
        -------
        DriftReport
            Assessment with per-dimension results, overall drift flag,
            and human-readable details.
        """
        # Confidence drift
        conf_shift = abs(current.confidence_stats.mean - baseline.confidence_stats.mean)
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
            details_parts.append(f"Confidence shifted by {conf_shift:.3f} ({conf_shift / baseline_std:.1f} std)")
        if source_changed:
            details_parts.append("Source distribution changed significantly")
        if coverage_drifted:
            details_parts.append(f"Identifier coverage changed by {coverage_delta:+.3f}")
        details = "; ".join(details_parts) if details_parts else "No drift detected"

        return DriftReport(
            is_drifted=is_drifted,
            confidence_shift=conf_shift,
            source_distribution_changed=source_changed,
            identifier_coverage_delta=coverage_delta,
            details=details,
        )

    def _check_source_drift(
        self,
        current: BatchMetadata,
        baseline: BatchMetadata,
    ) -> bool:
        """Check if the source distribution has changed significantly.

        Computes the relative proportion of each source in both batches
        and checks whether any single source's proportion has changed
        by more than ``_source_threshold``.

        Parameters
        ----------
        current : BatchMetadata
            Current batch metadata.
        baseline : BatchMetadata
            Baseline batch metadata.

        Returns
        -------
        bool
            ``True`` if any source's proportion changed beyond the
            threshold.
        """
        all_sources = set(current.source_distribution) | set(baseline.source_distribution)
        current_total = max(sum(current.source_distribution.values()), 1)
        baseline_total = max(sum(baseline.source_distribution.values()), 1)

        for source in all_sources:
            curr_ratio = current.source_distribution.get(source, 0) / current_total
            base_ratio = baseline.source_distribution.get(source, 0) / baseline_total
            if abs(curr_ratio - base_ratio) > self._source_threshold:
                return True

        return False
