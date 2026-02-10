"""Active learning priority queue for attribution review.

Ranks AttributionRecords by review priority for human experts.
Uses multi-factor priority formula combining boundary proximity,
source disagreement, ambiguity, review status, and staleness.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime

from music_attribution.schemas.attribution import AttributionRecord

logger = logging.getLogger(__name__)

# Priority formula weights
_WEIGHTS = {
    "boundary": 0.30,  # Proximity to decision boundary
    "disagreement": 0.25,  # Source disagreement
    "ambiguity": 0.15,  # Entity ambiguity (conformal set size)
    "never_reviewed": 0.15,  # Never reviewed penalty
    "staleness": 0.15,  # Time since last review
}


class ReviewPriorityQueue:
    """Priority queue for attribution review.

    Ranks records by composite priority score combining multiple
    factors that indicate review need.
    """

    def __init__(self, weights: dict[str, float] | None = None) -> None:
        self._weights = weights or _WEIGHTS

    def compute_priority(self, record: AttributionRecord) -> float:
        """Compute review priority score for an attribution record.

        Higher scores indicate higher review priority.

        Args:
            record: The AttributionRecord to prioritize.

        Returns:
            Priority score between 0.0 and 1.0.
        """
        boundary = self._boundary_score(record.confidence_score)
        disagreement = self._disagreement_score(record.source_agreement)
        ambiguity = self._ambiguity_score(record)
        never_reviewed = self._never_reviewed_score(record.version)
        staleness = self._staleness_score(record.updated_at)

        priority = (
            self._weights["boundary"] * boundary
            + self._weights["disagreement"] * disagreement
            + self._weights["ambiguity"] * ambiguity
            + self._weights["never_reviewed"] * never_reviewed
            + self._weights["staleness"] * staleness
        )

        return min(max(priority, 0.0), 1.0)

    def next_for_review(
        self,
        records: list[AttributionRecord],
        limit: int = 10,
    ) -> list[AttributionRecord]:
        """Return top records needing review, sorted by priority.

        Args:
            records: All attribution records to consider.
            limit: Maximum number of records to return.

        Returns:
            List of AttributionRecords sorted by priority (highest first).
        """
        scored = [(self.compute_priority(r), r) for r in records]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [r for _, r in scored[:limit]]

    @staticmethod
    def _boundary_score(confidence: float) -> float:
        """Score based on proximity to decision boundary (0.5).

        Records near 0.5 confidence are most informative for active learning.
        """
        return 1.0 - abs(confidence - 0.5) * 2.0

    @staticmethod
    def _disagreement_score(source_agreement: float) -> float:
        """Score based on source disagreement. Low agreement = high score."""
        return 1.0 - source_agreement

    @staticmethod
    def _ambiguity_score(record: AttributionRecord) -> float:
        """Score based on conformal set size (larger = more ambiguous)."""
        total_size = sum(record.conformal_set.set_sizes.values())
        # Normalize: single role = 0, many roles = high
        return min(total_size / 5.0, 1.0) if total_size > 0 else 0.0

    @staticmethod
    def _never_reviewed_score(version: int) -> float:
        """Score based on whether record has been reviewed (version > 1 means reviewed)."""
        return 1.0 if version == 1 else max(0.0, 1.0 - (version - 1) * 0.25)

    @staticmethod
    def _staleness_score(updated_at: datetime) -> float:
        """Score based on time since last update. Older = staler = higher priority."""
        age_days = (datetime.now(UTC) - updated_at).days
        # Normalize: 30+ days = 1.0
        return min(age_days / 30.0, 1.0)
