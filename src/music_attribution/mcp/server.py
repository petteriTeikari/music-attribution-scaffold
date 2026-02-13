"""MCP Server for AI platform consent and attribution queries.

Implements the "Permission Patchbay" from Teikari (2026, Section 6).
The Model Context Protocol (MCP) enables AI platforms to issue
machine-readable queries about training rights, attribution provenance,
and permission scopes before incorporating musical works.

This server uses the ``FastMCP`` framework to register three tools:

- ``query_attribution(work_id)`` -- retrieve a full ``AttributionRecord``
  including credits, assurance level, and confidence score.
- ``check_permission(entity_id, permission_type)`` -- check whether a
  specific permission (e.g. ``AI_TRAINING``, ``COMMERCIAL_USE``) is
  granted, denied, or conditional for a given entity.
- ``list_permissions(entity_id)`` -- enumerate all permissions in an
  entity's ``PermissionBundle`` with scope and delegation chain.

The server maintains in-memory dictionaries of attribution records and
permission bundles, suitable for development and testing. Production
deployments would replace these with database-backed repositories.

Notes
-----
MCP is part of the "consent infrastructure" layer that sits between
AI platforms and rights holders. It complements the REST API by
providing a protocol-native interface for LLM tool use.

See Also
--------
music_attribution.schemas.permissions : PermissionBundle and related models.
music_attribution.schemas.attribution : AttributionRecord boundary object.
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
    """MCP server for music attribution and permission queries.

    Wraps a ``FastMCP`` instance and registers three domain tools for
    querying attribution records and permission bundles. Designed as the
    "Permission Patchbay" -- a machine-readable consent layer enabling
    AI platforms to verify training rights before use.

    The server holds in-memory stores of ``AttributionRecord`` and
    ``PermissionBundle`` objects keyed by UUID. In production, these
    would be backed by the PostgreSQL repositories.

    Attributes
    ----------
    name : str
        MCP server name (``"music-attribution"``), used for service
        discovery and logging.

    Methods
    -------
    _query_attribution(work_id)
        Retrieve an attribution record by work entity UUID.
    _check_permission(entity_id, permission_type)
        Check a single permission for an entity.
    _list_permissions(entity_id)
        List all permissions for an entity.

    Examples
    --------
    >>> server = MCPAttributionServer()
    >>> result = await server._query_attribution("550e8400-...")
    """

    def __init__(self) -> None:
        """Initialise the MCP server and register tools.

        Creates the underlying ``FastMCP`` instance and registers the
        three domain tools (``query_attribution``, ``check_permission``,
        ``list_permissions``) via ``_register_tools``.
        """
        self.name = "music-attribution"
        self._mcp = FastMCP(self.name)
        self._attributions: dict[uuid.UUID, AttributionRecord] = {}
        self._permissions: dict[uuid.UUID, PermissionBundle] = {}
        self._register_tools()

    def _register_tools(self) -> None:
        """Register MCP tools with the FastMCP instance.

        Creates closure-based tool functions that delegate to the
        server's async methods. Each tool is decorated with
        ``@self._mcp.tool()`` for MCP protocol registration.
        """

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
        """Query attribution record by work entity ID.

        Looks up the full ``AttributionRecord`` in the in-memory store
        and returns it as a JSON-serialisable dictionary.

        Parameters
        ----------
        work_id : str
            Work entity UUID as a string (e.g. ``"550e8400-..."``).

        Returns
        -------
        dict
            Attribution record serialised via ``model_dump(mode="json")``,
            or an error dict with ``"error"`` key if the UUID is invalid
            or the record is not found.
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

        Looks up the entity's ``PermissionBundle`` and searches for a
        matching ``PermissionTypeEnum`` entry. Returns the permission
        value (``ALLOW``, ``DENY``, ``CONDITIONAL``) and any attached
        conditions.

        Parameters
        ----------
        entity_id : str
            Entity UUID as a string.
        permission_type : str
            Permission type to check (must match a ``PermissionTypeEnum``
            value, e.g. ``"AI_TRAINING"``, ``"COMMERCIAL_USE"``).

        Returns
        -------
        dict
            Permission check result with keys ``entity_id``,
            ``permission_type``, ``value``, and optionally ``conditions``.
            Returns ``"NOT_SET"`` value if the permission type is not
            found in the bundle.
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
        """List all permissions in an entity's permission bundle.

        Returns the scope and all permission entries (type + value)
        for the given entity.

        Parameters
        ----------
        entity_id : str
            Entity UUID as a string.

        Returns
        -------
        dict
            Permission bundle summary with keys ``entity_id``,
            ``scope``, and ``permissions`` (list of type/value dicts).
            Returns an error dict if the UUID is invalid or the bundle
            is not found.
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
    """Create and return a new MCP attribution server instance.

    Factory function that instantiates an ``MCPAttributionServer``
    with empty in-memory stores. Callers should populate the
    ``_attributions`` and ``_permissions`` dictionaries before serving.

    Returns
    -------
    MCPAttributionServer
        Configured server instance with tools registered.
    """
    return MCPAttributionServer()
