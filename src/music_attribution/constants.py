"""Shared constants for the music attribution scaffold.

Centralises magic numbers, confidence thresholds, and source reliability
weights that are referenced across multiple modules. Domain-specific
constants that are used only within a single module should stay local.

The confidence tier thresholds map directly to the frontend CSS tokens
(``--color-confidence-high``, ``--color-confidence-medium``,
``--color-confidence-low``) and the A0--A3 assurance-level colour scheme
defined in ``frontend/src/app/globals.css``.

Source reliability weights are the default priors for the
``CreditAggregator``'s weighted voting scheme
(see Teikari 2026, Section 4 on source agreement).

Constants
---------
CONFIDENCE_HIGH_THRESHOLD : float
    Scores >= 0.85 are "high confidence" (green tier).
CONFIDENCE_MEDIUM_THRESHOLD : float
    Scores >= 0.50 are "medium confidence" (amber tier);
    below is "low confidence" (red tier).
REVIEW_THRESHOLD : float
    Alias for ``CONFIDENCE_MEDIUM_THRESHOLD``. Records below this
    score are flagged for human review.
SOURCE_RELIABILITY_WEIGHTS : dict[SourceEnum, float]
    Default weight per data source for weighted aggregation (0.0--1.0).
    MusicBrainz is the most trusted (0.95), Artist Input the least
    (0.60) due to potential self-reporting bias.
"""

from __future__ import annotations

from music_attribution.schemas.enums import SourceEnum

# ── Confidence tier boundaries ──────────────────────────────────────
# Used by: aggregator (needs_review), seed data, frontend CSS tokens
CONFIDENCE_HIGH_THRESHOLD: float = 0.85
"""Confidence >= this is "high" (green tier)."""

CONFIDENCE_MEDIUM_THRESHOLD: float = 0.50
"""Confidence >= this is "medium" (amber tier); below is "low" (red)."""

REVIEW_THRESHOLD: float = CONFIDENCE_MEDIUM_THRESHOLD
"""Attributions below this score are flagged for human review."""

# ── Source agreement description thresholds ─────────────────────────
# Used by: chat agent (explain_confidence), voice tools
AGREEMENT_HIGH_THRESHOLD: float = 0.80
"""Source agreement >= this is described as "High"."""

AGREEMENT_MODERATE_THRESHOLD: float = 0.50
"""Source agreement >= this is described as "Moderate"; below is "Low"."""

# ── Center-bias detection ───────────────────────────────────────────
# Used by: FeedbackCard validator, chat agent, voice tools
CENTER_BIAS_LOW: float = 0.45
"""Lower bound of center-bias detection range."""

CENTER_BIAS_HIGH: float = 0.55
"""Upper bound of center-bias detection range."""

# ── Default source reliability weights ──────────────────────────────
# Used by: CreditAggregator (weighted voting), tests
SOURCE_RELIABILITY_WEIGHTS: dict[SourceEnum, float] = {
    SourceEnum.MUSICBRAINZ: 0.95,
    SourceEnum.DISCOGS: 0.85,
    SourceEnum.ACOUSTID: 0.80,
    SourceEnum.FILE_METADATA: 0.70,
    SourceEnum.ARTIST_INPUT: 0.60,
}
"""Default weight per data source for weighted aggregation (0.0–1.0)."""
