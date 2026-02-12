# fig-topic-10: MCP Permission Infrastructure

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-10 |
| **Title** | MCP Permissions — Machine-Readable Consent for the AI Era |
| **Audience** | General + Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card X (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Current music consent infrastructure (DDEX, CWR) has no fields for AI training permissions. Model Context Protocol (MCP) fills this gap by enabling machine-readable permission queries between AI agents and artist-controlled servers. This figure shows a concrete consent flow for "Hide and Seek," maps permissions to assurance levels (you can't query what you can't identify), and introduces Morreale et al.'s nuanced consent matrix (not just allow/deny — purpose-based, with pricing). Communicates: "an AI agent asks 'can I train on this track?' and gets a machine-readable answer in milliseconds — but the answer quality depends on the assurance level of the metadata."

Key concepts:
- **MCP**: JSON-RPC 2.0 protocol, Tools + Resources primitives, capability negotiation
- **Permission Patchbay**: Artist-owned server with per-use-type consent policies
- **Nuanced consent** (Morreale et al.): Not binary — purpose-based (training vs. inference vs. voice), with pricing tiers
- **A0–A3 gate**: Higher assurance enables finer-grained permissions
- **Gap**: DDEX/CWR carry ISRC, ISWC, splits — but zero AI training fields

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  THE CONSENT FLOW                                           │
│  ───────────────                                            │
│                                                              │
│  AI AGENT                MCP SERVER               ARTIST    │
│  (wants to train)        (Permission Patchbay)    POLICY    │
│                                                              │
│  ① DISCOVER                                                 │
│  Agent finds MCP server via ISRC registry                   │
│                                                              │
│  ② QUERY  ──────────────────────────────►                   │
│  {                                                          │
│    "tool": "check_permission",                              │
│    "isrc": "GBUM70500123",                                  │
│    "purpose": "model_training",                             │
│    "commercial": true                                       │
│  }                                                          │
│                                                              │
│  ③ EVALUATE  (server checks artist policy)                  │
│                                                              │
│  ④ RESPOND  ◄──────────────────────────                     │
│  {                                                          │
│    "training": DENIED,                                      │
│    "inference_conditioning": ALLOWED,                       │
│    "rate": "$0.003/generation",                             │
│    "voice_cloning": DENIED,                                 │
│    "assurance": "A2"                                        │
│  }                                                          │
│                                                              │
│  NUANCED CONSENT MATRIX (not binary)                        │
│  ────────────────────────────────────                       │
│  (after Morreale et al. 2025)                               │
│                                                              │
│  Use Type        "Hide & Seek"  "Headlock"  "Goodnight"    │
│  ─────────────────────────────────────────────────────      │
│  STREAMING         ■ allow       ■ allow     ■ allow       │
│  MODEL TRAINING    ■ deny        ■ deny      ◧ ask         │
│  INFERENCE COND.   ◧ $0.003      ◧ $0.005    ■ deny        │
│  VOICE CLONING     ■ deny        ■ deny      ■ deny        │
│  REMIX/SAMPLE      ◧ license     ◧ license   ■ deny        │
│                                                              │
│  ■ Allow  ■ Deny  ◧ Conditional (with terms)               │
│                                                              │
│  THE ASSURANCE GATE                                         │
│  ─────────────────                                          │
│  What you can query depends on what you can identify:       │
│                                                              │
│  A0: No identifiers → no machine-readable permissions       │
│  A1: ISRC only      → recording-level opt-in/out            │
│  A2: ISRC + ISWC    → composition-level rights              │
│  A3: + ISNI         → full provenance: voice, style, split  │
│                                                              │
│  THE GAP TODAY                                              │
│  ────────────                                               │
│  DDEX/CWR carry: ISRC, ISWC, writer splits, territories    │
│  DDEX/CWR lack:  AI training consent, voice cloning rights, │
│                  inference conditioning terms, pricing       │
│                                                              │
│  ── MCP PROTOCOL LAYER ──                                   │
│  JSON-RPC 2.0 │ OAuth 2.0 + PKCE │ Audit Logging           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Consent flow diagram | `line_flow` | Four-step horizontal flow: DISCOVER → QUERY → EVALUATE → RESPOND |
| JSON query/response | `typography_mono` | Monospace MCP request and response with real ISRC |
| AI agent | `data_primary` | Teal icon/label on left |
| MCP server | `data_accent` | Coral "Permission Patchbay" in center |
| Artist policy | `data_primary` | Teal policy store on right |
| Consent matrix | `region_secondary` | Grid: rows = use types, columns = tracks, cells = allow/deny/conditional |
| Allow cells | `status_allow` | Teal filled squares |
| Deny cells | `status_deny` | Coral filled squares |
| Conditional cells | `status_ask` | Amber half-filled with terms |
| Assurance gate | `data_gradient` | Four rows (A0→A3) showing increasing permission granularity |
| Gap callout | `data_warning` | Orange highlight: what DDEX/CWR carry vs. what they lack |
| Protocol layer | `region_secondary` | Bottom bar: JSON-RPC 2.0 + OAuth + Audit |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "THE CONSENT FLOW", "AI AGENT", "MCP SERVER", "PERMISSION PATCHBAY", "ARTIST POLICY", step numbers ①②③④, JSON-like query/response content, "NUANCED CONSENT MATRIX", use type names, track names, "Allow", "Deny", "Conditional", pricing, "THE ASSURANCE GATE", A0–A3 descriptions, "THE GAP TODAY", DDEX/CWR comparison, "MCP PROTOCOL LAYER", "JSON-RPC 2.0", "OAuth 2.0 + PKCE", "Audit Logging".

## Alt Text

MCP permission infrastructure infographic showing a four-step consent flow: an AI agent discovers an artist's MCP server via ISRC registry, sends a permission query for track GBUM70500123 (purpose: model training, commercial use), the server evaluates against the artist's policy, and responds with nuanced permissions — training denied, inference conditioning allowed at $0.003/generation, voice cloning denied. Below, a consent matrix (after Morreale et al. 2025) shows per-track, per-use-type permissions for three Imogen Heap tracks across five use types (streaming, model training, inference conditioning, voice cloning, remix). Cells are allow (teal), deny (coral), or conditional with terms (amber). The assurance gate shows that permission granularity depends on identification quality: A0 has no machine-readable permissions, A1 enables recording-level opt-in/out via ISRC, A2 adds composition-level rights via ISWC, A3 enables full provenance including voice and style rights via ISNI. A gap callout highlights that DDEX and CWR currently lack AI training consent fields. The MCP protocol layer runs on JSON-RPC 2.0 with OAuth 2.0 + PKCE and audit logging.
