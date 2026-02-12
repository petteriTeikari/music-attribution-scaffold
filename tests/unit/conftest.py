"""Shared fixtures for unit tests.

Centralizes the SQLite type compiler registration that was previously
duplicated across 13+ test files.
"""

from __future__ import annotations

import json

import pytest


@pytest.fixture(autouse=True, scope="session")
def _register_sqlite_type_compilers() -> None:
    """Register JSONB and HALFVEC compilation for SQLite dialect (test-only).

    Session-scoped and autouse so every unit test file gets these
    type mappings without needing a manual call.
    """
    from pgvector.sqlalchemy import HALFVEC
    from sqlalchemy.dialects.postgresql import JSONB
    from sqlalchemy.ext.compiler import compiles

    @compiles(JSONB, "sqlite")  # type: ignore[misc]
    def _compile_jsonb_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "JSON"

    @compiles(HALFVEC, "sqlite")  # type: ignore[misc]
    def _compile_halfvec_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "TEXT"

    _original_process = HALFVEC.bind_processor

    def _patched_bind_processor(self, dialect):  # noqa: ANN001, ANN202
        if dialect.name == "sqlite":

            def process(value):  # noqa: ANN001, ANN202
                if value is None:
                    return None
                if isinstance(value, list | tuple):
                    return json.dumps([float(v) for v in value])
                return str(value)

            return process
        return _original_process(self, dialect)

    HALFVEC.bind_processor = _patched_bind_processor  # type: ignore[assignment]
