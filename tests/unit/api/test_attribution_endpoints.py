"""Tests for attribution API endpoints."""

from __future__ import annotations

import ast
import uuid
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from music_attribution.api.app import create_app
from music_attribution.schemas.attribution import AttributionRecord
from tests.factories import make_attribution


def _make_attribution(
    work_id: uuid.UUID | None = None,
    confidence: float = 0.9,
) -> AttributionRecord:
    """Create an AttributionRecord for testing."""

    return make_attribution(
        work_entity_id=work_id or uuid.uuid4(),
        confidence_score=confidence,
    )


def _mock_session_factory(repo_mock: MagicMock) -> MagicMock:
    """Create a mock async_session_factory for tests.

    The mock session supports async context manager usage and
    the repo_mock is patched externally via @patch.
    """
    mock_session = AsyncMock()
    factory = MagicMock()
    factory.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    factory.return_value.__aexit__ = AsyncMock(return_value=False)
    return factory


@pytest.fixture
def client() -> TestClient:
    """Create a test client with mock session factory (no in-memory dict)."""
    app = create_app()
    app.state.async_session_factory = _mock_session_factory(MagicMock())
    return TestClient(app)


class TestNoFallbackCode:
    """Verify that in-memory dict fallback code has been removed."""

    def test_no_attributions_dict_on_app_state(self) -> None:
        """app.state must NOT have an 'attributions' attribute after create_app()."""
        app = create_app()
        assert not hasattr(app.state, "attributions"), "app.state.attributions still exists — remove the in-memory dict"

    def test_no_hasattr_guards_in_attribution_routes(self) -> None:
        """attribution.py must not contain hasattr(..., 'async_session_factory') guards."""
        source_path = (
            Path(__file__).resolve().parents[3] / "src" / "music_attribution" / "api" / "routes" / "attribution.py"
        )
        source = source_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "hasattr":
                pytest.fail("attribution.py still contains hasattr() calls — remove fallback guards")

    def test_agent_deps_has_no_attributions_field(self) -> None:
        """AgentDeps must not have an 'attributions' field."""
        from music_attribution.chat.agent import AgentDeps

        field_names = [f.name for f in AgentDeps.__dataclass_fields__.values()]
        assert "attributions" not in field_names, "AgentDeps still has 'attributions' field — remove it"


class TestAttributionEndpoints:
    """Tests for attribution API endpoints."""

    def test_health_check(self, client) -> None:
        """Test health endpoint returns OK."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"

    @patch("music_attribution.api.routes.attribution.AsyncAttributionRepository")
    def test_get_attribution_by_work_id(self, mock_repo_cls, client) -> None:
        """Test getting attribution by work entity ID."""
        work_id = uuid.uuid4()
        attr = _make_attribution(work_id=work_id)
        mock_repo_cls.return_value.find_by_work_entity_id = AsyncMock(return_value=attr)

        response = client.get(f"/api/v1/attributions/work/{work_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["work_entity_id"] == str(work_id)

    @patch("music_attribution.api.routes.attribution.AsyncAttributionRepository")
    def test_attribution_response_includes_confidence(self, mock_repo_cls, client) -> None:
        """Test that response includes confidence score."""
        work_id = uuid.uuid4()
        attr = _make_attribution(work_id=work_id, confidence=0.85)
        mock_repo_cls.return_value.find_by_work_entity_id = AsyncMock(return_value=attr)

        response = client.get(f"/api/v1/attributions/work/{work_id}")
        assert response.status_code == 200
        data = response.json()
        assert "confidence_score" in data
        assert data["confidence_score"] == 0.85

    @patch("music_attribution.api.routes.attribution.AsyncAttributionRepository")
    def test_attribution_response_includes_assurance_level(self, mock_repo_cls, client) -> None:
        """Test that response includes assurance level."""
        work_id = uuid.uuid4()
        attr = _make_attribution(work_id=work_id)
        mock_repo_cls.return_value.find_by_work_entity_id = AsyncMock(return_value=attr)

        response = client.get(f"/api/v1/attributions/work/{work_id}")
        assert response.status_code == 200
        data = response.json()
        assert "assurance_level" in data
        assert data["assurance_level"] == "LEVEL_2"

    @patch("music_attribution.api.routes.attribution.AsyncAttributionRepository")
    def test_not_found_returns_404(self, mock_repo_cls, client) -> None:
        """Test that nonexistent attribution returns 404."""
        mock_repo_cls.return_value.find_by_work_entity_id = AsyncMock(return_value=None)

        fake_id = uuid.uuid4()
        response = client.get(f"/api/v1/attributions/work/{fake_id}")
        assert response.status_code == 404

    @patch("music_attribution.api.routes.attribution.AsyncAttributionRepository")
    def test_list_attributions_returns_list(self, mock_repo_cls, client) -> None:
        """Test that list returns attribution records."""
        records = [_make_attribution() for _ in range(3)]
        mock_repo_cls.return_value.list_all = AsyncMock(return_value=records)

        response = client.get("/api/v1/attributions/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 3

    @patch("music_attribution.api.routes.attribution.AsyncAttributionRepository")
    def test_pagination_works(self, mock_repo_cls, client) -> None:
        """Test that pagination limits results."""
        records = [_make_attribution() for _ in range(3)]
        mock_repo_cls.return_value.list_all = AsyncMock(return_value=records)

        response = client.get("/api/v1/attributions/?limit=3&offset=0")
        assert response.status_code == 200
        data = response.json()
        assert len(data) <= 3

    def test_invalid_uuid_returns_422(self, client) -> None:
        """Test that invalid UUID returns validation error."""
        response = client.get("/api/v1/attributions/work/not-a-uuid")
        assert response.status_code == 422
