"""MCP Server for AI platform consent and attribution queries.

Implements the "Permission Patchbay" from the manuscript. Provides
machine-readable permission queries for AI training rights and
attribution verification.
"""

from __future__ import annotations

import logging
import uuid

from mcp.server import FastMCP

from music_attribution.schemas.attribution import AttributionRecord
from music_attribution.schemas.enums import PermissionTypeEnum
from music_attribution.schemas.permissions import PermissionBundle

logger = logging.getLogger(__name__)


class MCPAttributionServer:
    """MCP server for attribution and permission queries.

    Provides tools:
    - query_attribution(work_id) -> AttributionRecord
    - check_permission(entity_id, permission_type) -> PermissionValue
    - list_permissions(entity_id) -> PermissionBundle
    """

    def __init__(self) -> None:
        self.name = "music-attribution"
        self._mcp = FastMCP(self.name)
        self._attributions: dict[uuid.UUID, AttributionRecord] = {}
        self._permissions: dict[uuid.UUID, PermissionBundle] = {}
        self._register_tools()

    def _register_tools(self) -> None:
        """Register MCP tools."""

        @self._mcp.tool()
        async def query_attribution(work_id: str) -> dict:
            """Query attribution by work entity ID."""
            return await self._query_attribution(work_id)

        @self._mcp.tool()
        async def check_permission(entity_id: str, permission_type: str) -> dict:
            """Check a specific permission for an entity."""
            return await self._check_permission(entity_id, permission_type)

        @self._mcp.tool()
        async def list_permissions(entity_id: str) -> dict:
            """List all permissions for an entity."""
            return await self._list_permissions(entity_id)

    async def _query_attribution(self, work_id: str) -> dict:
        """Query attribution record by work ID.

        Args:
            work_id: Work entity UUID as string.

        Returns:
            Attribution record as dictionary, or error.
        """
        try:
            uid = uuid.UUID(work_id)
        except ValueError:
            return {"error": "Invalid UUID format"}

        record = self._attributions.get(uid)
        if record is None:
            return {"error": "Attribution not found", "work_id": work_id}

        return record.model_dump(mode="json")

    async def _check_permission(
        self,
        entity_id: str,
        permission_type: str,
    ) -> dict:
        """Check a specific permission for an entity.

        Args:
            entity_id: Entity UUID as string.
            permission_type: Permission type to check.

        Returns:
            Permission value and details.
        """
        try:
            uid = uuid.UUID(entity_id)
        except ValueError:
            return {"error": "Invalid UUID format"}

        bundle = self._permissions.get(uid)
        if bundle is None:
            return {"error": "Permissions not found", "entity_id": entity_id}

        try:
            ptype = PermissionTypeEnum(permission_type)
        except ValueError:
            return {"error": f"Unknown permission type: {permission_type}"}

        for entry in bundle.permissions:
            if entry.permission_type == ptype:
                return {
                    "entity_id": entity_id,
                    "permission_type": permission_type,
                    "value": entry.value.value,
                    "conditions": [c.model_dump() for c in entry.conditions],
                }

        return {
            "entity_id": entity_id,
            "permission_type": permission_type,
            "value": "NOT_SET",
        }

    async def _list_permissions(self, entity_id: str) -> dict:
        """List all permissions for an entity.

        Args:
            entity_id: Entity UUID as string.

        Returns:
            Full permission bundle.
        """
        try:
            uid = uuid.UUID(entity_id)
        except ValueError:
            return {"error": "Invalid UUID format"}

        bundle = self._permissions.get(uid)
        if bundle is None:
            return {"error": "Permissions not found", "entity_id": entity_id}

        return {
            "entity_id": entity_id,
            "scope": bundle.scope.value,
            "permissions": [
                {
                    "type": e.permission_type.value,
                    "value": e.value.value,
                }
                for e in bundle.permissions
            ],
        }


def create_mcp_server() -> MCPAttributionServer:
    """Create and return an MCP attribution server.

    Returns:
        Configured MCPAttributionServer instance.
    """
    return MCPAttributionServer()
