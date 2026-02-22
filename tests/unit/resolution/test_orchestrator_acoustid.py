"""Tests for acoustid field name fix in orchestrator resolution details."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from music_attribution.resolution.orchestrator import ResolutionOrchestrator
from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum
from music_attribution.schemas.normalized import IdentifierBundle, NormalizedRecord


def _make_record(
    *,
    canonical_name: str = "Test Work",
    acoustid: str | None = None,
    isrc: str | None = None,
) -> NormalizedRecord:
    """Create a minimal NormalizedRecord for testing."""
    return NormalizedRecord(
        source_id=str(uuid.uuid4()),
        source=SourceEnum.MUSICBRAINZ,
        entity_type=EntityTypeEnum.RECORDING,
        canonical_name=canonical_name,
        record_type="TRACK",
        identifiers=IdentifierBundle(
            acoustid=acoustid,
            isrc=isrc,
        ),
        fetch_timestamp=datetime.now(UTC),
        source_confidence=0.9,
    )


class TestComputeResolutionDetailsAcoustid:
    """Tests for acoustid identifier matching in resolution details."""

    def test_acoustid_match_detected(self) -> None:
        """Shared acoustid across records appears in matched_ids."""
        orch = ResolutionOrchestrator()
        r1 = _make_record(canonical_name="Track A", acoustid="abc123")
        r2 = _make_record(canonical_name="Track B", acoustid="abc123")

        details = orch._compute_resolution_details([r1, r2])

        assert any("acoustid:abc123" in mid for mid in details.matched_identifiers)

    def test_isrc_match_still_works(self) -> None:
        """ISRC matching unaffected by the fix."""
        orch = ResolutionOrchestrator()
        r1 = _make_record(canonical_name="Track A", isrc="USRC12345678")
        r2 = _make_record(canonical_name="Track B", isrc="USRC12345678")

        details = orch._compute_resolution_details([r1, r2])

        assert any("isrc:USRC12345678" in mid for mid in details.matched_identifiers)

    def test_different_acoustid_not_matched(self) -> None:
        """Different acoustid values across records produce no match."""
        orch = ResolutionOrchestrator()
        r1 = _make_record(canonical_name="Track A", acoustid="abc123")
        r2 = _make_record(canonical_name="Track B", acoustid="def456")

        details = orch._compute_resolution_details([r1, r2])

        assert not any("acoustid" in mid for mid in details.matched_identifiers)
