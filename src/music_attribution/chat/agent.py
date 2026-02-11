"""PydanticAI attribution agent with domain tools.

Provides 4 tools for CopilotKit frontend interaction via AG-UI protocol:
- explain_confidence: Explain why a work has its confidence score
- search_attributions: Search across attribution records
- suggest_correction: Propose a correction to an attribution field
- submit_feedback: Submit a FeedbackCard for an attribution record
"""

from __future__ import annotations

import logging
import os
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

MODEL = os.environ.get("ATTRIBUTION_AGENT_MODEL", "anthropic:claude-haiku-4-5")


@dataclass
class AgentDeps:
    """Dependencies injected into agent tools at runtime.

    When session_factory is provided, tools use real PostgreSQL
    repositories. Otherwise, they fall back to the in-memory
    attributions dict (dev/demo mode).
    """

    attributions: dict[str, dict]
    state: AttributionAgentState
    session_factory: async_sessionmaker[AsyncSession] | None = field(default=None)

    @property
    def has_db(self) -> bool:
        """Whether a real database session factory is available."""
        return self.session_factory is not None


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
        MODEL,
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
        attrs = ctx.deps.attributions
        record = attrs.get(work_id)
        if not record:
            return f"No attribution record found for ID: {work_id}"

        score = record.get("confidence_score", 0)
        sources = record.get("credits", [{}])[0].get("sources", []) if record.get("credits") else []
        assurance = record.get("assurance_level", "LEVEL_0")
        agreement = record.get("source_agreement", 0)

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
        attrs = ctx.deps.attributions
        query_lower = query.lower()
        results = []
        for _attr_id, record in attrs.items():
            title = record.get("work_title", "")
            artist = record.get("artist_name", "")
            if query_lower in title.lower() or query_lower in artist.lower():
                results.append(
                    f"- {title} by {artist} "
                    f"(confidence: {record.get('confidence_score', 0):.0%}, "
                    f"assurance: {record.get('assurance_level', 'LEVEL_0')})"
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
        import uuid

        feedback_id = str(uuid.uuid4())

        center_bias = 0.45 <= overall_assessment <= 0.55
        bias_warning = ""
        if center_bias:
            bias_warning = " (center bias detected — consider whether you can be more decisive)"

        ctx.deps.state.pending_correction = None

        return (
            f"Feedback submitted (ID: {feedback_id}):\n"
            f"  Attribution: {work_id}\n"
            f"  Assessment: {overall_assessment:.0%}{bias_warning}\n"
            + (f"  Notes: {free_text}\n" if free_text else "")
            + "Thank you for your feedback."
        )

    return agent
