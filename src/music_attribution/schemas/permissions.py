"""PermissionBundle boundary object schema (BO-5).

Machine-readable permission specification for MCP consent queries.
Implements the Permission Patchbay from Teikari (2026), section 7.

The ``PermissionBundle`` enables AI platforms and other consumers to
programmatically query whether specific uses of a musical work are
permitted, under what conditions, and who authorised the permission.
This is the MCP-native alternative to robots.txt for audio content.

See Also
--------
music_attribution.schemas.enums : Permission-related enums.
Teikari, P. (2026). *Music Attribution with Transparent Confidence*,
    section 7 (Permission Patchbay).
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
    """Optional condition attached to a permission entry.

    Conditions qualify a permission with additional constraints. For
    example, a permission might only apply in certain territories or
    time periods.

    Attributes
    ----------
    condition_type : str
        Type of condition (e.g., ``"territory"``, ``"date_range"``,
        ``"max_duration_seconds"``, ``"non_commercial_only"``).
    value : str
        Condition value as a string. Format depends on
        ``condition_type`` (e.g., ``"US,GB,DE"`` for territory,
        ``"2025-01-01/2026-12-31"`` for date range).

    Examples
    --------
    >>> cond = PermissionCondition(
    ...     condition_type="territory",
    ...     value="US,GB,DE",
    ... )
    """

    condition_type: str
    value: str


class PermissionEntry(BaseModel):
    """A single permission with optional conditions and requirements.

    Each entry specifies a permission type (what use), a value (allow,
    deny, ask, or conditional), and optional requirements. Conditional
    values (ALLOW_WITH_ATTRIBUTION, ALLOW_WITH_ROYALTY) require their
    respective fields to be populated.

    Attributes
    ----------
    permission_type : PermissionTypeEnum
        What kind of use this permission governs (e.g., AI_TRAINING,
        STREAM, REMIX).
    value : PermissionValueEnum
        The permission decision (ALLOW, DENY, ASK, ALLOW_WITH_ATTRIBUTION,
        ALLOW_WITH_ROYALTY).
    conditions : list of PermissionCondition
        Additional conditions qualifying this permission.
    royalty_rate : Decimal or None
        Royalty rate as a decimal (e.g., ``Decimal("0.015")`` for 1.5%).
        Required when ``value`` is ALLOW_WITH_ROYALTY; must be > 0.
    attribution_requirement : str or None
        Required attribution text or format. Required when ``value`` is
        ALLOW_WITH_ATTRIBUTION.
    territory : list of str or None
        ISO 3166-1 alpha-2 country codes where this permission applies.
        None means worldwide.

    Examples
    --------
    >>> entry = PermissionEntry(
    ...     permission_type=PermissionTypeEnum.AI_TRAINING,
    ...     value=PermissionValueEnum.ALLOW_WITH_ROYALTY,
    ...     royalty_rate=Decimal("0.015"),
    ...     territory=["US", "GB"],
    ... )
    """

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
    """An entry in the permission delegation chain.

    Models the chain of authority from the rights owner through
    intermediaries (manager, label, distributor). Each entry specifies
    what authority the entity has over the permissions.

    Attributes
    ----------
    entity_id : uuid.UUID
        UUID of the entity in the delegation chain (a ``ResolvedEntity``
        of type ARTIST, LABEL, etc.).
    role : DelegationRoleEnum
        The entity's role in the delegation chain (OWNER, MANAGER,
        LABEL, DISTRIBUTOR).
    can_modify : bool
        Whether this entity can modify permission entries. Typically
        True for OWNER and MANAGER, False for DISTRIBUTOR.
    can_delegate : bool
        Whether this entity can further delegate authority to another
        entity.

    Examples
    --------
    >>> entry = DelegationEntry(
    ...     entity_id=uuid.uuid4(),
    ...     role=DelegationRoleEnum.OWNER,
    ...     can_modify=True,
    ...     can_delegate=True,
    ... )
    """

    entity_id: uuid.UUID
    role: DelegationRoleEnum
    can_modify: bool
    can_delegate: bool


class PermissionBundle(BaseModel):
    """Machine-readable permission specification (BO-5).

    The ``PermissionBundle`` is the boundary object used by the API/MCP
    Server pipeline to answer permission queries from AI platforms and
    other consumers. It implements the Permission Patchbay design from
    Teikari (2026), section 7.

    Each bundle specifies permissions at a given scope (catalog, release,
    recording, or work) with an effective date range, a delegation chain
    showing who authorised the permissions, and a default permission for
    unlisted permission types.

    Attributes
    ----------
    schema_version : str
        Semantic version of the PermissionBundle schema. Defaults to
        ``"1.0.0"``.
    permission_id : uuid.UUID
        Unique identifier for this permission bundle. Auto-generated
        UUIDv4.
    entity_id : uuid.UUID
        UUID of the rights holder entity (artist, label, publisher).
    scope : PermissionScopeEnum
        Granularity of this permission bundle (CATALOG, RELEASE,
        RECORDING, WORK).
    scope_entity_id : uuid.UUID or None
        UUID of the specific entity this permission applies to. Must be
        None when scope is CATALOG; must be non-None otherwise.
    permissions : list of PermissionEntry
        List of individual permission entries. Must contain at least one.
    effective_from : datetime
        UTC timestamp from which this bundle is effective. Must be
        timezone-aware.
    effective_until : datetime or None
        UTC timestamp until which this bundle is effective. None means
        no expiry. Must be after ``effective_from`` when set.
    delegation_chain : list of DelegationEntry
        Chain of authority from the rights owner through intermediaries.
    default_permission : PermissionValueEnum
        Default response for permission types not explicitly listed in
        ``permissions``. Typically ASK or DENY.
    created_by : uuid.UUID
        UUID of the entity that created this permission bundle.
    updated_at : datetime
        UTC timestamp of the most recent update. Must be timezone-aware.
    version : int
        Monotonically increasing version number. Minimum 1.

    Examples
    --------
    >>> from datetime import datetime, UTC
    >>> from decimal import Decimal
    >>> bundle = PermissionBundle(
    ...     entity_id=uuid.uuid4(),
    ...     scope=PermissionScopeEnum.CATALOG,
    ...     permissions=[
    ...         PermissionEntry(
    ...             permission_type=PermissionTypeEnum.AI_TRAINING,
    ...             value=PermissionValueEnum.DENY,
    ...         ),
    ...     ],
    ...     effective_from=datetime.now(UTC),
    ...     default_permission=PermissionValueEnum.ASK,
    ...     created_by=uuid.uuid4(),
    ...     updated_at=datetime.now(UTC),
    ...     version=1,
    ... )

    See Also
    --------
    PermissionEntry : Individual permission with conditions.
    DelegationEntry : Authority chain for permission provenance.
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
