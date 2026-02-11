"""Tests for permission check API routes backed by database."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


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


def _make_permission_bundle(entity_id: uuid.UUID) -> dict:
    """Build a permission bundle dict matching Imogen Heap mock data pattern."""
    from music_attribution.schemas.enums import (
        PermissionScopeEnum,
        PermissionTypeEnum,
        PermissionValueEnum,
    )
    from music_attribution.schemas.permissions import (
        PermissionBundle,
        PermissionCondition,
        PermissionEntry,
    )

    now = datetime.now(UTC)
    return PermissionBundle(
        entity_id=entity_id,
        scope=PermissionScopeEnum.CATALOG,
        permissions=[
            PermissionEntry(
                permission_type=PermissionTypeEnum.STREAM,
                value=PermissionValueEnum.ALLOW,
            ),
            PermissionEntry(
                permission_type=PermissionTypeEnum.VOICE_CLONING,
                value=PermissionValueEnum.DENY,
            ),
            PermissionEntry(
                permission_type=PermissionTypeEnum.SYNC_LICENSE,
                value=PermissionValueEnum.ASK,
            ),
            PermissionEntry(
                permission_type=PermissionTypeEnum.AI_TRAINING,
                value=PermissionValueEnum.ALLOW_WITH_ATTRIBUTION,
                attribution_requirement="Credit original artist in model card",
                conditions=[
                    PermissionCondition(
                        condition_type="purpose",
                        value="non-commercial research only",
                    ),
                ],
            ),
        ],
        effective_from=now,
        default_permission=PermissionValueEnum.ASK,
        created_by=entity_id,
        updated_at=now,
        version=1,
    )


@pytest.fixture
async def permission_app():
    """Create a FastAPI app with seeded permission data."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    from music_attribution.api.app import create_app
    from music_attribution.db.models import AuditLogModel, PermissionBundleModel
    from music_attribution.permissions.persistence import AsyncPermissionRepository

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)

    async with engine.begin() as conn:
        await conn.run_sync(PermissionBundleModel.__table__.create)
        await conn.run_sync(AuditLogModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    # Seed permission data
    entity_id = uuid.UUID("11111111-1111-1111-1111-111111111111")
    bundle = _make_permission_bundle(entity_id)

    repo = AsyncPermissionRepository()
    async with factory() as session:
        await repo.store(bundle, session)
        await session.commit()

    app = create_app()
    app.state.async_engine = engine
    app.state.async_session_factory = factory

    yield app, entity_id

    await engine.dispose()


@pytest.fixture
def client(permission_app):
    """Create an async test client."""
    from httpx import ASGITransport, AsyncClient

    app, _ = permission_app
    return AsyncClient(transport=ASGITransport(app=app), base_url="http://test")


@pytest.fixture
def entity_id(permission_app):
    """Get the seeded entity ID."""
    _, eid = permission_app
    return eid


class TestPermissionCheckRoutes:
    """Tests for permission check API endpoints."""

    async def test_check_permission_allowed(self, client, entity_id) -> None:
        """POST check returns ALLOW for streaming."""
        async with client:
            response = await client.post(
                "/api/v1/permissions/check",
                json={
                    "entity_id": str(entity_id),
                    "permission_type": "STREAM",
                },
            )

        assert response.status_code == 200
        data = response.json()
        assert data["result"] == "ALLOW"

    async def test_check_permission_denied(self, client, entity_id) -> None:
        """POST check returns DENY for voice cloning."""
        async with client:
            response = await client.post(
                "/api/v1/permissions/check",
                json={
                    "entity_id": str(entity_id),
                    "permission_type": "VOICE_CLONING",
                },
            )

        assert response.status_code == 200
        data = response.json()
        assert data["result"] == "DENY"

    async def test_check_permission_ask(self, client, entity_id) -> None:
        """POST check returns ASK for sync license."""
        async with client:
            response = await client.post(
                "/api/v1/permissions/check",
                json={
                    "entity_id": str(entity_id),
                    "permission_type": "SYNC_LICENSE",
                },
            )

        assert response.status_code == 200
        data = response.json()
        assert data["result"] == "ASK"

    async def test_check_permission_with_conditions(self, client, entity_id) -> None:
        """POST check returns conditions for AI training."""
        async with client:
            response = await client.post(
                "/api/v1/permissions/check",
                json={
                    "entity_id": str(entity_id),
                    "permission_type": "AI_TRAINING",
                },
            )

        assert response.status_code == 200
        data = response.json()
        assert data["result"] == "ALLOW_WITH_ATTRIBUTION"

    async def test_list_permissions_for_entity(self, client, entity_id) -> None:
        """GET returns full permission bundle for entity."""
        async with client:
            response = await client.get(f"/api/v1/permissions/{entity_id}")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["entity_id"] == str(entity_id)
        assert len(data[0]["permissions"]) == 4

    async def test_check_permission_creates_audit_entry(self, client, entity_id, permission_app) -> None:
        """Permission check writes an audit log entry."""
        from sqlalchemy import func, select

        from music_attribution.db.models import AuditLogModel

        async with client:
            await client.post(
                "/api/v1/permissions/check",
                json={
                    "entity_id": str(entity_id),
                    "permission_type": "STREAM",
                    "requester_id": "test-agent",
                },
            )

        app, _ = permission_app
        async with app.state.async_session_factory() as session:
            result = await session.execute(select(func.count()).select_from(AuditLogModel))
            count = result.scalar()
            assert count >= 1
