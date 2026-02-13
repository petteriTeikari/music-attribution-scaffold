# fig-choice-01: Why PydanticAI over LangChain?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-01 |
| **Title** | Why PydanticAI over LangChain? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the AI framework strategy decision. The scaffold chose `direct_api_pydantic` (PydanticAI) over orchestration frameworks like LangChain/LangGraph. This is a philosophical choice: thin typed wrappers over heavy middleware. Shows the concrete differences in code patterns, dependency weight, and debugging experience.

The key message is: "PydanticAI provides typed, Pydantic-native LLM integration with zero middleware -- the scaffold values simplicity and type safety over framework magic."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY PYDANTICAI OVER LANGCHAIN?                                |
|  ■ AI Framework Strategy: direct_api_pydantic (selected)       |
+-------------------------------+-------------------------------+
|                               |                               |
|  PYDANTICAI (selected)        |  LANGCHAIN                    |
|  ═══════════════════          |  ═════════                    |
|                               |                               |
|  agent = Agent(               |  chain = prompt |             |
|    'anthropic:claude-....',   |    ChatAnthropic() |         |
|    result_type=Attribution,   |    StrOutputParser() |        |
|    tools=[search_mb, ...]     |    PydanticOutputParser(...)  |
|  )                            |  result = chain.invoke(...)    |
|  result = agent.run(prompt)   |                               |
|                               |                               |
|  ■ Typed end-to-end           |  ■ Middleware-heavy            |
|    Pydantic models in,        |    Chain composition,          |
|    Pydantic models out        |    multiple abstraction layers |
|                               |                               |
|  ■ 1 dependency               |  ■ 50+ transitive deps        |
|    pydantic-ai                |    langchain, langchain-core,  |
|                               |    langchain-community, ...    |
|                               |                               |
|  ■ Native FallbackModel       |  ■ Framework-specific fallback |
|    Zero-config failover       |    Requires RunnableWithFallba |
|                               |                               |
|  ■ Debug: standard Python     |  ■ Debug: framework internals  |
|    Stack traces you can read  |    Opaque chain execution      |
|                               |                               |
|  ■ MCP: via tool definitions  |  ■ MCP: via LangGraph MCP     |
|                               |                               |
+-------------------------------+-------------------------------+
|  PRD Node: ai_framework_strategy = direct_api_pydantic (P=0.40)|
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY PYDANTICAI OVER LANGCHAIN?" with coral accent square |
| PydanticAI panel (left) | `selected_option` | Code sample, feature bullets, selected indicator |
| LangChain panel (right) | `deferred_option` | Code sample, feature bullets, alternative indicator |
| Code samples | `data_mono` | Minimal code showing agent creation patterns |
| Feature comparison bullets | `feature_list` | Typed vs middleware, deps, fallback, debug, MCP |
| Vertical divider | `accent_line_v` | Coral red vertical line |
| PRD reference footer | `callout_bar` | Node name and probability |

## Anti-Hallucination Rules

1. The AI framework strategy decision has four options: direct_api_pydantic (selected), lightweight_sdk, orchestration_framework, no_llm.
2. PydanticAI is the library -- the PRD option is `direct_api_pydantic`, NOT "pydantic_ai".
3. PydanticAI FallbackModel is a real feature providing automatic failover between models.
4. The scaffold uses PydanticAI with Agent, result_type, and tools -- per the actual codebase.
5. LangChain is NOT rejected -- it is the `orchestration_framework` option with status "viable".
6. The PydanticAI string for the default agent model is "anthropic:claude-haiku-4-5".
7. Do NOT claim LangChain is bad -- frame as trade-off between simplicity and framework features.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Split-panel comparison of PydanticAI and LangChain showing code patterns, dependency counts, fallback mechanisms, and debugging experience differences.
