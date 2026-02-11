"""Permission check endpoints backed by async PostgreSQL repository."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from music_attribution.permissions.persistence import AsyncPermissionRepository
from music_attribution.schemas.enums import PermissionTypeEnum

router = APIRouter()


class PermissionCheckRequest(BaseModel):
    """Request body for permission check."""

    entity_id: uuid.UUID
    permission_type: str
    scope_entity_id: uuid.UUID | None = None
    requester_id: str = "anonymous"


class PermissionCheckResponse(BaseModel):
    """Response body for permission check."""

    entity_id: uuid.UUID
    permission_type: str
    result: str


async def _get_session(request: Request) -> AsyncSession:
    """Get an async session from the app's session factory."""
    factory: async_sessionmaker[AsyncSession] = request.app.state.async_session_factory
    return factory()


@router.post("/permissions/check")
async def check_permission(
    request: Request,
    body: PermissionCheckRequest,
) -> PermissionCheckResponse:
    """Check a specific permission for an entity.

    Args:
        request: FastAPI request with app state.
        body: Permission check request body.

    Returns:
        Permission check result.
    """
    repo = AsyncPermissionRepository()
    perm_type = PermissionTypeEnum(body.permission_type)

    async with await _get_session(request) as session:
        result = await repo.check_permission(
            entity_id=body.entity_id,
            permission_type=perm_type,
            scope_entity_id=body.scope_entity_id,
            session=session,
        )

        # Find the permission bundle for audit logging
        bundles = await repo.find_by_entity_id(body.entity_id, session)
        if bundles:
            await repo.record_audit(
                permission_id=bundles[0].permission_id,
                requester_id=body.requester_id,
                requester_type="api",
                permission_type=perm_type,
                result=result,
                request_context={"source": "api", "scope_entity_id": str(body.scope_entity_id) if body.scope_entity_id else None},
                session=session,
            )
            await session.commit()

    return PermissionCheckResponse(
        entity_id=body.entity_id,
        permission_type=body.permission_type,
        result=result.value,
    )


@router.get("/permissions/{entity_id}")
async def list_permissions(
    request: Request,
    entity_id: uuid.UUID,
) -> list[dict]:
    """Get all permission bundles for an entity.

    Args:
        request: FastAPI request with app state.
        entity_id: Entity UUID.

    Returns:
        List of permission bundles.
    """
    repo = AsyncPermissionRepository()

    async with await _get_session(request) as session:
        bundles = await repo.find_by_entity_id(entity_id, session)

    if not bundles:
        raise HTTPException(status_code=404, detail="No permissions found for entity")

    return [b.model_dump(mode="json") for b in bundles]
