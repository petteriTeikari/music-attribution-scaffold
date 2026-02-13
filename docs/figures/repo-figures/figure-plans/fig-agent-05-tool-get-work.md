# fig-agent-05: Agent Tool: explain_confidence

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-05 |
| **Title** | Agent Tool: explain_confidence -- From Work ID to Natural Language Explanation |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/agent.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure traces the explain_confidence tool's execution path: input (work_id string) -> UUID conversion -> AsyncAttributionRepository.find_by_id() query -> extract confidence_score, credits sources, assurance_level, source_agreement -> generate human-readable factors list -> update AttributionAgentState -> return explanation string. Error handling (no session, no record found) is shown.

The key message is: "explain_confidence breaks a confidence score into human-readable factors -- source agreement level, source count and names, and assurance tier -- updating shared state so CopilotKit can reflect the explanation in the UI."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  AGENT TOOL: explain_confidence                                        |
|  ■ Confidence Score Breakdown                                          |
+-----------------------------------------------------------------------+
|                                                                        |
|  INPUT                                                                 |
|  ─────                                                                 |
|  work_id: str  (e.g., "550e8400-e29b-41d4-a716-446655440000")         |
|                                                                        |
|       │                                                                |
|       ▼                                                                |
|  ┌──────────────────────────────────────────┐                         |
|  │  Guard: session_factory available?        │                         |
|  │  ├─ No → "Database not available"         │                         |
|  │  └─ Yes → continue                        │                         |
|  └──────────────────────┬───────────────────┘                         |
|                         │                                              |
|                         ▼                                              |
|  ┌──────────────────────────────────────────┐                         |
|  │  AsyncAttributionRepository.find_by_id() │                         |
|  │  UUID(work_id) → AttributionRecord       │                         |
|  │  ├─ None → "No record found for ID"      │                         |
|  │  └─ Found → extract fields               │                         |
|  └──────────────────────┬───────────────────┘                         |
|                         │                                              |
|                         ▼                                              |
|  ┌──────────────────────────────────────────┐                         |
|  │  EXTRACT FIELDS                           │                         |
|  │  ■ score = record.confidence_score        │                         |
|  │  ■ sources = credits[0].sources (values)  │                         |
|  │  ■ assurance = record.assurance_level     │                         |
|  │  ■ agreement = record.source_agreement    │                         |
|  └──────────────────────┬───────────────────┘                         |
|                         │                                              |
|                         ▼                                              |
|  ┌──────────────────────────────────────────┐                         |
|  │  BUILD FACTORS LIST                       │                         |
|  │  if agreement > 0.8:                      │                         |
|  │    "High source agreement (95%)"          │                         |
|  │  elif agreement > 0.5:                    │                         |
|  │    "Moderate source agreement (67%)"      │                         |
|  │  else:                                    │                         |
|  │    "Low source agreement (30%)"           │                         |
|  │                                           │                         |
|  │  "Data from 3 source(s): MUSICBRAINZ,     │                         |
|  │   DISCOGS, ARTIST_INPUT"                  │                         |
|  │                                           │                         |
|  │  "Assurance level: LEVEL_3"               │                         |
|  └──────────────────────┬───────────────────┘                         |
|                         │                                              |
|                         ▼                                              |
|  ┌──────────────────────────────────────────┐                         |
|  │  UPDATE STATE                             │                         |
|  │  state.current_work_id = work_id          │                         |
|  │  state.confidence_score = score           │                         |
|  │  state.explanation_text = explanation      │                         |
|  └──────────────────────┬───────────────────┘                         |
|                         │                                              |
|                         ▼                                              |
|  OUTPUT                                                                |
|  ──────                                                                |
|  "Confidence score: 92%. High source agreement (95%).                  |
|   Data from 3 source(s): MUSICBRAINZ, DISCOGS, ARTIST_INPUT.          |
|   Assurance level: LEVEL_3"                                            |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "AGENT TOOL: explain_confidence" in display font |
| Input | `data_mono` | work_id string parameter |
| Session guard | `decision_point` | Check if session_factory is available |
| Repository query | `storage_layer` | AsyncAttributionRepository.find_by_id() |
| Field extraction | `processing_stage` | confidence_score, sources, assurance, agreement |
| Factors builder | `source_corroborate` | Agreement level classification + source listing |
| State update | `feedback_loop` | Updates 3 fields on AttributionAgentState |
| Output | `final_score` | Human-readable explanation string |
| Flow arrows | `data_flow` | Top-to-bottom execution path |

## Anti-Hallucination Rules

1. The tool function signature is: explain_confidence(ctx, work_id: str) -> str.
2. It uses AsyncAttributionRepository (not a raw SQL query).
3. Source agreement thresholds: >0.8 = "High", >0.5 = "Moderate", else = "Low".
4. Sources are extracted from credits[0].sources (first credit's sources).
5. The state fields updated are: current_work_id, confidence_score, explanation_text (exactly 3).
6. The UUID conversion uses Python's uuid.UUID() constructor.
7. The return value is a plain string, NOT a Pydantic model (though ExplainConfidenceResult exists, the tool returns str).
8. Two error paths: "Database not available" (no session_factory) and "No attribution record found" (no record).

## Alt Text

explain_confidence tool flow: work ID input, database lookup, field extraction, factor generation, state update, and natural language explanation output.
