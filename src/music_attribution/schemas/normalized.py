"""NormalizedRecord boundary object schema (BO-1).

Output of the Data Engineering (ETL) pipeline. A single music entity
normalized from one external source. Multiple ``NormalizedRecord`` instances
for the same real-world entity (from different sources) feed into the
Entity Resolution pipeline, which merges them into a ``ResolvedEntity``.

This module defines the first boundary object in the five-pipeline
architecture. All ETL extractors -- regardless of source format -- produce
``NormalizedRecord`` instances with a common schema, enabling uniform
downstream processing.

See Also
--------
music_attribution.schemas.resolved : The next boundary object in the pipeline.
Teikari, P. (2026). *Music Attribution with Transparent Confidence*,
    section 5.
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
    """Standard music industry identifiers bundle.

    Collects all known standard identifiers for a music entity. At the
    A2/A3 assurance levels, at least one identifier must be present for
    machine-sourced records (MusicBrainz, Discogs, AcoustID). These
    identifiers are the primary key for exact-match entity resolution.

    Attributes
    ----------
    isrc : str or None
        International Standard Recording Code. 12-character alphanumeric
        code uniquely identifying a specific recording (e.g.,
        ``"GBAYE0601498"``). Assigned by the IFPI.
    iswc : str or None
        International Standard Musical Work Code. Identifies the
        underlying composition (e.g., ``"T-070.238.867-3"``). Assigned
        by CISAC.
    isni : str or None
        International Standard Name Identifier. 16-digit identifier for
        public identities of parties (e.g., ``"0000000121032683"`` for
        Imogen Heap). Assigned by the ISNI International Agency.
    ipi : str or None
        Interested Party Information code. 9-11 digit code identifying
        rights holders in collecting society databases.
    mbid : str or None
        MusicBrainz Identifier. UUID assigned by MusicBrainz to any
        entity in their database.
    discogs_id : int or None
        Discogs numeric entity ID. Integer identifier in the Discogs
        database.
    acoustid : str or None
        AcoustID identifier. UUID derived from audio fingerprint
        (Chromaprint) matching.

    Examples
    --------
    >>> bundle = IdentifierBundle(
    ...     isrc="GBAYE0601498",
    ...     mbid="a74b1b7f-71a5-4011-9441-d0b5e4122711",
    ... )
    >>> bundle.has_any()
    True
    >>> IdentifierBundle().has_any()
    False
    """

    isrc: str | None = None
    iswc: str | None = None
    isni: str | None = None
    ipi: str | None = None
    mbid: str | None = None
    discogs_id: int | None = None
    acoustid: str | None = None

    def has_any(self) -> bool:
        """Check if at least one identifier is set.

        Returns
        -------
        bool
            True if any identifier field is not None.
        """
        return any(
            v is not None
            for v in (self.isrc, self.iswc, self.isni, self.ipi, self.mbid, self.discogs_id, self.acoustid)
        )


class SourceMetadata(BaseModel):
    """Typed source-specific metadata attached to a NormalizedRecord.

    Contains supplementary information that varies by source but follows
    a common schema. Fields that do not apply to a particular source
    are left as their defaults (None or empty list).

    Attributes
    ----------
    roles : list of str
        Credit roles reported by the source (free-text, not yet mapped
        to ``CreditRoleEnum``). Examples: ``["performer", "producer"]``.
    release_date : str or None
        Release date as reported by the source. String format varies
        (ISO 8601 preferred, but partial dates like ``"2005"`` are
        common in MusicBrainz).
    release_country : str or None
        ISO 3166-1 alpha-2 country code for the release territory
        (e.g., ``"GB"``, ``"US"``).
    genres : list of str
        Genre tags reported by the source. Free-text, not standardised
        across sources.
    duration_ms : int or None
        Track duration in milliseconds. May differ between sources due
        to different mastering or silence handling.
    track_number : int or None
        Track position within the release medium.
    medium_format : str or None
        Physical or digital medium format (e.g., ``"CD"``, ``"Vinyl"``,
        ``"Digital Media"``).
    language : str or None
        ISO 639-1 language code for lyrics/vocals (e.g., ``"en"``).
    extras : dict of str to str
        Catch-all for source-specific fields that do not map to the
        common schema. Keys and values are both strings.

    Examples
    --------
    >>> meta = SourceMetadata(
    ...     roles=["performer", "songwriter"],
    ...     release_date="2005-10-17",
    ...     release_country="GB",
    ...     genres=["electronic", "art pop"],
    ...     duration_ms=265000,
    ... )
    """

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
    """Link between entities within a single data source.

    Represents a directed edge from the parent ``NormalizedRecord`` to
    another entity identified by its source-specific ID. These
    relationships are source-local; cross-source relationship resolution
    happens in the Entity Resolution pipeline, producing
    ``ResolvedRelationship`` objects.

    Attributes
    ----------
    relationship_type : RelationshipTypeEnum
        The type of relationship (e.g., PERFORMED, WROTE, PRODUCED).
    target_source : SourceEnum
        The data source of the target entity.
    target_source_id : str
        Source-specific identifier of the target entity (e.g., a
        MusicBrainz MBID or Discogs numeric ID as string).
    target_entity_type : EntityTypeEnum
        The entity type of the target (e.g., ARTIST, RECORDING).
    attributes : dict of str to str
        Additional relationship attributes (e.g., ``{"instrument":
        "piano"}``, ``{"begin_date": "2005-01"}``).

    Examples
    --------
    >>> rel = Relationship(
    ...     relationship_type=RelationshipTypeEnum.PERFORMED,
    ...     target_source=SourceEnum.MUSICBRAINZ,
    ...     target_source_id="a74b1b7f-71a5-4011-9441-d0b5e4122711",
    ...     target_entity_type=EntityTypeEnum.ARTIST,
    ...     attributes={"instrument": "vocals"},
    ... )
    """

    relationship_type: RelationshipTypeEnum
    target_source: SourceEnum
    target_source_id: str
    target_entity_type: EntityTypeEnum
    attributes: dict[str, str] = Field(default_factory=dict)


class NormalizedRecord(BaseModel):
    """ETL output: normalized music metadata from a single external source.

    The ``NormalizedRecord`` is the first boundary object (BO-1) in the
    five-pipeline architecture. All ETL extractors produce
    ``NormalizedRecord`` instances regardless of their source format.
    Multiple records for the same real-world entity (from different
    sources) are merged by the Entity Resolution pipeline into a
    ``ResolvedEntity``.

    Attributes
    ----------
    schema_version : str
        Semantic version of the NormalizedRecord schema. Defaults to
        ``"1.0.0"``. Used for forward/backward compatibility checks.
    record_id : uuid.UUID
        Unique identifier for this record. Auto-generated UUIDv4.
    source : SourceEnum
        Which data source provided this record.
    source_id : str
        Source-specific identifier (e.g., MusicBrainz MBID, Discogs
        release ID as string).
    entity_type : EntityTypeEnum
        The type of music entity this record represents.
    canonical_name : str
        Primary name of the entity as reported by the source. Must be
        non-empty after whitespace stripping.
    alternative_names : list of str
        Alternative names, aliases, or transliterations. Used during
        fuzzy entity resolution.
    identifiers : IdentifierBundle
        Standard music industry identifiers (ISRC, ISWC, ISNI, etc.).
        Machine sources (MusicBrainz, Discogs, AcoustID) must provide
        at least one identifier.
    metadata : SourceMetadata
        Source-specific metadata (genres, release date, duration, etc.).
    relationships : list of Relationship
        Links to other entities within the same source.
    fetch_timestamp : datetime
        UTC timestamp when this record was fetched from the source.
        Must be timezone-aware and not more than 60 seconds in the
        future (to catch clock skew).
    source_confidence : float
        Source-reported confidence in the data, range [0.0, 1.0].
        0.0 = no confidence data available; 1.0 = verified by authority.
    raw_payload : dict or None
        Original API response preserved for debugging and re-processing.
        May be None if raw data is not retained.

    Examples
    --------
    >>> from datetime import datetime, UTC
    >>> record = NormalizedRecord(
    ...     source=SourceEnum.MUSICBRAINZ,
    ...     source_id="a74b1b7f-71a5-4011-9441-d0b5e4122711",
    ...     entity_type=EntityTypeEnum.RECORDING,
    ...     canonical_name="Hide and Seek",
    ...     identifiers=IdentifierBundle(isrc="GBAYE0601498"),
    ...     fetch_timestamp=datetime.now(UTC),
    ...     source_confidence=0.87,
    ... )

    See Also
    --------
    ResolvedEntity : The next boundary object produced by Entity Resolution.
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
