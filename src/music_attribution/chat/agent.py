"""PydanticAI attribution agent with domain tools.

Provides four domain tools for CopilotKit frontend interaction via the
AG-UI (Agent-GUI) protocol. The agent acts as a conversational interface
to the attribution scaffold, enabling artists, managers, and musicologists
to query, review, and improve attribution records through natural language.

Tools
-----
explain_confidence
    Explain why a work has a given confidence score by decomposing
    source agreement, corroborating sources, and assurance level.
search_attributions
    Search across attribution records by title, artist, or keyword
    using the hybrid search service (text + vector + graph).
suggest_correction
    Propose a correction to a specific field on an attribution record,
    generating a CorrectionPreview for frontend review.
submit_feedback
    Submit a structured FeedbackCard for an attribution record,
    including overall assessment and optional free-text notes.

Notes
-----
The agent uses PydanticAI's ``Agent`` class with dependency injection
(``AgentDeps``) for database access. The system prompt encodes domain
knowledge about A0-A3 assurance levels, the Oracle Problem, and
conformal prediction (see Teikari 2026, Sections 3-5).

The model identifier is loaded lazily from ``Settings.attribution_agent_model``
so that import-time side effects are avoided and tests can mock the model.

See Also
--------
music_attribution.chat.state : Shared agent/frontend state model.
music_attribution.chat.agui_endpoint : AG-UI SSE streaming endpoint.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from music_attribution.chat.state import AttributionAgentState, CorrectionPreview
from music_attribution.constants import (
    AGREEMENT_HIGH_THRESHOLD,
    AGREEMENT_MODERATE_THRESHOLD,
    CENTER_BIAS_HIGH,
    CENTER_BIAS_LOW,
)

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
    """Get the PydanticAI model identifier from application settings.

    Performs a lazy import of ``Settings`` to avoid requiring environment
    variables at module import time. This allows tests to patch the
    function without triggering configuration validation.

    Returns
    -------
    str
        PydanticAI model string (e.g. ``"anthropic:claude-haiku-4-5"``).
    """
    from music_attribution.config import Settings

    settings = Settings()  # type: ignore[call-arg]
    return settings.attribution_agent_model


@dataclass
class AgentDeps:
    """Dependencies injected into PydanticAI agent tools at runtime.

    PydanticAI's dependency injection system passes this object to every
    tool call via ``ctx.deps``. Tools use the session factory for
    async database access and the state object for AG-UI state
    synchronisation with the CopilotKit frontend.

    Attributes
    ----------
    state : AttributionAgentState
        Shared mutable state that is serialised as AG-UI StateSnapshot
        events and consumed by CopilotKit ``useCopilotReadable`` hooks.
    session_factory : async_sessionmaker[AsyncSession] | None
        SQLAlchemy async session factory bound to the PostgreSQL engine.
        ``None`` when running without a database (e.g. unit tests),
        in which case tools return a graceful fallback message.
    """

    state: AttributionAgentState
    session_factory: async_sessionmaker[AsyncSession] | None = field(default=None)


class ExplainConfidenceResult(BaseModel):
    """Structured result of the ``explain_confidence`` tool.

    Captures both the numeric score and the human-readable explanation
    with contributing factors, enabling the frontend to render a rich
    confidence breakdown panel.

    Attributes
    ----------
    work_id : str
        Attribution record identifier that was explained.
    confidence_score : float
        Overall confidence score (0.0--1.0).
    explanation : str
        Human-readable explanation combining all factors.
    factors : list[str]
        Individual contributing factors (source agreement, number of
        sources, assurance level) as separate strings.
    """

    work_id: str
    confidence_score: float
    explanation: str
    factors: list[str] = Field(default_factory=list)


class SearchResult(BaseModel):
    """A single attribution search result returned by the agent.

    Provides the minimal fields needed for the frontend to render
    a search result row: title, artist, confidence, and assurance.

    Attributes
    ----------
    attribution_id : str
        UUID of the matching attribution record.
    work_title : str
        Display title of the musical work.
    artist_name : str
        Primary artist name.
    confidence_score : float
        Overall confidence score (0.0--1.0).
    assurance_level : str
        A0--A3 assurance level string (e.g. ``"A3"``).
    """

    attribution_id: str
    work_title: str
    artist_name: str
    confidence_score: float
    assurance_level: str


class SearchResultSet(BaseModel):
    """Aggregated result set from the ``search_attributions`` tool.

    Wraps the query, matching results, and total count for pagination.

    Attributes
    ----------
    query : str
        The original search query string.
    results : list[SearchResult]
        Matching attribution records (up to the limit).
    total_count : int
        Total number of matches (may exceed ``len(results)``).
    """

    query: str
    results: list[SearchResult]
    total_count: int


class SuggestCorrectionResult(BaseModel):
    """Result of the ``suggest_correction`` tool.

    Pairs the target work with a ``CorrectionPreview`` that the frontend
    renders as a diff (current value vs. suggested value) for user
    approval before submission.

    Attributes
    ----------
    work_id : str
        Attribution record identifier to correct.
    correction : CorrectionPreview
        Structured preview of the proposed change.
    """

    work_id: str
    correction: CorrectionPreview


class SubmitFeedbackResult(BaseModel):
    """Result of the ``submit_feedback`` tool.

    Returned after a FeedbackCard is persisted, confirming the
    submission and indicating whether center-bias was detected.

    Attributes
    ----------
    feedback_id : str
        UUID of the created FeedbackCard.
    attribution_id : str
        UUID of the attribution record the feedback targets.
    accepted : bool
        Whether the feedback was successfully stored.
    message : str
        Human-readable confirmation message (may include bias warning).
    """

    feedback_id: str
    attribution_id: str
    accepted: bool
    message: str


def create_attribution_agent() -> Agent[AgentDeps, str]:
    """Create and configure the PydanticAI attribution agent.

    Instantiates a PydanticAI ``Agent`` with a domain-specific system
    prompt and registers four tool functions (``explain_confidence``,
    ``search_attributions``, ``suggest_correction``, ``submit_feedback``).

    The agent model identifier is resolved lazily from application
    settings via ``_get_agent_model()``. The agent is configured with
    ``retries=2`` for transient LLM failures.

    Returns
    -------
    Agent[AgentDeps, str]
        Configured PydanticAI Agent with four domain tools, typed to
        accept ``AgentDeps`` and return ``str`` responses.

    Notes
    -----
    Tool functions are registered using PydanticAI's ``@agent.tool``
    decorator, which provides automatic parameter validation and
    dependency injection via ``ctx.deps``.

    Each tool updates ``ctx.deps.state`` to synchronise AG-UI state
    with the CopilotKit frontend (e.g. setting ``current_work_id``
    after explaining a confidence score).
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

        Fetches the full ``AttributionRecord`` from the database and
        decomposes the confidence score into contributing factors:
        source agreement level, number of corroborating data sources,
        and the A0--A3 assurance level.

        Updates ``ctx.deps.state`` with the current work context so the
        CopilotKit frontend can highlight the relevant record.

        Parameters
        ----------
        ctx : RunContext[AgentDeps]
            PydanticAI run context providing access to ``AgentDeps``.
        work_id : str
            UUID string of the attribution record to explain.

        Returns
        -------
        str
            Human-readable explanation combining all confidence factors,
            or an error message if the record is not found.
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
        if agreement > AGREEMENT_HIGH_THRESHOLD:
            factors.append(f"High source agreement ({agreement:.0%})")
        elif agreement > AGREEMENT_MODERATE_THRESHOLD:
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

        Delegates to ``HybridSearchService`` which fuses text search,
        vector similarity, and graph context via Reciprocal Rank Fusion
        (RRF). Results are formatted as a bullet list with title,
        artist, confidence, and assurance level.

        Updates ``ctx.deps.state`` with the search query and result
        count for the CopilotKit frontend to display.

        Parameters
        ----------
        ctx : RunContext[AgentDeps]
            PydanticAI run context providing access to ``AgentDeps``.
        query : str
            Free-text search query (title, artist name, or keyword).

        Returns
        -------
        str
            Formatted search results as a bullet list, or a "not found"
            message if no records match.
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

        Creates a ``CorrectionPreview`` and stores it in
        ``ctx.deps.state.pending_correction`` so the CopilotKit
        frontend can render a before/after diff for user approval.
        The correction is not applied until the user confirms via
        ``submit_feedback``.

        Parameters
        ----------
        ctx : RunContext[AgentDeps]
            PydanticAI run context providing access to ``AgentDeps``.
        work_id : str
            UUID string of the attribution record to correct.
        field : str
            Name of the field being corrected (e.g. ``"role_detail"``).
        current_value : str
            Current value of the field in the attribution record.
        suggested_value : str
            Proposed replacement value.
        reason : str
            Justification for the correction.

        Returns
        -------
        str
            Confirmation message with a human-readable correction
            preview and instructions to finalise via ``submit_feedback``.
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

        Creates and persists a ``FeedbackCard`` (BO-4 boundary object)
        via ``AsyncFeedbackRepository``. Detects center-bias when the
        assessment falls in the 0.45--0.55 range and includes a warning
        in the response (see Teikari 2026, Section 5 on calibration).

        Clears ``ctx.deps.state.pending_correction`` after successful
        submission.

        Parameters
        ----------
        ctx : RunContext[AgentDeps]
            PydanticAI run context providing access to ``AgentDeps``.
        work_id : str
            UUID string of the attribution record to submit feedback for.
        overall_assessment : float
            Overall quality assessment on a 0.0--1.0 scale. Values in
            the 0.45--0.55 range trigger a center-bias warning.
        free_text : str | None, optional
            Optional free-text notes from the reviewer.

        Returns
        -------
        str
            Confirmation message including feedback ID, assessment
            value, and any bias warning.
        """
        import uuid as _uuid

        center_bias = CENTER_BIAS_LOW <= overall_assessment <= CENTER_BIAS_HIGH
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
