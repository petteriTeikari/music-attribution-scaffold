"""Shared enumerations for boundary object schemas.

All enums are ``StrEnum`` for JSON-friendly serialization, ensuring that
values survive round-trips through JSON/YAML without requiring custom
serializers. Domain-extensible enums (``EntityTypeEnum``,
``RelationshipTypeEnum``, ``PermissionTypeEnum``) can be extended via
domain overlay YAML in a future phase.

This module provides the single source of truth for all categorical
values used across the five-pipeline architecture (ETL, Entity Resolution,
Attribution Engine, API/MCP Server, Chat Interface). Enums are grouped
by domain:

* **Core pipeline** -- source identification, entity types, resolution
* **Attribution** -- credit roles, assurance levels, provenance events
* **Permissions** -- MCP Permission Patchbay types, values, scopes
* **Uncertainty** -- uncertainty decomposition taxonomy, calibration
* **Commercial landscape** -- training attribution, watermarking, revenue
* **Regulatory/compliance** -- EU AI Act, ISO 42001, DSM Directive

See Also
--------
Teikari, P. (2026). *Music Attribution with Transparent Confidence*.
SSRN No. 6109087 -- sections 5-7 for assurance levels and permission
patchbay design.
"""

from __future__ import annotations

from enum import StrEnum


class SourceEnum(StrEnum):
    """Data source identifiers for the ETL pipeline.

    Each value represents an external data source from which music metadata
    is ingested. The source identity is preserved throughout the entire
    pipeline so that downstream confidence scoring can apply per-source
    reliability weights. See Teikari (2026), section 5.

    Attributes
    ----------
    MUSICBRAINZ : str
        MusicBrainz open database. Community-curated, high coverage
        for Western popular music. Provides MBIDs.
    DISCOGS : str
        Discogs marketplace/database. Strong on vinyl releases, credits,
        and label information. Provides Discogs numeric IDs.
    ACOUSTID : str
        AcoustID audio fingerprint service. Matches audio signals to
        MusicBrainz recordings via Chromaprint fingerprints.
    ARTIST_INPUT : str
        Direct input from the artist or their representative. Highest
        authority for creative intent, but unverifiable by third parties.
    FILE_METADATA : str
        Embedded file metadata (ID3 tags, Vorbis comments, etc.) extracted
        from the audio file itself. Quality varies widely.

    Examples
    --------
    >>> SourceEnum.MUSICBRAINZ
    <SourceEnum.MUSICBRAINZ: 'MUSICBRAINZ'>
    >>> SourceEnum("ARTIST_INPUT")
    <SourceEnum.ARTIST_INPUT: 'ARTIST_INPUT'>
    """

    MUSICBRAINZ = "MUSICBRAINZ"
    DISCOGS = "DISCOGS"
    ACOUSTID = "ACOUSTID"
    ARTIST_INPUT = "ARTIST_INPUT"
    FILE_METADATA = "FILE_METADATA"


class EntityTypeEnum(StrEnum):
    """Music entity types within the knowledge graph.

    Follows the MusicBrainz entity model with extensions for credits.
    Entity resolution produces a unified graph where each node is typed
    by one of these values.

    Attributes
    ----------
    RECORDING : str
        A specific audio recording (a unique performance captured in a
        studio or live). Identified by ISRC.
    WORK : str
        An abstract musical composition independent of any recording.
        Identified by ISWC. A single work may have many recordings.
    ARTIST : str
        A person or group who creates or performs music. Identified by
        ISNI or IPI.
    RELEASE : str
        A packaged product (album, single, EP) containing one or more
        recordings.
    LABEL : str
        A record label or publishing entity that owns or distributes
        releases.
    CREDIT : str
        A specific attribution credit linking an artist to a recording
        or work in a particular role (e.g., producer, songwriter).

    Examples
    --------
    >>> EntityTypeEnum.RECORDING
    <EntityTypeEnum.RECORDING: 'RECORDING'>
    """

    RECORDING = "RECORDING"
    WORK = "WORK"
    ARTIST = "ARTIST"
    RELEASE = "RELEASE"
    LABEL = "LABEL"
    CREDIT = "CREDIT"


class RelationshipTypeEnum(StrEnum):
    """Relationship types between music entities in the knowledge graph.

    Edges in the entity graph are typed by these values. Each relationship
    connects a source entity (typically an artist) to a target entity
    (typically a recording or work). Relationship types map loosely to
    ``CreditRoleEnum`` but represent graph edges rather than attribution
    line items.

    Attributes
    ----------
    PERFORMED : str
        Artist performed on a recording (vocalist, instrumentalist).
    WROTE : str
        Artist wrote the underlying composition (songwriter, composer).
    PRODUCED : str
        Artist produced the recording (creative/technical oversight).
    ENGINEERED : str
        Artist served as recording engineer.
    ARRANGED : str
        Artist arranged the composition for a specific performance.
    MASTERED : str
        Artist mastered the final audio (mastering engineer).
    MIXED : str
        Artist mixed the recording (mixing engineer).
    FEATURED : str
        Artist is a featured guest on the recording.
    SAMPLED : str
        Recording contains a sample from the target recording.
    REMIXED : str
        Recording is a remix of the target recording.
    """

    PERFORMED = "PERFORMED"
    WROTE = "WROTE"
    PRODUCED = "PRODUCED"
    ENGINEERED = "ENGINEERED"
    ARRANGED = "ARRANGED"
    MASTERED = "MASTERED"
    MIXED = "MIXED"
    FEATURED = "FEATURED"
    SAMPLED = "SAMPLED"
    REMIXED = "REMIXED"


class ResolutionMethodEnum(StrEnum):
    """Entity resolution methods used to merge NormalizedRecords.

    The Entity Resolution pipeline may use one or more of these methods
    to determine whether two NormalizedRecords refer to the same real-world
    entity. Methods are ordered roughly by computational cost and
    reliability. The chosen method is recorded on each ``ResolvedEntity``
    for provenance tracing.

    Attributes
    ----------
    EXACT_ID : str
        Exact match on a standard identifier (ISRC, ISWC, ISNI, MBID).
        Highest confidence, lowest cost.
    FUZZY_STRING : str
        Fuzzy string matching on names/titles (e.g., Levenshtein,
        Jaro-Winkler). Handles typos and transliterations.
    EMBEDDING : str
        Semantic similarity via vector embeddings (e.g., sentence
        transformers). Handles paraphrases and abbreviations.
    GRAPH : str
        Graph-based resolution using relationship structure (e.g., Splink).
        Exploits co-occurrence patterns in the entity graph.
    LLM : str
        LLM-assisted resolution for ambiguous cases. Most expensive,
        used as a fallback when other methods are inconclusive.
    MANUAL : str
        Human-in-the-loop resolution by a domain expert. Triggered
        when automated methods produce low-confidence matches.
    """

    EXACT_ID = "EXACT_ID"
    FUZZY_STRING = "FUZZY_STRING"
    EMBEDDING = "EMBEDDING"
    GRAPH = "GRAPH"
    LLM = "LLM"
    MANUAL = "MANUAL"


class AssuranceLevelEnum(StrEnum):
    """Tiered provenance classification (A0--A3).

    Maps to the assurance framework from Teikari (2026), section 6.
    Higher levels require stronger evidence chains. The assurance level
    determines how much trust downstream consumers can place in an
    attribution record.

    Ordered by verification depth: ``LEVEL_0`` < ``LEVEL_1`` <
    ``LEVEL_2`` < ``LEVEL_3``.

    Attributes
    ----------
    LEVEL_0 : str
        No provenance data. Self-declared or unknown origin.
        Corresponds to A0 in the manuscript.
    LEVEL_1 : str
        Single source. Documented but not independently verified.
        Corresponds to A1. Typical for file-metadata-only records.
    LEVEL_2 : str
        Multiple sources agree. Cross-referenced and corroborated
        across at least two independent data sources. Corresponds to A2.
    LEVEL_3 : str
        Artist-verified or authority-verified. Highest assurance level.
        Requires explicit confirmation from the rights holder or an
        authoritative registry (e.g., ISNI). Corresponds to A3.

    Examples
    --------
    >>> AssuranceLevelEnum.LEVEL_3
    <AssuranceLevelEnum.LEVEL_3: 'LEVEL_3'>
    >>> AssuranceLevelEnum("LEVEL_0") < AssuranceLevelEnum("LEVEL_3")
    True
    """

    LEVEL_0 = "LEVEL_0"
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_3 = "LEVEL_3"


class ConflictSeverityEnum(StrEnum):
    """Conflict severity levels between data sources.

    When entity resolution encounters disagreements between sources for
    the same field (e.g., different release dates or artist names), the
    conflict is assigned a severity level that determines whether it can
    be auto-resolved or requires human review.

    Attributes
    ----------
    LOW : str
        Minor discrepancy, auto-resolvable. Example: trailing whitespace
        differences in artist names.
    MEDIUM : str
        Significant discrepancy requiring attention but not blocking.
        Example: different release dates within the same year.
    HIGH : str
        Major disagreement likely indicating a data quality issue.
        Example: different artist names for the same ISRC.
    CRITICAL : str
        Fundamental conflict that blocks attribution. Example:
        contradictory songwriter credits from authoritative sources.
        Always triggers ``needs_review = True``.
    """

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class CreditRoleEnum(StrEnum):
    """Credit roles for music attribution.

    These roles appear in ``Credit`` objects within ``AttributionRecord``
    and as prediction targets in conformal prediction sets. The taxonomy
    covers the most common roles found across MusicBrainz, Discogs, and
    industry metadata standards (DDEX, CWR).

    Attributes
    ----------
    PERFORMER : str
        Primary performer (vocalist or lead instrumentalist).
    SONGWRITER : str
        Songwriter (both music and lyrics). Use ``COMPOSER`` or
        ``LYRICIST`` for more specific roles.
    COMPOSER : str
        Composed the music (melody, harmony, structure).
    LYRICIST : str
        Wrote the lyrics/text.
    PRODUCER : str
        Music producer (creative and/or technical oversight of
        the recording process).
    ENGINEER : str
        Recording/tracking engineer.
    MIXING_ENGINEER : str
        Mixing engineer (balance, EQ, effects in post-production).
    MASTERING_ENGINEER : str
        Mastering engineer (final audio processing for distribution).
    ARRANGER : str
        Arranged the composition for a specific performance context.
    SESSION_MUSICIAN : str
        Session musician (hired instrumentalist, not a band member).
    FEATURED_ARTIST : str
        Featured guest artist on the recording.
    CONDUCTOR : str
        Orchestra or ensemble conductor.
    DJ : str
        DJ (for electronic music, turntablism, or mix compilations).
    REMIXER : str
        Created a remix of the original recording.
    """

    PERFORMER = "PERFORMER"
    SONGWRITER = "SONGWRITER"
    COMPOSER = "COMPOSER"
    LYRICIST = "LYRICIST"
    PRODUCER = "PRODUCER"
    ENGINEER = "ENGINEER"
    MIXING_ENGINEER = "MIXING_ENGINEER"
    MASTERING_ENGINEER = "MASTERING_ENGINEER"
    ARRANGER = "ARRANGER"
    SESSION_MUSICIAN = "SESSION_MUSICIAN"
    FEATURED_ARTIST = "FEATURED_ARTIST"
    CONDUCTOR = "CONDUCTOR"
    DJ = "DJ"
    REMIXER = "REMIXER"


class ProvenanceEventTypeEnum(StrEnum):
    """Provenance event types for the attribution audit trail.

    Every ``ProvenanceEvent`` in an ``AttributionRecord`` is typed by one
    of these values. Together they form an immutable audit chain showing
    how an attribution was constructed and refined over time.

    Attributes
    ----------
    FETCH : str
        Data fetched from an external source (ETL pipeline). Records
        which source was queried and how many records were returned.
    RESOLVE : str
        Entity resolution step. Records the method used and the
        input/output record counts.
    SCORE : str
        Confidence scoring/calibration step. Records the previous and
        new confidence values and the scoring method applied.
    REVIEW : str
        Human review event. Records who reviewed, which feedback card
        was applied, and how many corrections were made.
    UPDATE : str
        Record update event. Records version bump, fields changed,
        and what triggered the update.
    FEEDBACK : str
        Feedback integration event. Records that a ``FeedbackCard`` was
        processed and whether its corrections were accepted.
    """

    FETCH = "FETCH"
    RESOLVE = "RESOLVE"
    SCORE = "SCORE"
    REVIEW = "REVIEW"
    UPDATE = "UPDATE"
    FEEDBACK = "FEEDBACK"


class ReviewerRoleEnum(StrEnum):
    """Feedback reviewer roles for the FeedbackCard system.

    Identifies the domain expertise of the person providing feedback.
    The reviewer role affects how feedback is weighted during
    calibration updates -- artist-provided corrections carry higher
    authority than fan suggestions.

    Attributes
    ----------
    ARTIST : str
        The artist themselves (or a confirmed representative).
        Highest authority for creative intent.
    MANAGER : str
        Artist manager or business representative. Authority for
        contractual and commercial metadata.
    MUSICOLOGIST : str
        Academic musicologist or music information retrieval expert.
        Authority for compositional analysis and historical context.
    PRODUCER : str
        Music producer who worked on the recording. Authority for
        session credits and technical contributions.
    FAN : str
        Community member / fan contributor. Valuable for crowd-sourced
        corrections but requires corroboration. Lowest weight.
    """

    ARTIST = "ARTIST"
    MANAGER = "MANAGER"
    MUSICOLOGIST = "MUSICOLOGIST"
    PRODUCER = "PRODUCER"
    FAN = "FAN"


class EvidenceTypeEnum(StrEnum):
    """Evidence types supporting feedback corrections.

    When a reviewer submits a ``FeedbackCard`` with corrections, they
    must indicate what evidence supports the correction. Evidence type
    affects the credibility weighting of the correction during
    calibration updates.

    Attributes
    ----------
    LINER_NOTES : str
        Physical or digital liner notes from the release packaging.
        Strong documentary evidence.
    MEMORY : str
        Personal recollection of the reviewer (e.g., artist remembering
        who played on a session). Subject to recall bias.
    DOCUMENT : str
        Contractual or legal document (e.g., publishing agreement,
        session contract). Strongest documentary evidence.
    SESSION_NOTES : str
        Studio session notes or recording logs. Strong evidence for
        engineering and performance credits.
    OTHER : str
        Other evidence type not covered above. Requires free-text
        explanation in the ``FeedbackCard.free_text`` field.
    """

    LINER_NOTES = "LINER_NOTES"
    MEMORY = "MEMORY"
    DOCUMENT = "DOCUMENT"
    SESSION_NOTES = "SESSION_NOTES"
    OTHER = "OTHER"


class PermissionTypeEnum(StrEnum):
    """Permission types for the MCP Permission Patchbay.

    Defines the universe of machine-readable permission queries that AI
    platforms and other consumers can issue via MCP. The taxonomy is
    hierarchical: ``AI_TRAINING`` is a broad category with
    ``AI_TRAINING_COMPOSITION``, ``AI_TRAINING_RECORDING``, and
    ``AI_TRAINING_STYLE`` as finer-grained sub-permissions.

    See Teikari (2026), section 7, for the Permission Patchbay design.

    Attributes
    ----------
    STREAM : str
        Permission to stream the recording.
    DOWNLOAD : str
        Permission to download the recording for offline use.
    SYNC_LICENSE : str
        Synchronisation license (music paired with visual media).
    AI_TRAINING : str
        Broad permission for AI model training on any aspect of the work.
    AI_TRAINING_COMPOSITION : str
        AI training specifically on the compositional elements (melody,
        harmony, structure).
    AI_TRAINING_RECORDING : str
        AI training specifically on the recording (audio signal, mix,
        production qualities).
    AI_TRAINING_STYLE : str
        AI training on stylistic elements (timbre, groove, aesthetic).
    DATASET_INCLUSION : str
        Inclusion in a published research or training dataset.
    VOICE_CLONING : str
        Use of vocal performance for voice cloning / synthesis.
    STYLE_LEARNING : str
        Learning artistic style for generative imitation.
    LYRICS_IN_CHATBOTS : str
        Reproduction of lyrics in chatbot / LLM responses.
    COVER_VERSIONS : str
        Permission to create and distribute cover versions.
    REMIX : str
        Permission to create remixes of the recording.
    SAMPLE : str
        Permission to sample portions of the recording.
    DERIVATIVE_WORK : str
        Broad permission for any derivative work not covered above.
    """

    STREAM = "STREAM"
    DOWNLOAD = "DOWNLOAD"
    SYNC_LICENSE = "SYNC_LICENSE"
    AI_TRAINING = "AI_TRAINING"
    AI_TRAINING_COMPOSITION = "AI_TRAINING_COMPOSITION"
    AI_TRAINING_RECORDING = "AI_TRAINING_RECORDING"
    AI_TRAINING_STYLE = "AI_TRAINING_STYLE"
    DATASET_INCLUSION = "DATASET_INCLUSION"
    VOICE_CLONING = "VOICE_CLONING"
    STYLE_LEARNING = "STYLE_LEARNING"
    LYRICS_IN_CHATBOTS = "LYRICS_IN_CHATBOTS"
    COVER_VERSIONS = "COVER_VERSIONS"
    REMIX = "REMIX"
    SAMPLE = "SAMPLE"
    DERIVATIVE_WORK = "DERIVATIVE_WORK"


class PermissionValueEnum(StrEnum):
    """Permission response values for MCP consent queries.

    Each permission entry in a ``PermissionBundle`` resolves to one of
    these values. The values form a spectrum from unconditional denial
    to unconditional allowance, with conditional variants in between.

    Attributes
    ----------
    ALLOW : str
        Unconditional permission granted.
    DENY : str
        Permission explicitly denied. No exceptions.
    ASK : str
        Permission not pre-determined; the requester must contact the
        rights holder for case-by-case approval.
    ALLOW_WITH_ATTRIBUTION : str
        Permission granted on condition that proper attribution is
        included. Requires ``PermissionEntry.attribution_requirement``
        to specify the required attribution text.
    ALLOW_WITH_ROYALTY : str
        Permission granted on condition of royalty payment. Requires
        ``PermissionEntry.royalty_rate`` to specify the rate.
    """

    ALLOW = "ALLOW"
    DENY = "DENY"
    ASK = "ASK"
    ALLOW_WITH_ATTRIBUTION = "ALLOW_WITH_ATTRIBUTION"
    ALLOW_WITH_ROYALTY = "ALLOW_WITH_ROYALTY"


class PermissionScopeEnum(StrEnum):
    """Permission scope levels defining granularity of consent.

    Permissions can be set at different levels of granularity, from an
    entire catalog down to a single work. Broader scopes act as defaults
    that can be overridden by narrower scopes.

    Attributes
    ----------
    CATALOG : str
        Applies to the entire catalog of the rights holder. Broadest
        scope. When scope is CATALOG, ``scope_entity_id`` must be None.
    RELEASE : str
        Applies to a specific release (album, EP, single). Requires
        ``scope_entity_id`` pointing to the release entity.
    RECORDING : str
        Applies to a specific recording. Requires ``scope_entity_id``
        pointing to the recording entity.
    WORK : str
        Applies to a specific musical work (composition). Requires
        ``scope_entity_id`` pointing to the work entity.
    """

    CATALOG = "CATALOG"
    RELEASE = "RELEASE"
    RECORDING = "RECORDING"
    WORK = "WORK"


class DelegationRoleEnum(StrEnum):
    """Delegation chain roles in the permission hierarchy.

    A ``PermissionBundle`` may include a delegation chain showing who
    granted permission authority to whom. This enables audit trails
    for permission provenance (e.g., artist -> manager -> label ->
    distributor).

    Attributes
    ----------
    OWNER : str
        Original rights holder (typically the artist or songwriter).
        Root of the delegation chain.
    MANAGER : str
        Artist manager or business representative acting on behalf
        of the owner.
    LABEL : str
        Record label holding master recording rights via contract.
    DISTRIBUTOR : str
        Digital distributor handling platform delivery. Typically
        the outermost link in the delegation chain.
    """

    OWNER = "OWNER"
    MANAGER = "MANAGER"
    LABEL = "LABEL"
    DISTRIBUTOR = "DISTRIBUTOR"


class PipelineFeedbackTypeEnum(StrEnum):
    """Pipeline feedback signal types for continuous improvement.

    These are reverse-flow signals between pipelines, enabling the
    system to self-correct. For example, the Attribution Engine can
    signal back to Entity Resolution that its confidence estimates
    were miscalibrated, or the API layer can signal a dispute.

    Attributes
    ----------
    REFETCH : str
        Signal from Entity Resolution to ETL: "data from source X is
        consistently wrong or stale, re-fetch from the source."
    RECALIBRATE : str
        Signal from Attribution Engine to Entity Resolution: "resolution
        confidence was miscalibrated; predicted confidence differs
        significantly from actual accuracy."
    DISPUTE : str
        Signal from API/Chat to Attribution Engine: "a user or rights
        holder has disputed this attribution; re-evaluate."
    STALE : str
        Signal from any pipeline: "this record has not been refreshed
        within its expected freshness window."
    """

    REFETCH = "REFETCH"
    RECALIBRATE = "RECALIBRATE"
    DISPUTE = "DISPUTE"
    STALE = "STALE"


class UncertaintySourceEnum(StrEnum):
    """Uncertainty source taxonomy based on UProp (Duan 2025).

    Classifies the origin of uncertainty in confidence estimates.
    The intrinsic/extrinsic decomposition (Duan 2025, arXiv:2506.17419)
    is the primary axis; aleatoric/epistemic is the classical secondary
    axis for compatibility with standard ML uncertainty literature.

    Attributes
    ----------
    INTRINSIC : str
        Intrinsic uncertainty arising from noise in the input data
        itself (e.g., conflicting metadata across sources, ambiguous
        artist names).
    EXTRINSIC : str
        Extrinsic uncertainty arising from the model or pipeline
        (e.g., embedding model limitations, resolution algorithm
        edge cases).
    ALEATORIC : str
        Irreducible uncertainty inherent in the data-generating process.
        Cannot be reduced by collecting more data.
    EPISTEMIC : str
        Reducible uncertainty due to limited knowledge or data.
        Can be reduced by collecting more evidence or better models.
    """

    INTRINSIC = "INTRINSIC"
    EXTRINSIC = "EXTRINSIC"
    ALEATORIC = "ALEATORIC"
    EPISTEMIC = "EPISTEMIC"


class UncertaintyDimensionEnum(StrEnum):
    """4-dimensional uncertainty framework (Liu 2025, arXiv:2503.15850).

    Orthogonal to the intrinsic/extrinsic decomposition, this framework
    decomposes uncertainty along the information processing pipeline:
    from input through reasoning to final prediction.

    Attributes
    ----------
    INPUT : str
        Uncertainty in the input data (noise, missing fields, ambiguity).
        Maps to ``StepUncertainty.input_uncertainty``.
    REASONING : str
        Uncertainty in the reasoning/inference process (e.g., entity
        resolution logic, LLM chain-of-thought). Maps to
        ``StepUncertainty.reasoning_uncertainty``.
    PARAMETER : str
        Uncertainty in model parameters (e.g., embedding model weights,
        fuzzy matching thresholds). Maps to
        ``StepUncertainty.parameter_uncertainty``.
    PREDICTION : str
        Uncertainty in the final prediction/output (e.g., the confidence
        score itself). Maps to
        ``StepUncertainty.prediction_uncertainty``.
    """

    INPUT = "INPUT"
    REASONING = "REASONING"
    PARAMETER = "PARAMETER"
    PREDICTION = "PREDICTION"


class ConfidenceMethodEnum(StrEnum):
    """Methods used to produce confidence scores.

    Each ``StepUncertainty`` records which method was used to generate
    its confidence estimate. Methods vary in cost, reliability, and
    calibration quality. See Teikari (2026), section 5, for the
    confidence scoring framework.

    Attributes
    ----------
    SELF_REPORT : str
        Source-reported confidence (e.g., MusicBrainz data quality
        rating). Cheapest but least calibrated.
    MULTI_SAMPLE : str
        Multiple-sample consistency (e.g., querying an LLM multiple
        times and measuring agreement).
    LOGPROB : str
        Token log-probability from an LLM. Fast but requires logprob
        API access.
    ENSEMBLE : str
        Ensemble of multiple models or methods. More expensive but
        better calibrated than single-model approaches.
    CONFORMAL : str
        Conformal prediction providing coverage guarantees. Produces
        prediction sets rather than point estimates.
    SOURCE_WEIGHTED : str
        Weighted average across data sources based on historical
        reliability (Yanez 2025 approach).
    HUMAN_RATED : str
        Human expert rating. Highest authority but most expensive
        and slowest.
    HTC : str
        Holistic Trajectory Calibration (Zhang 2026, arXiv:2601.15778).
        Uses trajectory-level features across the full pipeline for
        calibration.
    """

    SELF_REPORT = "SELF_REPORT"
    MULTI_SAMPLE = "MULTI_SAMPLE"
    LOGPROB = "LOGPROB"
    ENSEMBLE = "ENSEMBLE"
    CONFORMAL = "CONFORMAL"
    SOURCE_WEIGHTED = "SOURCE_WEIGHTED"
    HUMAN_RATED = "HUMAN_RATED"
    HTC = "HTC"


class CalibrationStatusEnum(StrEnum):
    """Calibration status of a confidence score.

    Indicates whether a confidence score has been post-hoc calibrated
    (e.g., via Platt scaling or isotonic regression) to ensure that
    stated confidence matches empirical accuracy.

    Attributes
    ----------
    CALIBRATED : str
        Score has been calibrated against a held-out calibration set.
        ``CalibrationMetadata.expected_calibration_error`` is meaningful.
    UNCALIBRATED : str
        Score is raw/uncalibrated. May exhibit over- or under-confidence.
    PENDING : str
        Calibration is pending (insufficient calibration data collected
        so far). Score should be treated as uncalibrated.
    """

    CALIBRATED = "CALIBRATED"
    UNCALIBRATED = "UNCALIBRATED"
    PENDING = "PENDING"


class ConfidenceTrendEnum(StrEnum):
    """Confidence trend across pipeline steps (Zhang 2026).

    Characterises the trajectory of confidence scores as a record
    passes through the pipeline. Used by ``TrajectoryCalibration``
    for HTC-based calibration. See Zhang (2026, arXiv:2601.15778).

    Attributes
    ----------
    INCREASING : str
        Confidence monotonically increases across steps. Typical when
        multiple corroborating sources are found.
    DECREASING : str
        Confidence monotonically decreases. May indicate conflicting
        evidence discovered during resolution.
    STABLE : str
        Confidence remains approximately constant. Typical for records
        with strong initial evidence (e.g., exact ID match).
    VOLATILE : str
        Confidence oscillates across steps. May indicate unstable
        resolution or contradictory evidence. Often triggers
        ``needs_review = True``.
    """

    INCREASING = "INCREASING"
    DECREASING = "DECREASING"
    STABLE = "STABLE"
    VOLATILE = "VOLATILE"


# --- Commercial Landscape Enums (future-readiness stubs) ---


class AttributionMethodEnum(StrEnum):
    """Training data attribution (TDA) methods.

    Future-readiness stubs for commercial landscape parity with Musical AI,
    Sureel, ProRata, and Sony's influence-function approach. These methods
    attempt to quantify how much a specific training example influenced a
    generative model's output.

    Attributes
    ----------
    TRAINING_TIME_INFLUENCE : str
        Influence measured at training time (e.g., data Shapley values,
        TracIn). Requires access to training checkpoints.
    UNLEARNING_BASED : str
        Influence measured via machine unlearning (retrain-without and
        compare). Expensive but theoretically sound.
    INFLUENCE_FUNCTIONS : str
        Classical influence functions (Koh & Liang 2017). Approximates
        leave-one-out retraining via Hessian-vector products.
    EMBEDDING_SIMILARITY : str
        Cosine similarity in embedding space between source and generated
        content. Cheapest but least rigorous.
    WATERMARK_DETECTION : str
        Detection of embedded watermarks in generated content that trace
        back to training data (e.g., SynthID, AudioSeal).
    INFERENCE_TIME_CONDITIONING : str
        Attribution via inference-time conditioning or prompting (e.g.,
        Musical AI's approach of conditioning generation on a known work).
    """

    TRAINING_TIME_INFLUENCE = "TRAINING_TIME_INFLUENCE"
    UNLEARNING_BASED = "UNLEARNING_BASED"
    INFLUENCE_FUNCTIONS = "INFLUENCE_FUNCTIONS"
    EMBEDDING_SIMILARITY = "EMBEDDING_SIMILARITY"
    WATERMARK_DETECTION = "WATERMARK_DETECTION"
    INFERENCE_TIME_CONDITIONING = "INFERENCE_TIME_CONDITIONING"


class RightsTypeEnum(StrEnum):
    """Music rights types distinguishing compositional vs recording rights.

    Future-readiness stub. In music licensing, rights are split between
    the composition (publishing) side and the recording (master) side.
    This distinction is critical for AI training attribution: a model
    may learn from the composition, the recording, or both.

    Based on Sureel patent and LANDR rights management approaches.

    Attributes
    ----------
    MASTER_RECORDING : str
        Rights in the specific audio recording (sound recording copyright).
        Typically held by the label or artist.
    COMPOSITION_PUBLISHING : str
        Rights in the underlying composition (musical work copyright).
        Typically held by the publisher or songwriter.
    PERFORMANCE : str
        Performance rights (public performance, broadcast). Managed by
        PROs (ASCAP, BMI, PRS, GEMA, etc.).
    MECHANICAL : str
        Mechanical reproduction rights (physical copies, downloads,
        interactive streams).
    SYNC : str
        Synchronisation rights (pairing music with visual media).
    """

    MASTER_RECORDING = "MASTER_RECORDING"
    COMPOSITION_PUBLISHING = "COMPOSITION_PUBLISHING"
    PERFORMANCE = "PERFORMANCE"
    MECHANICAL = "MECHANICAL"
    SYNC = "SYNC"


class MediaTypeEnum(StrEnum):
    """Multi-modal attribution media types.

    Future-readiness stub for multi-modal training data attribution.
    While this scaffold focuses on audio, the Sureel and ProRata
    approaches are modality-agnostic and support cross-modal attribution.

    Attributes
    ----------
    AUDIO : str
        Audio content (waveform, spectrogram). Primary modality for
        this scaffold.
    IMAGE : str
        Image content (album art, spectrograms as images).
    VIDEO : str
        Video content (music videos, live performances).
    TEXT : str
        Text content (lyrics, liner notes, reviews).
    SYMBOLIC_MUSIC : str
        Symbolic music representations (MIDI, MusicXML, ABC notation).
    MULTIMODAL : str
        Content spanning multiple modalities simultaneously.
    """

    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    TEXT = "TEXT"
    SYMBOLIC_MUSIC = "SYMBOLIC_MUSIC"
    MULTIMODAL = "MULTIMODAL"


class CertificationTypeEnum(StrEnum):
    """External certification and compliance attestation types.

    Future-readiness stub for third-party certifications that validate
    an AI system's training data practices. These certifications are
    attached to ``ComplianceAttestation`` records.

    Attributes
    ----------
    FAIRLY_TRAINED_LICENSED : str
        Fairly Trained certification indicating all training data was
        licensed or in the public domain.
    C2PA_PROVENANCE : str
        C2PA (Coalition for Content Provenance and Authenticity)
        provenance manifest attached to generated content.
    EU_AI_ACT_COMPLIANT : str
        Self-declared or audited compliance with EU AI Act requirements
        for general-purpose AI (GPAI) models.
    CMO_APPROVED : str
        Approved by a Collective Management Organisation (CMO) such as
        GEMA, PRS, or ASCAP for training data usage.
    """

    FAIRLY_TRAINED_LICENSED = "FAIRLY_TRAINED_LICENSED"
    C2PA_PROVENANCE = "C2PA_PROVENANCE"
    EU_AI_ACT_COMPLIANT = "EU_AI_ACT_COMPLIANT"
    CMO_APPROVED = "CMO_APPROVED"


class WatermarkTypeEnum(StrEnum):
    """Audio watermark types for provenance tracking.

    Future-readiness stub for audio watermarking systems that embed
    imperceptible identifiers in audio signals. Watermarks enable
    post-hoc attribution of AI-generated content back to training data
    or generation source.

    Attributes
    ----------
    SYNTHID : str
        Google DeepMind's SynthID audio watermarking. Embeds identifiers
        in spectrogram space.
    AUDIOSEAL : str
        Meta's AudioSeal. Localised audio watermarking with detector
        that identifies watermarked segments.
    WAVMARK : str
        WavMark academic watermarking approach. Embeds in the waveform
        domain.
    DIGIMARC : str
        Digimarc commercial watermarking. Used in broadcast monitoring
        and content identification.
    """

    SYNTHID = "SYNTHID"
    AUDIOSEAL = "AUDIOSEAL"
    WAVMARK = "WAVMARK"
    DIGIMARC = "DIGIMARC"


class RevenueModelEnum(StrEnum):
    """Revenue sharing models for AI-generated music attribution.

    Future-readiness stub for commercial revenue distribution models.
    Different platforms use different approaches to compensate rights
    holders whose works contributed to AI training.

    Attributes
    ----------
    FLAT_FEE_UPFRONT : str
        One-time flat fee paid for training data licensing (e.g., LANDR
        model for stem packs).
    PRO_RATA_MONTHLY : str
        Monthly pro-rata distribution based on catalog size or usage
        (e.g., streaming royalty model applied to AI training).
    PER_GENERATION : str
        Payment per generation event that uses the rights holder's
        contribution (e.g., Kits AI voice model usage).
    INFLUENCE_BASED : str
        Payment proportional to measured influence on generated output
        (e.g., Musical AI / Sureel approach using TDA methods).
    """

    FLAT_FEE_UPFRONT = "FLAT_FEE_UPFRONT"
    PRO_RATA_MONTHLY = "PRO_RATA_MONTHLY"
    PER_GENERATION = "PER_GENERATION"
    INFLUENCE_BASED = "INFLUENCE_BASED"


# --- Regulatory/Compliance Enums (ISO 42001 vs EU AI Act) ---


class RegulatoryFrameworkEnum(StrEnum):
    """Applicable regulatory and governance frameworks.

    ISO 42001 defines internal AI governance roles; EU AI Act defines
    supply chain liability actors. They have zero terminological overlap
    and must be tracked separately. See Teikari (2026), section 8, for
    the regulatory mapping.

    Attributes
    ----------
    ISO_42001 : str
        ISO/IEC 42001 AI Management System standard. Defines internal
        governance roles (Top Management, AI System Owner, Internal Audit).
    EU_AI_ACT : str
        EU Artificial Intelligence Act (Regulation 2024/1689). Defines
        risk categories and obligations for AI system providers/deployers.
    GPAI_CODE_OF_PRACTICE : str
        General-Purpose AI Model Code of Practice (July 2025). Specifies
        transparency and copyright compliance requirements for GPAI models.
    DSM_DIRECTIVE : str
        EU Digital Single Market Directive (2019/790). Art. 3-4 govern
        text-and-data mining exceptions and opt-out mechanisms.
    ESPR_DPP : str
        EU Ecodesign for Sustainable Products Regulation / Digital Product
        Passport. Cross-domain provenance framework.
    GDPR : str
        EU General Data Protection Regulation. Relevant when attribution
        records contain personal data (artist identities, reviewer info).
    """

    ISO_42001 = "ISO_42001"
    EU_AI_ACT = "EU_AI_ACT"
    GPAI_CODE_OF_PRACTICE = "GPAI_CODE_OF_PRACTICE"
    DSM_DIRECTIVE = "DSM_DIRECTIVE"
    ESPR_DPP = "ESPR_DPP"
    GDPR = "GDPR"


class ComplianceActorEnum(StrEnum):
    """EU AI Act supply chain actors (Art. 3).

    These are distinct from ISO 42001 internal governance roles (Top
    Management, AI System Owner, Internal Audit). An organization may
    simultaneously hold multiple actor classifications across different
    AI systems.

    Attributes
    ----------
    PROVIDER : str
        Entity that develops or has an AI system developed and places it
        on the market or puts it into service (Art. 3(3)).
    DEPLOYER : str
        Entity that uses an AI system under its authority (Art. 3(4)).
        The music platform using the attribution system.
    AUTHORISED_REPRESENTATIVE : str
        Entity established in the EU mandated by a non-EU provider to
        act on their behalf (Art. 3(5)).
    IMPORTER : str
        Entity established in the EU that places an AI system from a
        third country on the EU market (Art. 3(6)).
    DISTRIBUTOR : str
        Entity in the supply chain that makes an AI system available on
        the EU market (Art. 3(7)).
    PRODUCT_MANUFACTURER : str
        Manufacturer of a product that integrates an AI system as a
        safety component (Art. 3(8)).
    """

    PROVIDER = "PROVIDER"
    DEPLOYER = "DEPLOYER"
    AUTHORISED_REPRESENTATIVE = "AUTHORISED_REPRESENTATIVE"
    IMPORTER = "IMPORTER"
    DISTRIBUTOR = "DISTRIBUTOR"
    PRODUCT_MANUFACTURER = "PRODUCT_MANUFACTURER"


class TdmReservationMethodEnum(StrEnum):
    """Text-and-data-mining rights reservation methods.

    Under EU DSM Directive Art. 4, copyright holders can opt out of TDM
    via machine-readable reservation. The GPAI Code of Practice (July 2025)
    requires providers to respect robots.txt and emerging protocols.
    Music has a structural gap: robots.txt is web-only and does not cover
    audio content accessed via APIs or streaming platforms.

    See Teikari (2026), section 7, for the music-specific gap analysis.

    Attributes
    ----------
    ROBOTS_TXT : str
        Standard robots.txt file on web servers. Web-only; does not
        cover audio files served via APIs or streaming platforms.
    LLMS_TXT : str
        Emerging llms.txt protocol for specifying LLM training
        permissions at the domain level.
    MACHINE_READABLE_TAG : str
        HTML meta tags or HTTP headers expressing TDM reservation
        (e.g., ``<meta name="tdm-reservation" content="1">``).
    RIGHTS_RESERVATION_API : str
        Programmatic API for querying rights reservation status.
        More flexible than static files but requires infrastructure.
    MCP_PERMISSION_QUERY : str
        Model Context Protocol permission query. The approach advocated
        by this scaffold: machine-readable consent queries via MCP tools.
    """

    ROBOTS_TXT = "ROBOTS_TXT"
    LLMS_TXT = "LLMS_TXT"
    MACHINE_READABLE_TAG = "MACHINE_READABLE_TAG"
    RIGHTS_RESERVATION_API = "RIGHTS_RESERVATION_API"
    MCP_PERMISSION_QUERY = "MCP_PERMISSION_QUERY"
