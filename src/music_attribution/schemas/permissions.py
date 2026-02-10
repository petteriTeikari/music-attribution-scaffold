"""PermissionBundle boundary object schema (BO-5).

Machine-readable permission specification for MCP consent queries.
Implements the Permission Patchbay from the manuscript.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator, model_validator

from music_attribution.schemas.enums import (
    DelegationRoleEnum,
    PermissionScopeEnum,
    PermissionTypeEnum,
    PermissionValueEnum,
)


class PermissionCondition(BaseModel):
    """Optional condition on a permission entry."""

    condition_type: str
    value: str


class PermissionEntry(BaseModel):
    """A single permission with optional conditions."""

    permission_type: PermissionTypeEnum
    value: PermissionValueEnum
    conditions: list[PermissionCondition] = Field(default_factory=list)
    royalty_rate: Decimal | None = None
    attribution_requirement: str | None = None
    territory: list[str] | None = None

    @model_validator(mode="after")
    def validate_conditional_fields(self) -> PermissionEntry:
        """Validate fields required by specific permission values."""
        if self.value == PermissionValueEnum.ALLOW_WITH_ROYALTY and (
            self.royalty_rate is None or self.royalty_rate <= 0
        ):
            msg = "royalty_rate must be > 0 when value is ALLOW_WITH_ROYALTY"
            raise ValueError(msg)
        if self.value == PermissionValueEnum.ALLOW_WITH_ATTRIBUTION and self.attribution_requirement is None:
            msg = "attribution_requirement must be non-None when value is ALLOW_WITH_ATTRIBUTION"
            raise ValueError(msg)
        return self


class DelegationEntry(BaseModel):
    """An entry in the delegation chain."""

    entity_id: uuid.UUID
    role: DelegationRoleEnum
    can_modify: bool
    can_delegate: bool


class PermissionBundle(BaseModel):
    """Machine-readable permission specification.

    This is the primary boundary object used by the API/MCP Server pipeline
    to answer permission queries from AI platforms and other consumers.
    """

    schema_version: str = "1.0.0"
    permission_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    entity_id: uuid.UUID
    scope: PermissionScopeEnum
    scope_entity_id: uuid.UUID | None = None
    permissions: list[PermissionEntry] = Field(min_length=1)
    effective_from: datetime
    effective_until: datetime | None = None
    delegation_chain: list[DelegationEntry] = Field(default_factory=list)
    default_permission: PermissionValueEnum
    created_by: uuid.UUID
    updated_at: datetime
    version: int = Field(ge=1)

    @field_validator("effective_from", "updated_at")
    @classmethod
    def validate_timestamps(cls, v: datetime) -> datetime:
        """Timestamps must be timezone-aware."""
        if v.tzinfo is None:
            msg = "Timestamps must be timezone-aware (UTC)"
            raise ValueError(msg)
        return v

    @field_validator("effective_until")
    @classmethod
    def validate_effective_until(cls, v: datetime | None) -> datetime | None:
        """effective_until must be timezone-aware when set."""
        if v is not None and v.tzinfo is None:
            msg = "effective_until must be timezone-aware (UTC)"
            raise ValueError(msg)
        return v

    @model_validator(mode="after")
    def validate_scope_consistency(self) -> PermissionBundle:
        """scope_entity_id must be None for CATALOG, required for others."""
        if self.scope == PermissionScopeEnum.CATALOG and self.scope_entity_id is not None:
            msg = "scope_entity_id must be None when scope is CATALOG"
            raise ValueError(msg)
        if self.scope != PermissionScopeEnum.CATALOG and self.scope_entity_id is None:
            msg = f"scope_entity_id must be non-None when scope is {self.scope}"
            raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def validate_effective_range(self) -> PermissionBundle:
        """effective_from must be before effective_until."""
        if self.effective_until is not None and self.effective_from >= self.effective_until:
            msg = "effective_from must be before effective_until"
            raise ValueError(msg)
        return self
