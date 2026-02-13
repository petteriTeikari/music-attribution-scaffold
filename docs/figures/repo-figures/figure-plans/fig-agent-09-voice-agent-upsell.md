# fig-agent-09: Voice Agent Upsell UI

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-09 |
| **Title** | Voice Agent Upsell: Pro Feature Banner with Mic Animation and Example Queries |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 |
| **Location** | docs/architecture/frontend.md, docs/product.md |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the VoiceAgentBanner component -- an aspirational UI surface for a Pro-tier voice feature that does NOT have backend implementation. The banner displays a coral mic icon in a circle, the title "Voice Agent -- Pro Feature", an example query in italics, and an "Upgrade to Pro" button. It is dismissable and follows the design philosophy of subtle, aspirational upsell.

The key message is: "The voice agent is a Pro-tier upsell surface only -- the banner shows a mic animation, example queries, and an upgrade button, but NO actual voice processing is implemented. It's aspirational UI for a premium feature."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  VOICE AGENT UPSELL UI                                                 |
|  ■ Pro Feature Surface                                                 |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. BANNER COMPONENT                                                   |
|  ────────────────────                                                  |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────┐      |
|  │                                                          ✕  │      |
|  │  ┌────┐                                                     │      |
|  │  │ 🎤 │  Voice Agent — Pro Feature                          │      |
|  │  │    │  Ask questions about your attributions              │      |
|  │  └────┘  by voice. "Who produced Hide and Seek?"            │      |
|  │          (italic example query)                              │      |
|  │                                          ┌──────────────┐   │      |
|  │                                          │Upgrade to Pro│   │      |
|  │                                          └──────────────┘   │      |
|  └─────────────────────────────────────────────────────────────┘      |
|                                                                        |
|  II. COMPONENT ANATOMY                                                 |
|  ─────────────────────                                                 |
|                                                                        |
|  VoiceAgentBanner()                                                    |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  State: dismissed (useState boolean)                              │  |
|  │  Renders: null if dismissed                                       │  |
|  │                                                                   │  |
|  │  Mic icon:                                                        │  |
|  │  ■ 48x48 rounded-full coral bg                                   │  |
|  │  ■ White SVG microphone path                                     │  |
|  │  ■ No actual animation yet (CSS pulse planned)                   │  |
|  │                                                                   │  |
|  │  Title: "Voice Agent — Pro Feature" (font-semibold)              │  |
|  │  Body: example query in italic text-muted                        │  |
|  │  CTA: "Upgrade to Pro" button (bg-accent, white text)            │  |
|  │  Dismiss: ✕ button (top-right, aria-label="Dismiss")             │  |
|  │                                                                   │  |
|  │  Container: border-accent bg-accent-muted rounded-lg p-6        │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  III. DESIGN PHILOSOPHY                                                |
|  ──────────────────────                                                |
|  ■ Subtle and aspirational — never pushy or interruptive               |
|  ■ Pro tier = higher cost tier (voice processing is expensive)         |
|  ■ MVP: show aspirational UI ONLY — NO actual voice processing         |
|  ■ Example query uses Imogen Heap ("Who produced Hide and Seek?")      |
|  ■ Banner is dismissable (respects user preference)                    |
|  ■ TODO: not yet integrated into page layout (wire up during tuning)   |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "VOICE AGENT UPSELL UI" in display font |
| Banner mockup | `module_grid` | Visual layout of the banner component |
| Mic icon | `processing_stage` | 48x48 coral circle with white SVG microphone |
| Title text | `label_editorial` | "Voice Agent -- Pro Feature" |
| Example query | `data_mono` | Italic "Who produced Hide and Seek?" |
| CTA button | `selected_option` | "Upgrade to Pro" with bg-accent styling |
| Dismiss button | `processing_stage` | Top-right close with aria-label |
| Component anatomy | `processing_stage` | State, rendering logic, styling details |
| Design philosophy | `callout_box` | Subtle, aspirational, no actual voice processing |

## Anti-Hallucination Rules

1. The component is VoiceAgentBanner in `frontend/src/components/pro/voice-agent-banner.tsx`.
2. It has a TODO comment: "Component not yet integrated -- wire up during UI fine-tuning".
3. NO actual voice processing is implemented -- it is purely an upsell UI surface.
4. The mic icon uses a custom SVG path (not an icon library).
5. The container uses border-accent bg-accent-muted (not bg-surface or bg-elevated).
6. The "Upgrade to Pro" button has an empty onClick handler (`/* Pro upsell modal would open here */`).
7. The banner is dismissable via useState(false) -- renders null when dismissed.
8. The example query is "Who produced Hide and Seek?" -- references the Imogen Heap persona.
9. Voice is explicitly defined as a premium/Pro tier upsell in the UX philosophy rules.

## Alt Text

Voice agent upsell banner with coral mic icon, "Pro Feature" title, example query about Hide and Seek, "Upgrade to Pro" button, and dismiss control.
