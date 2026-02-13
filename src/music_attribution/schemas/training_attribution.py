"""Stub schemas for training data attribution (TDA).

Future-readiness stubs for commercial landscape parity with Musical AI,
Sureel, ProRata, and Sony's influence-function approach. These schemas
model the relationship between source training data and generative AI
model outputs, enabling attribution-by-design for AI-generated music.

These are schema definitions only -- no business logic. They will be
populated when integration with TDA platforms is implemented.

See Also
--------
music_attribution.schemas.enums.AttributionMethodEnum : TDA methods.
music_attribution.schemas.enums.MediaTypeEnum : Multi-modal media types.
Teikari, P. (2026). *Music Attribution with Transparent Confidence*,
    section 9 (commercial landscape).
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from music_attribution.schemas.enums import AttributionMethodEnum, MediaTypeEnum


class TemporalSegment(BaseModel):
    """A time segment within an audio work with influence weighting.

    Represents a specific time range within a source audio work that
    contributed to a generative model's output. Enables fine-grained
    temporal attribution (e.g., "the chorus from 1:30-2:15 was most
    influential").

    Attributes
    ----------
    start_seconds : float
        Start time of the segment in seconds from the beginning of the
        audio. Non-negative.
    end_seconds : float
        End time of the segment in seconds. Non-negative. Should be
        > ``start_seconds``.
    influence_weight : float
        How much this temporal segment influenced the generated output,
        range [0.0, 1.0]. Weights across segments for a single source
        work should sum to approximately 1.0.

    Examples
    --------
    >>> segment = TemporalSegment(
    ...     start_seconds=90.0,
    ...     end_seconds=135.0,
    ...     influence_weight=0.45,
    ... )
    """

    start_seconds: float = Field(ge=0.0)
    end_seconds: float = Field(ge=0.0)
    influence_weight: float = Field(ge=0.0, le=1.0)


class StemInfluence(BaseModel):
    """Per-stem influence attribution (vocals, drums, bass, etc.).

    Decomposes influence by audio stem, enabling attribution statements
    like "the vocal style was 40% influenced by Artist X, but the drum
    patterns were 60% influenced by Artist Y."

    Attributes
    ----------
    stem_type : str
        Type of audio stem (e.g., ``"vocals"``, ``"drums"``, ``"bass"``,
        ``"keys"``, ``"other"``). Free-text to accommodate various
        source separation taxonomies.
    media_type : MediaTypeEnum
        Media modality of this stem. Typically AUDIO, but could be
        SYMBOLIC_MUSIC for MIDI-based stems.
    influence_weight : float
        How much this stem influenced the generated output for the
        corresponding stem type, range [0.0, 1.0].

    Examples
    --------
    >>> stem = StemInfluence(
    ...     stem_type="vocals",
    ...     media_type=MediaTypeEnum.AUDIO,
    ...     influence_weight=0.40,
    ... )
    """

    stem_type: str
    media_type: MediaTypeEnum
    influence_weight: float = Field(ge=0.0, le=1.0)


class TrainingInfluence(BaseModel):
    """Training data attribution record linking source work to trained model.

    Represents a single influence measurement from a source musical work
    on a generative AI model's output, using one of several training data
    attribution (TDA) methods. This is the core data structure for
    answering "which training examples influenced this generated output?"

    Attributes
    ----------
    source_work_id : str
        Identifier of the source work that contributed to training
        (could be an ISRC, ISWC, or internal catalog ID).
    target_model_id : str
        Identifier of the generative model whose output is being
        attributed (e.g., model name + version).
    method : AttributionMethodEnum
        The TDA method used to measure influence (e.g.,
        TRAINING_TIME_INFLUENCE, INFLUENCE_FUNCTIONS,
        EMBEDDING_SIMILARITY).
    influence_percentage : float
        Measured influence as a percentage, range [0.0, 100.0].
        Sum across all source works for a single generation should
        ideally approximate 100.0.
    confidence : float
        Confidence in the influence measurement, range [0.0, 1.0].
        Higher confidence when using more rigorous methods (e.g.,
        influence functions vs. embedding similarity).
    temporal_segments : list of TemporalSegment
        Fine-grained temporal attribution within the source work.
        Empty if temporal decomposition was not performed.
    stem_influences : list of StemInfluence
        Per-stem influence decomposition (vocals, drums, etc.).
        Empty if stem decomposition was not performed.

    Examples
    --------
    >>> influence = TrainingInfluence(
    ...     source_work_id="GBAYE0601498",
    ...     target_model_id="music-gen-v2.1",
    ...     method=AttributionMethodEnum.INFLUENCE_FUNCTIONS,
    ...     influence_percentage=3.2,
    ...     confidence=0.78,
    ...     temporal_segments=[
    ...         TemporalSegment(
    ...             start_seconds=90.0,
    ...             end_seconds=135.0,
    ...             influence_weight=0.45,
    ...         ),
    ...     ],
    ... )
    """

    source_work_id: str
    target_model_id: str
    method: AttributionMethodEnum
    influence_percentage: float = Field(ge=0.0, le=100.0)
    confidence: float = Field(ge=0.0, le=1.0)
    temporal_segments: list[TemporalSegment] = Field(default_factory=list)
    stem_influences: list[StemInfluence] = Field(default_factory=list)
