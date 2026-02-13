# fig-agent-07: Model Failover Strategy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-07 |
| **Title** | Model Failover Strategy: PydanticAI FallbackModel with Environment Configuration |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/agent.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how the agent's LLM model is configured and how failover works. The ATTRIBUTION_AGENT_MODEL env var feeds into Settings, which create_attribution_agent() reads via _get_agent_model(). PydanticAI's FallbackModel chain is shown: Haiku 4.5 (default, fast, cheap) -> Sonnet 4.5 (fallback, more capable) -> Opus (complex tasks). The retries=2 configuration for automatic retry on transient failures is also shown.

The key message is: "The agent defaults to Claude Haiku 4.5 for fast, cheap responses, with PydanticAI FallbackModel providing automatic failover to more capable models, all configurable via a single environment variable."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  MODEL FAILOVER STRATEGY                                               |
|  ■ PydanticAI FallbackModel                                           |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. CONFIGURATION CHAIN                                                |
|  ───────────────────────                                               |
|                                                                        |
|  Environment                                                           |
|  ┌────────────────────────────────────────┐                           |
|  │  ATTRIBUTION_AGENT_MODEL=              │                           |
|  │    "anthropic:claude-haiku-4-5"        │   (default)               |
|  └────────────────┬───────────────────────┘                           |
|                   │                                                    |
|                   ▼                                                    |
|  Settings (Pydantic BaseSettings)                                      |
|  ┌────────────────────────────────────────┐                           |
|  │  attribution_agent_model: str          │                           |
|  └────────────────┬───────────────────────┘                           |
|                   │                                                    |
|                   ▼                                                    |
|  _get_agent_model() -> str                                             |
|  ┌────────────────────────────────────────┐                           |
|  │  return settings.attribution_agent_model│                           |
|  └────────────────┬───────────────────────┘                           |
|                   │                                                    |
|                   ▼                                                    |
|  Agent(model_string, retries=2)                                        |
|                                                                        |
|  II. FAILOVER CHAIN                                                    |
|  ──────────────────                                                    |
|                                                                        |
|  ┌─────────────────────┐     ┌─────────────────────┐                 |
|  │  Claude Haiku 4.5    │     │  Claude Sonnet 4.5   │                 |
|  │  (Default Primary)   │ ──> │  (Fallback)          │                 |
|  │  ■ Fast (< 1s)       │     │  ■ More capable      │                 |
|  │  ■ Cheapest           │     │  ■ Complex queries   │                 |
|  │  ■ 4 tool calls       │     │  ■ Nuanced reasoning │                 |
|  │  ■ Most queries       │     │                      │                 |
|  └─────────────────────┘     └─────────────────────┘                 |
|          │                            │                                |
|          │  retries=2                 │  retries=2                     |
|          │  (auto-retry on           │  (auto-retry on                |
|          │   transient failure)       │   transient failure)           |
|          │                            │                                |
|                                                                        |
|  III. PRD DECISION                                                     |
|  ─────────────────                                                     |
|                                                                        |
|  llm_provider: anthropic_primary (selected)                            |
|  llm_routing_strategy: pydantic_ai_native (selected)                   |
|  ■ FallbackModel for automatic model cascading                         |
|  ■ Runtime override via ATTRIBUTION_AGENT_MODEL env var                |
|  ■ No custom routing logic needed -- PydanticAI handles it             |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "MODEL FAILOVER STRATEGY" in display font |
| Env var | `data_mono` | ATTRIBUTION_AGENT_MODEL configuration |
| Settings class | `processing_stage` | Pydantic BaseSettings reading env var |
| _get_agent_model | `processing_stage` | Helper function returning model string |
| Haiku primary | `selected_option` | Default model: fast, cheap |
| Sonnet fallback | `deferred_option` | Fallback model: more capable |
| Retry mechanism | `security_layer` | retries=2 for transient failures |
| PRD decision reference | `decision_point` | llm_provider and llm_routing_strategy selections |
| Failover arrow | `data_flow` | Haiku -> Sonnet cascade |

## Anti-Hallucination Rules

1. The default model is "anthropic:claude-haiku-4-5" (NOT Sonnet or Opus).
2. The env var is ATTRIBUTION_AGENT_MODEL (exact name).
3. retries=2 is set on the Agent constructor (not a FallbackModel setting).
4. _get_agent_model() is a regular function, not an async function.
5. The PRD decisions are: llm_provider=anthropic_primary, llm_routing_strategy=pydantic_ai_native.
6. PydanticAI's FallbackModel is the recommended approach for model cascading.
7. The model string format is "provider:model-name" (PydanticAI convention).
8. The agent is created as a lazy singleton via _get_agent() in agui_endpoint.py.

## Alt Text

Model failover chain: ATTRIBUTION_AGENT_MODEL env var configures default Haiku 4.5, with PydanticAI FallbackModel cascading to Sonnet 4.5 on failure.
