"""Tests for async PostgreSQL permission repository."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from music_attribution.db.models import AuditLogModel, PermissionBundleModel
from music_attribution.schemas.enums import (
    PermissionScopeEnum,
    PermissionTypeEnum,
    PermissionValueEnum,
)
from music_attribution.schemas.permissions import (
    PermissionBundle,
    PermissionEntry,
)


def _register_sqlite_type_compilers() -> None:
    """Register JSONB and HALFVEC compilation for SQLite dialect (test-only)."""
    from pgvector.sqlalchemy import HALFVEC
    from sqlalchemy.dialects.postgresql import JSONB
    from sqlalchemy.ext.compiler import compiles

    @compiles(JSONB, "sqlite")  # type: ignore[misc]
    def _compile_jsonb_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "JSON"

    @compiles(HALFVEC, "sqlite")  # type: ignore[misc]
    def _compile_halfvec_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "TEXT"


_register_sqlite_type_compilers()


def _make_bundle(
    *,
    entity_id: uuid.UUID | None = None,
    scope: PermissionScopeEnum = PermissionScopeEnum.CATALOG,
    scope_entity_id: uuid.UUID | None = None,
    permission_type: PermissionTypeEnum = PermissionTypeEnum.AI_TRAINING,
    permission_value: PermissionValueEnum = PermissionValueEnum.DENY,
) -> PermissionBundle:
    """Create a minimal valid PermissionBundle for testing."""
    now = datetime.now(UTC)
    return PermissionBundle(
        entity_id=entity_id or uuid.uuid4(),
        scope=scope,
        scope_entity_id=scope_entity_id,
        permissions=[
            PermissionEntry(
                permission_type=permission_type,
                value=permission_value,
            ),
        ],
        effective_from=now,
        delegation_chain=[],
        default_permission=PermissionValueEnum.ASK,
        created_by=uuid.uuid4(),
        updated_at=now,
        version=1,
    )


@pytest.fixture
async def async_session():
    """Create an in-memory async SQLite database with permission tables."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(PermissionBundleModel.__table__.create)
        await conn.run_sync(AuditLogModel.__table__.create)

    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with session_factory() as session:
        yield session

    await engine.dispose()


class TestAsyncPermissionRepository:
    """Tests for AsyncPermissionRepository."""

    async def test_store_and_retrieve(self, async_session: AsyncSession) -> None:
        """Round-trip: store → find_by_id returns equivalent bundle."""
        from music_attribution.permissions.persistence import AsyncPermissionRepository

        repo = AsyncPermissionRepository()
        bundle = _make_bundle()

        stored_id = await repo.store(bundle, async_session)
        assert stored_id == bundle.permission_id

        found = await repo.find_by_id(bundle.permission_id, async_session)
        assert found is not None
        assert found.permission_id == bundle.permission_id
        assert found.entity_id == bundle.entity_id

    async def test_find_by_entity_id(self, async_session: AsyncSession) -> None:
        """Find permissions for an entity returns all bundles."""
        from music_attribution.permissions.persistence import AsyncPermissionRepository

        repo = AsyncPermissionRepository()
        entity_id = uuid.uuid4()

        b1 = _make_bundle(entity_id=entity_id)
        b2 = _make_bundle(entity_id=entity_id)
        b3 = _make_bundle()  # different entity

        await repo.store(b1, async_session)
        await repo.store(b2, async_session)
        await repo.store(b3, async_session)

        results = await repo.find_by_entity_id(entity_id, async_session)
        assert len(results) == 2
        assert all(r.entity_id == entity_id for r in results)

    async def test_check_permission(self, async_session: AsyncSession) -> None:
        """check_permission returns the correct value for a type."""
        from music_attribution.permissions.persistence import AsyncPermissionRepository

        repo = AsyncPermissionRepository()
        entity_id = uuid.uuid4()
        bundle = _make_bundle(
            entity_id=entity_id,
            permission_type=PermissionTypeEnum.AI_TRAINING,
            permission_value=PermissionValueEnum.DENY,
        )
        await repo.store(bundle, async_session)

        result = await repo.check_permission(
            entity_id=entity_id,
            permission_type=PermissionTypeEnum.AI_TRAINING,
            session=async_session,
        )
        assert result == PermissionValueEnum.DENY

    async def test_check_permission_scope_override(self, async_session: AsyncSession) -> None:
        """Work-level scope overrides catalog-level default."""
        from music_attribution.permissions.persistence import AsyncPermissionRepository

        repo = AsyncPermissionRepository()
        entity_id = uuid.uuid4()
        work_id = uuid.uuid4()

        catalog = _make_bundle(
            entity_id=entity_id,
            scope=PermissionScopeEnum.CATALOG,
            permission_type=PermissionTypeEnum.AI_TRAINING,
            permission_value=PermissionValueEnum.DENY,
        )
        work_override = _make_bundle(
            entity_id=entity_id,
            scope=PermissionScopeEnum.WORK,
            scope_entity_id=work_id,
            permission_type=PermissionTypeEnum.AI_TRAINING,
            permission_value=PermissionValueEnum.ALLOW,
        )
        await repo.store(catalog, async_session)
        await repo.store(work_override, async_session)

        result = await repo.check_permission(
            entity_id=entity_id,
            permission_type=PermissionTypeEnum.AI_TRAINING,
            scope_entity_id=work_id,
            session=async_session,
        )
        assert result == PermissionValueEnum.ALLOW

    async def test_check_permission_not_found_returns_default(self, async_session: AsyncSession) -> None:
        """check_permission returns default_permission when type not found."""
        from music_attribution.permissions.persistence import AsyncPermissionRepository

        repo = AsyncPermissionRepository()
        entity_id = uuid.uuid4()

        bundle = _make_bundle(
            entity_id=entity_id,
            permission_type=PermissionTypeEnum.AI_TRAINING,
            permission_value=PermissionValueEnum.DENY,
        )
        await repo.store(bundle, async_session)

        result = await repo.check_permission(
            entity_id=entity_id,
            permission_type=PermissionTypeEnum.VOICE_CLONING,
            session=async_session,
        )
        assert result == PermissionValueEnum.ASK  # default_permission from bundle

    async def test_delegation_chain_stored(self, async_session: AsyncSession) -> None:
        """Delegation chain is stored and retrieved as JSONB."""
        from music_attribution.permissions.persistence import AsyncPermissionRepository

        repo = AsyncPermissionRepository()
        bundle = _make_bundle()

        await repo.store(bundle, async_session)
        found = await repo.find_by_id(bundle.permission_id, async_session)
        assert found is not None
        assert found.delegation_chain == []
