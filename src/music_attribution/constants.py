"""Shared constants for the music attribution scaffold.

Centralizes magic numbers and thresholds that are referenced
across multiple modules. Domain-specific constants that are
only used within a single module should stay local.
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
