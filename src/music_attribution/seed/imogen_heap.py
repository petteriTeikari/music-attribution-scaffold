"""Seed data loader: Imogen Heap mock attribution data → PostgreSQL.

Ports the 8 Imogen Heap attribution records from the frontend mock data
(frontend/src/lib/data/mock-works.ts) into Pydantic objects, then stores
them via the async attribution repository.

Uses deterministic UUIDs (uuid5) for idempotent seeding.
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.attribution.persistence import AsyncAttributionRepository
from music_attribution.db.models import AttributionRecordModel
from music_attribution.schemas.attribution import (
    AttributionRecord,
    ConformalSet,
    Credit,
    FetchEventDetails,
    ProvenanceEvent,
    ResolveEventDetails,
    ReviewEventDetails,
    ScoreEventDetails,
)
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
    ProvenanceEventTypeEnum,
    SourceEnum,
)

logger = logging.getLogger(__name__)

# Namespace UUID for deterministic seed IDs
_SEED_NAMESPACE = uuid.UUID("a1b2c3d4-e5f6-7890-abcd-ef1234567890")


def deterministic_uuid(key: str) -> uuid.UUID:
    """Generate a deterministic UUID from a string key."""
    return uuid.uuid5(_SEED_NAMESPACE, key)


def _dt(iso: str) -> datetime:
    """Parse ISO datetime string to timezone-aware datetime."""
    return datetime.fromisoformat(iso).replace(tzinfo=UTC)


def _build_works() -> list[AttributionRecord]:
    """Build the 8 Imogen Heap attribution records."""
    ih = deterministic_uuid("artist-imogen-heap")
    gs = deterministic_uuid("artist-guy-sigsworth")

    return [
        # 1. Hide and Seek — 0.95
        AttributionRecord(
            attribution_id=deterministic_uuid("work-001"),
            work_entity_id=deterministic_uuid("work-hide-and-seek"),
            credits=[
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PERFORMER,
                    role_detail="Lead vocals, vocoder arrangement",
                    confidence=0.99,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS, SourceEnum.ACOUSTID, SourceEnum.ARTIST_INPUT],
                    assurance_level=AssuranceLevelEnum.LEVEL_3,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.SONGWRITER,
                    role_detail="Sole songwriter",
                    confidence=0.98,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS, SourceEnum.ARTIST_INPUT],
                    assurance_level=AssuranceLevelEnum.LEVEL_3,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PRODUCER,
                    role_detail="Co-producer",
                    confidence=0.92,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS, SourceEnum.ARTIST_INPUT],
                    assurance_level=AssuranceLevelEnum.LEVEL_3,
                ),
                Credit(
                    entity_id=gs,
                    role=CreditRoleEnum.PRODUCER,
                    role_detail="Co-producer",
                    confidence=0.91,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
                    assurance_level=AssuranceLevelEnum.LEVEL_2,
                ),
            ],
            assurance_level=AssuranceLevelEnum.LEVEL_3,
            confidence_score=0.95,
            conformal_set=ConformalSet(
                coverage_level=0.9,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=0.92,
                calibration_error=0.018,
                calibration_method="temperature_scaling",
                calibration_set_size=1200,
            ),
            source_agreement=0.94,
            provenance_chain=[
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2024-06-15T10:00:00Z"),
                    agent="etl-musicbrainz-v2",
                    details=FetchEventDetails(
                        source=SourceEnum.MUSICBRAINZ,
                        source_id="mb-rec-hide-and-seek",
                        records_fetched=4,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.RESOLVE,
                    timestamp=_dt("2024-06-15T10:05:00Z"),
                    agent="resolution-orchestrator-v1",
                    details=ResolveEventDetails(
                        method="splink_linkage", records_input=12, entities_output=4, confidence_range=(0.78, 0.99)
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-06-15T10:10:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=None, new_confidence=0.3, scoring_method="weighted_source_agreement"
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-07-01T14:30:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=0.3, new_confidence=0.6, scoring_method="conformal_prediction"
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.REVIEW,
                    timestamp=_dt("2024-08-10T09:00:00Z"),
                    agent="human-reviewer-musicologist",
                    details=ReviewEventDetails(
                        reviewer_id="reviewer-m-001",
                        feedback_card_id=deterministic_uuid("fb-hide-seek-001"),
                        corrections_applied=0,
                    ),
                    feedback_card_id=deterministic_uuid("fb-hide-seek-001"),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-08-10T09:15:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=0.6, new_confidence=0.95, scoring_method="bayesian_update_post_review"
                    ),
                ),
            ],
            needs_review=False,
            review_priority=0.05,
            created_at=_dt("2024-06-15T10:00:00Z"),
            updated_at=_dt("2024-08-10T09:15:00Z"),
            version=4,
        ),
        # 2. Tiny Human — 0.91
        AttributionRecord(
            attribution_id=deterministic_uuid("work-002"),
            work_entity_id=deterministic_uuid("work-tiny-human"),
            credits=[
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PERFORMER,
                    role_detail="Vocals, all instruments",
                    confidence=0.97,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS, SourceEnum.ARTIST_INPUT],
                    assurance_level=AssuranceLevelEnum.LEVEL_3,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.SONGWRITER,
                    role_detail="Sole songwriter",
                    confidence=0.96,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS, SourceEnum.ARTIST_INPUT],
                    assurance_level=AssuranceLevelEnum.LEVEL_3,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PRODUCER,
                    role_detail="Self-produced, artist-confirmed",
                    confidence=0.95,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.ARTIST_INPUT],
                    assurance_level=AssuranceLevelEnum.LEVEL_3,
                ),
            ],
            assurance_level=AssuranceLevelEnum.LEVEL_3,
            confidence_score=0.91,
            conformal_set=ConformalSet(
                coverage_level=0.9,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=0.91,
                calibration_error=0.022,
                calibration_method="temperature_scaling",
                calibration_set_size=980,
            ),
            source_agreement=0.92,
            provenance_chain=[
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2024-07-20T11:00:00Z"),
                    agent="etl-musicbrainz-v2",
                    details=FetchEventDetails(
                        source=SourceEnum.MUSICBRAINZ,
                        source_id="mb-rec-tiny-human",
                        records_fetched=3,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.RESOLVE,
                    timestamp=_dt("2024-07-20T11:05:00Z"),
                    agent="resolution-orchestrator-v1",
                    details=ResolveEventDetails(
                        method="exact_id_match", records_input=8, entities_output=3, confidence_range=(0.88, 0.97)
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-07-20T11:10:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=None, new_confidence=0.82, scoring_method="weighted_source_agreement"
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.REVIEW,
                    timestamp=_dt("2024-08-05T16:00:00Z"),
                    agent="artist-self-review",
                    details=ReviewEventDetails(
                        reviewer_id="artist-imogen-heap",
                        feedback_card_id=deterministic_uuid("fb-tiny-human-001"),
                        corrections_applied=0,
                    ),
                    feedback_card_id=deterministic_uuid("fb-tiny-human-001"),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-08-05T16:05:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=0.82, new_confidence=0.91, scoring_method="bayesian_update_artist_confirmed"
                    ),
                ),
            ],
            needs_review=False,
            review_priority=0.09,
            created_at=_dt("2024-07-20T11:00:00Z"),
            updated_at=_dt("2024-08-05T16:05:00Z"),
            version=3,
        ),
        # 3. The Moment I Said It — 0.82
        AttributionRecord(
            attribution_id=deterministic_uuid("work-003"),
            work_entity_id=deterministic_uuid("work-the-moment-i-said-it"),
            credits=[
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PERFORMER,
                    role_detail="Vocals, piano, electronics",
                    confidence=0.95,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS, SourceEnum.FILE_METADATA],
                    assurance_level=AssuranceLevelEnum.LEVEL_2,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.SONGWRITER,
                    role_detail="Sole songwriter",
                    confidence=0.88,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
                    assurance_level=AssuranceLevelEnum.LEVEL_2,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PRODUCER,
                    confidence=0.78,
                    sources=[SourceEnum.MUSICBRAINZ],
                    assurance_level=AssuranceLevelEnum.LEVEL_2,
                ),
            ],
            assurance_level=AssuranceLevelEnum.LEVEL_2,
            confidence_score=0.82,
            conformal_set=ConformalSet(
                coverage_level=0.9,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=0.88,
                calibration_error=0.035,
                calibration_method="platt_scaling",
                calibration_set_size=750,
            ),
            source_agreement=0.81,
            provenance_chain=[
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2024-09-01T08:00:00Z"),
                    agent="etl-musicbrainz-v2",
                    details=FetchEventDetails(
                        source=SourceEnum.MUSICBRAINZ,
                        source_id="mb-rec-moment-i-said-it",
                        records_fetched=3,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.RESOLVE,
                    timestamp=_dt("2024-09-01T08:10:00Z"),
                    agent="resolution-orchestrator-v1",
                    details=ResolveEventDetails(
                        method="fuzzy_string_match", records_input=9, entities_output=3, confidence_range=(0.72, 0.95)
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-09-01T08:15:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=None, new_confidence=0.75, scoring_method="weighted_source_agreement"
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-10-15T12:00:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=0.75, new_confidence=0.82, scoring_method="conformal_prediction"
                    ),
                ),
            ],
            needs_review=False,
            review_priority=0.18,
            created_at=_dt("2024-09-01T08:00:00Z"),
            updated_at=_dt("2024-10-15T12:00:00Z"),
            version=2,
        ),
        # 4. Goodnight and Go — 0.72
        AttributionRecord(
            attribution_id=deterministic_uuid("work-004"),
            work_entity_id=deterministic_uuid("work-goodnight-and-go"),
            credits=[
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PERFORMER,
                    role_detail="Vocals, keyboards",
                    confidence=0.90,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
                    assurance_level=AssuranceLevelEnum.LEVEL_2,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.SONGWRITER,
                    confidence=0.85,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
                    assurance_level=AssuranceLevelEnum.LEVEL_2,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PRODUCER,
                    role_detail="Partial credits, some sources list co-producer",
                    confidence=0.62,
                    sources=[SourceEnum.DISCOGS],
                    assurance_level=AssuranceLevelEnum.LEVEL_1,
                ),
            ],
            assurance_level=AssuranceLevelEnum.LEVEL_2,
            confidence_score=0.72,
            conformal_set=ConformalSet(
                coverage_level=0.9,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=0.85,
                calibration_error=0.048,
                calibration_method="platt_scaling",
                calibration_set_size=620,
            ),
            source_agreement=0.71,
            provenance_chain=[
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2024-09-10T14:00:00Z"),
                    agent="etl-discogs-v1",
                    details=FetchEventDetails(
                        source=SourceEnum.DISCOGS,
                        source_id="discogs-rel-goodnight-go",
                        records_fetched=2,
                        rate_limited=True,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.RESOLVE,
                    timestamp=_dt("2024-09-10T14:15:00Z"),
                    agent="resolution-orchestrator-v1",
                    details=ResolveEventDetails(
                        method="fuzzy_string_match", records_input=6, entities_output=3, confidence_range=(0.58, 0.90)
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-09-10T14:20:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=None, new_confidence=0.72, scoring_method="weighted_source_agreement"
                    ),
                ),
            ],
            needs_review=False,
            review_priority=0.28,
            created_at=_dt("2024-09-10T14:00:00Z"),
            updated_at=_dt("2024-09-10T14:20:00Z"),
            version=1,
        ),
        # 5. Headlock — 0.58
        AttributionRecord(
            attribution_id=deterministic_uuid("work-005"),
            work_entity_id=deterministic_uuid("work-headlock"),
            credits=[
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PERFORMER,
                    role_detail="Vocals, guitar",
                    confidence=0.88,
                    sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
                    assurance_level=AssuranceLevelEnum.LEVEL_2,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.SONGWRITER,
                    confidence=0.80,
                    sources=[SourceEnum.MUSICBRAINZ],
                    assurance_level=AssuranceLevelEnum.LEVEL_1,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PRODUCER,
                    role_detail="Conflicting: MusicBrainz lists self-produced, Discogs lists Guy Sigsworth",
                    confidence=0.45,
                    sources=[SourceEnum.MUSICBRAINZ],
                    assurance_level=AssuranceLevelEnum.LEVEL_1,
                ),
                Credit(
                    entity_id=gs,
                    role=CreditRoleEnum.PRODUCER,
                    role_detail="Conflicting: listed as producer on Discogs only",
                    confidence=0.42,
                    sources=[SourceEnum.DISCOGS],
                    assurance_level=AssuranceLevelEnum.LEVEL_1,
                ),
            ],
            assurance_level=AssuranceLevelEnum.LEVEL_1,
            confidence_score=0.58,
            conformal_set=ConformalSet(
                coverage_level=0.9,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=0.78,
                calibration_error=0.072,
                calibration_method="platt_scaling",
                calibration_set_size=480,
            ),
            source_agreement=0.55,
            provenance_chain=[
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2024-10-01T09:00:00Z"),
                    agent="etl-musicbrainz-v2",
                    details=FetchEventDetails(
                        source=SourceEnum.MUSICBRAINZ,
                        source_id="mb-rec-headlock",
                        records_fetched=3,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2024-10-01T09:02:00Z"),
                    agent="etl-discogs-v1",
                    details=FetchEventDetails(
                        source=SourceEnum.DISCOGS,
                        source_id="discogs-rel-headlock",
                        records_fetched=2,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.RESOLVE,
                    timestamp=_dt("2024-10-01T09:10:00Z"),
                    agent="resolution-orchestrator-v1",
                    details=ResolveEventDetails(
                        method="splink_linkage", records_input=10, entities_output=4, confidence_range=(0.40, 0.88)
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-10-01T09:15:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=None, new_confidence=0.58, scoring_method="weighted_source_agreement"
                    ),
                ),
            ],
            needs_review=True,
            review_priority=0.42,
            created_at=_dt("2024-10-01T09:00:00Z"),
            updated_at=_dt("2024-10-01T09:15:00Z"),
            version=1,
        ),
        # 6. Just for Now — 0.35
        AttributionRecord(
            attribution_id=deterministic_uuid("work-006"),
            work_entity_id=deterministic_uuid("work-just-for-now"),
            credits=[
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PERFORMER,
                    role_detail="Vocals, multi-tracked layers",
                    confidence=0.70,
                    sources=[SourceEnum.MUSICBRAINZ],
                    assurance_level=AssuranceLevelEnum.LEVEL_1,
                ),
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.SONGWRITER,
                    confidence=0.55,
                    sources=[SourceEnum.MUSICBRAINZ],
                    assurance_level=AssuranceLevelEnum.LEVEL_1,
                ),
            ],
            assurance_level=AssuranceLevelEnum.LEVEL_1,
            confidence_score=0.35,
            conformal_set=ConformalSet(
                coverage_level=0.9,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=0.72,
                calibration_error=0.11,
                calibration_method="histogram_binning",
                calibration_set_size=320,
            ),
            source_agreement=0.33,
            provenance_chain=[
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2024-11-05T16:00:00Z"),
                    agent="etl-musicbrainz-v2",
                    details=FetchEventDetails(
                        source=SourceEnum.MUSICBRAINZ,
                        source_id="mb-rec-just-for-now",
                        records_fetched=2,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.RESOLVE,
                    timestamp=_dt("2024-11-05T16:05:00Z"),
                    agent="resolution-orchestrator-v1",
                    details=ResolveEventDetails(
                        method="exact_id_match", records_input=3, entities_output=2, confidence_range=(0.50, 0.70)
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2024-11-05T16:10:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=None, new_confidence=0.35, scoring_method="single_source_penalty"
                    ),
                ),
            ],
            needs_review=True,
            review_priority=0.65,
            created_at=_dt("2024-11-05T16:00:00Z"),
            updated_at=_dt("2024-11-05T16:10:00Z"),
            version=1,
        ),
        # 7. 2-1 — 0.28
        AttributionRecord(
            attribution_id=deterministic_uuid("work-007"),
            work_entity_id=deterministic_uuid("work-2-1"),
            credits=[
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PERFORMER,
                    role_detail="Extracted from ID3 artist tag",
                    confidence=0.55,
                    sources=[SourceEnum.FILE_METADATA],
                    assurance_level=AssuranceLevelEnum.LEVEL_1,
                ),
            ],
            assurance_level=AssuranceLevelEnum.LEVEL_1,
            confidence_score=0.28,
            conformal_set=ConformalSet(
                coverage_level=0.9,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=0.65,
                calibration_error=0.14,
                calibration_method="histogram_binning",
                calibration_set_size=200,
            ),
            source_agreement=0.2,
            provenance_chain=[
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2025-01-10T20:00:00Z"),
                    agent="etl-file-metadata-v1",
                    details=FetchEventDetails(
                        source=SourceEnum.FILE_METADATA,
                        source_id="file-2-1-flac",
                        records_fetched=1,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.RESOLVE,
                    timestamp=_dt("2025-01-10T20:02:00Z"),
                    agent="resolution-orchestrator-v1",
                    details=ResolveEventDetails(
                        method="fuzzy_string_match", records_input=1, entities_output=1, confidence_range=(0.55, 0.55)
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2025-01-10T20:05:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=None, new_confidence=0.28, scoring_method="single_source_penalty"
                    ),
                ),
            ],
            needs_review=True,
            review_priority=0.72,
            created_at=_dt("2025-01-10T20:00:00Z"),
            updated_at=_dt("2025-01-10T20:05:00Z"),
            version=1,
        ),
        # 8. Blanket (unreleased) — 0.0
        AttributionRecord(
            attribution_id=deterministic_uuid("work-008"),
            work_entity_id=deterministic_uuid("work-blanket"),
            credits=[
                Credit(
                    entity_id=ih,
                    role=CreditRoleEnum.PERFORMER,
                    role_detail="Claimed by artist, no external verification",
                    confidence=0.1,
                    sources=[],
                    assurance_level=AssuranceLevelEnum.LEVEL_0,
                ),
            ],
            assurance_level=AssuranceLevelEnum.LEVEL_0,
            confidence_score=0.0,
            conformal_set=ConformalSet(
                coverage_level=0.9,
                prediction_sets={},
                set_sizes={},
                marginal_coverage=0.5,
                calibration_error=0.25,
                calibration_method="none",
                calibration_set_size=0,
            ),
            source_agreement=0.0,
            provenance_chain=[
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2025-02-01T10:00:00Z"),
                    agent="etl-musicbrainz-v2",
                    details=FetchEventDetails(
                        source=SourceEnum.MUSICBRAINZ,
                        source_id="mb-query-blanket-imogen-heap",
                        records_fetched=0,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.FETCH,
                    timestamp=_dt("2025-02-01T10:01:00Z"),
                    agent="etl-discogs-v1",
                    details=FetchEventDetails(
                        source=SourceEnum.DISCOGS,
                        source_id="discogs-query-blanket-imogen-heap",
                        records_fetched=0,
                        rate_limited=False,
                    ),
                ),
                ProvenanceEvent(
                    event_type=ProvenanceEventTypeEnum.SCORE,
                    timestamp=_dt("2025-02-01T10:05:00Z"),
                    agent="attribution-aggregator-v1",
                    details=ScoreEventDetails(
                        previous_confidence=None, new_confidence=0.0, scoring_method="no_data_fallback"
                    ),
                ),
            ],
            needs_review=True,
            review_priority=1.0,
            created_at=_dt("2025-02-01T10:00:00Z"),
            updated_at=_dt("2025-02-01T10:05:00Z"),
            version=1,
        ),
    ]


async def seed_imogen_heap(session: AsyncSession) -> None:
    """Seed the database with 8 Imogen Heap attribution records.

    Uses upsert semantics — safe to call multiple times.

    Args:
        session: Active async database session.
    """
    repo = AsyncAttributionRepository()
    works = _build_works()

    for work in works:
        # Check if already exists (idempotent)
        existing = await session.execute(
            select(AttributionRecordModel).where(
                AttributionRecordModel.attribution_id == work.attribution_id,
            )
        )
        if existing.scalar_one_or_none() is None:
            await repo.store(work, session)

    await session.flush()
    logger.info("Seeded %d Imogen Heap attribution records", len(works))
