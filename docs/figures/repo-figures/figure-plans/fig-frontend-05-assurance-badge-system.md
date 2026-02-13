# fig-frontend-05: Assurance Badge System

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-05 |
| **Title** | Assurance Badge System: A0-A3 Provenance Levels with Color-Coded Underlines |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 |
| **Location** | docs/architecture/frontend.md, docs/design-system.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure explains the four-level assurance badge system (A0-A3) used throughout the UI to indicate provenance quality. Each level has a distinct color, label, and plain-English meaning. The figure shows how badges appear as color-underlined editorial-caps text and maps each level to its data source requirements and real-world meaning.

The key message is: "Four assurance levels -- A0 (No Data, gray) through A3 (Artist Verified, green) -- give users an instant visual signal of how trustworthy an attribution record's provenance chain is."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  ASSURANCE BADGE SYSTEM                                                |
|  ■ A0-A3 Provenance Levels                                            |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. THE FOUR LEVELS                                                    |
|  ──────────────────                                                    |
|                                                                        |
|  ┌────────────────────────────────────────────────────────────────┐   |
|  │                                                                 │   |
|  │   A0 -- No Data         No provenance information found         │   |
|  │   ───────────── (gray)  System has no sources for this field    │   |
|  │                                                                 │   |
|  │   A1 -- Single Source   One database claims this attribution    │   |
|  │   ─────────────── (amber) e.g., only Discogs has a credit      │   |
|  │                                                                 │   |
|  │   A2 -- Multi-Source    Multiple independent sources agree      │   |
|  │   ─────────────── (blue) e.g., MusicBrainz + Discogs match     │   |
|  │                                                                 │   |
|  │   A3 -- Artist Verified Artist has directly confirmed           │   |
|  │   ─────────────── (green) Highest trust; requires artist input  │   |
|  │                                                                 │   |
|  └────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  II. BADGE ANATOMY                                                     |
|  ─────────────────                                                     |
|                                                                        |
|  ┌──────────────────────────────────────┐                             |
|  │  <span class="editorial-caps text-xs │                             |
|  │         border-b-2">                 │                             |
|  │    A2 -- Multi-Source                │                             |
|  │    ═══════════════════  (blue line)  │                             |
|  │  </span>                             │                             |
|  │                                      │                             |
|  │  Color from: getAssuranceCssVar()    │                             |
|  │  Label from: ASSURANCE_LABELS map    │                             |
|  └──────────────────────────────────────┘                             |
|                                                                        |
|  III. USAGE CONTEXT                                                    |
|  ──────────────────                                                    |
|                                                                        |
|  ■ Works list: beside each work title                                  |
|  ■ Work detail: hero section, next to confidence score                 |
|  ■ Review queue: with confidence gauge per item                        |
|  ■ Agent responses: referenced in explain_confidence tool output       |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ASSURANCE BADGE SYSTEM" in display font |
| A0 level | `assurance_a0` | Gray underline, "No Data", plain-English meaning |
| A1 level | `assurance_a1` | Amber underline, "Single Source", plain-English meaning |
| A2 level | `assurance_a2` | Blue underline, "Multi-Source", plain-English meaning |
| A3 level | `assurance_a3` | Green underline, "Artist Verified", plain-English meaning |
| Badge anatomy | `processing_stage` | HTML structure with editorial-caps and border-b-2 |
| Utility function references | `data_mono` | getAssuranceCssVar(), ASSURANCE_LABELS |
| Usage context list | `feature_list` | Four locations where badges appear in the UI |
| Roman numerals I-III | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. Assurance levels are A0-A3 (four levels), NOT A1-A4 or any other range.
2. A0 = gray (#9E9E9E), A1 = amber (#E09F3E), A2 = blue (#5B9BD5), A3 = green (#4A7C59).
3. The badge labels are: "A0 -- No Data", "A1 -- Single Source", "A2 -- Multi-Source", "A3 -- Artist Verified".
4. Badges use editorial-caps class (uppercase Plus Jakarta Sans) with a 2px bottom border in the assurance color.
5. The enum values in code are LEVEL_0, LEVEL_1, LEVEL_2, LEVEL_3 (not A0, A1, A2, A3 directly).
6. Colors come from CSS variables: var(--color-assurance-a0) through var(--color-assurance-a3).
7. The AssuranceBadge component is in `frontend/src/components/works/assurance-badge.tsx`.
8. Do NOT confuse assurance levels with confidence tiers -- they are different systems.

## Alt Text

Four assurance levels A0 through A3 with color-coded underline badges, anatomy diagram, and usage context across works list, detail, review, and agent.
