"""Database infrastructure for Music Attribution Scaffold.

Provides the async SQLAlchemy engine factory, ORM model definitions,
and shared persistence utilities for the five boundary objects:

- ``NormalizedRecordModel`` (BO-1)
- ``ResolvedEntityModel`` (BO-2)
- ``AttributionRecordModel`` (BO-3)
- ``FeedbackCardModel`` (BO-4)
- ``PermissionBundleModel`` (BO-5)

Plus supporting models for graph edges, vector embeddings, and the
permission audit log.

Submodules
----------
engine
    Async engine factory with pool hardening and session management.
models
    SQLAlchemy ORM models mapping to Pydantic boundary object schemas.
utils
    Shared helpers for ORM-to-Pydantic conversion (UTC normalisation,
    JSONB parsing).
"""

from __future__ import annotations
