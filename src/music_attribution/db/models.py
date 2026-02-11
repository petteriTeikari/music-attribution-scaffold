"""SQLAlchemy ORM models mapping to Pydantic boundary object schemas.

These models define the database tables. Column names and types correspond
to the Pydantic schema fields defined in music_attribution.schemas.

Tables:
  - normalized_records  (BO-1: NormalizedRecord)
  - resolved_entities   (BO-2: ResolvedEntity)
  - attribution_records (BO-3: AttributionRecord)
  - permission_bundles  (BO-5: PermissionBundle)
  - feedback_cards      (BO-4: FeedbackCard)
  - edges               (Graph relationships)
  - entity_embeddings   (Vector embeddings)
  - audit_log           (Permission check audit trail)
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
    """Base class for all ORM models."""


class NormalizedRecordModel(Base):
    """SQLAlchemy model for NormalizedRecord boundary object."""

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
    """SQLAlchemy model for ResolvedEntity boundary object."""

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
    """SQLAlchemy model for AttributionRecord boundary object."""

    __tablename__ = "attribution_records"

    attribution_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    schema_version: Mapped[str] = mapped_column(String(20), default="1.0.0")
    work_entity_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    credits: Mapped[dict] = mapped_column(JSONB, nullable=False)
    assurance_level: Mapped[str] = mapped_column(String(20), nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    conformal_set: Mapped[dict] = mapped_column(JSONB, nullable=False)
    source_agreement: Mapped[float] = mapped_column(Float, nullable=False)
    provenance_chain: Mapped[dict] = mapped_column(JSONB, default=list)
    needs_review: Mapped[bool] = mapped_column(Boolean, default=False)
    review_priority: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)


class PermissionBundleModel(Base):
    """SQLAlchemy model for PermissionBundle boundary object (BO-5)."""

    __tablename__ = "permission_bundles"

    permission_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    entity_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("resolved_entities.entity_id"), nullable=False
    )
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
    """SQLAlchemy model for FeedbackCard boundary object (BO-4)."""

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
    """SQLAlchemy model for graph edges (entity relationships + provenance)."""

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
    from_entity_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("resolved_entities.entity_id"), nullable=False
    )
    to_entity_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("resolved_entities.entity_id"), nullable=False
    )
    relationship_type: Mapped[str] = mapped_column(String(100), nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)


class EntityEmbeddingModel(Base):
    """SQLAlchemy model for vector embeddings (pgvector halfvec)."""

    __tablename__ = "entity_embeddings"
    __table_args__ = (
        UniqueConstraint("entity_id", "model_name", name="uq_entity_embeddings_entity_model"),
    )

    embedding_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    entity_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("resolved_entities.entity_id"), nullable=False
    )
    model_name: Mapped[str] = mapped_column(String(255), nullable=False)
    model_version: Mapped[str] = mapped_column(String(100), nullable=False)
    embedding = mapped_column(HALFVEC(768), nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False)


class AuditLogModel(Base):
    """SQLAlchemy model for permission check audit trail."""

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
