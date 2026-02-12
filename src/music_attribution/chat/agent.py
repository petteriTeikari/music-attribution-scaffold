"""PydanticAI attribution agent with domain tools.

Provides 4 tools for CopilotKit frontend interaction via AG-UI protocol:
- explain_confidence: Explain why a work has its confidence score
- search_attributions: Search across attribution records
- suggest_correction: Propose a correction to an attribution field
- submit_feedback: Submit a FeedbackCard for an attribution record
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from music_attribution.chat.state import AttributionAgentState, CorrectionPreview

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """\
You are the Music Attribution Assistant, an expert in music credit attribution,
provenance tracking, and confidence scoring.

You help artists, managers, and musicologists review and improve attribution
records for musical works. You understand:

- A0-A3 assurance levels (None → Artist-verified) mapped to ISRC/ISWC/ISNI
- The Oracle Problem: digital systems cannot fully verify physical reality
- Conformal prediction sets for uncertainty quantification
- Source agreement across MusicBrainz, Discogs, AcoustID, and file metadata
- FeedbackCard structured corrections from domain experts

When explaining confidence scores, break down the contributing factors:
source agreement, number of corroborating sources, conformal set sizes,
and calibration quality. Use clear, non-technical language for artists
while being precise for technical users.

Be concise. Prefer bullet points. Reference specific data sources by name.
"""


def _get_agent_model() -> str:
    """Get the agent model string from Settings."""
    from music_attribution.config import Settings

    settings = Settings()  # type: ignore[call-arg]
    return settings.attribution_agent_model


@dataclass
class AgentDeps:
    """Dependencies injected into agent tools at runtime.

    Tools use async_session_factory for PostgreSQL access.
    """

    state: AttributionAgentState
    session_factory: async_sessionmaker[AsyncSession] | None = field(default=None)


class ExplainConfidenceResult(BaseModel):
    """Result of explain_confidence tool."""

    work_id: str
    confidence_score: float
    explanation: str
    factors: list[str] = Field(default_factory=list)


class SearchResult(BaseModel):
    """A single search result."""

    attribution_id: str
    work_title: str
    artist_name: str
    confidence_score: float
    assurance_level: str


class SearchResultSet(BaseModel):
    """Result of search_attributions tool."""

    query: str
    results: list[SearchResult]
    total_count: int


class SuggestCorrectionResult(BaseModel):
    """Result of suggest_correction tool."""

    work_id: str
    correction: CorrectionPreview


class SubmitFeedbackResult(BaseModel):
    """Result of submit_feedback tool."""

    feedback_id: str
    attribution_id: str
    accepted: bool
    message: str


def create_attribution_agent() -> Agent[AgentDeps, str]:
    """Create and configure the PydanticAI attribution agent.

    Returns:
        Configured PydanticAI Agent with 4 domain tools.
    """
    agent = Agent(
        _get_agent_model(),
        system_prompt=SYSTEM_PROMPT,
        deps_type=AgentDeps,
        retries=2,
    )

    @agent.tool
    async def explain_confidence(ctx, work_id: str) -> str:
        """Explain the confidence score for a specific attribution record.

        Args:
            ctx: Agent context with dependencies.
            work_id: Attribution ID to explain.

        Returns:
            Human-readable explanation of the confidence score.
        """
        import uuid as _uuid

        from music_attribution.attribution.persistence import AsyncAttributionRepository

        if not ctx.deps.session_factory:
            return "Database not available. Cannot look up attribution records."

        repo = AsyncAttributionRepository()
        async with ctx.deps.session_factory() as session:
            record = await repo.find_by_id(_uuid.UUID(work_id), session)
        if not record:
            return f"No attribution record found for ID: {work_id}"

        score = record.confidence_score
        sources: list[str] = []
        if record.credits:
            sources = [s.value for s in record.credits[0].sources]
        assurance = record.assurance_level.value
        agreement = record.source_agreement

        factors = []
        if agreement > 0.8:
            factors.append(f"High source agreement ({agreement:.0%})")
        elif agreement > 0.5:
            factors.append(f"Moderate source agreement ({agreement:.0%})")
        else:
            factors.append(f"Low source agreement ({agreement:.0%})")

        factors.append(f"Data from {len(sources)} source(s): {', '.join(sources) if sources else 'none'}")
        factors.append(f"Assurance level: {assurance}")

        explanation = f"Confidence score: {score:.0%}. " + " ".join(factors)

        ctx.deps.state.current_work_id = work_id
        ctx.deps.state.confidence_score = score
        ctx.deps.state.explanation_text = explanation

        return explanation

    @agent.tool
    async def search_attributions(ctx, query: str) -> str:
        """Search attribution records by title, artist, or keyword.

        Args:
            ctx: Agent context with dependencies.
            query: Search query string.

        Returns:
            Formatted search results.
        """
        results: list[str] = []

        if not ctx.deps.session_factory:
            return "Database not available. Cannot search attribution records."

        from music_attribution.search.hybrid_search import HybridSearchService

        svc = HybridSearchService()
        async with ctx.deps.session_factory() as session:
            hits = await svc.search(query, session=session, limit=10)
        for hit in hits:
            rec = hit.record
            results.append(
                f"- {rec.work_title} by {rec.artist_name} "
                f"(confidence: {rec.confidence_score:.0%}, "
                f"assurance: {rec.assurance_level.value})"
            )

        ctx.deps.state.last_search_query = query
        ctx.deps.state.last_search_count = len(results)

        if not results:
            return f"No attributions found for '{query}'."
        return f"Found {len(results)} result(s):\n" + "\n".join(results)

    @agent.tool
    async def suggest_correction(
        ctx,
        work_id: str,
        field: str,
        current_value: str,
        suggested_value: str,
        reason: str,
    ) -> str:
        """Suggest a correction to an attribution record field.

        Args:
            ctx: Agent context with dependencies.
            work_id: Attribution ID to correct.
            field: Field name to correct.
            current_value: Current value of the field.
            suggested_value: Suggested new value.
            reason: Reason for the correction.

        Returns:
            Confirmation message with correction preview.
        """
        preview = CorrectionPreview(
            field=field,
            current_value=current_value,
            suggested_value=suggested_value,
            reason=reason,
            confidence_in_correction=0.8,
        )

        ctx.deps.state.pending_correction = preview
        ctx.deps.state.current_work_id = work_id

        return (
            f"Correction suggested for {work_id}:\n"
            f"  {field}: '{current_value}' → '{suggested_value}'\n"
            f"  Reason: {reason}\n"
            "Use submit_feedback to finalize."
        )

    @agent.tool
    async def submit_feedback(
        ctx,
        work_id: str,
        overall_assessment: float,
        free_text: str | None = None,
    ) -> str:
        """Submit structured feedback for an attribution record.

        Args:
            ctx: Agent context with dependencies.
            work_id: Attribution ID to submit feedback for.
            overall_assessment: Overall quality assessment (0.0-1.0).
            free_text: Optional free-text notes.

        Returns:
            Confirmation message.
        """
        import uuid as _uuid

        center_bias = 0.45 <= overall_assessment <= 0.55
        bias_warning = ""
        if center_bias:
            bias_warning = " (center bias detected — consider whether you can be more decisive)"

        if not ctx.deps.session_factory:
            return "Database not available. Cannot submit feedback."

        from datetime import UTC, datetime

        from music_attribution.feedback.persistence import AsyncFeedbackRepository
        from music_attribution.schemas.enums import EvidenceTypeEnum, ReviewerRoleEnum
        from music_attribution.schemas.feedback import FeedbackCard

        card = FeedbackCard(
            feedback_id=_uuid.uuid4(),
            attribution_id=_uuid.UUID(work_id),
            reviewer_id="agent-assisted",
            reviewer_role=ReviewerRoleEnum.MUSICOLOGIST,
            attribution_version=1,
            corrections=[],
            overall_assessment=overall_assessment,
            center_bias_flag=center_bias,
            free_text=free_text,
            evidence_type=EvidenceTypeEnum.OTHER,
            submitted_at=datetime.now(UTC),
        )
        repo = AsyncFeedbackRepository()
        async with ctx.deps.session_factory() as session:
            await repo.store(card, session)
            await session.commit()
        feedback_id = str(card.feedback_id)

        ctx.deps.state.pending_correction = None

        return (
            f"Feedback submitted (ID: {feedback_id}):\n"
            f"  Attribution: {work_id}\n"
            f"  Assessment: {overall_assessment:.0%}{bias_warning}\n"
            + (f"  Notes: {free_text}\n" if free_text else "")
            + "Thank you for your feedback."
        )

    return agent
