# fig-scenario-02: Four Archetype Scenario Comparison

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-scenario-02 |
| **Title** | Four Archetype Scenario Comparison |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/prd/decisions/REPORT.md, docs/prd/archetypes/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows how the four team archetypes activate dramatically different subsets of the 78-node network. Ecosystem nodes (v3.0.0 additions) are archetype-sensitive but lack formal conditional probability tables yet, making this a key area for future work. This answers: "How does team composition reshape the scaffold's architecture?"

## Key Message

Four team archetypes activate dramatically different subsets of the 78-node network -- Engineer-Heavy activates 40+ nodes including edge inference, while Musician-First activates approximately 25 with managed-service preferences.

## Visual Concept

Four mini-network diagrams arranged in a 2x2 grid, each showing the same 78-node topology but with different subsets highlighted. Each panel uses Roman numeral headings. Active nodes are solid, inactive are muted outlines. Ecosystem nodes are specifically called out with a distinctive treatment to show archetype sensitivity. Each panel includes a compact stats bar: team size, tech depth, budget, and approximate active node count.

```
+-----------------------------------------------------------------------+
|  FOUR ARCHETYPE SCENARIO COMPARISON                                    |
|  ■ Same Network, Four Activation Patterns                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. ENGINEER-HEAVY                  II. MUSICIAN-FIRST                 |
|  ──────────────────                 ──────────────────                  |
|  Team: 5-15 | Deep | Moderate      Team: 1-3 | Shallow | Low          |
|  ┌────────────────────────┐        ┌────────────────────────┐          |
|  │  ◉◉◉◉  L1              │        │  ◉◉◉◉  L1              │          |
|  │  ◉◉◉◉◉◉◉  L2           │        │  ◉◉◉◉◉ ○○  L2          │          |
|  │  ◉◉◉◉◉◉◉◉◉◉◉◉  L3     │        │  ◉◉◉◉◉◉ ○○○○○○  L3    │          |
|  │  ◉◉◉◉◉◉  L4            │        │  ◉◉◉ ○○○  L4           │          |
|  │  ◉◉◉◉◉  L5             │        │  ◉◉ ○○○  L5            │          |
|  │  ~40+ nodes active      │        │  ~25 nodes active       │          |
|  │  Custom, edge inference │        │  Managed, Supabase      │          |
|  └────────────────────────┘        └────────────────────────┘          |
|                                                                        |
|  III. SOLO HACKER                   IV. WELL-FUNDED STARTUP            |
|  ──────────────────                 ──────────────────────              |
|  Team: 1 | Variable | Minimal      Team: 10-30+ | Deep | High         |
|  ┌────────────────────────┐        ┌────────────────────────┐          |
|  │  ◉◉◉◉  L1              │        │  ◉◉◉◉  L1              │          |
|  │  ◉◉◉ ○○○○  L2          │        │  ◉◉◉◉◉◉◉◉◉  L2        │          |
|  │  ◉◉◉◉ ○○○○○○○○  L3    │        │  ◉◉◉◉◉◉◉◉◉◉◉◉◉◉  L3  │          |
|  │  ◉◉ ○○○  L4            │        │  ◉◉◉◉◉◉◉  L4           │          |
|  │  ◉ ○○○○  L5            │        │  ◉◉◉◉◉◉◉  L5           │          |
|  │  ~18 nodes active       │        │  ~50+ nodes active      │          |
|  │  SQLite path, minimal   │        │  Full ecosystem, AWS    │          |
|  └────────────────────────┘        └────────────────────────┘          |
|                                                                        |
+-----------------------------------------------------------------------+
|  ■ Ecosystem nodes (28) lack formal archetype weights -- future work   |
+-----------------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "FOUR ARCHETYPE SCENARIO COMPARISON"
    role: title

  - id: panel_engineer
    bounds: [60, 140, 880, 380]
    content: "I. ENGINEER-HEAVY"
    role: archetype_overlay

  - id: panel_musician
    bounds: [980, 140, 880, 380]
    content: "II. MUSICIAN-FIRST"
    role: archetype_overlay

  - id: panel_solo
    bounds: [60, 540, 880, 380]
    content: "III. SOLO HACKER"
    role: archetype_overlay

  - id: panel_funded
    bounds: [980, 540, 880, 380]
    content: "IV. WELL-FUNDED STARTUP"
    role: archetype_overlay

  - id: footer_callout
    bounds: [60, 940, 1800, 80]
    role: callout_bar

anchors:
  - id: engineer_network
    position: [100, 200]
    size: [800, 280]
    role: decision_point

  - id: musician_network
    position: [1020, 200]
    size: [800, 280]
    role: decision_point

  - id: solo_network
    position: [100, 600]
    size: [800, 280]
    role: decision_point

  - id: funded_network
    position: [1020, 600]
    size: [800, 280]
    role: decision_point
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Engineer-Heavy panel | `archetype_overlay` | Mini-network with ~40+ active nodes, custom-code preferences |
| Musician-First panel | `archetype_overlay` | Mini-network with ~25 active nodes, managed-service preferences |
| Solo Hacker panel | `archetype_overlay` | Mini-network with ~18 active nodes, minimal path |
| Well-Funded panel | `archetype_overlay` | Mini-network with ~50+ active nodes, full ecosystem |
| Active nodes per panel | `selected_option` | Solid nodes within each mini-network |
| Inactive nodes per panel | `deferred_option` | Muted/dashed nodes within each mini-network |
| Stats bar per panel | `data_mono` | Team size, tech depth, budget, active node count |
| Footer callout | `callout_bar` | Note about ecosystem nodes lacking archetype weights |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Engineer-Heavy active set | Edge inference, custom DB | arrow | "custom infrastructure" |
| Musician-First active set | Supabase, Render | arrow | "managed services" |
| Solo Hacker active set | SQLite, Railway | arrow | "minimal dependencies" |
| Well-Funded active set | Full ecosystem nodes | arrow | "enterprise coverage" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ECOSYSTEM SENSITIVITY" | 28 ecosystem nodes do not yet have archetype-specific conditional probability weights -- noted as future work | bottom-center |
| "KEY DIVERGENCES" | Database: PostgreSQL vs Supabase vs SQLite; Compute: AWS vs Render vs Railway; Ecosystem: full vs partial vs none | top-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Team: 5-15 | Deep"
- Label 2: "Team: 1-3 | Shallow"
- Label 3: "Team: 1 | Variable"
- Label 4: "Team: 10-30+ | Deep"
- Label 5: "~40+ nodes active"
- Label 6: "~25 nodes active"
- Label 7: "~18 nodes active"
- Label 8: "~50+ nodes active"

### Caption (for embedding in documentation)

Four team archetypes produce dramatically different activation patterns across the 78-node decision network, from the Solo Hacker's minimal 18-node path to the Well-Funded Startup's 50+ node enterprise configuration.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `archetype_overlay`, `selected_option`, `deferred_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text.

### Figure-Specific Rules

9. The 4 archetypes are: Engineer-Heavy Startup, Musician-First Team, Solo Hacker, Well-Funded Startup. Do NOT invent a fifth archetype.
10. These archetypes have conditional probability tables defined in core PRD nodes (build_vs_buy, primary_database, compute_platform, etc.).
11. Ecosystem nodes (28 added in v3.0.0) do NOT have archetype-specific weights yet -- this is noted in the expand-prd document Section 5.2 as future work.
12. Node activation counts are approximate/illustrative. Do NOT claim exact per-archetype counts as verified.
13. Team sizes from archetypes README: Engineer-Heavy 5-15, Musician-First 1-3, Solo Hacker 1, Well-Funded 10-30+.
14. Technical depth: Engineer-Heavy = Deep, Musician-First = Shallow, Solo Hacker = Variable, Well-Funded = Deep.
15. Budget: Engineer-Heavy = Moderate, Musician-First = Low, Solo Hacker = Minimal, Well-Funded = High.

## Alt Text

Four archetypes activating different 78-node subsets with ecosystem sensitivity

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "scenario-02",
    "title": "Four Archetype Scenario Comparison",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Four team archetypes activate dramatically different subsets of the 78-node network.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Engineer-Heavy Panel",
        "role": "archetype_overlay",
        "is_highlighted": true,
        "labels": ["~40+ nodes", "Custom, Deep"]
      },
      {
        "name": "Musician-First Panel",
        "role": "archetype_overlay",
        "is_highlighted": true,
        "labels": ["~25 nodes", "Managed, Shallow"]
      },
      {
        "name": "Solo Hacker Panel",
        "role": "archetype_overlay",
        "is_highlighted": true,
        "labels": ["~18 nodes", "Minimal, Variable"]
      },
      {
        "name": "Well-Funded Panel",
        "role": "archetype_overlay",
        "is_highlighted": true,
        "labels": ["~50+ nodes", "Enterprise, Deep"]
      }
    ],
    "relationships": [
      {
        "from": "Engineer-Heavy",
        "to": "Custom infrastructure",
        "type": "arrow",
        "label": "edge inference, PostgreSQL, Terraform"
      },
      {
        "from": "Musician-First",
        "to": "Managed services",
        "type": "arrow",
        "label": "Supabase, Render, no IaC"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ECOSYSTEM SENSITIVITY",
        "body_text": "28 ecosystem nodes lack formal archetype weights -- future work",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
