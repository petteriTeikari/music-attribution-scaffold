"""Boundary object schemas for the Music Attribution Scaffold.

These Pydantic models define the contracts between pipelines:
- NormalizedRecord: Data Engineering -> Entity Resolution
- ResolvedEntity: Entity Resolution -> Attribution Engine
- AttributionRecord: Attribution Engine -> API/MCP + Chat
- FeedbackCard: Chat Interface -> Attribution Engine (reverse flow)
- PermissionBundle: API/MCP Server (consent queries)
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
