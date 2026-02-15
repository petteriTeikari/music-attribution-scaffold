"""Active learning priority queue for attribution review.

Ranks ``AttributionRecord`` objects by review priority for human experts.
Uses a multi-factor priority formula combining five signals:

1. **Boundary proximity** (weight=0.30): Records near the 0.5 confidence
   decision boundary are most informative for active learning, as human
   feedback on these cases maximally reduces model uncertainty.
2. **Source disagreement** (weight=0.25): Low inter-source agreement
   indicates conflicting evidence that needs human arbitration.
3. **Ambiguity** (weight=0.15): Large conformal prediction set sizes
   indicate genuine uncertainty about the credit role.
4. **Never-reviewed penalty** (weight=0.15): Records that have never
   been reviewed (version=1) are prioritized over already-reviewed ones.
5. **Staleness** (weight=0.15): Records not updated for 30+ days are
   prioritized to ensure periodic re-validation.

Notes
-----
This implements the active learning review queue described in
Teikari (2026), Section 5.4. The boundary proximity criterion follows
the uncertainty sampling strategy from Settles (2009), "Active Learning
Literature Survey."

See Also
--------
music_attribution.attribution.persistence : Persistence layer that provides
    ``find_needs_review()`` for initial candidate retrieval.
music_attribution.attribution.aggregator : Produces the confidence and
    agreement scores used for priority computation.
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

    Ranks records by a composite priority score combining five factors
    that indicate review urgency. Higher scores mean higher priority
    for human expert review.

    Parameters
    ----------
    weights : dict[str, float] | None, optional
        Override the default factor weights. Keys must be:
        ``"boundary"``, ``"disagreement"``, ``"ambiguity"``,
        ``"never_reviewed"``, ``"staleness"``. Defaults to ``_WEIGHTS``.

    Attributes
    ----------
    _weights : dict[str, float]
        Active priority factor weights.
    """

    def __init__(self, weights: dict[str, float] | None = None) -> None:
        self._weights = weights or _WEIGHTS

    def compute_priority(self, record: AttributionRecord) -> float:
        """Compute review priority score for an attribution record.

        Combines five weighted factors into a single priority score.
        Higher scores indicate higher review urgency.

        Parameters
        ----------
        record : AttributionRecord
            The attribution record to prioritize.

        Returns
        -------
        float
            Priority score clamped to range [0.0, 1.0].
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

        Scores all input records and returns the top ``limit`` by
        descending priority. Does not filter by ``needs_review`` flag;
        the caller should pre-filter if desired.

        Parameters
        ----------
        records : list[AttributionRecord]
            All attribution records to consider.
        limit : int, optional
            Maximum number of records to return. Default is 10.

        Returns
        -------
        list[AttributionRecord]
            Records sorted by priority (highest first), limited to
            ``limit`` entries.
        """
        scored = [(self.compute_priority(r), r) for r in records]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [r for _, r in scored[:limit]]

    @staticmethod
    def _boundary_score(confidence: float) -> float:
        """Score based on proximity to the 0.5 decision boundary.

        Records near the decision boundary (confidence ~0.5) are the most
        informative for active learning because they represent the cases
        where the model is least certain.

        Parameters
        ----------
        confidence : float
            Attribution confidence score in [0.0, 1.0].

        Returns
        -------
        float
            Score in [0.0, 1.0]. Maximum (1.0) at confidence=0.5,
            minimum (0.0) at confidence=0.0 or 1.0.
        """
        return 1.0 - abs(confidence - 0.5) * 2.0

    @staticmethod
    def _disagreement_score(source_agreement: float) -> float:
        """Score based on inter-source disagreement.

        Low agreement between sources indicates conflicting evidence
        that requires human arbitration.

        Parameters
        ----------
        source_agreement : float
            Inter-source agreement score in [0.0, 1.0].

        Returns
        -------
        float
            Score in [0.0, 1.0]. Higher when sources disagree more.
        """
        return 1.0 - source_agreement

    @staticmethod
    def _ambiguity_score(record: AttributionRecord) -> float:
        """Score based on conformal prediction set size.

        Larger prediction sets indicate genuine uncertainty about the
        credit role assignment. A set size of 1 means the model is
        confident; 5+ roles in the set means high ambiguity.

        Parameters
        ----------
        record : AttributionRecord
            The attribution record to score.

        Returns
        -------
        float
            Score in [0.0, 1.0]. Normalized such that set size >= 5
            yields 1.0.
        """
        total_size = sum(record.conformal_set.set_sizes.values())
        # Normalize: single role = 0, many roles = high
        return min(total_size / 5.0, 1.0) if total_size > 0 else 0.0

    @staticmethod
    def _never_reviewed_score(version: int) -> float:
        """Score based on whether the record has ever been reviewed.

        Version 1 records have never been reviewed and receive the
        maximum score. Each subsequent review (version increment)
        reduces the score by 0.25, reaching 0.0 after 5 reviews.

        Parameters
        ----------
        version : int
            Record version number (1 = initial, 2+ = reviewed).

        Returns
        -------
        float
            Score in [0.0, 1.0]. Maximum (1.0) for never-reviewed records.
        """
        return 1.0 if version == 1 else max(0.0, 1.0 - (version - 1) * 0.25)

    @staticmethod
    def _staleness_score(updated_at: datetime) -> float:
        """Score based on time since last update.

        Older records are prioritized for re-validation. The score
        increases linearly until 30 days, after which it saturates at 1.0.

        Parameters
        ----------
        updated_at : datetime
            UTC timestamp of the last record update.

        Returns
        -------
        float
            Score in [0.0, 1.0]. Reaches maximum (1.0) after 30+ days
            without update.
        """
        age_days = (datetime.now(UTC) - updated_at).days
        # Normalize: 30+ days = 1.0
        return min(age_days / 30.0, 1.0)
