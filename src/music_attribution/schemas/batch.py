"""Batch metadata envelope for pipeline boundary crossing.

Wraps boundary object collections in a BatchMetadata envelope with
statistical summary. Enables full provenance tracing and quality
monitoring across the attribution pipeline.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from music_attribution.schemas.enums import SourceEnum

T = TypeVar("T")


class ConfidenceStats(BaseModel):
    """Statistical summary of confidence scores in a batch."""

    mean: float
    std: float
    min_val: float
    max_val: float
    median: float
    count: int = Field(ge=0)


class BatchMetadata(BaseModel):
    """Metadata envelope for a batch of records at pipeline boundary."""

    batch_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    record_count: int = Field(ge=0)
    source_distribution: dict[SourceEnum, int] = Field(default_factory=dict)
    confidence_stats: ConfidenceStats
    identifier_coverage: float = Field(ge=0.0, le=1.0)
    created_at: datetime


class BatchEnvelope(BaseModel, Generic[T]):
    """Generic envelope wrapping a batch of records with metadata."""

    metadata: BatchMetadata
    records: list[T]
