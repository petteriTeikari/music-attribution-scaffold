"""Integration tests: agent tools → real SQLite DB round-trip.

Verifies that dual-path agent tools correctly read from and write to
a real database when session_factory is provided on AgentDeps.
Uses SQLite for fast CI without Docker.

Mark with @pytest.mark.integration for selective running.
"""

from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from music_attribution.attribution.persistence import AsyncAttributionRepository
from music_attribution.chat.agent import AgentDeps
from music_attribution.chat.state import AttributionAgentState
from music_attribution.feedback.persistence import AsyncFeedbackRepository
from music_attribution.schemas.enums import EvidenceTypeEnum, ReviewerRoleEnum
from music_attribution.schemas.feedback import FeedbackCard


def _register_sqlite_type_compilers() -> None:
    """Register JSONB and HALFVEC compilation for SQLite dialect (test-only)."""
    from pgvector.sqlalchemy import HALFVEC
    from sqlalchemy.dialects.postgresql import JSONB
    from sqlalchemy.ext.compiler import compiles

    @compiles(JSONB, "sqlite")  # type: ignore[misc]
    def _compile_jsonb_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "JSON"

    @compiles(HALFVEC, "sqlite")  # type: ignore[misc]
    def _compile_halfvec_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "TEXT"


_register_sqlite_type_compilers()

pytestmark = pytest.mark.integration


@pytest.fixture
async def db_session_factory():
    """Create a SQLite-backed async session factory with seeded Imogen Heap data."""
    from music_attribution.db.models import (
        AttributionRecordModel,
        FeedbackCardModel,
    )
    from music_attribution.seed.imogen_heap import seed_imogen_heap

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)
        await conn.run_sync(FeedbackCardModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with factory() as session:
        await seed_imogen_heap(session)
        await session.commit()

    yield factory

    await engine.dispose()


class TestExplainConfidenceWithDB:
    """Test explain_confidence tool path with real database."""

    async def test_find_hide_and_seek_by_id(self, db_session_factory) -> None:
        """AsyncAttributionRepository finds Hide and Seek record from DB."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        work_id = deterministic_uuid("work-001")
        repo = AsyncAttributionRepository()
        async with db_session_factory() as session:
            record = await repo.find_by_id(work_id, session)

        assert record is not None
        assert record.confidence_score == 0.95
        # work_title is a Pydantic display field, not stored in DB
        # Verify attribution_id round-trips correctly
        assert record.attribution_id == work_id

    async def test_agent_deps_has_db_true(self, db_session_factory) -> None:
        """AgentDeps.has_db is True when session_factory is provided."""
        deps = AgentDeps(
            attributions={},
            state=AttributionAgentState(),
            session_factory=db_session_factory,
        )
        assert deps.has_db is True

    async def test_explain_reads_real_data(self, db_session_factory) -> None:
        """The explain_confidence DB path reads correct fields from seeded data."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        work_id = deterministic_uuid("work-001")
        repo = AsyncAttributionRepository()
        async with db_session_factory() as session:
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

    async def test_store_feedback_card(self, db_session_factory) -> None:
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
        async with db_session_factory() as session:
            stored_id = await repo.store(card, session)
            await session.commit()

        assert stored_id == feedback_id

        # Retrieve and verify
        async with db_session_factory() as session:
            retrieved = await repo.find_by_id(feedback_id, session)

        assert retrieved is not None
        assert retrieved.overall_assessment == 0.85
        assert retrieved.reviewer_id == "agent-assisted"
        assert retrieved.free_text == "Good attribution"

    async def test_center_bias_flag_persisted(self, db_session_factory) -> None:
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
        async with db_session_factory() as session:
            await repo.store(card, session)
            await session.commit()

        async with db_session_factory() as session:
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
