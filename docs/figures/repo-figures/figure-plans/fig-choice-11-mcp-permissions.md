# fig-choice-11: Why MCP for Permissions?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-11 |
| **Title** | Why MCP for Permissions? |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural overview) |
| **Location** | docs/planning/, docs/prd/decisions/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains why MCP (Model Context Protocol) was selected as the primary API protocol for machine-readable AI training consent. This is a core thesis of the companion paper: attribution infrastructure needs machine-readable permission queries so AI platforms can programmatically check training rights. Compares against custom REST API and blockchain-based approaches.

The key message is: "MCP provides standardized, machine-readable permission queries for AI training consent -- enabling 'attribution-by-design' where AI platforms check rights before training, not after."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY MCP FOR PERMISSIONS?                                      |
|  ■ Machine-Readable AI Training Consent                        |
+---------------------------------------------------------------+
|                                                                |
|  THE PROBLEM                                                   |
|  AI platforms need to check: "Can I use this track for         |
|  training?" Currently: no standardized way to ask.             |
|                                                                |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │  MCP PERMISSION QUERY FLOW                              │   |
|  │                                                         │   |
|  │  AI Platform ──── MCP Query ────> Attribution Scaffold  │   |
|  │    "Can I train     │              Checks:              │   |
|  │     on ISRC         │              - Rights holder      │   |
|  │     X12345?"        │              - License terms       │   |
|  │                     │              - Territorial scope   │   |
|  │  AI Platform <── MCP Response ─── Returns:              │   |
|  │    { allowed: true,                - Permission status  │   |
|  │      conditions: [...],            - Conditions          │   |
|  │      confidence: 0.87 }            - Confidence score   │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ MCP          │ │ CUSTOM REST  │ │ BLOCKCHAIN   │          |
|  │ ■ SELECTED   │ │ API          │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Standardized │ │ Per-provider │ │ Immutable    │          |
|  │ protocol     │ │ contracts    │ │ ledger       │          |
|  │              │ │              │ │              │          |
|  │ Machine-     │ │ Human-       │ │ Slow, energy-│          |
|  │ readable     │ │ readable docs│ │ intensive    │          |
|  │              │ │              │ │              │          |
|  │ Ecosystem    │ │ No ecosystem │ │ Oracle       │          |
|  │ growing      │ │ integration  │ │ Problem      │          |
|  │ (Anthropic)  │ │              │ │              │          |
|  │              │ │              │ │              │          |
|  │ Agent-native │ │ Requires     │ │ Not agent-   │          |
|  │              │ │ custom code  │ │ friendly     │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  Paper concept: MCP as consent infrastructure                  |
|  (Teikari 2026, SSRN 6109087)                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY MCP FOR PERMISSIONS?" with coral accent square |
| Problem statement | `problem_statement` | No standardized way for AI platforms to check training rights |
| MCP query flow diagram | `api_endpoint` | Request/response flow showing permission check |
| MCP card | `selected_option` | Standardized, machine-readable, ecosystem growing, agent-native |
| Custom REST card | `deferred_option` | Per-provider contracts, no ecosystem |
| Blockchain card | `deferred_option` | Immutable but slow, Oracle Problem |
| Paper reference footer | `citation_bar` | SSRN 6109087 reference |

## Anti-Hallucination Rules

1. MCP is Model Context Protocol -- originally developed by Anthropic for LLM tool-calling.
2. The scaffold extends MCP for permission queries -- this is the "consent infrastructure" concept from the paper.
3. The API protocol decision selected `mcp_primary` -- per the network and scenario paths.
4. The permission response includes confidence score -- this ties to the A0-A3 assurance levels.
5. ISRC (International Standard Recording Code) is the track identifier used in queries.
6. The "Oracle Problem" (mentioned in blockchain cons) is a key concept from the paper: digital systems cannot fully verify physical/training reality.
7. Do NOT claim MCP is a permission-specific protocol -- it is a general LLM tool protocol that the scaffold extends for permissions.
8. The scaffold's permission routes are at `/api/v1/permissions`.
9. This is L2 audience -- use "consent infrastructure" and "training rights" language, not code.
10. Background must be warm cream (#f6f3e6).

## Alt Text

Decision diagram: MCP as consent infrastructure for music attribution, showing machine-readable AI training permission queries with transparent confidence responses, compared against custom REST API and blockchain approaches for the open-source attribution scaffold enabling attribution-by-design.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Decision diagram: MCP as consent infrastructure for music attribution, showing machine-readable AI training permission queries with transparent confidence responses, compared against custom REST API and blockchain approaches for the open-source attribution scaffold enabling attribution-by-design.](docs/figures/repo-figures/assets/fig-choice-11-mcp-permissions.jpg)

*Model Context Protocol (MCP) enables standardized, machine-readable permission queries for AI training consent in the music attribution scaffold, allowing AI platforms to programmatically check training rights with confidence-scored responses before use, not after (Teikari 2026, SSRN 6109087).*

### From this figure plan (relative)

![Decision diagram: MCP as consent infrastructure for music attribution, showing machine-readable AI training permission queries with transparent confidence responses, compared against custom REST API and blockchain approaches for the open-source attribution scaffold enabling attribution-by-design.](../assets/fig-choice-11-mcp-permissions.jpg)
