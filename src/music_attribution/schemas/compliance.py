"""Stub schemas for compliance and certification attestations.

Future-readiness stubs for Fairly Trained, C2PA provenance,
EU AI Act compliance, and CMO approval records.
No business logic — schema definitions only.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from music_attribution.schemas.enums import CertificationTypeEnum


class ComplianceAttestation(BaseModel):
    """External certification or compliance attestation record."""

    certification_type: CertificationTypeEnum
    issuer: str
    issued_at: datetime
    valid_until: datetime | None = None
    scope: str = ""
    certificate_url: str | None = None
