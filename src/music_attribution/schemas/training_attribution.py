"""Stub schemas for training data attribution (TDA).

Future-readiness stubs for commercial landscape parity with
Musical AI, Sureel, ProRata, and Sony's influence-function approach.
No business logic — schema definitions only.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from music_attribution.schemas.enums import AttributionMethodEnum, MediaTypeEnum


class TemporalSegment(BaseModel):
    """A time segment within an audio work with influence weighting."""

    start_seconds: float = Field(ge=0.0)
    end_seconds: float = Field(ge=0.0)
    influence_weight: float = Field(ge=0.0, le=1.0)


class StemInfluence(BaseModel):
    """Per-stem influence attribution (vocals, drums, bass, etc.)."""

    stem_type: str
    media_type: MediaTypeEnum
    influence_weight: float = Field(ge=0.0, le=1.0)


class TrainingInfluence(BaseModel):
    """Training data attribution record linking source work to trained model.

    Represents a single influence measurement from a source work
    on a generative model's output, using one of several TDA methods.
    """

    source_work_id: str
    target_model_id: str
    method: AttributionMethodEnum
    influence_percentage: float = Field(ge=0.0, le=100.0)
    confidence: float = Field(ge=0.0, le=1.0)
    temporal_segments: list[TemporalSegment] = Field(default_factory=list)
    stem_influences: list[StemInfluence] = Field(default_factory=list)
