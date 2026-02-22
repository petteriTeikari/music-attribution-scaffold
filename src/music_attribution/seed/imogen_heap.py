"""Seed data loader: Imogen Heap mock attribution data to PostgreSQL.

Ports the 8 Imogen Heap attribution records from the frontend mock data
(``frontend/src/lib/data/mock-works.ts``) into fully-populated Pydantic
``AttributionRecord`` objects with credits, provenance chains, conformal
prediction sets, and uncertainty metadata. Records are then persisted
via the async attribution repository.

The 8 records span the full confidence range (0.0--0.95) and
assurance levels (A0--A3), providing a representative dataset for
development, demonstration, and testing:

1. Hide and Seek -- 0.95 (A3, 4 sources, reviewed by musicologist)
2. Tiny Human -- 0.91 (A3, artist self-confirmed)
3. The Moment I Said It -- 0.82 (A2, 3 sources)
4. Goodnight and Go -- 0.72 (A2, 2 sources, rate-limited fetch)
5. Headlock -- 0.58 (A1, conflicting producer credits)
6. Just for Now -- 0.35 (A1, single source penalty)
7. 2-1 -- 0.28 (A1, file metadata only)
8. Blanket (unreleased) -- 0.0 (A0, no external verification)

All UUIDs are deterministic (``uuid5`` with a fixed namespace) to
ensure idempotent seeding -- running the loader multiple times produces
identical records.

Functions
---------
deterministic_uuid
    Generate a deterministic UUID from a string key.
build_imogen_heap_records
    Build the 8 records as Pydantic objects (public API).
seed_imogen_heap
    Persist the records to the database via ``AsyncAttributionRepository``.

See Also
--------
music_attribution.schemas.attribution : AttributionRecord schema.
music_attribution.schemas.uncertainty : UncertaintyAwareProvenance.
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.attribution.persistence import AsyncAttributionRepository
from music_attribution.constants import CONFIDENCE_HIGH_THRESHOLD, CONFIDENCE_MEDIUM_THRESHOLD
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
    CalibrationStatusEnum,
    ConfidenceMethodEnum,
    CreditRoleEnum,
    ProvenanceEventTypeEnum,
    SourceEnum,
    UncertaintySourceEnum,
)
from music_attribution.schemas.uncertainty import (
    CalibrationMetadata,
    SourceContribution,
    StepUncertainty,
    UncertaintyAwareProvenance,
)

logger = logging.getLogger(__name__)

# Namespace UUID for deterministic seed IDs
_SEED_NAMESPACE = uuid.UUID("a1b2c3d4-e5f6-7890-abcd-ef1234567890")


def deterministic_uuid(key: str) -> uuid.UUID:
    """Generate a deterministic UUID from a string key.

    Uses ``uuid5`` with a fixed namespace UUID to produce the same
    UUID for the same key on every invocation. This ensures idempotent
    seeding -- records have stable IDs across environments.

    Parameters
    ----------
    key : str
        String key to hash (e.g. ``"work-001"``, ``"artist-imogen-heap"``).

    Returns
    -------
    uuid.UUID
        Deterministic UUIDv5.
    """
    return uuid.uuid5(_SEED_NAMESPACE, key)


def _dt(iso: str) -> datetime:
    """Parse an ISO datetime string to a timezone-aware UTC datetime.

    Parameters
    ----------
    iso : str
        ISO 8601 datetime string (e.g. ``"2024-06-15T10:00:00Z"``).

    Returns
    -------
    datetime
        Parsed datetime with UTC timezone attached.
    """
    return datetime.fromisoformat(iso).replace(tzinfo=UTC)


def _build_uncertainty_for_record(record: AttributionRecord) -> UncertaintyAwareProvenance:
    """Build mock uncertainty metadata for a single attribution record.

    Generates coherent uncertainty values derived from the record's
    confidence score and credit sources. The mapping follows the
    uncertainty decomposition framework from the manuscript:

    - **High confidence (>= 0.85)**: Low total uncertainty, aleatoric
      dominant, calibrated.
    - **Medium confidence (0.50--0.84)**: Moderate uncertainty, extrinsic
      dominant, calibrated.
    - **Low confidence (0.20--0.49)**: High uncertainty, epistemic
      dominant, pending calibration.
    - **Very low confidence (< 0.20)**: Very high uncertainty, epistemic
      dominant, uncalibrated.

    Step uncertainties are derived from the provenance chain events,
    and source contributions are derived from the credit sources.

    Parameters
    ----------
    record : AttributionRecord
        Attribution record to generate uncertainty metadata for.

    Returns
    -------
    UncertaintyAwareProvenance
        Complete uncertainty metadata including per-step uncertainties,
        source contributions, calibration metadata, and the dominant
        uncertainty source.
    """
    confidence = record.confidence_score
    credit_sources: set[SourceEnum] = set()
    for credit in record.credits:
        credit_sources.update(credit.sources)

    # Derive uncertainty from confidence level
    if confidence >= CONFIDENCE_HIGH_THRESHOLD:
        intrinsic = 0.02
        extrinsic = 0.04
        total = 0.06
        dominant = UncertaintySourceEnum.ALEATORIC
        cal_status = CalibrationStatusEnum.CALIBRATED
        cal_ece = 0.02
    elif confidence >= CONFIDENCE_MEDIUM_THRESHOLD:
        intrinsic = 0.08
        extrinsic = 0.15
        total = 0.23
        dominant = UncertaintySourceEnum.EXTRINSIC
        cal_status = CalibrationStatusEnum.CALIBRATED
        cal_ece = 0.05
    elif confidence >= 0.20:
        intrinsic = 0.15
        extrinsic = 0.30
        total = 0.45
        dominant = UncertaintySourceEnum.EPISTEMIC
        cal_status = CalibrationStatusEnum.PENDING
        cal_ece = 0.12
    else:
        intrinsic = 0.25
        extrinsic = 0.50
        total = 0.75
        dominant = UncertaintySourceEnum.EPISTEMIC
        cal_status = CalibrationStatusEnum.UNCALIBRATED
        cal_ece = 0.25

    # Build step uncertainties from provenance chain
    steps = []
    for i, event in enumerate(record.provenance_chain):
        step_conf = confidence * (0.5 + 0.5 * (i / max(len(record.provenance_chain) - 1, 1)))
        steps.append(
            StepUncertainty(
                step_id=f"{event.agent}-step-{i}",
                step_name=f"{event.event_type.value} by {event.agent}",
                step_index=i,
                stated_confidence=min(step_conf + 0.05, 1.0),
                calibrated_confidence=min(step_conf, 1.0),
                intrinsic_uncertainty=intrinsic,
                extrinsic_uncertainty=extrinsic * (1 - i / max(len(record.provenance_chain), 1)),
                total_uncertainty=total * (1 - 0.3 * i / max(len(record.provenance_chain), 1)),
                confidence_method=ConfidenceMethodEnum.SOURCE_WEIGHTED,
                preceding_step_ids=[f"{record.provenance_chain[j].agent}-step-{j}" for j in range(i)],
            )
        )

    # Build source contributions from credit sources
    source_weights = {
        SourceEnum.MUSICBRAINZ: (0.90, 0.88, False),
        SourceEnum.DISCOGS: (0.82, 0.80, False),
        SourceEnum.ACOUSTID: (0.75, 0.70, False),
        SourceEnum.ARTIST_INPUT: (0.95, 0.92, True),
        SourceEnum.FILE_METADATA: (0.60, 0.55, False),
    }
    contributions = []
    n_sources = max(len(credit_sources), 1)
    for source in sorted(credit_sources, key=lambda s: s.value):
        conf, cal_q, is_human = source_weights.get(source, (0.70, 0.65, False))
        contributions.append(
            SourceContribution(
                source=source,
                confidence=conf * min(confidence + 0.3, 1.0),
                weight=round(1.0 / n_sources, 2),
                calibration_quality=cal_q,
                is_human=is_human,
            )
        )

    return UncertaintyAwareProvenance(
        steps=steps,
        source_contributions=contributions,
        calibration=CalibrationMetadata(
            expected_calibration_error=cal_ece,
            calibration_set_size=int(confidence * 1000),
            status=cal_status,
        ),
        total_uncertainty=total,
        dominant_uncertainty_source=dominant,
    )


def _add_citation_indexes(record: AttributionRecord) -> None:
    """Add sequential citation indexes to provenance events.

    Mutates the record's provenance chain in place, assigning a
    1-based ``citation_index`` to each event for use as footnote
    references in the frontend provenance timeline.

    Parameters
    ----------
    record : AttributionRecord
        Record whose provenance events will be annotated.
    """
    idx = 1
    for event in record.provenance_chain:
        event.citation_index = idx
        idx += 1


def _build_works() -> list[AttributionRecord]:
    """Build the 8 Imogen Heap attribution records with full metadata.

    Creates all records with credits, provenance chains, conformal
    prediction sets, then enriches them with uncertainty metadata,
    citation indexes, and entity display names.

    Returns
    -------
    list[AttributionRecord]
        8 fully-populated ``AttributionRecord`` objects ordered by
        descending confidence score.
    """
    ih = deterministic_uuid("artist-imogen-heap")
    gs = deterministic_uuid("artist-guy-sigsworth")

    # Entity name lookup for post-processing credits
    _entity_names: dict[uuid.UUID, str] = {
        ih: "Imogen Heap",
        gs: "Guy Sigsworth",
    }

    records = [
        # 1. Hide and Seek — 0.95
        AttributionRecord(
            attribution_id=deterministic_uuid("work-001"),
            work_entity_id=deterministic_uuid("work-hide-and-seek"),
            work_title="Hide and Seek",
            artist_name="Imogen Heap",
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
            work_title="Tiny Human",
            artist_name="Imogen Heap",
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
            work_title="The Moment I Said It",
            artist_name="Imogen Heap",
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
            work_title="Goodnight and Go",
            artist_name="Imogen Heap",
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
            work_title="Headlock",
            artist_name="Imogen Heap",
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
            work_title="Just for Now",
            artist_name="Imogen Heap",
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
            work_title="2-1",
            artist_name="Imogen Heap",
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
            work_title="Blanket",
            artist_name="Imogen Heap",
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

    # Enrich all records with uncertainty metadata, citation indexes, and entity names
    for rec in records:
        rec.uncertainty_summary = _build_uncertainty_for_record(rec)
        _add_citation_indexes(rec)
        # Populate entity_name on each credit from the lookup
        for credit in rec.credits:
            credit.entity_name = _entity_names.get(credit.entity_id, "Unknown")

    return records


def build_imogen_heap_records() -> list[AttributionRecord]:
    """Build the 8 Imogen Heap attribution records (public API).

    Convenience wrapper around ``_build_works()`` for external consumers.
    Records include all display fields (``work_title``, ``artist_name``,
    ``entity_name`` on each credit), full provenance chains with
    citation indexes, and uncertainty metadata.

    Returns
    -------
    list[AttributionRecord]
        List of 8 fully-populated ``AttributionRecord`` objects
        spanning confidence 0.0--0.95 and assurance levels A0--A3.
    """
    return _build_works()


async def seed_imogen_heap(session: AsyncSession) -> None:
    """Seed the database with 8 Imogen Heap attribution records.

    Uses check-then-insert semantics for idempotency -- existing
    records (matched by ``attribution_id``) are skipped. Safe to
    call multiple times without duplicating data.

    The session is flushed but not committed, allowing the caller
    to control transaction boundaries.

    Parameters
    ----------
    session : AsyncSession
        Active async database session. The caller is responsible
        for committing after this function returns.
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
