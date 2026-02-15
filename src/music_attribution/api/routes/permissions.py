"""Permission check endpoints backed by async PostgreSQL repository.

Provides MCP-compatible permission query endpoints:

* ``POST /api/v1/permissions/check`` — check a single permission
* ``GET /api/v1/permissions/{entity_id}`` — list all permission bundles

These endpoints implement machine-readable permission queries for AI
training rights, following the *MCP as consent infrastructure* model
described in the companion paper (Section 6).  Each permission check is
audit-logged for transparency and compliance.

Notes
-----
Permission bundles use the ``PermissionTypeEnum`` to represent
training, derivative-work, commercial-use, and other permission types.
The audit trail records who asked, when, and with what context.
"""

from __future__ import annotations

import uuid

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from music_attribution.permissions.persistence import AsyncPermissionRepository
from music_attribution.schemas.enums import PermissionTypeEnum

router = APIRouter()


class PermissionCheckRequest(BaseModel):
    """Request body for a permission check query.

    Attributes
    ----------
    entity_id : uuid.UUID
        UUID of the entity whose permissions are being queried (e.g., a
        recording or work entity).
    permission_type : str
        Permission type string matching a ``PermissionTypeEnum`` value
        (e.g., ``"AI_TRAINING"``, ``"DERIVATIVE_WORK"``).
    scope_entity_id : uuid.UUID or None
        Optional UUID to scope the permission check to a specific
        context (e.g., a particular AI model or service).
    requester_id : str
        Identifier for the requesting party, by default ``"anonymous"``.
        Used for audit logging.
    """

    entity_id: uuid.UUID
    permission_type: str
    scope_entity_id: uuid.UUID | None = None
    requester_id: str = "anonymous"


class PermissionCheckResponse(BaseModel):
    """Response body for a permission check query.

    Attributes
    ----------
    entity_id : uuid.UUID
        UUID of the entity whose permission was checked.
    permission_type : str
        The permission type that was queried.
    result : str
        Permission result value (e.g., ``"ALLOW"``, ``"DENY"``,
        ``"UNKNOWN"``).
    """

    entity_id: uuid.UUID
    permission_type: str
    result: str


async def _get_session(request: Request) -> AsyncSession:
    """Get an async session from the application's session factory.

    Parameters
    ----------
    request : Request
        FastAPI request object with access to ``app.state``.

    Returns
    -------
    AsyncSession
        A new async database session (caller must use it as a context
        manager to ensure proper cleanup).
    """
    factory: async_sessionmaker[AsyncSession] = request.app.state.async_session_factory
    return factory()


@router.post("/permissions/check")
async def check_permission(
    request: Request,
    body: PermissionCheckRequest,
) -> PermissionCheckResponse:
    """Check a specific permission for an entity.

    ``POST /api/v1/permissions/check``

    Queries the permission repository for the given entity and
    permission type, then records an audit log entry.  This implements
    the machine-readable consent query pattern described in the
    companion paper (Section 6).

    Parameters
    ----------
    request : Request
        FastAPI request with access to ``app.state``.
    body : PermissionCheckRequest
        JSON request body containing the entity ID, permission type,
        optional scope entity, and requester identifier.

    Returns
    -------
    PermissionCheckResponse
        The permission check result with entity ID, type, and outcome.
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
                request_context={
                    "source": "api",
                    "scope_entity_id": str(body.scope_entity_id) if body.scope_entity_id else None,
                },
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
    """List all permission bundles for an entity.

    ``GET /api/v1/permissions/{entity_id}``

    Returns every permission bundle associated with the given entity
    UUID.  Each bundle contains the full set of permissions (training,
    derivative work, commercial use, etc.) and their current status.

    Parameters
    ----------
    request : Request
        FastAPI request with access to ``app.state``.
    entity_id : uuid.UUID
        UUID of the entity whose permission bundles are requested.

    Returns
    -------
    list[dict]
        JSON-serializable list of permission bundle dictionaries.

    Raises
    ------
    HTTPException
        404 if no permission bundles exist for the given entity.
    """
    repo = AsyncPermissionRepository()

    async with await _get_session(request) as session:
        bundles = await repo.find_by_entity_id(entity_id, session)

    if not bundles:
        raise HTTPException(status_code=404, detail="No permissions found for entity")

    return [b.model_dump(mode="json") for b in bundles]
