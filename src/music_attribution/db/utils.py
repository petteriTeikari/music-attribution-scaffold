"""Shared persistence utilities for ORM-to-Pydantic conversion.

Provides helper functions used by the attribution, feedback, and
permissions persistence modules when converting between SQLAlchemy
ORM model instances and Pydantic boundary objects.

These utilities handle two cross-database compatibility issues:

1. **Timezone normalisation**: SQLite strips timezone info from
   ``datetime`` columns, so ``ensure_utc`` re-attaches UTC.
2. **JSONB parsing**: SQLite stores JSONB columns as JSON strings,
   while PostgreSQL returns native Python dicts/lists.

Functions
---------
ensure_utc
    Ensure a datetime value has UTC timezone.
parse_jsonb
    Parse a JSONB value from either PostgreSQL (dict/list) or
    SQLite (JSON string) storage format.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime


def ensure_utc(dt: datetime | str) -> datetime:
    """Ensure a datetime value has UTC timezone attached.

    SQLite strips timezone information from ``DateTime`` columns,
    resulting in naive datetime objects at runtime. This function
    re-attaches ``UTC`` to naive datetimes. Already timezone-aware
    datetimes pass through unchanged.

    The function also accepts ISO-format strings because ORM models
    annotate ``DateTime`` columns as ``Mapped[str]`` for mypy, even
    though the actual runtime value is a ``datetime`` object.

    Parameters
    ----------
    dt : datetime | str
        A datetime object (possibly naive) or an ISO-format string.

    Returns
    -------
    datetime
        Timezone-aware datetime with UTC tzinfo.
    """
    if isinstance(dt, str):
        parsed = datetime.fromisoformat(dt)
        return parsed.replace(tzinfo=UTC) if parsed.tzinfo is None else parsed
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt


def parse_jsonb(value: dict | list | str) -> dict | list:
    """Parse a JSONB column value from either database backend.

    PostgreSQL returns native Python ``dict`` or ``list`` objects from
    JSONB columns. SQLite (used in tests) stores JSONB as a JSON string
    that must be deserialised.

    Parameters
    ----------
    value : dict | list | str
        Raw value from the ORM column. A ``str`` is parsed as JSON;
        ``dict`` or ``list`` values pass through unchanged.

    Returns
    -------
    dict | list
        Parsed Python object.
    """
    if isinstance(value, str):
        return json.loads(value)  # type: ignore[no-any-return]
    return value
