"""Tests for MCP server consent and attribution queries."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from music_attribution.mcp.server import create_mcp_server
from music_attribution.schemas.attribution import (
    AttributionRecord,
    ConformalSet,
    Credit,
)
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
    PermissionScopeEnum,
    PermissionTypeEnum,
    PermissionValueEnum,
    SourceEnum,
)
from music_attribution.schemas.permissions import (
    PermissionBundle,
    PermissionEntry,
)


def _make_attribution(work_id: uuid.UUID | None = None) -> AttributionRecord:
    """Create an AttributionRecord for testing."""
    now = datetime.now(UTC)
    return AttributionRecord(
        work_entity_id=work_id or uuid.uuid4(),
        credits=[
            Credit(
                entity_id=uuid.uuid4(),
                role=CreditRoleEnum.PERFORMER,
                confidence=0.9,
                sources=[SourceEnum.MUSICBRAINZ],
                assurance_level=AssuranceLevelEnum.LEVEL_2,
            ),
        ],
        assurance_level=AssuranceLevelEnum.LEVEL_2,
        confidence_score=0.9,
        conformal_set=ConformalSet(
            coverage_level=0.9,
            marginal_coverage=0.9,
            calibration_error=0.02,
            calibration_method="APS",
            calibration_set_size=100,
        ),
        source_agreement=0.95,
        review_priority=0.1,
        created_at=now,
        updated_at=now,
        version=1,
    )


def _make_permission_bundle(entity_id: uuid.UUID) -> PermissionBundle:
    """Create a PermissionBundle for testing."""
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
                permission_type=PermissionTypeEnum.AI_TRAINING,
                value=PermissionValueEnum.DENY,
            ),
            PermissionEntry(
                permission_type=PermissionTypeEnum.SYNC_LICENSE,
                value=PermissionValueEnum.ASK,
            ),
        ],
        default_permission=PermissionValueEnum.ASK,
        effective_from=now,
        updated_at=now,
        created_by=uuid.uuid4(),
        version=1,
    )


class TestMCPServer:
    """Tests for MCP server tools."""

    def test_mcp_server_creates_successfully(self) -> None:
        """Test that MCP server can be created."""
        server = create_mcp_server()
        assert server is not None
        assert server.name == "music-attribution"

    async def test_query_attribution_tool(self) -> None:
        """Test the query_attribution MCP tool."""
        server = create_mcp_server()
        work_id = uuid.uuid4()
        attr = _make_attribution(work_id=work_id)
        server._attributions[work_id] = attr

        result = await server._query_attribution(str(work_id))
        assert result is not None
        assert "work_entity_id" in result

    async def test_check_permission_allowed(self) -> None:
        """Test checking a permission that is ALLOW."""
        server = create_mcp_server()
        entity_id = uuid.uuid4()
        bundle = _make_permission_bundle(entity_id)
        server._permissions[entity_id] = bundle

        result = await server._check_permission(
            str(entity_id), "STREAM",
        )
        assert result["value"] == "ALLOW"

    async def test_check_permission_denied(self) -> None:
        """Test checking a permission that is DENY."""
        server = create_mcp_server()
        entity_id = uuid.uuid4()
        bundle = _make_permission_bundle(entity_id)
        server._permissions[entity_id] = bundle

        result = await server._check_permission(
            str(entity_id), "AI_TRAINING",
        )
        assert result["value"] == "DENY"

    async def test_check_permission_ask(self) -> None:
        """Test checking a permission that is ASK."""
        server = create_mcp_server()
        entity_id = uuid.uuid4()
        bundle = _make_permission_bundle(entity_id)
        server._permissions[entity_id] = bundle

        result = await server._check_permission(
            str(entity_id), "SYNC_LICENSE",
        )
        assert result["value"] == "ASK"

    async def test_list_permissions(self) -> None:
        """Test listing all permissions for an entity."""
        server = create_mcp_server()
        entity_id = uuid.uuid4()
        bundle = _make_permission_bundle(entity_id)
        server._permissions[entity_id] = bundle

        result = await server._list_permissions(str(entity_id))
        assert len(result["permissions"]) == 3
        assert result["scope"] == "CATALOG"
