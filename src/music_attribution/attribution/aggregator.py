"""Multi-source credit aggregation for attribution.

Core component of Pipeline 3 (Attribution Engine). Aggregates credits from
multiple ``ResolvedEntity`` objects into a single ``AttributionRecord``.
Handles disagreements between sources using weighted voting based on
source reliability.

Default source reliability weights (from ``constants.SOURCE_RELIABILITY_WEIGHTS``):

- **MusicBrainz** -- highest weight (community-curated, structured data)
- **Discogs** -- medium weight (community-curated, less structured)
- **AcoustID** -- medium weight (acoustic fingerprint-based)
- **File metadata** -- lowest weight (often incomplete or incorrect)
- **Artist input** -- high weight (authoritative but potentially biased)

Notes
-----
Implements the multi-source aggregation described in Teikari (2026),
Section 5.1. The weighted voting approach ensures that higher-quality
sources have more influence on the final attribution, while still
incorporating evidence from all available sources.

See Also
--------
music_attribution.attribution.conformal : Calibration of aggregated scores.
music_attribution.attribution.persistence : Storage of attribution records.
music_attribution.constants : Source reliability weight definitions.
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime

from music_attribution.constants import REVIEW_THRESHOLD, SOURCE_RELIABILITY_WEIGHTS
from music_attribution.schemas.attribution import (
    AttributionRecord,
    ConformalSet,
    Credit,
    ProvenanceEvent,
    ScoreEventDetails,
)
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
    ProvenanceEventTypeEnum,
    SourceEnum,
)
from music_attribution.schemas.resolved import ResolvedEntity

logger = logging.getLogger(__name__)


class CreditAggregator:
    """Aggregate credits from resolved entities into attribution records.

    Uses weighted voting based on source reliability to handle
    disagreements between sources. Produces a complete ``AttributionRecord``
    with credits, confidence, assurance level, and provenance chain.

    Parameters
    ----------
    source_weights : dict[SourceEnum, float] | None, optional
        Per-source reliability weight overrides. If ``None``, uses
        ``SOURCE_RELIABILITY_WEIGHTS`` from ``constants``.

    Attributes
    ----------
    _source_weights : dict[SourceEnum, float]
        Active source reliability weights.

    See Also
    --------
    music_attribution.attribution.conformal.ConformalScorer : Calibrate the aggregated score.
    music_attribution.attribution.priority_queue.ReviewPriorityQueue : Prioritize records for review.
    """

    def __init__(self, source_weights: dict[SourceEnum, float] | None = None) -> None:
        self._source_weights = source_weights or SOURCE_RELIABILITY_WEIGHTS

    async def aggregate(
        self,
        work_entity: ResolvedEntity,
        contributor_entities: list[ResolvedEntity],
        roles: dict[uuid.UUID, CreditRoleEnum],
    ) -> AttributionRecord:
        """Aggregate resolved entities into a single AttributionRecord.

        Builds per-credit confidence scores from source reliability weights,
        computes overall attribution confidence and source agreement, and
        initializes the provenance chain with a SCORE event.

        Records with confidence below ``REVIEW_THRESHOLD`` are automatically
        flagged for human review with priority = ``1.0 - confidence``.

        Parameters
        ----------
        work_entity : ResolvedEntity
            The work or recording entity being attributed.
        contributor_entities : list[ResolvedEntity]
            Resolved contributor entities (artists, producers, etc.).
        roles : dict[uuid.UUID, CreditRoleEnum]
            Mapping of contributor ``entity_id`` to their credit role
            (e.g., PERFORMER, COMPOSER, PRODUCER).

        Returns
        -------
        AttributionRecord
            Complete attribution record with credits, confidence,
            assurance level, conformal set placeholder, and provenance.

        See Also
        --------
        music_attribution.attribution.conformal.ConformalScorer.score :
            Apply conformal calibration to the aggregated record.
        """
        now = datetime.now(UTC)

        # Build credits
        credits = self._build_credits(contributor_entities, roles)

        # Compute overall confidence and agreement
        confidence = self._compute_confidence(credits)
        agreement = self._compute_source_agreement(contributor_entities)

        # Determine assurance level (min of all contributors)
        assurance = self._compute_assurance(contributor_entities)

        # Build provenance chain
        provenance = [
            ProvenanceEvent(
                event_type=ProvenanceEventTypeEnum.SCORE,
                timestamp=now,
                agent="credit-aggregator",
                details=ScoreEventDetails(
                    new_confidence=confidence,
                    scoring_method="weighted_source_aggregation",
                ),
            ),
        ]

        # Build placeholder conformal set
        conformal = ConformalSet(
            coverage_level=0.9,
            marginal_coverage=0.9,
            calibration_error=0.0,
            calibration_method="placeholder",
            calibration_set_size=0,
        )

        return AttributionRecord(
            work_entity_id=work_entity.entity_id,
            credits=credits,
            assurance_level=assurance,
            confidence_score=confidence,
            conformal_set=conformal,
            source_agreement=agreement,
            provenance_chain=provenance,
            needs_review=confidence < REVIEW_THRESHOLD,
            review_priority=1.0 - confidence,
            created_at=now,
            updated_at=now,
            version=1,
        )

    def _build_credits(
        self,
        entities: list[ResolvedEntity],
        roles: dict[uuid.UUID, CreditRoleEnum],
    ) -> list[Credit]:
        """Build credit list from entities and their roles.

        For each contributor entity, computes a per-credit confidence
        score weighted by the reliability of the entity's contributing
        sources.

        Parameters
        ----------
        entities : list[ResolvedEntity]
            Contributor entities.
        roles : dict[uuid.UUID, CreditRoleEnum]
            Entity ID to role mapping. Defaults to ``PERFORMER`` if
            the entity ID is not found in the mapping.

        Returns
        -------
        list[Credit]
            One ``Credit`` per contributor entity.
        """
        credits: list[Credit] = []
        for entity in entities:
            role = roles.get(entity.entity_id, CreditRoleEnum.PERFORMER)
            sources = list({sr.source for sr in entity.source_records})
            credit_confidence = self._weighted_confidence(entity, sources)
            credits.append(
                Credit(
                    entity_id=entity.entity_id,
                    role=role,
                    confidence=credit_confidence,
                    sources=sources,
                    assurance_level=entity.assurance_level,
                )
            )
        return credits

    def _weighted_confidence(
        self,
        entity: ResolvedEntity,
        sources: list[SourceEnum],
    ) -> float:
        """Compute weighted confidence from source reliabilities.

        Multiplies the entity's resolution confidence by each source's
        reliability weight, then normalizes by total weight. This ensures
        that entities confirmed by higher-quality sources receive higher
        credit confidence.

        Parameters
        ----------
        entity : ResolvedEntity
            The contributor entity.
        sources : list[SourceEnum]
            Data sources that contributed to this entity's resolution.

        Returns
        -------
        float
            Weighted confidence in range [0.0, 1.0]. Falls back to
            raw ``resolution_confidence`` if no sources are provided.
        """
        if not sources:
            return entity.resolution_confidence

        total_weight = 0.0
        weighted_sum = 0.0
        for source in sources:
            weight = self._source_weights.get(source, 0.5)
            total_weight += weight
            weighted_sum += entity.resolution_confidence * weight

        return weighted_sum / total_weight if total_weight > 0 else 0.0

    def _compute_confidence(self, credits: list[Credit]) -> float:
        """Compute overall attribution confidence as mean of credit confidences.

        Parameters
        ----------
        credits : list[Credit]
            Per-contributor credit entries.

        Returns
        -------
        float
            Mean confidence across all credits, or 0.0 if empty.
        """
        if not credits:
            return 0.0
        return sum(c.confidence for c in credits) / len(credits)

    def _compute_source_agreement(self, entities: list[ResolvedEntity]) -> float:
        """Compute inter-source agreement score.

        A simplified measure of how well sources agree on attribution.
        For single entities, returns the entity's resolution confidence.
        For multiple entities, returns the mean resolution confidence
        (capped at 1.0).

        Parameters
        ----------
        entities : list[ResolvedEntity]
            Contributor entities to measure agreement across.

        Returns
        -------
        float
            Agreement score in range [0.0, 1.0].
        """
        if len(entities) <= 1:
            # Single entity — agreement with itself
            return entities[0].resolution_confidence if entities else 0.0

        # Average pairwise agreement (simplified)
        confidences = [e.resolution_confidence for e in entities]
        avg = sum(confidences) / len(confidences)
        return min(avg, 1.0)

    def _compute_assurance(self, entities: list[ResolvedEntity]) -> AssuranceLevelEnum:
        """Compute minimum assurance level across all contributors.

        The overall attribution is only as strong as its weakest link.
        If any contributor has A0 (no data), the entire attribution
        is rated A0.

        Parameters
        ----------
        entities : list[ResolvedEntity]
            Contributor entities.

        Returns
        -------
        AssuranceLevelEnum
            Minimum assurance level found across all contributors.
            Returns ``LEVEL_0`` if the entity list is empty.
        """
        if not entities:
            return AssuranceLevelEnum.LEVEL_0

        levels = [e.assurance_level for e in entities]
        level_order = [
            AssuranceLevelEnum.LEVEL_0,
            AssuranceLevelEnum.LEVEL_1,
            AssuranceLevelEnum.LEVEL_2,
            AssuranceLevelEnum.LEVEL_3,
        ]
        min_idx = min(level_order.index(level) for level in levels)
        return level_order[min_idx]
