"""Shared enumerations for boundary object schemas.

All enums are StrEnum for JSON-friendly serialization. Domain-extensible
enums (EntityType, RelationshipType, PermissionType) can be extended via
domain overlay YAML in a future phase.
"""

from __future__ import annotations

from enum import StrEnum


class SourceEnum(StrEnum):
    """Data source identifiers."""

    MUSICBRAINZ = "MUSICBRAINZ"
    DISCOGS = "DISCOGS"
    ACOUSTID = "ACOUSTID"
    ARTIST_INPUT = "ARTIST_INPUT"
    FILE_METADATA = "FILE_METADATA"


class EntityTypeEnum(StrEnum):
    """Music entity types."""

    RECORDING = "RECORDING"
    WORK = "WORK"
    ARTIST = "ARTIST"
    RELEASE = "RELEASE"
    LABEL = "LABEL"
    CREDIT = "CREDIT"


class RelationshipTypeEnum(StrEnum):
    """Relationship types between entities."""

    PERFORMED = "PERFORMED"
    WROTE = "WROTE"
    PRODUCED = "PRODUCED"
    ENGINEERED = "ENGINEERED"
    ARRANGED = "ARRANGED"
    MASTERED = "MASTERED"
    MIXED = "MIXED"
    FEATURED = "FEATURED"
    SAMPLED = "SAMPLED"
    REMIXED = "REMIXED"


class ResolutionMethodEnum(StrEnum):
    """Entity resolution methods."""

    EXACT_ID = "EXACT_ID"
    FUZZY_STRING = "FUZZY_STRING"
    EMBEDDING = "EMBEDDING"
    GRAPH = "GRAPH"
    LLM = "LLM"
    MANUAL = "MANUAL"


class AssuranceLevelEnum(StrEnum):
    """A0-A3 assurance levels reflecting verification depth.

    Ordered by verification depth: LEVEL_0 < LEVEL_1 < LEVEL_2 < LEVEL_3.
    """

    LEVEL_0 = "LEVEL_0"
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_3 = "LEVEL_3"


class ConflictSeverityEnum(StrEnum):
    """Conflict severity levels between sources."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class CreditRoleEnum(StrEnum):
    """Credit roles for attribution."""

    PERFORMER = "PERFORMER"
    SONGWRITER = "SONGWRITER"
    COMPOSER = "COMPOSER"
    LYRICIST = "LYRICIST"
    PRODUCER = "PRODUCER"
    ENGINEER = "ENGINEER"
    MIXING_ENGINEER = "MIXING_ENGINEER"
    MASTERING_ENGINEER = "MASTERING_ENGINEER"
    ARRANGER = "ARRANGER"
    SESSION_MUSICIAN = "SESSION_MUSICIAN"
    FEATURED_ARTIST = "FEATURED_ARTIST"
    CONDUCTOR = "CONDUCTOR"
    DJ = "DJ"
    REMIXER = "REMIXER"


class ProvenanceEventTypeEnum(StrEnum):
    """Provenance event types for audit trail."""

    FETCH = "FETCH"
    RESOLVE = "RESOLVE"
    SCORE = "SCORE"
    REVIEW = "REVIEW"
    UPDATE = "UPDATE"
    FEEDBACK = "FEEDBACK"


class ReviewerRoleEnum(StrEnum):
    """Feedback reviewer roles."""

    ARTIST = "ARTIST"
    MANAGER = "MANAGER"
    MUSICOLOGIST = "MUSICOLOGIST"
    PRODUCER = "PRODUCER"
    FAN = "FAN"


class EvidenceTypeEnum(StrEnum):
    """Evidence types for feedback corrections."""

    LINER_NOTES = "LINER_NOTES"
    MEMORY = "MEMORY"
    DOCUMENT = "DOCUMENT"
    SESSION_NOTES = "SESSION_NOTES"
    OTHER = "OTHER"


class PermissionTypeEnum(StrEnum):
    """Permission types for the Permission Patchbay."""

    STREAM = "STREAM"
    DOWNLOAD = "DOWNLOAD"
    SYNC_LICENSE = "SYNC_LICENSE"
    AI_TRAINING = "AI_TRAINING"
    VOICE_CLONING = "VOICE_CLONING"
    STYLE_LEARNING = "STYLE_LEARNING"
    LYRICS_IN_CHATBOTS = "LYRICS_IN_CHATBOTS"
    COVER_VERSIONS = "COVER_VERSIONS"
    REMIX = "REMIX"
    SAMPLE = "SAMPLE"
    DERIVATIVE_WORK = "DERIVATIVE_WORK"


class PermissionValueEnum(StrEnum):
    """Permission values."""

    ALLOW = "ALLOW"
    DENY = "DENY"
    ASK = "ASK"
    ALLOW_WITH_ATTRIBUTION = "ALLOW_WITH_ATTRIBUTION"
    ALLOW_WITH_ROYALTY = "ALLOW_WITH_ROYALTY"


class PermissionScopeEnum(StrEnum):
    """Permission scope levels."""

    CATALOG = "CATALOG"
    RELEASE = "RELEASE"
    RECORDING = "RECORDING"
    WORK = "WORK"


class DelegationRoleEnum(StrEnum):
    """Delegation chain roles."""

    OWNER = "OWNER"
    MANAGER = "MANAGER"
    LABEL = "LABEL"
    DISTRIBUTOR = "DISTRIBUTOR"


class PipelineFeedbackTypeEnum(StrEnum):
    """Pipeline feedback signal types for continuous improvement."""

    REFETCH = "REFETCH"
    RECALIBRATE = "RECALIBRATE"
    DISPUTE = "DISPUTE"
    STALE = "STALE"
