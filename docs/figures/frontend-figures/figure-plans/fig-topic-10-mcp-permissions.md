# fig-topic-10: MCP Permission Infrastructure

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-10 |
| **Title** | MCP Permission Infrastructure — Consent Matrix & Auth Stack |
| **Audience** | Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card X (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Permission matrix grid combined with an authentication stack diagram. Communicates: "granular, per-use-type consent backed by real security infrastructure."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ■ □ ◧ ■    STREAM                  │
│  □ □ ■ □    AI TRAINING             │
│  □ □ □ □    VOICE CLONING           │
│  ■ ◧ ■ ■    REMIX                   │
│                                      │
│  ■ Allow  □ Deny  ◧ Ask             │
│                                      │
│  ── MCP PROTOCOL LAYER ──           │
│                                      │
│  ┌─────────────────┐                │
│  │ OAuth 2.0 + PKCE │                │
│  │ Authorization    │                │
│  │ Audit Logging    │                │
│  └─────────────────┘                │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Allow cells | `status_allow` | Teal filled squares |
| Deny cells | `status_deny` | Coral filled squares |
| Ask cells | `status_ask` | Amber filled squares |
| Usage type labels | `label_editorial` | ALL-CAPS row labels |
| MCP layer | `line_accent` | Coral horizontal divider |
| Auth stack | `region_secondary` | Navy rectangle with stack items |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "MCP PERMISSIONS", "STREAM", "AI TRAINING", "VOICE CLONING", "REMIX", "Allow", "Deny", "Ask", "MCP PROTOCOL", "OAUTH 2.0", "AUTHORIZATION", "AUDIT LOG".

## Alt Text

Permission matrix grid showing usage types (stream, AI training, voice cloning, remix) as rows with colored squares indicating allow (teal), deny (coral), and ask (amber) consent states. Below, the MCP protocol layer connects to an authentication stack showing OAuth 2.0, authorization, and audit logging.
