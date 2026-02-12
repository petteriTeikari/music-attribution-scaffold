"""Full-stack integration tests: FastAPI → PostgreSQL → seed data → API responses.

Verifies the complete data flow from HTTP request through the API layer
to the database and back. Uses testcontainers PostgreSQL for real DB testing.
Mark with @pytest.mark.integration for selective running.
"""

from __future__ import annotations

import httpx
import pytest
from fastapi import FastAPI
from httpx import ASGITransport

pytestmark = [
    pytest.mark.integration,
]


@pytest.fixture
async def test_client(pg_session_factory):
    """Create a FastAPI test client backed by seeded PostgreSQL."""
    from music_attribution.api.routes.attribution import router as attribution_router
    from music_attribution.api.routes.permissions import router as permissions_router

    app = FastAPI()
    app.include_router(attribution_router)
    app.include_router(permissions_router)
    app.state.async_session_factory = pg_session_factory

    @app.get("/health")
    async def health() -> dict:
        return {"status": "healthy"}

    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


class TestFullStackIntegration:
    """Full-stack integration tests: API → Database → Response."""

    async def test_health_endpoint(self, test_client: httpx.AsyncClient) -> None:
        """/health returns 200."""
        resp = await test_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "healthy"

    async def test_list_works_returns_8(self, test_client: httpx.AsyncClient) -> None:
        """/attributions/ returns 8 Imogen Heap works."""
        resp = await test_client.get("/attributions/", params={"limit": 50})
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 8

    async def test_get_work_hide_and_seek(self, test_client: httpx.AsyncClient) -> None:
        """Hide and Seek: confidence 0.95, assurance LEVEL_3."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        work_id = str(deterministic_uuid("work-hide-and-seek"))
        resp = await test_client.get(f"/attributions/work/{work_id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["confidence_score"] == 0.95
        assert data["assurance_level"] == "LEVEL_3"

    async def test_sort_by_confidence_desc(self, test_client: httpx.AsyncClient) -> None:
        """Works are ordered by confidence score descending."""
        resp = await test_client.get("/attributions/", params={"limit": 50})
        data = resp.json()
        scores = [w["confidence_score"] for w in data]
        assert scores == sorted(scores, reverse=True)

    async def test_filter_needs_review(self, test_client: httpx.AsyncClient) -> None:
        """needs_review=true returns works that need review."""
        resp = await test_client.get("/attributions/", params={"needs_review": "true", "limit": 50})
        data = resp.json()
        # Headlock (0.58), Just for Now (0.35), 2-1 (0.28), Blanket (0.0)
        assert len(data) == 4
        for work in data:
            assert work["needs_review"] is True

    async def test_permission_check_streaming(self, test_client: httpx.AsyncClient) -> None:
        """Streaming permission for Imogen Heap returns ALLOW."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        ih_id = str(deterministic_uuid("artist-imogen-heap"))
        resp = await test_client.post(
            "/permissions/check",
            json={"entity_id": ih_id, "permission_type": "STREAM"},
        )
        assert resp.status_code == 200
        assert resp.json()["result"] == "ALLOW"

    async def test_permission_check_voice_cloning(self, test_client: httpx.AsyncClient) -> None:
        """Voice cloning permission for Imogen Heap returns DENY."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        ih_id = str(deterministic_uuid("artist-imogen-heap"))
        resp = await test_client.post(
            "/permissions/check",
            json={"entity_id": ih_id, "permission_type": "VOICE_CLONING"},
        )
        assert resp.status_code == 200
        assert resp.json()["result"] == "DENY"

    async def test_search_works(self, test_client: httpx.AsyncClient) -> None:
        """Search for 'vocoder' returns results including Hide and Seek."""
        resp = await test_client.get("/attributions/search", params={"q": "vocoder"})
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) >= 1
        # Hide and Seek has role_detail "Lead vocals, vocoder arrangement"
        attr_ids = [r["attribution"]["attribution_id"] for r in data]
        from music_attribution.seed.imogen_heap import deterministic_uuid

        hide_seek_id = str(deterministic_uuid("work-001"))
        assert hide_seek_id in attr_ids
