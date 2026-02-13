# fig-frontend-08: Review Queue Workflow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-08 |
| **Title** | Review Queue: AI Suggestion Diffs, Batch Approval, and Progress Tracking |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 |
| **Location** | docs/architecture/frontend.md, docs/workflow.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure explains the review queue workflow -- the primary friction reducer for attribution work. It shows the AgentReviewQueue component: agent narration header, progress bar with counter, work items with Roman numeral indices, expandable AI suggestion diffs (strikethrough current -> accent arrow -> suggested), and the batch "Approve All" action.

The key message is: "The review queue transforms tedious one-by-one attribution review into a momentum-driven workflow with AI-generated diffs, batch approval, and progress tracking."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  REVIEW QUEUE WORKFLOW                                                 |
|  ■ AI-Assisted Attribution Review                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. AGENT NARRATION HEADER                                             |
|  ──────────────────────────                                            |
|                                                                        |
|  ■ Agent: I've analyzed 5 attributions and generated suggestions.       |
|    Items are sorted by review priority.                                 |
|                                                                        |
|  II. PROGRESS BAR                                                      |
|  ────────────────                                                      |
|                                                                        |
|  ═══════════════════░░░░░░░░░░░░░░░░░░░░  3/8    APPROVE ALL          |
|  (green filled portion)   (unfilled)      counter  batch action        |
|                                                                        |
|  III. REVIEW ITEMS                                                     |
|  ─────────────────                                                     |
|                                                                        |
|  ────────────────────────────────────────────────────────────          |
|  I    ╭─╮  Goodnight and Go          A1 -- Single Source    APPROVE    |
|       │34│  Imogen Heap                                                |
|       ╰─╯  2 suggestions                                              |
|            ┌─────────────────────────────────────────────┐             |
|            │  ̶L̶E̶V̶E̶L̶_̶1̶  →  LEVEL_2                        │             |
|            │  Cross-referencing MusicBrainz and Discogs  │             |
|            │  confirms credit chain                      │             |
|            ├─────────────────────────────────────────────┤             |
|            │  ̶1̶ ̶s̶o̶u̶r̶c̶e̶(̶s̶)̶  →  Add MusicBrainz cross-ref  │             |
|            │  Additional source improves confidence ~15% │             |
|            └─────────────────────────────────────────────┘             |
|  ────────────────────────────────────────────────────────────          |
|  II   ╭─╮  The Moment I Said It      A1 -- Single Source    APPROVE   |
|       │41│  Imogen Heap                                                |
|       ╰─╯  1 suggestion                                               |
|  ────────────────────────────────────────────────────────────          |
|                                                                        |
|  IV. SUGGESTION DIFF ANATOMY                                           |
|  ────────────────────────────                                          |
|  ■ Current value: red strikethrough text                               |
|  ■ Arrow: coral accent "→"                                             |
|  ■ Suggested value: green bold text                                    |
|  ■ Confidence in suggestion: monospace percentage (82%)                |
|  ■ Reason: explanation text below                                      |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "REVIEW QUEUE WORKFLOW" in display font |
| Agent narration | `callout_box` | Agent message with accent square marker |
| Progress bar | `data_flow` | Green fill proportional to approved/total, counter, Approve All button |
| Review items | `feature_list` | Roman numeral index, sm gauge, title, artist, assurance badge, approve button |
| Suggestion toggle | `decision_point` | "N suggestions" expandable link |
| Diff view | `problem_statement` / `solution_component` | Strikethrough current -> arrow -> suggested with reason |
| Approve button | `selected_option` | Per-item approval action with green underline |
| Approve All | `selected_option` | Batch approval with accent underline |
| Roman numerals | `section_numeral` | I, II, III... per review item (Warp Records homage) |

## Anti-Hallucination Rules

1. The AgentReviewQueue component is in `frontend/src/components/review/agent-review-queue.tsx`.
2. Suggestions are generated by `generateAgentSuggestions()` function based on work data (not from the LLM agent).
3. Three suggestion types: assurance level upgrade, add source cross-reference, request artist verification.
4. Diffs show: red strikethrough (current) -> coral arrow -> green (suggested) with confidence percentage and reason.
5. Progress bar is a 1px line with green fill, not a thick bar or circle.
6. Roman numerals are used for item indices (I, II, III...), generated by a toRoman() utility.
7. "Approve All" is an editorial-caps underlined text link, not a pill button.
8. The /review route is only visible in artist role (artistOnly: true in NAV_ITEMS).

## Alt Text

Review queue workflow showing agent narration, progress bar, work items with Roman numerals, expandable AI suggestion diffs, and batch approval action.
