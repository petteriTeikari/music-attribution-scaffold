"""Shared state model for the attribution chat agent.

Used by PydanticAI agent and exposed via AG-UI StateSnapshot/StateDelta
events for CopilotKit to consume on the frontend.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class AttributionAgentState(BaseModel):
    """Shared state between agent and frontend via AG-UI protocol.

    Fields correspond to AG-UI state properties that CopilotKit
    useCopilotReadable hooks observe for real-time UI updates.
    """

    current_work_id: str | None = Field(
        default=None,
        description="Attribution ID of the work currently being discussed",
    )
    current_work_title: str | None = Field(
        default=None,
        description="Display title of the current work",
    )
    confidence_score: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Current confidence score being discussed",
    )
    review_queue_size: int = Field(
        default=0,
        ge=0,
        description="Number of works pending review",
    )
    pending_correction: CorrectionPreview | None = Field(
        default=None,
        description="Preview of a correction the agent is suggesting",
    )
    explanation_text: str | None = Field(
        default=None,
        description="Agent's current explanation text for confidence score",
    )
    last_search_query: str | None = Field(
        default=None,
        description="Last search query the agent executed",
    )
    last_search_count: int = Field(
        default=0,
        ge=0,
        description="Number of results from last search",
    )


class CorrectionPreview(BaseModel):
    """Preview of a correction suggestion before submission."""

    field: str = Field(description="Field being corrected")
    current_value: str = Field(description="Current value in the record")
    suggested_value: str = Field(description="Suggested new value")
    reason: str = Field(description="Why the agent suggests this correction")
    confidence_in_correction: float = Field(
        ge=0.0,
        le=1.0,
        description="Agent's confidence in the suggested correction",
    )
