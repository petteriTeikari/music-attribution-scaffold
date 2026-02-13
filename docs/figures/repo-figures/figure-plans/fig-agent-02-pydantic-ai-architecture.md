# fig-agent-02: PydanticAI Agent Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-02 |
| **Title** | PydanticAI Agent: System Prompt, Dependencies, and 4 Domain Tools |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/agent.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure details the PydanticAI Agent construction. It shows the Agent class with its configuration (model, system prompt, deps_type, retries), the AgentDeps dataclass (state + session_factory), and the four registered tools with their input/output signatures. The model routing via ATTRIBUTION_AGENT_MODEL env var and the Pydantic result models (ExplainConfidenceResult, SearchResultSet, SuggestCorrectionResult, SubmitFeedbackResult) are included.

The key message is: "The PydanticAI agent is configured with a domain-specific system prompt about music attribution, receives database access via AgentDeps, and exposes 4 tools that directly query and modify attribution records."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  PYDANTIC AI AGENT ARCHITECTURE                                        |
|  ■ 4 Domain Tools                                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. AGENT CONFIGURATION                                                |
|  ───────────────────────                                               |
|                                                                        |
|  create_attribution_agent() -> Agent[AgentDeps, str]                   |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  model: _get_agent_model()  (from Settings.attribution_agent_model)│ |
|  │  system_prompt: SYSTEM_PROMPT  (music attribution expert)        │  |
|  │  deps_type: AgentDeps                                            │  |
|  │  retries: 2                                                      │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  II. DEPENDENCIES                                                      |
|  ────────────────                                                      |
|                                                                        |
|  @dataclass AgentDeps                                                  |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  state: AttributionAgentState        (shared with frontend)      │  |
|  │  session_factory: async_sessionmaker  (PostgreSQL access)        │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  III. FOUR TOOLS                                                       |
|  ───────────────                                                       |
|                                                                        |
|  ┌────────────────────────────────────────────────────────────────┐   |
|  │  @agent.tool                                                    │   |
|  │  explain_confidence(work_id: str) -> str                        │   |
|  │  ■ Looks up record by UUID                                      │   |
|  │  ■ Breaks down: source agreement, source count, assurance level │   |
|  │  ■ Updates state: current_work_id, confidence_score, explanation │   |
|  ├────────────────────────────────────────────────────────────────┤   |
|  │  @agent.tool                                                    │   |
|  │  search_attributions(query: str) -> str                         │   |
|  │  ■ Uses HybridSearchService (text + vector)                     │   |
|  │  ■ Returns up to 10 results                                     │   |
|  │  ■ Updates state: last_search_query, last_search_count          │   |
|  ├────────────────────────────────────────────────────────────────┤   |
|  │  @agent.tool                                                    │   |
|  │  suggest_correction(work_id, field, current, suggested,         │   |
|  │                     reason: str) -> str                          │   |
|  │  ■ Creates CorrectionPreview                                    │   |
|  │  ■ Updates state: pending_correction, current_work_id           │   |
|  ├────────────────────────────────────────────────────────────────┤   |
|  │  @agent.tool                                                    │   |
|  │  submit_feedback(work_id: str, overall_assessment: float,       │   |
|  │                  free_text: str | None) -> str                  │   |
|  │  ■ Creates FeedbackCard with center bias detection              │   |
|  │  ■ Persists via AsyncFeedbackRepository                         │   |
|  │  ■ Clears state: pending_correction                             │   |
|  └────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  MODEL ROUTING                                                         |
|  ─────────────                                                         |
|  ■ ATTRIBUTION_AGENT_MODEL env var -> Settings.attribution_agent_model |
|  ■ Default: anthropic:claude-haiku-4-5                                 |
|  ■ PydanticAI FallbackModel for failover                               |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "PYDANTIC AI AGENT ARCHITECTURE" in display font |
| Agent configuration | `processing_stage` | Model, system prompt, deps_type, retries |
| AgentDeps dataclass | `processing_stage` | state (AttributionAgentState) + session_factory |
| explain_confidence tool | `source_corroborate` | Input, behavior, state updates |
| search_attributions tool | `etl_extract` | HybridSearchService, result limit, state updates |
| suggest_correction tool | `feedback_loop` | CorrectionPreview creation, state updates |
| submit_feedback tool | `feedback_loop` | FeedbackCard creation, center bias detection, persistence |
| Model routing | `decision_point` | Env var, default model, FallbackModel |
| Roman numerals I-III | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. There are exactly 4 tools: explain_confidence, search_attributions, suggest_correction, submit_feedback.
2. The agent type is Agent[AgentDeps, str] -- it returns strings, not structured Pydantic models.
3. AgentDeps is a @dataclass (not a Pydantic model) with state and session_factory fields.
4. The default model is obtained from Settings.attribution_agent_model (configured via env var ATTRIBUTION_AGENT_MODEL).
5. The default model string is "anthropic:claude-haiku-4-5" (NOT Sonnet or Opus).
6. explain_confidence uses AsyncAttributionRepository.find_by_id().
7. search_attributions uses HybridSearchService.search() with limit=10.
8. submit_feedback detects center bias when overall_assessment is between 0.45 and 0.55.
9. submit_feedback creates a FeedbackCard with reviewer_role=ReviewerRoleEnum.MUSICOLOGIST.
10. The agent is created by create_attribution_agent() factory function, not directly instantiated.

## Alt Text

PydanticAI agent architecture showing configuration, AgentDeps dependencies, four domain tools with signatures, and model routing via env var.
