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
    AI_TRAINING_COMPOSITION = "AI_TRAINING_COMPOSITION"
    AI_TRAINING_RECORDING = "AI_TRAINING_RECORDING"
    AI_TRAINING_STYLE = "AI_TRAINING_STYLE"
    DATASET_INCLUSION = "DATASET_INCLUSION"
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


class UncertaintySourceEnum(StrEnum):
    """Uncertainty source taxonomy (UProp, Duan 2025)."""

    INTRINSIC = "INTRINSIC"
    EXTRINSIC = "EXTRINSIC"
    ALEATORIC = "ALEATORIC"
    EPISTEMIC = "EPISTEMIC"


class UncertaintyDimensionEnum(StrEnum):
    """4-dimensional uncertainty framework (Liu 2025, arXiv:2503.15850)."""

    INPUT = "INPUT"
    REASONING = "REASONING"
    PARAMETER = "PARAMETER"
    PREDICTION = "PREDICTION"


class ConfidenceMethodEnum(StrEnum):
    """Methods used to produce confidence scores."""

    SELF_REPORT = "SELF_REPORT"
    MULTI_SAMPLE = "MULTI_SAMPLE"
    LOGPROB = "LOGPROB"
    ENSEMBLE = "ENSEMBLE"
    CONFORMAL = "CONFORMAL"
    SOURCE_WEIGHTED = "SOURCE_WEIGHTED"
    HUMAN_RATED = "HUMAN_RATED"
    HTC = "HTC"


class CalibrationStatusEnum(StrEnum):
    """Calibration status of a confidence score."""

    CALIBRATED = "CALIBRATED"
    UNCALIBRATED = "UNCALIBRATED"
    PENDING = "PENDING"


class ConfidenceTrendEnum(StrEnum):
    """Confidence trend across pipeline steps (Zhang 2026)."""

    INCREASING = "INCREASING"
    DECREASING = "DECREASING"
    STABLE = "STABLE"
    VOLATILE = "VOLATILE"


# --- Commercial Landscape Enums (future-readiness stubs) ---


class AttributionMethodEnum(StrEnum):
    """Training data attribution methods (Musical AI, Sureel, Sony)."""

    TRAINING_TIME_INFLUENCE = "TRAINING_TIME_INFLUENCE"
    UNLEARNING_BASED = "UNLEARNING_BASED"
    INFLUENCE_FUNCTIONS = "INFLUENCE_FUNCTIONS"
    EMBEDDING_SIMILARITY = "EMBEDDING_SIMILARITY"
    WATERMARK_DETECTION = "WATERMARK_DETECTION"
    INFERENCE_TIME_CONDITIONING = "INFERENCE_TIME_CONDITIONING"


class RightsTypeEnum(StrEnum):
    """Compositional vs recording rights (Sureel patent, LANDR)."""

    MASTER_RECORDING = "MASTER_RECORDING"
    COMPOSITION_PUBLISHING = "COMPOSITION_PUBLISHING"
    PERFORMANCE = "PERFORMANCE"
    MECHANICAL = "MECHANICAL"
    SYNC = "SYNC"


class MediaTypeEnum(StrEnum):
    """Multi-modal attribution media types (Sureel, ProRata)."""

    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    TEXT = "TEXT"
    SYMBOLIC_MUSIC = "SYMBOLIC_MUSIC"
    MULTIMODAL = "MULTIMODAL"


class CertificationTypeEnum(StrEnum):
    """External certification types (Fairly Trained, C2PA, EU AI Act)."""

    FAIRLY_TRAINED_LICENSED = "FAIRLY_TRAINED_LICENSED"
    C2PA_PROVENANCE = "C2PA_PROVENANCE"
    EU_AI_ACT_COMPLIANT = "EU_AI_ACT_COMPLIANT"
    CMO_APPROVED = "CMO_APPROVED"


class WatermarkTypeEnum(StrEnum):
    """Audio watermark types (SynthID, AudioSeal, Digimarc)."""

    SYNTHID = "SYNTHID"
    AUDIOSEAL = "AUDIOSEAL"
    WAVMARK = "WAVMARK"
    DIGIMARC = "DIGIMARC"


class RevenueModelEnum(StrEnum):
    """Revenue sharing models (LANDR, Kits AI, Musical AI)."""

    FLAT_FEE_UPFRONT = "FLAT_FEE_UPFRONT"
    PRO_RATA_MONTHLY = "PRO_RATA_MONTHLY"
    PER_GENERATION = "PER_GENERATION"
    INFLUENCE_BASED = "INFLUENCE_BASED"


# --- Regulatory/Compliance Enums (ISO 42001 vs EU AI Act) ---


class RegulatoryFrameworkEnum(StrEnum):
    """Applicable regulatory and governance frameworks.

    ISO 42001 defines internal AI governance roles; EU AI Act defines
    supply chain liability actors. They have zero terminological overlap
    and must be tracked separately.
    """

    ISO_42001 = "ISO_42001"
    EU_AI_ACT = "EU_AI_ACT"
    GPAI_CODE_OF_PRACTICE = "GPAI_CODE_OF_PRACTICE"
    DSM_DIRECTIVE = "DSM_DIRECTIVE"
    ESPR_DPP = "ESPR_DPP"
    GDPR = "GDPR"


class ComplianceActorEnum(StrEnum):
    """EU AI Act supply chain actors (Art. 3).

    These are distinct from ISO 42001 internal governance roles (Top
    Management, AI System Owner, Internal Audit). An organization may
    simultaneously hold multiple actor classifications across different
    AI systems.
    """

    PROVIDER = "PROVIDER"
    DEPLOYER = "DEPLOYER"
    AUTHORISED_REPRESENTATIVE = "AUTHORISED_REPRESENTATIVE"
    IMPORTER = "IMPORTER"
    DISTRIBUTOR = "DISTRIBUTOR"
    PRODUCT_MANUFACTURER = "PRODUCT_MANUFACTURER"


class TdmReservationMethodEnum(StrEnum):
    """Text-and-data-mining rights reservation methods.

    Under EU DSM Directive Art. 4, copyright holders can opt out of TDM
    via machine-readable reservation. The GPAI Code of Practice (July 2025)
    requires providers to respect robots.txt and emerging protocols.
    Music has a structural gap: robots.txt is web-only and does not cover
    audio content accessed via APIs or streaming platforms.
    """

    ROBOTS_TXT = "ROBOTS_TXT"
    LLMS_TXT = "LLMS_TXT"
    MACHINE_READABLE_TAG = "MACHINE_READABLE_TAG"
    RIGHTS_RESERVATION_API = "RIGHTS_RESERVATION_API"
    MCP_PERMISSION_QUERY = "MCP_PERMISSION_QUERY"
