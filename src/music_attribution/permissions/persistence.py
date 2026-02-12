"""Async PostgreSQL permission repository.

Implements permission lookup with scope-specific overrides and audit logging.
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.db.models import AuditLogModel, PermissionBundleModel
from music_attribution.db.utils import ensure_utc, parse_jsonb
from music_attribution.schemas.enums import PermissionTypeEnum, PermissionValueEnum
from music_attribution.schemas.permissions import PermissionBundle

logger = logging.getLogger(__name__)


def _bundle_to_model(bundle: PermissionBundle) -> PermissionBundleModel:
    """Convert a Pydantic PermissionBundle to an ORM model."""
    return PermissionBundleModel(
        permission_id=bundle.permission_id,
        entity_id=bundle.entity_id,
        scope=bundle.scope.value,
        scope_entity_id=bundle.scope_entity_id,
        permissions=[p.model_dump(mode="json") for p in bundle.permissions],
        effective_from=bundle.effective_from,
        effective_until=bundle.effective_until,
        delegation_chain=[d.model_dump(mode="json") for d in bundle.delegation_chain],
        default_permission=bundle.default_permission.value,
        created_by=bundle.created_by,
        updated_at=bundle.updated_at,
        version=bundle.version,
    )


def _model_to_bundle(model: PermissionBundleModel) -> PermissionBundle:
    """Convert an ORM model to a Pydantic PermissionBundle."""
    return PermissionBundle(
        permission_id=model.permission_id,
        entity_id=model.entity_id,
        scope=model.scope,  # type: ignore[arg-type]
        scope_entity_id=model.scope_entity_id,
        permissions=parse_jsonb(model.permissions),  # type: ignore[arg-type]
        effective_from=ensure_utc(model.effective_from),
        effective_until=ensure_utc(model.effective_until) if model.effective_until else None,
        delegation_chain=parse_jsonb(model.delegation_chain),  # type: ignore[arg-type]
        default_permission=model.default_permission,  # type: ignore[arg-type]
        created_by=model.created_by,
        updated_at=ensure_utc(model.updated_at),
        version=model.version,
    )


class AsyncPermissionRepository:
    """Async PostgreSQL repository for PermissionBundle persistence."""

    async def store(self, bundle: PermissionBundle, session: AsyncSession) -> uuid.UUID:
        """Store a permission bundle."""
        model = _bundle_to_model(bundle)
        session.add(model)
        await session.flush()
        return bundle.permission_id

    async def find_by_id(
        self,
        permission_id: uuid.UUID,
        session: AsyncSession,
    ) -> PermissionBundle | None:
        """Find a permission bundle by its ID."""
        stmt = select(PermissionBundleModel).where(
            PermissionBundleModel.permission_id == permission_id,
        )
        result = await session.execute(stmt)
        model = result.scalar_one_or_none()
        return _model_to_bundle(model) if model is not None else None

    async def find_by_entity_id(
        self,
        entity_id: uuid.UUID,
        session: AsyncSession,
    ) -> list[PermissionBundle]:
        """Find all permission bundles for an entity."""
        stmt = select(PermissionBundleModel).where(
            PermissionBundleModel.entity_id == entity_id,
        )
        result = await session.execute(stmt)
        return [_model_to_bundle(m) for m in result.scalars().all()]

    async def check_permission(
        self,
        entity_id: uuid.UUID,
        permission_type: PermissionTypeEnum,
        *,
        scope_entity_id: uuid.UUID | None = None,
        session: AsyncSession,
    ) -> PermissionValueEnum:
        """Check permission value for entity + type, with scope override.

        If a scope-specific bundle exists (e.g. WORK-level for a specific work),
        it takes precedence over the CATALOG-level default.

        Returns the default_permission from the most relevant bundle if the
        specific permission_type is not found.
        """
        bundles = await self.find_by_entity_id(entity_id, session)
        if not bundles:
            return PermissionValueEnum.ASK

        # Try scope-specific bundle first
        if scope_entity_id is not None:
            for bundle in bundles:
                if bundle.scope_entity_id == scope_entity_id:
                    for perm in bundle.permissions:
                        if perm.permission_type == permission_type:
                            return perm.value
                    return bundle.default_permission

        # Fall back to catalog-level
        for bundle in bundles:
            if bundle.scope_entity_id is None:
                for perm in bundle.permissions:
                    if perm.permission_type == permission_type:
                        return perm.value
                return bundle.default_permission

        # No matching bundle found — use first bundle's default
        return bundles[0].default_permission

    async def record_audit(
        self,
        permission_id: uuid.UUID,
        requester_id: str,
        requester_type: str,
        permission_type: PermissionTypeEnum,
        result: PermissionValueEnum,
        request_context: dict[str, object] | None = None,
        *,
        session: AsyncSession,
    ) -> uuid.UUID:
        """Record a permission check in the audit log."""
        audit = AuditLogModel(
            permission_id=permission_id,
            requester_id=requester_id,
            requester_type=requester_type,
            permission_type=permission_type.value,
            result=result.value,
            request_context=request_context or {},
            checked_at=datetime.now(UTC),
        )
        session.add(audit)
        await session.flush()
        return audit.audit_id
