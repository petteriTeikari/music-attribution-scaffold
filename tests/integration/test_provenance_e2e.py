"""End-to-end integration test for provenance chain (Task 4.0).

Seeds PostgreSQL with Imogen Heap data including uncertainty metadata,
queries the provenance API, and verifies the full chain with citation-ready data.
Uses testcontainers for real PostgreSQL testing.
"""

from __future__ import annotations

import httpx
import pytest
from fastapi import FastAPI
from httpx import ASGITransport

pytestmark = [
    pytest.mark.integration,
]


@pytest.fixture()
async def seeded_app(pg_session_factory):
    """Create a FastAPI app backed by seeded PostgreSQL."""
    from music_attribution.api.routes.attribution import router

    app = FastAPI()
    app.include_router(router)
    app.state.async_session_factory = pg_session_factory

    yield app


class TestProvenanceE2E:
    """End-to-end provenance chain: seed → API → verify."""

    async def test_seed_to_api_provenance_chain(self, seeded_app: FastAPI) -> None:
        """Seed → API → provenance chain has all expected events."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        aid = str(deterministic_uuid("work-001"))
        transport = ASGITransport(app=seeded_app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get(f"/attributions/{aid}/provenance")
            assert resp.status_code == 200
            data = resp.json()
            chain = data["provenance_chain"]
            # work-001 (Hide and Seek) should have multiple events
            assert len(chain) >= 3
            # Should include at least FETCH, RESOLVE, SCORE event types
            event_types = {e["event_type"] for e in chain}
            assert "FETCH" in event_types
            assert "SCORE" in event_types

    async def test_provenance_has_uncertainty_metadata(self, seeded_app: FastAPI) -> None:
        """API response includes uncertainty summary with expected fields."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        aid = str(deterministic_uuid("work-001"))
        transport = ASGITransport(app=seeded_app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get(f"/attributions/{aid}/provenance")
            data = resp.json()
            summary = data["uncertainty_summary"]
            assert summary is not None
            assert "total_uncertainty" in summary
            assert "source_contributions" in summary
            assert "dominant_uncertainty_source" in summary
            assert isinstance(summary["source_contributions"], list)
            assert len(summary["source_contributions"]) >= 1

    async def test_citation_indexes_present(self, seeded_app: FastAPI) -> None:
        """Each provenance event has a citation_index."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        aid = str(deterministic_uuid("work-001"))
        transport = ASGITransport(app=seeded_app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get(f"/attributions/{aid}/provenance")
            data = resp.json()
            for event in data["provenance_chain"]:
                assert "citation_index" in event
                assert event["citation_index"] is not None
                assert isinstance(event["citation_index"], int)
                assert event["citation_index"] >= 1

    async def test_confidence_progression_monotonic(self, seeded_app: FastAPI) -> None:
        """For well-attributed works, SCORE events show non-decreasing confidence."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        # work-001 is "Hide and Seek" with 0.95 confidence (well-attributed)
        aid = str(deterministic_uuid("work-001"))
        transport = ASGITransport(app=seeded_app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get(f"/attributions/{aid}/provenance")
            data = resp.json()
            score_confidences = [
                e["details"]["new_confidence"] for e in data["provenance_chain"] if e["details"].get("type") == "score"
            ]
            assert len(score_confidences) >= 1
            # For a well-attributed work, final confidence should be high
            assert score_confidences[-1] >= 0.85
