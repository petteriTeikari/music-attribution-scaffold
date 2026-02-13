"""Tests for PermissionBundle boundary object schema."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from music_attribution.schemas.permissions import PermissionBundle


class TestPermissionBundle:
    """Tests for PermissionBundle boundary object."""

    def _valid_kwargs(self) -> dict:
        """Return minimal valid kwargs for PermissionBundle."""
        return {
            "entity_id": str(uuid.uuid4()),
            "scope": "CATALOG",
            "permissions": [
                {
                    "permission_type": "STREAM",
                    "value": "ALLOW",
                },
                {
                    "permission_type": "AI_TRAINING",
                    "value": "DENY",
                },
            ],
            "effective_from": datetime.now(UTC),
            "delegation_chain": [
                {
                    "entity_id": str(uuid.uuid4()),
                    "role": "OWNER",
                    "can_modify": True,
                    "can_delegate": True,
                },
            ],
            "default_permission": "ASK",
            "created_by": str(uuid.uuid4()),
            "updated_at": datetime.now(UTC),
            "version": 1,
        }

    def test_permission_bundle_valid_creation(self) -> None:
        """Test that a valid PermissionBundle can be created."""
        bundle = PermissionBundle(**self._valid_kwargs())
        assert bundle.permission_id is not None
        assert bundle.scope == "CATALOG"
        assert bundle.schema_version == "1.0.0"

    def test_permission_bundle_all_types_covered(self) -> None:
        """Test that all permission types from the spec exist."""
        from music_attribution.schemas.enums import PermissionTypeEnum

        expected_types = {
            "STREAM",
            "DOWNLOAD",
            "SYNC_LICENSE",
            "AI_TRAINING",
            "AI_TRAINING_COMPOSITION",
            "AI_TRAINING_RECORDING",
            "AI_TRAINING_STYLE",
            "DATASET_INCLUSION",
            "VOICE_CLONING",
            "STYLE_LEARNING",
            "LYRICS_IN_CHATBOTS",
            "COVER_VERSIONS",
            "REMIX",
            "SAMPLE",
            "DERIVATIVE_WORK",
        }
        actual_types = {e.value for e in PermissionTypeEnum}
        assert expected_types == actual_types

    def test_permission_bundle_serializes_for_mcp(self) -> None:
        """Test that PermissionBundle serializes to MCP-compatible JSON."""
        bundle = PermissionBundle(**self._valid_kwargs())
        json_str = bundle.model_dump_json()
        assert isinstance(json_str, str)
        assert "STREAM" in json_str
        assert "AI_TRAINING" in json_str

    def test_permission_bundle_requires_permissions(self) -> None:
        """Test that permissions list must be non-empty."""
        kwargs = self._valid_kwargs()
        kwargs["permissions"] = []
        with pytest.raises(ValidationError):
            PermissionBundle(**kwargs)

    def test_permission_bundle_effective_until_after_from(self) -> None:
        """Test that effective_until must be after effective_from."""
        kwargs = self._valid_kwargs()
        kwargs["effective_from"] = datetime(2026, 2, 10, tzinfo=UTC)
        kwargs["effective_until"] = datetime(2026, 2, 9, tzinfo=UTC)
        with pytest.raises(ValidationError):
            PermissionBundle(**kwargs)

    def test_permission_bundle_scope_entity_id_consistency(self) -> None:
        """Test that scope_entity_id is required for non-CATALOG scopes."""
        kwargs = self._valid_kwargs()
        kwargs["scope"] = "RECORDING"
        kwargs["scope_entity_id"] = None
        with pytest.raises(ValidationError):
            PermissionBundle(**kwargs)

    def test_permission_bundle_royalty_requires_rate(self) -> None:
        """Test that ALLOW_WITH_ROYALTY requires royalty_rate > 0."""
        kwargs = self._valid_kwargs()
        kwargs["permissions"] = [
            {
                "permission_type": "STREAM",
                "value": "ALLOW_WITH_ROYALTY",
                "royalty_rate": None,
            },
        ]
        with pytest.raises(ValidationError):
            PermissionBundle(**kwargs)
