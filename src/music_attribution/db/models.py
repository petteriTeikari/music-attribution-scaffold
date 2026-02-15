"""SQLAlchemy ORM models mapping to Pydantic boundary object schemas.

Defines the relational database schema for the music attribution scaffold.
Each model corresponds to a Pydantic boundary object (BO) from the
``music_attribution.schemas`` package, with column names and types
mirroring the Pydantic field definitions.

The models use PostgreSQL-specific features (``JSONB``, ``pgvector
HALFVEC``) but are designed to degrade gracefully to SQLite via
aiosqlite for unit testing.

Tables
------
normalized_records
    BO-1: Raw records from external sources (MusicBrainz, Discogs,
    AcoustID, file metadata) after ETL normalisation.
resolved_entities
    BO-2: Deduplicated entities after probabilistic record linkage
    (Splink Fellegi-Sunter model).
attribution_records
    BO-3: Aggregated attribution scores with confidence, assurance
    level, conformal prediction sets, and provenance chain.
feedback_cards
    BO-4: Structured reviewer feedback with corrections, overall
    assessment, and center-bias detection flag.
permission_bundles
    BO-5: Permission scopes and entries for the MCP "Permission
    Patchbay" (training rights, commercial use, etc.).
edges
    Graph relationships between resolved entities (e.g.
    artist-performed-on-work, work-part-of-album).
entity_embeddings
    Vector embeddings (pgvector HALFVEC-768) for semantic similarity
    search across entities.
audit_log
    Immutable audit trail of permission check requests and results.

See Also
--------
music_attribution.schemas : Pydantic boundary object definitions.
music_attribution.db.engine : Async engine factory for these models.
"""

from __future__ import annotations

import uuid

from pgvector.sqlalchemy import HALFVEC
from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    Uuid,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Declarative base class for all ORM models.

    All models inherit from this class to share the same metadata
    registry and participate in ``Base.metadata.create_all()`` calls
    during migrations and test setup.
    """


class NormalizedRecordModel(Base):
    """SQLAlchemy model for NormalizedRecord boundary object (BO-1).

    Stores ETL-normalised records from external data sources. Each
    record represents a single source's view of an entity (artist,
    work, label) before entity resolution.

    The ``(source, source_id)`` pair is unique-constrained to prevent
    duplicate imports from the same source.

    Attributes
    ----------
    record_id : uuid.UUID
        Primary key (auto-generated UUIDv4).
    source : str
        Data source identifier (e.g. ``"musicbrainz"``, ``"discogs"``).
    source_id : str
        Source-specific identifier for the record.
    entity_type : str
        Type of entity (``"artist"``, ``"work"``, ``"label"``).
    canonical_name : str
        Normalised canonical name for the entity.
    alternative_names : dict
        JSONB array of alternative names/aliases.
    identifiers : dict
        JSONB map of standard identifiers (ISRC, ISWC, ISNI, etc.).
    metadata_ : dict
        JSONB map of source-specific metadata (mapped to ``metadata``
        column to avoid Python keyword conflict).
    source_confidence : float
        Source's self-reported confidence in the record (0.0--1.0).
    raw_payload : dict | None
        Optional raw API response for debugging and audit.
    """

    __tablename__ = "normalized_records"
    __table_args__ = (UniqueConstraint("source", "source_id", name="uq_normalized_records_source_source_id"),)

    record_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    schema_version: Mapped[str] = mapped_column(String(20), default="1.0.0")
    source: Mapped[str] = mapped_column(String(50), nullable=False)
    source_id: Mapped[str] = mapped_column(String(255), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(50), nullable=False)
    canonical_name: Mapped[str] = mapped_column(Text, nullable=False)
    alternative_names: Mapped[dict] = mapped_column(JSONB, default=list)
    identifiers: Mapped[dict] = mapped_column(JSONB, default=dict)
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict)
    relationships: Mapped[dict] = mapped_column(JSONB, default=list)
    fetch_timestamp: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)
    source_confidence: Mapped[float] = mapped_column(Float, nullable=False)
    raw_payload: Mapped[dict | None] = mapped_column(JSONB, nullable=True)


class ResolvedEntityModel(Base):
    """SQLAlchemy model for ResolvedEntity boundary object (BO-2).

    Stores deduplicated entities after probabilistic record linkage.
    Each resolved entity aggregates one or more ``NormalizedRecord``
    entries that refer to the same real-world entity.

    Attributes
    ----------
    entity_id : uuid.UUID
        Primary key (auto-generated UUIDv4).
    entity_type : str
        Type of entity (``"artist"``, ``"work"``, ``"label"``).
    canonical_name : str
        Best canonical name selected during resolution.
    resolution_method : str
        Algorithm used (e.g. ``"splink_linkage"``, ``"exact_id_match"``).
    resolution_confidence : float
        Confidence in the resolution (0.0--1.0).
    assurance_level : str
        A0--A3 assurance level string.
    needs_review : bool
        Whether the entity requires human review.
    review_reason : str | None
        Explanation if ``needs_review`` is ``True``.
    """

    __tablename__ = "resolved_entities"

    entity_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    schema_version: Mapped[str] = mapped_column(String(20), default="1.0.0")
    entity_type: Mapped[str] = mapped_column(String(50), nullable=False)
    canonical_name: Mapped[str] = mapped_column(Text, nullable=False)
    alternative_names: Mapped[dict] = mapped_column(JSONB, default=list)
    identifiers: Mapped[dict] = mapped_column(JSONB, default=dict)
    source_records: Mapped[dict] = mapped_column(JSONB, nullable=False)
    resolution_method: Mapped[str] = mapped_column(String(50), nullable=False)
    resolution_confidence: Mapped[float] = mapped_column(Float, nullable=False)
    resolution_details: Mapped[dict] = mapped_column(JSONB, default=dict)
    assurance_level: Mapped[str] = mapped_column(String(20), nullable=False)
    relationships: Mapped[dict] = mapped_column(JSONB, default=list)
    conflicts: Mapped[dict] = mapped_column(JSONB, default=list)
    needs_review: Mapped[bool] = mapped_column(Boolean, default=False)
    review_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    merged_from: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    resolved_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)


class AttributionRecordModel(Base):
    """SQLAlchemy model for AttributionRecord boundary object (BO-3).

    The central table of the attribution scaffold. Each record
    represents the aggregated attribution for a musical work,
    including credits, confidence score, conformal prediction set,
    source agreement, and full provenance chain.

    Attributes
    ----------
    attribution_id : uuid.UUID
        Primary key (auto-generated UUIDv4).
    work_entity_id : uuid.UUID
        Foreign reference to the resolved work entity.
    work_title : str
        Display title of the musical work.
    artist_name : str
        Primary artist display name.
    credits : dict
        JSONB array of ``Credit`` objects (role, confidence, sources).
    assurance_level : str
        A0--A3 assurance level (see Teikari 2026, Section 3).
    confidence_score : float
        Overall attribution confidence (0.0--1.0).
    conformal_set : dict
        JSONB conformal prediction set metadata (coverage, calibration).
    source_agreement : float
        Inter-source agreement score (0.0--1.0).
    provenance_chain : dict
        JSONB array of ``ProvenanceEvent`` objects tracing the full
        attribution history.
    needs_review : bool
        Whether the record is flagged for human review.
    review_priority : float
        Priority score for the review queue (higher = more urgent).
    version : int
        Optimistic concurrency version counter.
    """

    __tablename__ = "attribution_records"

    attribution_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    schema_version: Mapped[str] = mapped_column(String(20), default="1.0.0")
    work_entity_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    work_title: Mapped[str] = mapped_column(String(500), default="")
    artist_name: Mapped[str] = mapped_column(String(500), default="")
    credits: Mapped[dict] = mapped_column(JSONB, nullable=False)
    assurance_level: Mapped[str] = mapped_column(String(20), nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    conformal_set: Mapped[dict] = mapped_column(JSONB, nullable=False)
    source_agreement: Mapped[float] = mapped_column(Float, nullable=False)
    provenance_chain: Mapped[dict] = mapped_column(JSONB, default=list)
    uncertainty_summary: Mapped[dict | None] = mapped_column(JSONB, nullable=True, default=None)
    needs_review: Mapped[bool] = mapped_column(Boolean, default=False)
    review_priority: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)


class PermissionBundleModel(Base):
    """SQLAlchemy model for PermissionBundle boundary object (BO-5).

    Stores machine-readable permission entries for the MCP "Permission
    Patchbay". Each bundle is scoped to a resolved entity and contains
    permission entries for AI training, commercial use, derivative
    works, and other rights.

    Attributes
    ----------
    permission_id : uuid.UUID
        Primary key (auto-generated UUIDv4).
    entity_id : uuid.UUID
        Foreign key to ``resolved_entities.entity_id``.
    scope : str
        Permission scope (e.g. ``"GLOBAL"``, ``"WORK"``, ``"CATALOG"``).
    permissions : dict
        JSONB array of permission entries (type, value, conditions).
    effective_from : str
        Timestamp when permissions become active.
    effective_until : str | None
        Optional expiry timestamp. ``None`` means indefinite.
    delegation_chain : dict
        JSONB array of delegation events (who granted what to whom).
    default_permission : str
        Fallback permission value when a specific type is not set.
    version : int
        Optimistic concurrency version counter.
    """

    __tablename__ = "permission_bundles"

    permission_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    entity_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("resolved_entities.entity_id"), nullable=False)
    scope: Mapped[str] = mapped_column(String(50), nullable=False)
    scope_entity_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, nullable=True)
    permissions: Mapped[dict] = mapped_column(JSONB, nullable=False)
    effective_from: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)
    effective_until: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    delegation_chain: Mapped[dict] = mapped_column(JSONB, default=list)
    default_permission: Mapped[str] = mapped_column(String(50), nullable=False)
    created_by: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)


class FeedbackCardModel(Base):
    """SQLAlchemy model for FeedbackCard boundary object (BO-4).

    Stores structured reviewer feedback on attribution records.
    Each card captures corrections, an overall quality assessment,
    and a center-bias detection flag.

    The ``center_bias_flag`` is set when ``overall_assessment`` falls
    in the 0.45--0.55 range, indicating the reviewer may be avoiding
    a decisive judgement (see Teikari 2026, Section 5 on calibration).

    Attributes
    ----------
    feedback_id : uuid.UUID
        Primary key (auto-generated UUIDv4).
    attribution_id : uuid.UUID
        Foreign key to the reviewed attribution record.
    reviewer_id : str
        Identifier of the reviewer (user ID or ``"agent-assisted"``).
    reviewer_role : str
        Role enum value (e.g. ``"MUSICOLOGIST"``, ``"ARTIST"``).
    attribution_version : int
        Version of the attribution record at the time of review.
    corrections : dict
        JSONB array of field-level corrections.
    overall_assessment : float
        Quality assessment on a 0.0--1.0 scale.
    center_bias_flag : bool
        ``True`` if assessment falls in the indecisive 0.45--0.55 range.
    free_text : str | None
        Optional free-form reviewer notes.
    evidence_type : str
        Type of evidence supporting the feedback.
    """

    __tablename__ = "feedback_cards"

    feedback_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    attribution_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("attribution_records.attribution_id"), nullable=False
    )
    reviewer_id: Mapped[str] = mapped_column(String(255), nullable=False)
    reviewer_role: Mapped[str] = mapped_column(String(50), nullable=False)
    attribution_version: Mapped[int] = mapped_column(Integer, nullable=False)
    corrections: Mapped[dict] = mapped_column(JSONB, default=list)
    overall_assessment: Mapped[float] = mapped_column(Float, nullable=False)
    center_bias_flag: Mapped[bool] = mapped_column(Boolean, default=False)
    free_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    evidence_type: Mapped[str] = mapped_column(String(50), nullable=False)
    submitted_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)


class EdgeModel(Base):
    """SQLAlchemy model for graph edges between resolved entities.

    Represents directional relationships in the attribution knowledge
    graph (e.g. artist-performed-on-work, work-part-of-album,
    artist-member-of-group). Used by the hybrid search service for
    graph-context expansion.

    The ``(from_entity_id, to_entity_id, relationship_type)`` triple
    is unique-constrained to prevent duplicate edges.

    Attributes
    ----------
    edge_id : uuid.UUID
        Primary key (auto-generated UUIDv4).
    from_entity_id : uuid.UUID
        Source entity (foreign key to ``resolved_entities``).
    to_entity_id : uuid.UUID
        Target entity (foreign key to ``resolved_entities``).
    relationship_type : str
        Edge type label (e.g. ``"performed_on"``, ``"produced_by"``).
    confidence : float
        Confidence in the relationship (0.0--1.0).
    metadata_ : dict
        JSONB map of additional edge properties.
    """

    __tablename__ = "edges"
    __table_args__ = (
        UniqueConstraint(
            "from_entity_id",
            "to_entity_id",
            "relationship_type",
            name="uq_edges_from_to_type",
        ),
    )

    edge_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    from_entity_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("resolved_entities.entity_id"), nullable=False)
    to_entity_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("resolved_entities.entity_id"), nullable=False)
    relationship_type: Mapped[str] = mapped_column(String(100), nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)


class EntityEmbeddingModel(Base):
    """SQLAlchemy model for entity vector embeddings.

    Stores 768-dimensional half-precision embeddings (pgvector
    ``HALFVEC``) for semantic similarity search across entities.
    Used by the vector search service and hybrid search RRF fusion.

    The ``(entity_id, model_name)`` pair is unique-constrained to
    allow storing embeddings from multiple models for the same entity.

    Attributes
    ----------
    embedding_id : uuid.UUID
        Primary key (auto-generated UUIDv4).
    entity_id : uuid.UUID
        Foreign key to ``resolved_entities``.
    model_name : str
        Name of the embedding model (e.g. ``"text-embedding-3-small"``).
    model_version : str
        Version string of the embedding model.
    embedding : HALFVEC(768)
        768-dimensional half-precision float vector.
    """

    __tablename__ = "entity_embeddings"
    __table_args__ = (UniqueConstraint("entity_id", "model_name", name="uq_entity_embeddings_entity_model"),)

    embedding_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    entity_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("resolved_entities.entity_id"), nullable=False)
    model_name: Mapped[str] = mapped_column(String(255), nullable=False)
    model_version: Mapped[str] = mapped_column(String(100), nullable=False)
    embedding = mapped_column(HALFVEC(768), nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)


class AuditLogModel(Base):
    """SQLAlchemy model for the permission check audit trail.

    Records every permission check request and its result for
    compliance and forensic analysis. Entries are append-only
    and should never be updated or deleted.

    Attributes
    ----------
    audit_id : uuid.UUID
        Primary key (auto-generated UUIDv4).
    permission_id : uuid.UUID
        Foreign key to the checked ``permission_bundles`` entry.
    requester_id : str
        Identifier of the entity or service requesting the check.
    requester_type : str
        Type of requester (e.g. ``"ai_platform"``, ``"api_client"``).
    permission_type : str
        Permission type that was checked (e.g. ``"AI_TRAINING"``).
    result : str
        Check result (e.g. ``"ALLOW"``, ``"DENY"``, ``"CONDITIONAL"``).
    request_context : dict
        JSONB map of additional request context (IP, user-agent, etc.).
    checked_at : str
        Timestamp of the permission check.
    """

    __tablename__ = "audit_log"

    audit_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    permission_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("permission_bundles.permission_id"), nullable=False
    )
    requester_id: Mapped[str] = mapped_column(String(255), nullable=False)
    requester_type: Mapped[str] = mapped_column(String(100), nullable=False)
    permission_type: Mapped[str] = mapped_column(String(50), nullable=False)
    result: Mapped[str] = mapped_column(String(50), nullable=False)
    request_context: Mapped[dict] = mapped_column(JSONB, default=dict)
    checked_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)
