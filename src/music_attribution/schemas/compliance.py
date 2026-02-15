"""Stub schemas for compliance and certification attestations.

Future-readiness stubs for external certification records: Fairly Trained
licensing certification, C2PA content provenance manifests, EU AI Act
compliance declarations, and Collective Management Organisation (CMO)
approvals.

These are schema definitions only -- no business logic. They will be
populated when integration with certification providers is implemented.

See Also
--------
music_attribution.schemas.enums.CertificationTypeEnum : Certification types.
Teikari, P. (2026). *Music Attribution with Transparent Confidence*,
    section 8 (regulatory compliance).
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from music_attribution.schemas.enums import CertificationTypeEnum


class ComplianceAttestation(BaseModel):
    """External certification or compliance attestation record.

    Represents a third-party certification that an AI system or dataset
    meets specific compliance requirements. Attestations are attached to
    training data usage records or permission bundles as evidence of
    responsible AI practices.

    Attributes
    ----------
    certification_type : CertificationTypeEnum
        Type of certification (FAIRLY_TRAINED_LICENSED, C2PA_PROVENANCE,
        EU_AI_ACT_COMPLIANT, CMO_APPROVED).
    issuer : str
        Name of the certifying body (e.g., ``"Fairly Trained Inc."``,
        ``"C2PA"``, ``"GEMA"``).
    issued_at : datetime
        Timestamp when the certification was issued.
    valid_until : datetime or None
        Expiry timestamp. None means the certification does not expire.
    scope : str
        Textual description of what the certification covers (e.g.,
        ``"All audio training data for model v2.1"``). Defaults to
        empty string.
    certificate_url : str or None
        URL to the publicly verifiable certificate, if available.

    Examples
    --------
    >>> from datetime import datetime, UTC
    >>> attestation = ComplianceAttestation(
    ...     certification_type=CertificationTypeEnum.FAIRLY_TRAINED_LICENSED,
    ...     issuer="Fairly Trained Inc.",
    ...     issued_at=datetime(2025, 6, 1, tzinfo=UTC),
    ...     scope="Audio training dataset v3",
    ...     certificate_url="https://fairlytrained.org/cert/12345",
    ... )
    """

    certification_type: CertificationTypeEnum
    issuer: str
    issued_at: datetime
    valid_until: datetime | None = None
    scope: str = ""
    certificate_url: str | None = None
