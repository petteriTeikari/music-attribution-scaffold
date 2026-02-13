"""ResolvedEntity boundary object schema (BO-2).

Output of the Entity Resolution pipeline. A unified entity that merges
multiple ``NormalizedRecord`` instances from different sources into a
single canonical entity with resolution confidence and assurance level.

The ``ResolvedEntity`` is the second boundary object in the five-pipeline
architecture. It carries forward the provenance of every source that
contributed to it, enabling downstream attribution scoring to weight
sources by reliability.

See Also
--------
music_attribution.schemas.normalized : The preceding boundary object.
music_attribution.schemas.attribution : The next boundary object.
Teikari, P. (2026). *Music Attribution with Transparent Confidence*,
    section 5.
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
    """Reference to a contributing NormalizedRecord.

    Links a ``ResolvedEntity`` back to the specific ``NormalizedRecord``
    that contributed to it, preserving full provenance. The agreement
    score measures how well this source's data aligns with the resolved
    consensus.

    Attributes
    ----------
    record_id : uuid.UUID
        UUID of the contributing ``NormalizedRecord``.
    source : SourceEnum
        Which data source provided the record.
    source_id : str
        Source-specific identifier of the record.
    agreement_score : float
        How well this source agrees with the resolved consensus,
        range [0.0, 1.0]. 1.0 = perfect agreement on all fields;
        0.0 = complete disagreement.

    Examples
    --------
    >>> ref = SourceReference(
    ...     record_id=uuid.uuid4(),
    ...     source=SourceEnum.MUSICBRAINZ,
    ...     source_id="a74b1b7f-71a5-4011-9441-d0b5e4122711",
    ...     agreement_score=0.95,
    ... )
    """

    record_id: uuid.UUID
    source: SourceEnum
    source_id: str
    agreement_score: float = Field(ge=0.0, le=1.0)


class ResolutionDetails(BaseModel):
    """Per-method confidence breakdown for entity resolution.

    Records the confidence contribution from each resolution method that
    was attempted. Only populated fields were actually used; ``None``
    means that method was not applied. This enables post-hoc analysis
    of which methods are most effective for different entity types.

    Attributes
    ----------
    string_similarity : float or None
        Confidence from fuzzy string matching (Jaro-Winkler, Levenshtein),
        range [0.0, 1.0]. None if not attempted.
    embedding_similarity : float or None
        Confidence from semantic embedding similarity (cosine distance),
        range [0.0, 1.0]. None if not attempted.
    graph_path_confidence : float or None
        Confidence from graph-based resolution (path length, co-occurrence
        patterns), range [0.0, 1.0]. None if not attempted.
    llm_confidence : float or None
        Confidence from LLM-assisted resolution, range [0.0, 1.0].
        None if not attempted.
    matched_identifiers : list of str
        Names of identifiers that matched exactly (e.g.,
        ``["isrc", "mbid"]``). Empty if no exact matches.

    Examples
    --------
    >>> details = ResolutionDetails(
    ...     string_similarity=0.92,
    ...     matched_identifiers=["isrc"],
    ... )
    """

    string_similarity: float | None = None
    embedding_similarity: float | None = None
    graph_path_confidence: float | None = None
    llm_confidence: float | None = None
    matched_identifiers: list[str] = Field(default_factory=list)


class ResolvedRelationship(BaseModel):
    """Resolved cross-entity relationship link.

    Unlike source-local ``Relationship`` objects in ``NormalizedRecord``,
    a ``ResolvedRelationship`` links two ``ResolvedEntity`` instances
    and is backed by one or more corroborating data sources.

    Attributes
    ----------
    target_entity_id : uuid.UUID
        UUID of the target ``ResolvedEntity``.
    relationship_type : RelationshipTypeEnum
        The type of relationship (e.g., PERFORMED, WROTE).
    confidence : float
        Confidence in this relationship, range [0.0, 1.0]. Higher when
        multiple sources corroborate the link.
    supporting_sources : list of SourceEnum
        Data sources that corroborate this relationship. More sources
        generally means higher confidence.

    Examples
    --------
    >>> rel = ResolvedRelationship(
    ...     target_entity_id=uuid.uuid4(),
    ...     relationship_type=RelationshipTypeEnum.PERFORMED,
    ...     confidence=0.92,
    ...     supporting_sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
    ... )
    """

    target_entity_id: uuid.UUID
    relationship_type: RelationshipTypeEnum
    confidence: float = Field(ge=0.0, le=1.0)
    supporting_sources: list[SourceEnum] = Field(default_factory=list)


class Conflict(BaseModel):
    """Unresolved disagreement between data sources.

    When entity resolution encounters contradictory information from
    different sources for the same field, it records a ``Conflict``
    rather than silently choosing one value. Conflicts with severity
    HIGH or CRITICAL trigger ``needs_review = True`` on the parent
    ``ResolvedEntity``.

    Attributes
    ----------
    field : str
        Name of the field in conflict (e.g., ``"canonical_name"``,
        ``"release_date"``).
    values : dict of str to str
        Mapping of source name to its reported value. Keys are source
        identifiers (e.g., ``"MUSICBRAINZ"``), values are the
        conflicting field values.
    severity : ConflictSeverityEnum
        How severe the disagreement is, from LOW (auto-resolvable)
        to CRITICAL (blocks attribution).

    Examples
    --------
    >>> conflict = Conflict(
    ...     field="canonical_name",
    ...     values={"MUSICBRAINZ": "Imogen Heap", "DISCOGS": "I. Heap"},
    ...     severity=ConflictSeverityEnum.LOW,
    ... )
    """

    field: str
    values: dict[str, str] = Field(default_factory=dict)
    severity: ConflictSeverityEnum


class ResolvedEntity(BaseModel):
    """Unified entity resolved from multiple data sources.

    The ``ResolvedEntity`` is the second boundary object (BO-2) in the
    five-pipeline architecture. It is produced by the Entity Resolution
    pipeline and consumed by the Attribution Engine. Each instance
    represents a single real-world music entity (artist, recording,
    work, etc.) with a canonical identity established by merging one
    or more ``NormalizedRecord`` instances.

    Attributes
    ----------
    schema_version : str
        Semantic version of the ResolvedEntity schema. Defaults to
        ``"1.0.0"``.
    entity_id : uuid.UUID
        Unique identifier for this resolved entity. Auto-generated
        UUIDv4.
    entity_type : EntityTypeEnum
        The type of music entity (RECORDING, WORK, ARTIST, etc.).
    canonical_name : str
        Best-consensus name for the entity, chosen from contributing
        sources by the resolution algorithm.
    alternative_names : list of str
        All other names/aliases from contributing sources, used for
        future matching and display.
    identifiers : IdentifierBundle
        Merged identifier bundle combining identifiers from all
        contributing sources.
    source_records : list of SourceReference
        References to all ``NormalizedRecord`` instances that were
        merged into this entity. Must contain at least one.
    resolution_method : ResolutionMethodEnum
        Primary method used to resolve/merge the source records.
    resolution_confidence : float
        Overall confidence in the resolution, range [0.0, 1.0]. This
        is the resolution pipeline's assessment of how likely it is
        that all merged records truly refer to the same entity.
    resolution_details : ResolutionDetails
        Per-method confidence breakdown showing which methods contributed
        and their individual confidence scores.
    assurance_level : AssuranceLevelEnum
        A0-A3 assurance level determined by the number and quality of
        corroborating sources. See Teikari (2026), section 6.
    relationships : list of ResolvedRelationship
        Cross-entity links resolved from source-local relationships.
    conflicts : list of Conflict
        Unresolved disagreements between sources. May trigger human
        review if severity is HIGH or CRITICAL.
    needs_review : bool
        Flag indicating this entity requires human review before
        attribution scoring proceeds.
    review_reason : str or None
        Human-readable explanation of why review is needed. Required
        when ``needs_review`` is True.
    merged_from : list of uuid.UUID or None
        If this entity was formed by merging previously separate
        ``ResolvedEntity`` instances, their IDs are listed here.
    resolved_at : datetime
        UTC timestamp when resolution was performed. Must be
        timezone-aware.

    Examples
    --------
    >>> from datetime import datetime, UTC
    >>> entity = ResolvedEntity(
    ...     entity_type=EntityTypeEnum.RECORDING,
    ...     canonical_name="Hide and Seek",
    ...     source_records=[
    ...         SourceReference(
    ...             record_id=uuid.uuid4(),
    ...             source=SourceEnum.MUSICBRAINZ,
    ...             source_id="abc-123",
    ...             agreement_score=0.95,
    ...         ),
    ...     ],
    ...     resolution_method=ResolutionMethodEnum.EXACT_ID,
    ...     resolution_confidence=0.98,
    ...     assurance_level=AssuranceLevelEnum.LEVEL_2,
    ...     resolved_at=datetime.now(UTC),
    ... )

    See Also
    --------
    NormalizedRecord : The preceding boundary object from ETL.
    AttributionRecord : The next boundary object from Attribution Engine.
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
