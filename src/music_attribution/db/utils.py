"""Shared persistence utilities for ORM ↔ Pydantic conversion.

Used by attribution, feedback, and permissions persistence modules.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime


def ensure_utc(dt: datetime | str) -> datetime:
    """Ensure a datetime has UTC timezone (SQLite strips tzinfo).

    ORM models annotate DateTime columns as Mapped[str] but the actual
    runtime value is a datetime object. Accept both to satisfy mypy.
    """
    if isinstance(dt, str):
        parsed = datetime.fromisoformat(dt)
        return parsed.replace(tzinfo=UTC) if parsed.tzinfo is None else parsed
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt


def parse_jsonb(value: dict | list | str) -> dict | list:
    """Parse JSONB value — str from SQLite, native dict/list from PostgreSQL."""
    if isinstance(value, str):
        return json.loads(value)  # type: ignore[no-any-return]
    return value
