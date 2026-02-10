"""NormalizedRecord boundary object schema (BO-1).

Output of the Data Engineering pipeline. A single music entity normalized
from one external source. Multiple NormalizedRecords for the same entity
(from different sources) feed into Entity Resolution.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator

from music_attribution.schemas.enums import (
    EntityTypeEnum,
    RelationshipTypeEnum,
    SourceEnum,
)


class IdentifierBundle(BaseModel):
    """Standard music industry identifiers."""

    isrc: str | None = None
    iswc: str | None = None
    isni: str | None = None
    ipi: str | None = None
    mbid: str | None = None
    discogs_id: int | None = None
    acoustid: str | None = None

    def has_any(self) -> bool:
        """Check if at least one identifier is set."""
        return any(
            v is not None
            for v in (self.isrc, self.iswc, self.isni, self.ipi, self.mbid, self.discogs_id, self.acoustid)
        )


class SourceMetadata(BaseModel):
    """Typed source-specific metadata."""

    roles: list[str] = Field(default_factory=list)
    release_date: str | None = None
    release_country: str | None = None
    genres: list[str] = Field(default_factory=list)
    duration_ms: int | None = None
    track_number: int | None = None
    medium_format: str | None = None
    language: str | None = None
    extras: dict[str, str] = Field(default_factory=dict)


class Relationship(BaseModel):
    """Link between entities."""

    relationship_type: RelationshipTypeEnum
    target_source: SourceEnum
    target_source_id: str
    target_entity_type: EntityTypeEnum
    attributes: dict[str, str] = Field(default_factory=dict)


class NormalizedRecord(BaseModel):
    """Normalized record from a single external source.

    This is the primary boundary object produced by the Data Engineering
    pipeline and consumed by the Entity Resolution pipeline.
    """

    schema_version: str = "1.0.0"
    record_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    source: SourceEnum
    source_id: str
    entity_type: EntityTypeEnum
    canonical_name: str
    alternative_names: list[str] = Field(default_factory=list)
    identifiers: IdentifierBundle = Field(default_factory=IdentifierBundle)
    metadata: SourceMetadata = Field(default_factory=SourceMetadata)
    relationships: list[Relationship] = Field(default_factory=list)
    fetch_timestamp: datetime
    source_confidence: float = Field(ge=0.0, le=1.0)
    raw_payload: dict[str, Any] | None = None

    @field_validator("canonical_name")
    @classmethod
    def validate_canonical_name(cls, v: str) -> str:
        """Canonical name must be non-empty after stripping."""
        if not v.strip():
            msg = "canonical_name must be non-empty after stripping whitespace"
            raise ValueError(msg)
        return v.strip()

    @field_validator("fetch_timestamp")
    @classmethod
    def validate_fetch_timestamp(cls, v: datetime) -> datetime:
        """Fetch timestamp must be timezone-aware and not far in the future."""
        if v.tzinfo is None:
            msg = "fetch_timestamp must be timezone-aware (UTC)"
            raise ValueError(msg)
        max_future = datetime.now(UTC) + timedelta(seconds=60)
        if v > max_future:
            msg = "fetch_timestamp must not be more than 60 seconds in the future"
            raise ValueError(msg)
        return v

    @model_validator(mode="after")
    def validate_identifiers_for_machine_sources(self) -> NormalizedRecord:
        """Machine sources require at least one identifier."""
        machine_sources = {SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS, SourceEnum.ACOUSTID}
        if self.source in machine_sources and not self.identifiers.has_any():
            msg = f"Source {self.source} requires at least one identifier in IdentifierBundle"
            raise ValueError(msg)
        return self
