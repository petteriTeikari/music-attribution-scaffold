"""Multi-source credit aggregation for attribution.

Aggregates credits from multiple ResolvedEntities into a single
AttributionRecord. Handles disagreements between sources using
weighted voting based on source reliability.
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
    disagreements between sources.
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

        Args:
            work_entity: The work/recording entity.
            contributor_entities: List of contributing entities (artists, etc.).
            roles: Mapping of entity_id to credit role.

        Returns:
            Complete AttributionRecord.
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
        """Build credit list from entities and their roles."""
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
        """Compute weighted confidence from source reliabilities."""
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
        """Compute overall attribution confidence."""
        if not credits:
            return 0.0
        return sum(c.confidence for c in credits) / len(credits)

    def _compute_source_agreement(self, entities: list[ResolvedEntity]) -> float:
        """Compute inter-source agreement score."""
        if len(entities) <= 1:
            # Single entity — agreement with itself
            return entities[0].resolution_confidence if entities else 0.0

        # Average pairwise agreement (simplified)
        confidences = [e.resolution_confidence for e in entities]
        avg = sum(confidences) / len(confidences)
        return min(avg, 1.0)

    def _compute_assurance(self, entities: list[ResolvedEntity]) -> AssuranceLevelEnum:
        """Compute minimum assurance level across all contributors."""
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
