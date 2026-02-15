"""Boundary object schemas for the Music Attribution Scaffold.

These Pydantic models define the data contracts between the five
pipelines in the attribution architecture:

* ``NormalizedRecord`` (BO-1): Data Engineering -> Entity Resolution
* ``ResolvedEntity`` (BO-2): Entity Resolution -> Attribution Engine
* ``AttributionRecord`` (BO-3): Attribution Engine -> API/MCP + Chat
* ``FeedbackCard`` (BO-4): Chat Interface -> Attribution Engine (reverse)
* ``PermissionBundle`` (BO-5): API/MCP Server (consent queries)

Cross-cutting schemas (``BatchEnvelope``, ``PipelineFeedback``,
``UncertaintyAwareProvenance``) and future-readiness stubs
(``ComplianceAttestation``, ``TrainingInfluence``) are available in
their respective submodules.

See Also
--------
Teikari, P. (2026). *Music Attribution with Transparent Confidence*.
    SSRN No. 6109087.
"""

from __future__ import annotations

from music_attribution.schemas.attribution import AttributionRecord
from music_attribution.schemas.feedback import FeedbackCard
from music_attribution.schemas.normalized import NormalizedRecord
from music_attribution.schemas.permissions import PermissionBundle
from music_attribution.schemas.resolved import ResolvedEntity

__all__ = [
    "AttributionRecord",
    "FeedbackCard",
    "NormalizedRecord",
    "PermissionBundle",
    "ResolvedEntity",
]
