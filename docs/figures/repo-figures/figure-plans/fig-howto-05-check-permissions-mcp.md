# fig-howto-05: How to Check Permissions via MCP

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-05 |
| **Title** | How to Check Permissions via MCP |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural mapping) |
| **Location** | docs/guides/mcp-permissions.md, docs/architecture/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how an AI agent queries the MCP (Model Context Protocol) server to check whether a specific use of a music work is permitted. It illustrates the consent infrastructure concept from the paper -- machine-readable permission queries that replace ambiguous license text. It answers: "How does an AI system ask 'Can I use this track for AI training?' and get a clear answer?"

The key message is: "MCP turns ambiguous licensing into a machine-readable permission check: an AI agent asks a structured question, the MCP server evaluates the rights holder's declared permissions, and returns an explicit ALLOW or DENY with provenance."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO CHECK PERMISSIONS VIA MCP                              |
|  ■ Machine-Readable Consent Infrastructure                     |
+---------------------------------------------------------------+
|                                                                |
|  I. AI AGENT ASKS                                              |
|  ────────────────                                              |
|  ┌─────────────────────────────────┐                          |
|  │ "Can I use USRC17607839 for     │                          |
|  │  AI training?"                   │                          |
|  │                                  │                          |
|  │  use_type: AI_TRAINING           │                          |
|  │  isrc: USRC17607839              │                          |
|  └────────────────┬────────────────┘                          |
|                    │                                            |
|                    v                                            |
|  II. MCP SERVER RECEIVES                                       |
|  ───────────────────────                                       |
|  ┌─────────────────────────────────┐                          |
|  │ mcp/server.py                    │                          |
|  │                                  │                          |
|  │ ■ Parse structured query         │                          |
|  │ ■ Lookup rights holder prefs     │                          |
|  │ ■ Evaluate permission rules      │                          |
|  └────────────────┬────────────────┘                          |
|                    │                                            |
|                    v                                            |
|  III. PERMISSION CHECK                                         |
|  ─────────────────────                                         |
|  ┌──────────────────┐  ┌──────────────────┐                  |
|  │ Rights Holder     │  │ Permission       │                  |
|  │ Preferences       │  │ Rules            │                  |
|  │ ──────────────   │  │ ──────────────   │                  |
|  │ AI Training: NO  │  │ if use_type ==   │                  |
|  │ Sync License: YES│  │  AI_TRAINING     │                  |
|  │ Sampling: ASK    │  │  → check prefs   │                  |
|  └────────┬─────────┘  └────────┬─────────┘                  |
|            └──────────┬──────────┘                             |
|                       v                                        |
|  IV. RESPONSE                                                  |
|  ────────────                                                  |
|  ┌─────────────────────────────────┐                          |
|  │ { "permission": "DENY",         │                          |
|  │   "reason": "Rights holder      │                          |
|  │    prohibits AI training",       │                          |
|  │   "assurance": "A2",            │                          |
|  │   "alternatives": ["SYNC"] }    │                          |
|  └─────────────────────────────────┘                          |
|                                                                |
+---------------------------------------------------------------+
|  ■ MCP replaces ambiguous license text with structured consent |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO CHECK PERMISSIONS VIA MCP" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Machine-Readable Consent Infrastructure" in Plus Jakarta Sans caps |
| Step I: Agent query | `stakeholder_platform` | AI agent formulating a structured permission query with use_type and ISRC |
| Step II: MCP server | `security_layer` | Server receiving query and processing through three sub-steps |
| Step III: Permission check (left) | `security_layer` | Rights holder preference table showing per-use-type permissions |
| Step III: Permission rules (right) | `processing_stage` | Rule evaluation logic matching use_type against preferences |
| Step IV: Response | `data_mono` | JSON response with DENY result, reason, assurance level, and alternatives |
| Flow arrows (I to IV) | `data_flow` | Downward arrows showing query-response lifecycle |
| Roman numerals I-IV | `section_numeral` | Step headers in editorial style |
| DENY badge | `confidence_low` | Red-tier indicator for denied permission |
| Assurance "A2" | `assurance_a2` | Blue corroborated level in response |
| Footer callout | `callout_box` | "MCP replaces ambiguous license text with structured consent" |

## Anti-Hallucination Rules

1. MCP stands for Model Context Protocol -- do not expand it differently.
2. The permission response uses ALLOW/DENY (binary) plus a reason string -- not a numeric score.
3. Use types shown (AI_TRAINING, SYNC, SAMPLING) are illustrative -- the actual enum may differ.
4. Assurance level A2 means the permission data is "Corroborated" by multiple sources -- not that the artist personally verified (that would be A3).
5. The MCP server lives at `mcp/server.py` -- not in the API routes directory.
6. This is consent INFRASTRUCTURE -- it does not enforce DRM or technical protection. It provides machine-readable queries.
7. The ISRC "USRC17607839" is an illustrative example, not a real track identifier.
8. The "alternatives" field in the response is a scaffold concept -- it may not exist in all implementations.
9. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Workflow diagram: four-step MCP permission check for music attribution consent infrastructure, showing how an AI agent queries training rights for a music work, the MCP server evaluates rights holder preferences, and returns a structured ALLOW or DENY response with assurance level -- replacing ambiguous license text with machine-readable, transparent confidence-backed consent.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Workflow diagram: four-step MCP permission check for music attribution consent infrastructure, showing how an AI agent queries training rights for a music work, the MCP server evaluates rights holder preferences, and returns a structured ALLOW or DENY response with assurance level -- replacing ambiguous license text with machine-readable, transparent confidence-backed consent.](docs/figures/repo-figures/assets/fig-howto-05-check-permissions-mcp.jpg)

*MCP consent infrastructure workflow for the Music Attribution Scaffold. An AI agent submits a structured permission query, the MCP server evaluates it against declared rights holder preferences, and returns an explicit decision with provenance -- embodying the paper's principle that consent must be machine-readable, not buried in license text (Teikari, 2026).*

### From this figure plan (relative)

![Workflow diagram: four-step MCP permission check for music attribution consent infrastructure, showing how an AI agent queries training rights for a music work, the MCP server evaluates rights holder preferences, and returns a structured ALLOW or DENY response with assurance level -- replacing ambiguous license text with machine-readable, transparent confidence-backed consent.](../assets/fig-howto-05-check-permissions-mcp.jpg)
