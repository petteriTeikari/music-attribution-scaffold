# fig-theory-20: MCP Permission Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-20 |
| **Title** | MCP Permission Flow |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (code terms, API references, protocol flow) |
| **Location** | docs/theory/mcp-consent.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 675px (16:9) |

## Purpose & Key Message

This figure shows the technical flow of an MCP permission query: from the AI agent making a request, through the MCP server, to the permission lookup and response. It answers: "What is the actual protocol flow when an AI system checks whether it can use a piece of music?"

The key message is: "An AI agent sends a structured MCP query specifying the work and intended use -- the MCP server looks up the artist's permissions and returns ALLOW, DENY, or CONDITIONS with machine-readable terms."

## Visual Concept (ASCII Layout)

```
+-------------------------------------------------------------------------------+
|  MCP PERMISSION FLOW                                                           |
|  ■ Query → Lookup → Response                                                  |
+-------------------------------------------------------------------------------+
|                                                                                |
|  ┌──────────┐         ┌──────────────┐         ┌──────────────┐               |
|  │ AI Agent │         │  MCP Server  │         │  Permission  │               |
|  │          │         │              │         │  Store       │               |
|  │(Claude,  │         │  music_      │         │              │               |
|  │ GPT,     │         │  attribution/│         │  (PostgreSQL │               |
|  │ custom)  │         │  permissions │         │   + cache)   │               |
|  └────┬─────┘         └──────┬───────┘         └──────┬───────┘               |
|       │                      │                        │                        |
|       │  1. MCP Query        │                        │                        |
|       │  ────────────        │                        │                        |
|       │  tool: check_        │                        │                        |
|       │    permission        │                        │                        |
|       │  work_id: ISRC-XX    │                        │                        |
|       │  use_type: "ai_      │                        │                        |
|       │    training"         │                        │                        |
|       │─────────────────────►│                        │                        |
|       │                      │  2. Lookup              │                        |
|       │                      │  ──────                 │                        |
|       │                      │  SELECT permission      │                        |
|       │                      │  WHERE work_id AND      │                        |
|       │                      │  use_type               │                        |
|       │                      │───────────────────────►│                        |
|       │                      │                        │                        |
|       │                      │  3. Result              │                        |
|       │                      │◄───────────────────────│                        |
|       │                      │                        │                        |
|       │  4. MCP Response     │                        │                        |
|       │  ───────────────     │                        │                        |
|       │  status: "DENY"      │                        │                        |
|       │  reason: "Artist     │                        │                        |
|       │    has opted out     │                        │                        |
|       │    of AI training"   │                        │                        |
|       │  alternatives: [     │                        │                        |
|       │    "streaming",      │                        │                        |
|       │    "sync_license"]   │                        │                        |
|       │◄─────────────────────│                        │                        |
|       │                      │                        │                        |
+-------┴──────────────────────┴────────────────────────┴───────────────────────+
|                                                                                |
|  USE CASE EXAMPLES                                                             |
|  ─────────────────                                                             |
|                                                                                |
|  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      |
|  │  Streaming   │  │  Sync        │  │  AI Training │  │  Voice       │      |
|  │  ──────────  │  │  License     │  │  ──────────  │  │  Cloning     │      |
|  │  ALLOW       │  │  ──────      │  │  DENY        │  │  ──────      │      |
|  │  (default)   │  │  CONDITIONS  │  │  (opted out) │  │  DENY        │      |
|  │              │  │  (fee + attr)│  │              │  │  (never)     │      |
|  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘      |
|                                                                                |
+-------------------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "MCP PERMISSION FLOW" with coral accent square |
| Subtitle | `label_editorial` | "Query -> Lookup -> Response" |
| AI Agent column | `stakeholder_platform` | Generic AI agent (Claude, GPT, custom) |
| MCP Server column | `api_endpoint` | music_attribution/permissions endpoint |
| Permission Store column | `storage_layer` | PostgreSQL + cache for permission data |
| Step 1: MCP Query | `data_flow` | Structured query: tool name, work_id (ISRC), use_type |
| Step 2: Lookup | `data_flow` | SQL-style lookup: WHERE work_id AND use_type |
| Step 3: Result | `data_flow` | Internal result from store to server |
| Step 4: MCP Response | `data_flow` | Structured response: status, reason, alternatives |
| Query parameters | `data_mono` | tool, work_id, use_type in monospace |
| Response fields | `data_mono` | status, reason, alternatives in monospace |
| Use case: Streaming | `confidence_high` | ALLOW (default) |
| Use case: Sync License | `confidence_medium` | CONDITIONS (fee + attribution) |
| Use case: AI Training | `confidence_low` | DENY (opted out) |
| Use case: Voice Cloning | `confidence_low` | DENY (never) |

## Anti-Hallucination Rules

1. MCP = Model Context Protocol. The tool name is `check_permission` -- do NOT use other tool names.
2. The four steps are: Query, Lookup, Result, Response. Do NOT add authentication or rate limiting steps.
3. Response statuses are: ALLOW, DENY, CONDITIONS. Do NOT add PENDING or UNKNOWN.
4. The response includes "alternatives" when denying -- this is a key design feature.
5. "AI Training" and "Voice Cloning" are both DENY but for different reasons -- do NOT merge them.
6. The Permission Store is PostgreSQL -- do NOT substitute Redis, MongoDB, etc.
7. AI Agent examples (Claude, GPT, custom) are GENERIC -- do NOT favor any specific vendor.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Sequence diagram: MCP permission flow for music attribution showing an AI agent sending a structured check_permission query with ISRC work identifier and use type, the MCP server looking up permissions in PostgreSQL, and returning a DENY response with machine-readable reason and alternative allowed uses -- demonstrating how the open-source attribution scaffold enables transparent confidence in AI training consent for music metadata.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Sequence diagram: MCP permission flow for music attribution showing an AI agent sending a structured check_permission query with ISRC work identifier and use type, the MCP server looking up permissions in PostgreSQL, and returning a DENY response with machine-readable reason and alternative allowed uses -- demonstrating how the open-source attribution scaffold enables transparent confidence in AI training consent for music metadata.](docs/figures/repo-figures/assets/fig-theory-20-mcp-permission-flow.jpg)

*Figure 20. The MCP permission flow: an AI agent sends a structured query specifying work ID and intended use, the MCP server looks up the artist's permissions in PostgreSQL, and returns ALLOW, DENY, or CONDITIONS with machine-readable terms and suggested alternatives when denying.*

### From this figure plan (relative)

![Sequence diagram: MCP permission flow for music attribution showing an AI agent sending a structured check_permission query with ISRC work identifier and use type, the MCP server looking up permissions in PostgreSQL, and returning a DENY response with machine-readable reason and alternative allowed uses -- demonstrating how the open-source attribution scaffold enables transparent confidence in AI training consent for music metadata.](../assets/fig-theory-20-mcp-permission-flow.jpg)
