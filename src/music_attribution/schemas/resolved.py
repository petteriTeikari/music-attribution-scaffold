"""ResolvedEntity boundary object schema (BO-2).

Output of the Entity Resolution pipeline. A unified entity that merges
multiple NormalizedRecords from different sources into a single canonical
entity with resolution confidence.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator

from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    ConflictSeverityEnum,
    EntityTypeEnum,
    RelationshipTypeEnum,
    ResolutionMethodEnum,
    SourceEnum,
)
from music_attribution.schemas.normalized import IdentifierBundle


class SourceReference(BaseModel):
    """Reference to a contributing NormalizedRecord."""

    record_id: uuid.UUID
    source: SourceEnum
    source_id: str
    agreement_score: float = Field(ge=0.0, le=1.0)


class ResolutionDetails(BaseModel):
    """Per-method confidence breakdown."""

    string_similarity: float | None = None
    embedding_similarity: float | None = None
    graph_path_confidence: float | None = None
    llm_confidence: float | None = None
    matched_identifiers: list[str] = Field(default_factory=list)


class ResolvedRelationship(BaseModel):
    """Resolved cross-entity link."""

    target_entity_id: uuid.UUID
    relationship_type: RelationshipTypeEnum
    confidence: float = Field(ge=0.0, le=1.0)
    supporting_sources: list[SourceEnum] = Field(default_factory=list)


class Conflict(BaseModel):
    """Unresolved disagreement between sources."""

    field: str
    values: dict[str, str] = Field(default_factory=dict)
    severity: ConflictSeverityEnum


class ResolvedEntity(BaseModel):
    """Unified entity resolved from multiple sources.

    This is the primary boundary object produced by the Entity Resolution
    pipeline and consumed by the Attribution Engine pipeline.
    """

    schema_version: str = "1.0.0"
    entity_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    entity_type: EntityTypeEnum
    canonical_name: str
    alternative_names: list[str] = Field(default_factory=list)
    identifiers: IdentifierBundle = Field(default_factory=IdentifierBundle)
    source_records: list[SourceReference] = Field(min_length=1)
    resolution_method: ResolutionMethodEnum
    resolution_confidence: float = Field(ge=0.0, le=1.0)
    resolution_details: ResolutionDetails = Field(default_factory=ResolutionDetails)
    assurance_level: AssuranceLevelEnum
    relationships: list[ResolvedRelationship] = Field(default_factory=list)
    conflicts: list[Conflict] = Field(default_factory=list)
    needs_review: bool = False
    review_reason: str | None = None
    merged_from: list[uuid.UUID] | None = None
    resolved_at: datetime

    @field_validator("resolved_at")
    @classmethod
    def validate_resolved_at(cls, v: datetime) -> datetime:
        """Resolved timestamp must be timezone-aware."""
        if v.tzinfo is None:
            msg = "resolved_at must be timezone-aware (UTC)"
            raise ValueError(msg)
        return v

    @model_validator(mode="after")
    def validate_review_fields(self) -> ResolvedEntity:
        """If needs_review is True, review_reason must be provided."""
        if self.needs_review and self.review_reason is None:
            msg = "review_reason must be non-None when needs_review is True"
            raise ValueError(msg)
        return self
