"""Tests for attribution API endpoints."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from fastapi.testclient import TestClient

from music_attribution.api.app import create_app
from music_attribution.schemas.attribution import (
    AttributionRecord,
    ConformalSet,
    Credit,
)
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
    SourceEnum,
)


def _make_attribution(
    work_id: uuid.UUID | None = None,
    confidence: float = 0.9,
) -> AttributionRecord:
    """Create an AttributionRecord for testing."""
    now = datetime.now(UTC)
    return AttributionRecord(
        work_entity_id=work_id or uuid.uuid4(),
        credits=[
            Credit(
                entity_id=uuid.uuid4(),
                role=CreditRoleEnum.PERFORMER,
                confidence=confidence,
                sources=[SourceEnum.MUSICBRAINZ],
                assurance_level=AssuranceLevelEnum.LEVEL_2,
            ),
        ],
        assurance_level=AssuranceLevelEnum.LEVEL_2,
        confidence_score=confidence,
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


@pytest.fixture
def client() -> TestClient:
    """Create a test client with mocked repository."""
    app = create_app()
    return TestClient(app)


class TestAttributionEndpoints:
    """Tests for attribution API endpoints."""

    def test_health_check(self, client) -> None:
        """Test health endpoint returns OK."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"

    def test_get_attribution_by_work_id(self, client) -> None:
        """Test getting attribution by work entity ID."""
        work_id = uuid.uuid4()
        attr = _make_attribution(work_id=work_id)

        # Store in the in-memory repo via app state
        client.app.state.attributions[work_id] = attr

        response = client.get(f"/api/v1/attributions/work/{work_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["work_entity_id"] == str(work_id)

    def test_attribution_response_includes_confidence(self, client) -> None:
        """Test that response includes confidence score."""
        work_id = uuid.uuid4()
        attr = _make_attribution(work_id=work_id, confidence=0.85)
        client.app.state.attributions[work_id] = attr

        response = client.get(f"/api/v1/attributions/work/{work_id}")
        assert response.status_code == 200
        data = response.json()
        assert "confidence_score" in data
        assert data["confidence_score"] == 0.85

    def test_attribution_response_includes_assurance_level(self, client) -> None:
        """Test that response includes assurance level."""
        work_id = uuid.uuid4()
        attr = _make_attribution(work_id=work_id)
        client.app.state.attributions[work_id] = attr

        response = client.get(f"/api/v1/attributions/work/{work_id}")
        assert response.status_code == 200
        data = response.json()
        assert "assurance_level" in data
        assert data["assurance_level"] == "LEVEL_2"

    def test_not_found_returns_404(self, client) -> None:
        """Test that nonexistent attribution returns 404."""
        fake_id = uuid.uuid4()
        response = client.get(f"/api/v1/attributions/work/{fake_id}")
        assert response.status_code == 404

    def test_search_attributions_returns_list(self, client) -> None:
        """Test that search returns a list of attributions."""
        for _ in range(3):
            work_id = uuid.uuid4()
            client.app.state.attributions[work_id] = _make_attribution(work_id=work_id)

        response = client.get("/api/v1/attributions/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 3

    def test_pagination_works(self, client) -> None:
        """Test that pagination limits results."""
        for _ in range(10):
            work_id = uuid.uuid4()
            client.app.state.attributions[work_id] = _make_attribution(work_id=work_id)

        response = client.get("/api/v1/attributions/?limit=3&offset=0")
        assert response.status_code == 200
        data = response.json()
        assert len(data) <= 3

    def test_invalid_uuid_returns_422(self, client) -> None:
        """Test that invalid UUID returns validation error."""
        response = client.get("/api/v1/attributions/work/not-a-uuid")
        assert response.status_code == 422
