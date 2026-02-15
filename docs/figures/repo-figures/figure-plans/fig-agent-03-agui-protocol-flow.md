# fig-agent-03: AG-UI Protocol Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-03 |
| **Title** | AG-UI Protocol Flow: SSE Event Sequence from Connection to Completion |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/agent.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the SSE event sequence of the AG-UI protocol as implemented in the agui_endpoint.py adapter. It traces the timeline: CopilotKit sends POST with messages -> server emits RunStarted -> TextMessageStart -> N chunks of TextMessageContent -> TextMessageEnd -> StateSnapshot -> RunFinished. The chunking mechanism (50 chars) and the state snapshot (AttributionAgentState serialized) are detailed.

The key message is: "The AG-UI protocol streams 6 SSE event types in a fixed sequence -- the agent's response is chunked at 50 characters for a streaming feel, and a StateSnapshot is emitted before RunFinished so CopilotKit can update shared state."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  AG-UI PROTOCOL FLOW                                                   |
|  ■ SSE Event Sequence                                                  |
+-----------------------------------------------------------------------+
|                                                                        |
|  CLIENT (CopilotKit)                    SERVER (FastAPI)               |
|  ───────────────────                    ────────────────               |
|                                                                        |
|  POST /api/v1/copilotkit                                               |
|  { "messages": [                                                       |
|      { "role": "user",                                                 |
|        "content": "Explain                                             |
|         confidence for                                                 |
|         Hide and Seek" }                                               |
|  ] }                                                                   |
|       ══════════════════════════>                                      |
|                                          Extract last user message     |
|                                          Create AgentDeps              |
|                                          Run PydanticAI agent          |
|                                                                        |
|       <──── data: {"type":"RunStarted","runId":"uuid-1"}               |
|                                                                        |
|       <──── data: {"type":"TextMessageStart",                          |
|                     "messageId":"uuid-2","role":"assistant"}            |
|                                                                        |
|       <──── data: {"type":"TextMessageContent",                        |
|                     "content":"Confidence score: 92%. High so"}         |
|             (chunk 1 of N, 50 chars max)                               |
|                                                                        |
|       <──── data: {"type":"TextMessageContent",                        |
|                     "content":"urce agreement (95%). Data fro"}         |
|             (chunk 2 of N)                                             |
|                                                                        |
|       <──── ...more chunks...                                          |
|                                                                        |
|       <──── data: {"type":"TextMessageEnd"}                            |
|                                                                        |
|       <──── data: {"type":"StateSnapshot",                             |
|                     "snapshot": {                                       |
|                       "current_work_id": "uuid-3",                     |
|                       "confidence_score": 0.92,                        |
|                       "explanation_text": "...",                        |
|                       ...                                              |
|                     }}                                                  |
|                                                                        |
|       <──── data: {"type":"RunFinished","runId":"uuid-1"}              |
|                                                                        |
|  CONNECTION CLOSED                                                     |
|                                                                        |
|  RESPONSE HEADERS                                                      |
|  ────────────────                                                      |
|  Content-Type: text/event-stream                                       |
|  Cache-Control: no-cache                                               |
|  Connection: keep-alive                                                |
|  X-Accel-Buffering: no                                                 |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "AG-UI PROTOCOL FLOW" in display font |
| Client column | `api_endpoint` | CopilotKit sending POST request |
| Server column | `processing_stage` | FastAPI processing and agent execution |
| POST request | `data_flow` | Messages array with user content |
| RunStarted event | `data_mono` | First event with runId |
| TextMessageStart event | `data_mono` | messageId and role |
| TextMessageContent events | `data_mono` | Chunked content (50 char max) |
| TextMessageEnd event | `data_mono` | End marker |
| StateSnapshot event | `data_mono` | Serialized AttributionAgentState |
| RunFinished event | `data_mono` | Final event with runId |
| Response headers | `data_mono` | SSE headers |

## Anti-Hallucination Rules

1. The protocol is AG-UI via SSE (Server-Sent Events), NOT WebSockets or polling.
2. The endpoint is POST /api/v1/copilotkit (a POST, not GET -- SSE response to a POST request).
3. There are exactly 6 event types in this implementation: RunStarted, TextMessageStart, TextMessageContent, TextMessageEnd, StateSnapshot, RunFinished.
4. Content is chunked at 50 characters (chunk_size = 50 in the code).
5. The full AG-UI protocol has 31 event types -- this is a "simplified AG-UI adapter" per the code comments.
6. StateSnapshot contains the full AttributionAgentState serialized via model_dump(mode="json").
7. Response headers include X-Accel-Buffering: no (for nginx compatibility).
8. The agent runs the full query synchronously (await agent.run), then chunks the result -- it does NOT stream token-by-token from the LLM.
9. Each SSE event is formatted as: `data: {json}\n\n` via the _sse_event() helper.

## Alt Text

Sequence diagram: AG-UI protocol flow for music attribution agentic UI showing the complete Server-Sent Events lifecycle from CopilotKit POST request through six SSE event types including chunked text streaming of confidence scoring explanations and a StateSnapshot that synchronizes music metadata state between the PydanticAI backend and the frontend sidebar.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Sequence diagram: AG-UI protocol flow for music attribution agentic UI showing the complete Server-Sent Events lifecycle from CopilotKit POST request through six SSE event types including chunked text streaming of confidence scoring explanations and a StateSnapshot that synchronizes music metadata state between the PydanticAI backend and the frontend sidebar.](docs/figures/repo-figures/assets/fig-agent-03-agui-protocol-flow.jpg)

*AG-UI SSE event sequence as implemented in the open-source attribution scaffold, showing the fixed order of RunStarted, TextMessageStart, chunked TextMessageContent (50-character segments), TextMessageEnd, StateSnapshot, and RunFinished events streamed from FastAPI to CopilotKit.*

### From this figure plan (relative)

![Sequence diagram: AG-UI protocol flow for music attribution agentic UI showing the complete Server-Sent Events lifecycle from CopilotKit POST request through six SSE event types including chunked text streaming of confidence scoring explanations and a StateSnapshot that synchronizes music metadata state between the PydanticAI backend and the frontend sidebar.](../assets/fig-agent-03-agui-protocol-flow.jpg)
