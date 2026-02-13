# fig-frontend-06: Works List Page Layout

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-06 |
| **Title** | Works List Page: Sidebar + Catalog with Confidence Gauges and Assurance Badges |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/frontend.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the spatial layout of the /works page as it appears in the browser. The fixed sidebar (60px) anchors the left edge, while the main content area displays the works catalog with search/sort controls, horizontal work rows separated by dividers, each row containing a small confidence gauge, work title, artist name, assurance badge, and source agreement percentage.

The key message is: "The works catalog uses horizontal rows with divider lines (not shadow-box cards), each row showing confidence, title, assurance level, and source agreement at a glance."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  WORKS LIST PAGE LAYOUT                                                |
|  ■ /works Route                                                        |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌────┐ ┌──────────────────────────────────────────────────────────┐  |
|  │ MA │ │  WORKS                                                    │  |
|  │    │ │  ─────                                                    │  |
|  │ W  │ │                                                           │  |
|  │ O  │ │  ┌─ Search ──────────────┐  Sort: [Confidence ▼] [↓]    │  |
|  │ R  │ │  │ Search works...       │                                │  |
|  │ K  │ │  └───────────────────────┘                                │  |
|  │ S  │ │                                                           │  |
|  │    │ │  ────────────────────────────────────────────────────     │  |
|  │ R  │ │                                                           │  |
|  │ E  │ │   ╭─╮  Hide and Seek               A3 -- Verified        │  |
|  │ V  │ │   │92│  Imogen Heap                 Src: 95%   v3        │  |
|  │ I  │ │   ╰─╯                                                    │  |
|  │ E  │ │                                                           │  |
|  │ W  │ │  ────────────────────────────────────────────────────     │  |
|  │    │ │                                                           │  |
|  │ P  │ │   ╭─╮  Ellipse                     A2 -- Multi-Source    │  |
|  │ E  │ │   │78│  Imogen Heap                 Src: 80%   v2        │  |
|  │ R  │ │   ╰─╯                                                    │  |
|  │ M  │ │                                                           │  |
|  │ S  │ │  ────────────────────────────────────────────────────     │  |
|  │    │ │                                                           │  |
|  │────│ │   ╭─╮  Goodnight and Go             A1 -- Single Source  │  |
|  │ A/Q│ │   │34│  Imogen Heap                 Src: 40%   v1        │  |
|  │ 🔔 │ │   ╰─╯                                                    │  |
|  │ ☀️ │ │                                                           │  |
|  │ ■  │ │  ────────────────────────────────────────────────────     │  |
|  └────┘ └──────────────────────────────────────────────────────────┘  |
|                                                                        |
|  DATA FLOW                                                             |
|  ─────────                                                             |
|  worksAtom → searchQueryAtom → sortFieldAtom → filteredWorksAtom       |
|  filteredWorksAtom → map(WorkCard) → render rows                       |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WORKS LIST PAGE LAYOUT" in display font |
| Sidebar | `module_grid` | Fixed 60px sidebar with rotated nav links |
| Search input | `processing_stage` | Search box bound to searchQueryAtom |
| Sort controls | `processing_stage` | Sort field dropdown (confidence/title/updated) and direction toggle |
| Work rows | `feature_list` | Horizontal rows with divider lines, not cards |
| Confidence gauges (sm) | `confidence_high`, `confidence_medium`, `confidence_low` | Small gauges per row |
| Work titles | `heading_display` | Clickable, navigate to /works/[workId] |
| Assurance badges | `assurance_a3`, `assurance_a2`, `assurance_a1` | Color-underlined badges |
| Source agreement | `data_mono` | Percentage in monospace |
| Data flow diagram | `data_flow` | Jotai atom chain from worksAtom to rendered output |

## Anti-Hallucination Rules

1. The page route is /works, rendering `frontend/src/app/works/page.tsx`.
2. Works are displayed as horizontal rows with divider lines, NOT shadow-box cards.
3. Sort options are: confidence, title, updated (3 options). Direction is asc/desc.
4. Each row shows: sm ConfidenceGauge, work title (clickable), artist name, AssuranceBadge, source agreement %, version.
5. The Jotai atom chain is: worksAtom + searchQueryAtom + sortFieldAtom + sortDirectionAtom -> filteredWorksAtom.
6. The sidebar width is 60px (var(--sidebar-width)), fixed position.
7. Sidebar navigation links use vertical-rl writing mode with 180deg rotation.
8. The mock data uses Imogen Heap works (the project's persona), not generic or invented artists.

## Alt Text

Works list page with fixed sidebar and horizontal catalog rows showing confidence gauges, titles, assurance badges, and source agreement percentages.
