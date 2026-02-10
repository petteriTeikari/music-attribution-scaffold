"""SQLAlchemy ORM models mapping to Pydantic boundary object schemas.

These models define the database tables. Column names and types correspond
to the Pydantic schema fields defined in music_attribution.schemas.
"""

from __future__ import annotations

import uuid

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
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
    __table_args__ = (
        UniqueConstraint("source", "source_id", name="uq_normalized_records_source_source_id"),
    )

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
