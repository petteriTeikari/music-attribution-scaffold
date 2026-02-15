"""Music Attribution Scaffold - Model Context Protocol (MCP) module.

Implements the "Permission Patchbay" concept from Teikari (2026, Section 6):
machine-readable permission queries that enable AI platforms to check
training rights and attribution provenance before using musical works.

The MCP server exposes three tools via the FastMCP framework:

- ``query_attribution`` -- retrieve an attribution record by work ID
- ``check_permission`` -- check a specific permission for an entity
- ``list_permissions`` -- list all permissions for an entity

See Also
--------
music_attribution.mcp.server : MCP server implementation.
"""

from __future__ import annotations
