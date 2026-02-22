"""Shared test factories — single source of truth for domain object construction.

Replaces 8+ near-identical ``_make_attribution`` / ``_make_record`` helpers
scattered across test files.  Each factory uses ``**overrides`` for maximum
flexibility while providing sensible defaults.

Usage::

    from tests.factories import make_attribution, make_credit

    record = make_attribution(confidence_score=0.5, needs_review=True)
    credit = make_credit(entity_name="Imogen Heap")
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from music_attribution.schemas.attribution import (
    AttributionRecord,
    ConformalSet,
    Credit,
)
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
    SourceEnum,
)


def make_credit(**overrides: object) -> Credit:
    """Create a Credit with sensible defaults.

    Parameters
    ----------
    **overrides
        Any Credit field to override (entity_id, entity_name, role,
        confidence, sources, assurance_level, role_detail).

    Returns
    -------
    Credit
        A valid Credit instance.
    """
    defaults: dict = {
        "entity_id": uuid.uuid4(),
        "entity_name": "",
        "role": CreditRoleEnum.PERFORMER,
        "confidence": 0.9,
        "sources": [SourceEnum.MUSICBRAINZ],
        "assurance_level": AssuranceLevelEnum.LEVEL_2,
    }
    defaults.update(overrides)
    return Credit(**defaults)


def make_conformal_set(**overrides: object) -> ConformalSet:
    """Create a ConformalSet with sensible defaults.

    Parameters
    ----------
    **overrides
        Any ConformalSet field to override.

    Returns
    -------
    ConformalSet
        A valid ConformalSet instance.
    """
    defaults: dict = {
        "coverage_level": 0.9,
        "marginal_coverage": 0.9,
        "calibration_error": 0.02,
        "calibration_method": "APS",
        "calibration_set_size": 100,
    }
    defaults.update(overrides)
    return ConformalSet(**defaults)


def make_attribution(**overrides: object) -> AttributionRecord:
    """Create an AttributionRecord with sensible defaults.

    Accepts any ``AttributionRecord`` field as a keyword argument.
    If ``credits`` is not provided, a single default Credit is created.
    If ``conformal_set`` is not provided (or is a dict), a default
    ConformalSet is created.

    Parameters
    ----------
    **overrides
        Any AttributionRecord field to override (work_entity_id,
        confidence_score, source_agreement, needs_review,
        review_priority, version, credits, conformal_set, etc.).

    Returns
    -------
    AttributionRecord
        A valid AttributionRecord instance.

    Examples
    --------
    >>> record = make_attribution(confidence_score=0.5, needs_review=True)
    >>> record.confidence_score
    0.5
    >>> record = make_attribution(
    ...     credits=[make_credit(entity_name="Imogen Heap")],
    ...     work_title="Hide and Seek",
    ... )
    """
    now = datetime.now(UTC)

    # Handle conformal_set: allow dict or ConformalSet or omit
    conformal = overrides.pop("conformal_set", None) if "conformal_set" in overrides else None  # type: ignore[arg-type]
    if conformal is None:
        conformal = make_conformal_set()
    elif isinstance(conformal, dict):
        conformal = make_conformal_set(**conformal)

    defaults: dict = {
        "work_entity_id": uuid.uuid4(),
        "credits": [make_credit()],
        "assurance_level": AssuranceLevelEnum.LEVEL_2,
        "confidence_score": 0.9,
        "conformal_set": conformal,
        "source_agreement": 0.95,
        "needs_review": False,
        "review_priority": 0.1,
        "created_at": now,
        "updated_at": now,
        "version": 1,
    }
    defaults.update(overrides)
    return AttributionRecord(**defaults)
