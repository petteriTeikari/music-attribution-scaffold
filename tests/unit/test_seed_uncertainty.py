"""Tests for Imogen Heap seed data with uncertainty values (Task 1.3)."""

from __future__ import annotations

import pytest


class TestSeedUncertainty:
    """Tests for uncertainty-enriched seed data."""

    def test_all_seed_records_have_uncertainty(self) -> None:
        """All 8 Imogen Heap records have uncertainty_summary populated."""
        from music_attribution.seed.imogen_heap import _build_works

        records = _build_works()
        assert len(records) == 8
        for rec in records:
            assert rec.uncertainty_summary is not None, f"Record {rec.attribution_id} missing uncertainty_summary"

    def test_high_confidence_low_uncertainty(self) -> None:
        """Hide and Seek (0.95): total_uncertainty < 0.10."""
        from music_attribution.seed.imogen_heap import _build_works

        records = _build_works()
        hide_and_seek = records[0]
        assert hide_and_seek.confidence_score == pytest.approx(0.95)
        assert hide_and_seek.uncertainty_summary is not None
        assert hide_and_seek.uncertainty_summary.total_uncertainty < 0.10

    def test_low_confidence_high_uncertainty(self) -> None:
        """Blanket (0.0): dominant epistemic uncertainty."""
        from music_attribution.schemas.enums import UncertaintySourceEnum
        from music_attribution.seed.imogen_heap import _build_works

        records = _build_works()
        blanket = records[7]
        assert blanket.confidence_score == pytest.approx(0.0)
        assert blanket.uncertainty_summary is not None
        assert blanket.uncertainty_summary.dominant_uncertainty_source == UncertaintySourceEnum.EPISTEMIC

    def test_citation_indexes_sequential(self) -> None:
        """Each record's provenance events have sequential citation_index values."""
        from music_attribution.seed.imogen_heap import _build_works

        records = _build_works()
        for rec in records:
            indexes = [e.citation_index for e in rec.provenance_chain if e.citation_index is not None]
            if indexes:
                assert indexes == list(range(1, len(indexes) + 1)), (
                    f"Record {rec.attribution_id}: citation_indexes not sequential: {indexes}"
                )

    def test_source_contributions_match_credits(self) -> None:
        """Each record's source_contributions list covers its credit sources."""
        from music_attribution.seed.imogen_heap import _build_works

        records = _build_works()
        for rec in records:
            if rec.uncertainty_summary is None:
                continue
            contrib_sources = {sc.source for sc in rec.uncertainty_summary.source_contributions}
            credit_sources = set()
            for credit in rec.credits:
                credit_sources.update(credit.sources)
            # All credit sources should appear in source contributions
            assert credit_sources <= contrib_sources, (
                f"Record {rec.attribution_id}: credit sources {credit_sources} "
                f"not covered by contributions {contrib_sources}"
            )
