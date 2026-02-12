"""Integration tests: agent tools → real PostgreSQL DB round-trip.

Verifies that dual-path agent tools correctly read from and write to
a real database when session_factory is provided on AgentDeps.
Uses testcontainers for real PostgreSQL testing.

Mark with @pytest.mark.integration for selective running.
"""

from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, patch

import pytest

from music_attribution.attribution.persistence import AsyncAttributionRepository
from music_attribution.chat.agent import AgentDeps
from music_attribution.chat.state import AttributionAgentState
from music_attribution.feedback.persistence import AsyncFeedbackRepository
from music_attribution.schemas.enums import EvidenceTypeEnum, ReviewerRoleEnum
from music_attribution.schemas.feedback import FeedbackCard

pytestmark = [
    pytest.mark.integration,
]


class TestExplainConfidenceWithDB:
    """Test explain_confidence tool path with real database."""

    async def test_find_hide_and_seek_by_id(self, pg_session_factory) -> None:
        """AsyncAttributionRepository finds Hide and Seek record from DB."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        work_id = deterministic_uuid("work-001")
        repo = AsyncAttributionRepository()
        async with pg_session_factory() as session:
            record = await repo.find_by_id(work_id, session)

        assert record is not None
        assert record.confidence_score == 0.95
        assert record.work_title == "Hide and Seek"
        assert record.artist_name == "Imogen Heap"
        assert record.attribution_id == work_id

    async def test_agent_deps_has_session_factory(self, pg_session_factory) -> None:
        """AgentDeps.session_factory is set when provided."""
        deps = AgentDeps(
            state=AttributionAgentState(),
            session_factory=pg_session_factory,
        )
        assert deps.session_factory is not None

    async def test_explain_reads_real_data(self, pg_session_factory) -> None:
        """The explain_confidence DB path reads correct fields from seeded data."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        work_id = deterministic_uuid("work-001")
        repo = AsyncAttributionRepository()
        async with pg_session_factory() as session:
            record = await repo.find_by_id(work_id, session)

        assert record is not None
        # Verify fields that explain_confidence tool uses
        assert record.confidence_score == 0.95
        assert record.assurance_level.value == "LEVEL_3"
        assert record.source_agreement == 0.94
        assert len(record.credits) >= 1
        sources = [s.value for s in record.credits[0].sources]
        assert len(sources) >= 1


class TestSubmitFeedbackWithDB:
    """Test submit_feedback tool path with real database."""

    async def test_store_feedback_card(self, pg_session_factory) -> None:
        """AsyncFeedbackRepository stores and retrieves a FeedbackCard."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        work_id = deterministic_uuid("work-001")
        feedback_id = uuid.uuid4()
        card = FeedbackCard(
            feedback_id=feedback_id,
            attribution_id=work_id,
            reviewer_id="agent-assisted",
            reviewer_role=ReviewerRoleEnum.MUSICOLOGIST,
            attribution_version=1,
            corrections=[],
            overall_assessment=0.85,
            center_bias_flag=False,
            free_text="Good attribution",
            evidence_type=EvidenceTypeEnum.OTHER,
            submitted_at=datetime.now(UTC),
        )

        repo = AsyncFeedbackRepository()
        async with pg_session_factory() as session:
            stored_id = await repo.store(card, session)
            await session.commit()

        assert stored_id == feedback_id

        # Retrieve and verify
        async with pg_session_factory() as session:
            retrieved = await repo.find_by_id(feedback_id, session)

        assert retrieved is not None
        assert retrieved.overall_assessment == 0.85
        assert retrieved.reviewer_id == "agent-assisted"
        assert retrieved.free_text == "Good attribution"

    async def test_center_bias_flag_persisted(self, pg_session_factory) -> None:
        """Center bias flag is correctly persisted."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        work_id = deterministic_uuid("work-001")
        card = FeedbackCard(
            feedback_id=uuid.uuid4(),
            attribution_id=work_id,
            reviewer_id="agent-assisted",
            reviewer_role=ReviewerRoleEnum.MUSICOLOGIST,
            attribution_version=1,
            corrections=[],
            overall_assessment=0.50,
            center_bias_flag=True,
            free_text="Uncertain assessment",
            evidence_type=EvidenceTypeEnum.OTHER,
            submitted_at=datetime.now(UTC),
        )

        repo = AsyncFeedbackRepository()
        async with pg_session_factory() as session:
            await repo.store(card, session)
            await session.commit()

        async with pg_session_factory() as session:
            retrieved = await repo.find_by_id(card.feedback_id, session)

        assert retrieved is not None
        assert retrieved.center_bias_flag is True
        assert retrieved.overall_assessment == 0.50


class TestAgentEndpointWithSessionFactory:
    """Test AG-UI SSE endpoint with real session_factory on app.state."""

    def test_endpoint_with_db_session_factory(self) -> None:
        """SSE endpoint works when app.state has async_session_factory."""
        from fastapi.testclient import TestClient

        from music_attribution.api.app import create_app

        mock_result = AsyncMock()
        mock_result.data = "Test response with DB."
        mock_agent = AsyncMock()
        mock_agent.run = AsyncMock(return_value=mock_result)

        with patch("music_attribution.chat.agui_endpoint._get_agent") as mock_get:
            mock_get.return_value = mock_agent

            app = create_app()
            # Set a mock session factory on app.state (tests wiring, not actual DB query)
            app.state.async_session_factory = AsyncMock()

            client = TestClient(app)
            response = client.post(
                "/api/v1/copilotkit",
                json={"messages": [{"role": "user", "content": "hello"}]},
            )

        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]

        # Parse SSE events
        events = []
        for line in response.text.strip().split("\n\n"):
            for part in line.split("\n"):
                if part.startswith("data: "):
                    events.append(json.loads(part[6:]))

        types = [e["type"] for e in events]
        assert types[0] == "RunStarted"
        assert types[-1] == "RunFinished"
