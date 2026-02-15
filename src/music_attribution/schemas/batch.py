"""Batch metadata envelope for pipeline boundary crossing.

Wraps boundary object collections in a ``BatchEnvelope`` with
statistical summary metadata. Enables batch-level provenance tracing,
quality monitoring, and drift detection across the attribution pipeline.

Every time a batch of records crosses a pipeline boundary, it is
wrapped in a ``BatchEnvelope[T]`` where ``T`` is the boundary object
type (``NormalizedRecord``, ``ResolvedEntity``, ``AttributionRecord``).

See Also
--------
music_attribution.schemas.normalized : NormalizedRecord (ETL output).
music_attribution.schemas.resolved : ResolvedEntity (resolution output).
music_attribution.schemas.attribution : AttributionRecord (engine output).
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from music_attribution.schemas.enums import SourceEnum

T = TypeVar("T")


class ConfidenceStats(BaseModel):
    """Statistical summary of confidence scores in a batch.

    Provides descriptive statistics for the confidence scores across
    all records in a batch, enabling monitoring for drift, anomalies,
    and quality regressions.

    Attributes
    ----------
    mean : float
        Mean confidence score across the batch.
    std : float
        Standard deviation of confidence scores. High std may indicate
        heterogeneous data quality.
    min_val : float
        Minimum confidence score in the batch.
    max_val : float
        Maximum confidence score in the batch.
    median : float
        Median confidence score. More robust than mean when outliers
        are present.
    count : int
        Number of records in the batch. Non-negative.

    Examples
    --------
    >>> stats = ConfidenceStats(
    ...     mean=0.82,
    ...     std=0.12,
    ...     min_val=0.45,
    ...     max_val=0.99,
    ...     median=0.85,
    ...     count=150,
    ... )
    """

    mean: float
    std: float
    min_val: float
    max_val: float
    median: float
    count: int = Field(ge=0)


class BatchMetadata(BaseModel):
    """Metadata envelope for a batch of records at a pipeline boundary.

    Contains aggregate statistics about a batch, enabling quality
    monitoring and drift detection without inspecting individual records.

    Attributes
    ----------
    batch_id : uuid.UUID
        Unique identifier for this batch. Auto-generated UUIDv4.
    record_count : int
        Total number of records in the batch. Non-negative.
    source_distribution : dict of SourceEnum to int
        Count of records per data source. Enables monitoring for
        source availability issues (e.g., if MusicBrainz suddenly
        contributes zero records).
    confidence_stats : ConfidenceStats
        Descriptive statistics for confidence scores across the batch.
    identifier_coverage : float
        Fraction of records that have at least one standard identifier
        (ISRC, ISWC, ISNI, etc.), range [0.0, 1.0]. Lower coverage
        may indicate data quality issues.
    created_at : datetime
        UTC timestamp when this batch was created.

    Examples
    --------
    >>> from datetime import datetime, UTC
    >>> meta = BatchMetadata(
    ...     record_count=150,
    ...     source_distribution={SourceEnum.MUSICBRAINZ: 80, SourceEnum.DISCOGS: 70},
    ...     confidence_stats=ConfidenceStats(
    ...         mean=0.82,
    ...         std=0.12,
    ...         min_val=0.45,
    ...         max_val=0.99,
    ...         median=0.85,
    ...         count=150,
    ...     ),
    ...     identifier_coverage=0.93,
    ...     created_at=datetime.now(UTC),
    ... )
    """

    batch_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    record_count: int = Field(ge=0)
    source_distribution: dict[SourceEnum, int] = Field(default_factory=dict)
    confidence_stats: ConfidenceStats
    identifier_coverage: float = Field(ge=0.0, le=1.0)
    created_at: datetime


class BatchEnvelope(BaseModel, Generic[T]):
    """Generic envelope wrapping a batch of records with metadata.

    The ``BatchEnvelope`` is a cross-cutting concern used at every
    pipeline boundary. It wraps any list of boundary objects (typed by
    ``T``) with a ``BatchMetadata`` header containing aggregate
    statistics.

    Parameters
    ----------
    T : TypeVar
        The boundary object type (e.g., ``NormalizedRecord``,
        ``ResolvedEntity``, ``AttributionRecord``).

    Attributes
    ----------
    metadata : BatchMetadata
        Aggregate metadata for the batch.
    records : list of T
        The boundary objects in this batch.

    Examples
    --------
    >>> envelope = BatchEnvelope[NormalizedRecord](
    ...     metadata=batch_metadata,
    ...     records=normalized_records,
    ... )
    """

    metadata: BatchMetadata
    records: list[T]
