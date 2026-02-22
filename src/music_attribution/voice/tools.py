"""Bridge PydanticAI domain tools to Pipecat function calling.

Registers the 4 existing domain tools (explain_confidence, search_attributions,
suggest_correction, submit_feedback) as Pipecat-compatible function schemas
and handlers. Tool handlers delegate to the existing PydanticAI tool logic —
no business logic duplication.

The bridge uses Pipecat's ``FunctionCallParams`` for handler signatures and
``FunctionSchema`` for tool declaration. Each handler creates an in-memory
``AgentDeps`` with the shared database session factory.

See Also
--------
music_attribution.chat.agent : Existing PydanticAI agent with domain tools.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from music_attribution.constants import (
    AGREEMENT_HIGH_THRESHOLD,
    AGREEMENT_MODERATE_THRESHOLD,
    CENTER_BIAS_HIGH,
    CENTER_BIAS_LOW,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

logger = logging.getLogger(__name__)

# Optional Pipecat imports
try:
    from pipecat.adapters.schemas.function_schema import FunctionSchema

    PIPECAT_AVAILABLE = True
except ImportError:
    PIPECAT_AVAILABLE = False

# Module-level session factory — set by server.py on startup
_session_factory: async_sessionmaker[AsyncSession] | None = None


def set_session_factory(factory: async_sessionmaker[AsyncSession]) -> None:
    """Set the database session factory for voice tool handlers.

    Called by server.py during FastAPI startup to share the same
    database connection pool used by the REST API.

    Parameters
    ----------
    factory : async_sessionmaker[AsyncSession]
        SQLAlchemy async session factory.
    """
    global _session_factory  # noqa: PLW0603
    _session_factory = factory
    logger.info("Voice tools: database session factory configured")


def get_tool_schemas() -> list[dict]:
    """Return Pipecat-compatible function schemas for domain tools.

    Each schema defines the function name, description, and parameters
    in the format expected by Pipecat's ToolsSchema / FunctionSchema.

    Returns
    -------
    list[dict]
        List of function schema dictionaries.
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "explain_confidence",
                "description": "Explain the confidence score for an attribution record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_id": {
                            "type": "string",
                            "description": "UUID of the attribution record",
                        },
                    },
                    "required": ["work_id"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_attributions",
                "description": "Search attribution records by title, artist, or keyword",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query",
                        },
                    },
                    "required": ["query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "suggest_correction",
                "description": "Suggest a correction to an attribution record field",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_id": {"type": "string"},
                        "field": {"type": "string"},
                        "current_value": {"type": "string"},
                        "suggested_value": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["work_id", "field", "current_value", "suggested_value", "reason"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "submit_feedback",
                "description": "Submit structured feedback for an attribution record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_id": {"type": "string"},
                        "overall_assessment": {"type": "number"},
                        "free_text": {"type": "string"},
                    },
                    "required": ["work_id", "overall_assessment"],
                },
            },
        },
    ]


def get_function_schemas() -> list[Any]:
    """Return Pipecat FunctionSchema objects for domain tools.

    This is the Pipecat-native format used by ``ToolsSchema``.
    Falls back to dict format when Pipecat is not installed.

    Returns
    -------
    list[FunctionSchema] | list[dict]
        FunctionSchema objects when Pipecat is available, dicts otherwise.
    """
    if not PIPECAT_AVAILABLE:
        return get_tool_schemas()

    schemas = []
    for tool in get_tool_schemas():
        func = tool["function"]
        schemas.append(
            FunctionSchema(
                name=func["name"],
                description=func["description"],
                properties=func["parameters"].get("properties", {}),
                required=func["parameters"].get("required", []),
            )
        )
    return schemas


def register_domain_tools(llm_service: Any) -> None:
    """Register all 4 domain tools as Pipecat function handlers.

    Each handler bridges to the existing PydanticAI tool logic in
    ``music_attribution.chat.agent``, using the shared session factory
    for database access.

    Parameters
    ----------
    llm_service : LLMService
        A Pipecat LLM service instance to register handlers on.

    Raises
    ------
    ImportError
        If Pipecat is not installed.
    """
    if not PIPECAT_AVAILABLE:
        msg = "pipecat-ai is not installed. Install with: uv sync --group voice"
        raise ImportError(msg)

    llm_service.register_function("explain_confidence", _handle_explain_confidence)
    llm_service.register_function("search_attributions", _handle_search_attributions)
    llm_service.register_function("suggest_correction", _handle_suggest_correction)
    llm_service.register_function("submit_feedback", _handle_submit_feedback)

    logger.info("Voice tools: 4 domain functions registered with LLM service")


def _validate_uuid(value: str) -> bool:
    """Validate that a string is a valid UUID.

    Parameters
    ----------
    value : str
        String to validate.

    Returns
    -------
    bool
        True if the string is a valid UUID.
    """
    import uuid as _uuid

    try:
        _uuid.UUID(value)
    except (ValueError, AttributeError):
        return False
    return True


async def _handle_explain_confidence(params: Any) -> None:
    """Handle explain_confidence function call from voice LLM.

    Bridges to the existing PydanticAI explain_confidence tool by
    directly calling the attribution repository.

    Parameters
    ----------
    params : FunctionCallParams
        Pipecat function call parameters with work_id argument.
    """
    work_id = params.arguments.get("work_id", "")

    if not _validate_uuid(work_id):
        await params.result_callback({"explanation": f"Invalid work ID format: '{work_id}'. Expected a UUID."})
        return

    if not _session_factory:
        await params.result_callback({"explanation": "Database not available. Cannot look up attribution records."})
        return

    try:
        import uuid as _uuid

        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()
        async with _session_factory() as session:
            record = await repo.find_by_id(_uuid.UUID(work_id), session)

        if not record:
            await params.result_callback({"explanation": f"No attribution record found for ID: {work_id}"})
            return

        score = record.confidence_score
        sources: list[str] = []
        if record.credits:
            sources = [s.value for s in record.credits[0].sources]
        assurance = record.assurance_level.value
        agreement = record.source_agreement

        factors = []
        if agreement > AGREEMENT_HIGH_THRESHOLD:
            factors.append(f"High source agreement at {agreement:.0%}")
        elif agreement > AGREEMENT_MODERATE_THRESHOLD:
            factors.append(f"Moderate source agreement at {agreement:.0%}")
        else:
            factors.append(f"Low source agreement at {agreement:.0%}")
        factors.append(
            f"Data from {len(sources)} source{'s' if len(sources) != 1 else ''}: "
            f"{', '.join(sources) if sources else 'none'}"
        )
        factors.append(f"Assurance level {assurance}")

        explanation = f"The confidence score is {score:.0%}. {'. '.join(factors)}."

        await params.result_callback({"explanation": explanation})

    except Exception:
        logger.exception("Error in explain_confidence handler")
        await params.result_callback({"explanation": f"Error looking up attribution record {work_id}."})


async def _handle_search_attributions(params: Any) -> None:
    """Handle search_attributions function call from voice LLM.

    Parameters
    ----------
    params : FunctionCallParams
        Pipecat function call parameters with query argument.
    """
    query = params.arguments.get("query", "")

    if not _session_factory:
        await params.result_callback({"results": "Database not available. Cannot search attribution records."})
        return

    try:
        from music_attribution.search.hybrid_search import HybridSearchService

        svc = HybridSearchService()
        async with _session_factory() as session:
            hits = await svc.search(query, session=session, limit=5)

        if not hits:
            await params.result_callback({"results": f"No attributions found for '{query}'."})
            return

        results = []
        for hit in hits:
            rec = hit.record
            results.append(
                f"{rec.work_title} by {rec.artist_name}, "
                f"confidence {rec.confidence_score:.0%}, "
                f"assurance {rec.assurance_level.value}"
            )

        summary = f"Found {len(results)} result{'s' if len(results) != 1 else ''}. "
        summary += ". ".join(results) + "."

        await params.result_callback({"results": summary})

    except Exception:
        logger.exception("Error in search_attributions handler")
        await params.result_callback({"results": f"Error searching for '{query}'."})


async def _handle_suggest_correction(params: Any) -> None:
    """Handle suggest_correction function call from voice LLM.

    Parameters
    ----------
    params : FunctionCallParams
        Pipecat function call parameters with correction details.
    """
    work_id = params.arguments.get("work_id", "")

    if not _validate_uuid(work_id):
        await params.result_callback({"result": f"Invalid work ID format: '{work_id}'. Expected a UUID."})
        return

    field_name = params.arguments.get("field", "")
    current_value = params.arguments.get("current_value", "")
    suggested_value = params.arguments.get("suggested_value", "")
    reason = params.arguments.get("reason", "")

    response = (
        f"Correction suggested for record {work_id}: "
        f"change {field_name} from '{current_value}' to '{suggested_value}'. "
        f"Reason: {reason}. "
        "Please confirm to apply this correction."
    )

    await params.result_callback({"result": response})


async def _handle_submit_feedback(params: Any) -> None:
    """Handle submit_feedback function call from voice LLM.

    Parameters
    ----------
    params : FunctionCallParams
        Pipecat function call parameters with feedback details.
    """
    work_id = params.arguments.get("work_id", "")

    if not _validate_uuid(work_id):
        await params.result_callback({"result": f"Invalid work ID format: '{work_id}'. Expected a UUID."})
        return

    assessment = params.arguments.get("overall_assessment", 0.5)
    free_text = params.arguments.get("free_text", "")

    if not _session_factory:
        await params.result_callback({"result": "Database not available. Cannot submit feedback."})
        return

    try:
        import uuid as _uuid
        from datetime import UTC, datetime

        from music_attribution.feedback.persistence import AsyncFeedbackRepository
        from music_attribution.schemas.enums import EvidenceTypeEnum, ReviewerRoleEnum
        from music_attribution.schemas.feedback import FeedbackCard

        center_bias = CENTER_BIAS_LOW <= assessment <= CENTER_BIAS_HIGH
        card = FeedbackCard(
            feedback_id=_uuid.uuid4(),
            attribution_id=_uuid.UUID(work_id),
            reviewer_id="voice-agent-assisted",
            reviewer_role=ReviewerRoleEnum.MUSICOLOGIST,
            attribution_version=1,
            corrections=[],
            overall_assessment=assessment,
            center_bias_flag=center_bias,
            free_text=free_text or None,
            evidence_type=EvidenceTypeEnum.OTHER,
            submitted_at=datetime.now(UTC),
        )
        repo = AsyncFeedbackRepository()
        async with _session_factory() as session:
            await repo.store(card, session)
            await session.commit()

        bias_note = " Note: center bias detected." if center_bias else ""
        response = f"Feedback submitted for record {work_id}. Assessment: {assessment:.0%}.{bias_note} Thank you."

        await params.result_callback({"result": response})

    except Exception:
        logger.exception("Error in submit_feedback handler")
        await params.result_callback({"result": f"Error submitting feedback for {work_id}."})
