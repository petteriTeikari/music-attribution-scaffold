# fig-agent-06: Agent Tool: search_attributions

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-06 |
| **Title** | Agent Tool: search_attributions -- Hybrid Search Across Attribution Records |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/agent.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure traces the search_attributions tool's execution path: input (query string) -> HybridSearchService.search() with limit=10 -> format results (title, artist, confidence, assurance per hit) -> update state (last_search_query, last_search_count) -> return formatted results string. The hybrid search service (text + vector) is noted as an implementation detail.

The key message is: "search_attributions uses the HybridSearchService to find up to 10 matching attribution records, returning a formatted summary of each hit's title, artist, confidence score, and assurance level."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  AGENT TOOL: search_attributions                                       |
|  ■ Hybrid Search Query                                                 |
+-----------------------------------------------------------------------+
|                                                                        |
|  INPUT                                                                 |
|  ─────                                                                 |
|  query: str  (e.g., "Imogen Heap producer credits")                    |
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
|  │  HybridSearchService.search()             │                         |
|  │  ■ query: user input string               │                         |
|  │  ■ session: async PostgreSQL session       │                         |
|  │  ■ limit: 10                               │                         |
|  │  ■ Returns: list[SearchHit]                │                         |
|  │    (text + vector hybrid matching)         │                         |
|  └──────────────────────┬───────────────────┘                         |
|                         │                                              |
|                         ▼                                              |
|  ┌──────────────────────────────────────────┐                         |
|  │  FORMAT RESULTS                           │                         |
|  │  For each hit:                            │                         |
|  │  "- {work_title} by {artist_name}         │                         |
|  │     (confidence: {score}%,                │                         |
|  │      assurance: {level})"                 │                         |
|  └──────────────────────┬───────────────────┘                         |
|                         │                                              |
|                         ▼                                              |
|  ┌──────────────────────────────────────────┐                         |
|  │  UPDATE STATE                             │                         |
|  │  state.last_search_query = query          │                         |
|  │  state.last_search_count = len(results)   │                         |
|  └──────────────────────┬───────────────────┘                         |
|                         │                                              |
|                         ▼                                              |
|  OUTPUT                                                                |
|  ──────                                                                |
|  "Found 3 result(s):                                                   |
|   - Hide and Seek by Imogen Heap (confidence: 92%, assurance: LEVEL_3) |
|   - Ellipse by Imogen Heap (confidence: 78%, assurance: LEVEL_2)       |
|   - Goodnight and Go by Imogen Heap (confidence: 34%, assurance: ..."  |
|                                                                        |
|  OR: "No attributions found for '{query}'."                            |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "AGENT TOOL: search_attributions" in display font |
| Input | `data_mono` | query string parameter |
| Session guard | `decision_point` | Check if session_factory is available |
| HybridSearchService | `etl_extract` | Text + vector hybrid search with limit=10 |
| Result formatting | `processing_stage` | Per-hit format: title, artist, confidence, assurance |
| State update | `feedback_loop` | Updates last_search_query and last_search_count |
| Output examples | `data_mono` | Formatted results string or empty message |
| Flow arrows | `data_flow` | Top-to-bottom execution path |

## Anti-Hallucination Rules

1. The tool function signature is: search_attributions(ctx, query: str) -> str.
2. It uses HybridSearchService (from music_attribution.search.hybrid_search), NOT raw SQL.
3. The search limit is 10 (hardcoded in the tool).
4. Each result is formatted as: "- {work_title} by {artist_name} (confidence: {score:.0%}, assurance: {level.value})".
5. The state fields updated are: last_search_query and last_search_count (exactly 2).
6. Empty results return: "No attributions found for '{query}'."
7. Non-empty results start with: "Found {N} result(s):" followed by bulleted list.
8. The search_attributions tool accesses hit.record to get the AttributionRecord.

## Alt Text

search_attributions tool flow: query string input, HybridSearchService database search, result formatting with confidence and assurance, and state update.
