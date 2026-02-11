# Agentic UX Research Influences

Academic grounding for the probabilistic PRD's UI/UX decision nodes.
Maps research concepts to implementation readiness and specific PRD nodes.

**Last updated**: 2026-02-11

---

## Concept Map

Each concept links an academic insight to PRD decision nodes and current library support.

### 1. Bidirectional Context Loop

| Attribute | Value |
|-----------|-------|
| **Paper** | DuetUI: Human-AI Joint Interface Design (arXiv:2509.13444) |
| **Core idea** | Shared state between user and AI agent — both can read/write UI context, creating a co-evolutionary loop rather than request-response |
| **PRD nodes** | `agentic_ui_framework` (CopilotKit shared state), `ui_adaptation_strategy` (malleable AI-driven) |
| **Library support** | CopilotKit `useCopilotReadable`/`useCopilotAction` + AG-UI protocol (31 event types) |
| **Maturity** | **HIGH** — production-ready |
| **Music attribution mapping** | Attribution confidence state shared bidirectionally: agent updates confidence scores, user corrections feed back into resolution pipeline |

### 2. Cognitive Oversight / Interruptible Processes

| Attribute | Value |
|-----------|-------|
| **Paper** | Deep Cognition: Interaction as Intelligence (arXiv:2507.15759) |
| **Core idea** | AI processes must be interruptible, inspectable, and steerable — not black boxes. Transparent reasoning chains as first-class UI element |
| **PRD nodes** | `agentic_ui_framework` (LangGraph interrupt + CoAgents), `ui_adaptation_strategy` (progressive disclosure) |
| **Library support** | LangGraph `interrupt()` + CopilotKit CoAgents for human-in-the-loop; Vercel AI SDK `<Reasoning>` component |
| **Maturity** | **HIGH** — production-ready |
| **Music attribution mapping** | Dispute resolution workflows where users can interrupt automated attribution, inspect reasoning chain (why was this credit assigned?), and override with evidence |

### 3. Preference-Aligned UI Generation

| Attribute | Value |
|-----------|-------|
| **Paper** | AlignUI: Aligning LLM-Generated UIs with User Preferences (arXiv:2601.17614) |
| **Core idea** | Predictability/Efficiency/Explorability trichotomy for generated interfaces. Users have measurably different layout preferences that LLMs can learn |
| **PRD nodes** | `ui_adaptation_strategy` (malleable AI-driven, configurable presets) |
| **Library support** | None — CrowdGenUI (arXiv:2411.03477) is paper-only |
| **Maturity** | **LOW** — research frontier |
| **Music attribution mapping** | High-confidence attributions favor predictable controls (show result immediately); uncertain multi-source results favor explorable controls (show alternatives, evidence chains) |
| **Watchlist** | CrowdGenUI (no OSS), AlignX (github.com/JinaLeejnl/AlignX — LLM alignment, not UI-specific) |

### 4. Specification-Driven UI (SPEC)

| Attribute | Value |
|-----------|-------|
| **Paper** | SpecifyUI: Structured Specifications and Generative AI (arXiv:2509.07334) |
| **Core idea** | SPEC: structured parameterized hierarchy (Global → Section → Component) for declarative UI generation. Separates *what* from *how* |
| **PRD nodes** | `ui_adaptation_strategy` (malleable AI-driven), `agentic_ui_framework` (CopilotKit generative UI) |
| **Library support** | Google A2UI (github.com/google/A2UI, 11.2k stars, v0.9) |
| **Maturity** | **HIGH** — production-ready |
| **Music attribution mapping** | A2UI's declarative JSON component catalog maps to attribution views: confidence dashboard spec, provenance drill-down spec, dispute form spec. Dynamic agency allocation (more AI control early, more user control during refinement) maps to Autonomous/Recommend/Escalate governance tiers |

### 5. Just-in-Time Objectives

| Attribute | Value |
|-----------|-------|
| **Paper** | Poppins: Proactive Assistance for Just-In-Time Objectives (Stanford, arXiv:2510.14591) |
| **Core idea** | Context-aware goal inference without explicit prompting. System observes interaction patterns and infers user's current objective |
| **PRD nodes** | `ui_adaptation_strategy` (malleable AI-driven) |
| **Library support** | None — Flask+Svelte prototype, no OSS release |
| **Maturity** | **LOW** — research frontier |
| **Music attribution mapping** | Attribution system could infer user's current task (browsing catalog vs. disputing a credit vs. verifying provenance chain) from interaction patterns and adapt UI density/actions accordingly |
| **Watchlist** | Monitor Stanford HCI group for OSS release |

### 6. Progressive Scaffolding / Dynamic Agency

| Attribute | Value |
|-----------|-------|
| **Papers** | DuetUI (arXiv:2509.13444) + SpecifyUI (arXiv:2509.07334) |
| **Core idea** | Graduated autonomy: AI agent starts with high control (generating initial UI), user takes more control during refinement. Agency shifts dynamically based on task phase and confidence |
| **PRD nodes** | `ui_adaptation_strategy` (all options), `agentic_ui_framework` (CopilotKit tiers) |
| **Library support** | CopilotKit action tiers + agentic-design.ai patterns |
| **Maturity** | **MEDIUM** — composable from existing primitives |
| **Music attribution mapping** | New users see AI-curated attribution summaries (high AI agency); experienced rights administrators interact with raw confidence scores and edit directly (high user agency). Maps to archetype-driven probability overrides in PRD |

### 7. Transparent Reasoning Chains

| Attribute | Value |
|-----------|-------|
| **Paper** | Deep Cognition: Interaction as Intelligence (arXiv:2507.15759) |
| **Core idea** | Reasoning processes should be visible, not hidden. Users should see *why* an AI made a decision, not just the result. Reasoning-as-UI, not reasoning-as-backend |
| **PRD nodes** | `agentic_ui_framework` (Vercel AI SDK, CopilotKit), `ui_adaptation_strategy` (progressive disclosure) |
| **Library support** | Vercel AI SDK `<Reasoning>` component + assistant-ui (github.com/assistant-ui/assistant-ui, 8.4k stars) — Radix-style composable primitives |
| **Maturity** | **HIGH** — production-ready |
| **Music attribution mapping** | Attribution confidence should expose reasoning chains: "85% confidence because: ISRC match (100%), MusicBrainz credit (90%), string similarity (75%), Discogs conflict (-10%)" |

### 8. Real-Time Guidance Design

| Attribute | Value |
|-----------|-------|
| **Paper** | Real-Time Guidance Design for AI Assistants (ICIS 2025, Grau & Blohm) |
| **Core idea** | Three design principles for real-time AI guidance validated by eye-tracking: progressive disclosure, attention-aware placement, cognitive load management. Grounded in Wickens' Multiple Resource Theory |
| **PRD nodes** | `voice_agent_stack` (progressive disclosure for voice), `ui_adaptation_strategy` (progressive disclosure) |
| **Library support** | Design principles, not a library — applicable to any framework |
| **Maturity** | **MEDIUM** — validated design patterns, no library needed |
| **Music attribution mapping** | Voice attribution queries should progressively disclose: summary first ("3 credits found, 85% average confidence"), then details on request. Attention-aware placement for confidence indicators |

### 9. Malleable Browser Spaces (Orca)

| Attribute | Value |
|-----------|-------|
| **Paper** | Orca: Malleable Browser Spaces for Agentic Tasks (Jiang & Xia, UCSD) |
| **Core idea** | Parallel agent monitoring through tldraw-style canvas. Spatial organization of agent workspaces. Users see multiple agents' states simultaneously |
| **PRD nodes** | `agentic_ui_framework` (custom agent UI option), `ui_adaptation_strategy` (malleable AI-driven) |
| **Library support** | Code released: github.com/peilingjiang/orca (research prototype) |
| **Maturity** | **LOW** — research prototype, not production-ready |
| **Music attribution mapping** | Multi-source attribution resolution could use spatial canvas: one space per source (MusicBrainz, Discogs, AcoustID), agent resolving conflicts visually |
| **Watchlist** | Monitor for tldraw integration patterns applicable to CopilotKit |

---

## Research Frontier Watchlist

Concepts with LOW library maturity — monitor for OSS releases and maturing implementations.

| Concept | Paper | What to watch | Why it matters |
|---------|-------|---------------|----------------|
| Preference-Aligned UI | AlignUI (2601.17614) | CrowdGenUI OSS release, AlignX UI pivot | Would enable automatic UI adaptation to user preference profiles |
| Just-in-Time Objectives | Poppins (Stanford) | Stanford HCI group repos, UIST/CHI proceedings | Would eliminate need for explicit mode-switching in attribution UI |
| Malleable Browser Spaces | Orca (UCSD) | github.com/peilingjiang/orca, tldraw ecosystem | Spatial multi-agent monitoring pattern for complex attribution cases |

---

## Implementation-Ready Concepts

Concepts with HIGH maturity — directly usable in the CopilotKit/LangGraph/Vercel stack.

| Concept | Library | Integration path |
|---------|---------|-----------------|
| Bidirectional Context Loop | CopilotKit shared state + AG-UI | `useCopilotReadable` for attribution state, `useCopilotAction` for user corrections |
| Cognitive Oversight | LangGraph `interrupt()` + CoAgents | Human-in-the-loop checkpoints during automated attribution pipeline |
| Specification-Driven UI | Google A2UI (v0.9) | Declarative JSON specs for attribution views, composable with CopilotKit |
| Transparent Reasoning | Vercel AI SDK `<Reasoning>` + assistant-ui | Confidence explanation UI components, composable Radix-style primitives |

**assistant-ui** (github.com/assistant-ui/assistant-ui, 8.4k stars) is a key complement to any framework choice:
- Composable Radix-style chat primitives (not a monolithic widget)
- Integrates with both Vercel AI SDK and LangGraph
- Provides `<Thread>`, `<Message>`, `<Composer>` components
- Can be layered on top of CopilotKit for chat-specific UI needs

---

## Paper Index

Full citations for all referenced papers.

| # | Short name | Full citation | Identifier |
|---|-----------|---------------|------------|
| 1 | DuetUI | "DuetUI: Human-AI Joint Interface Design" | arXiv:2509.13444 |
| 2 | Deep Cognition | "Deep Cognition: Interaction as Intelligence for AI Agents" | arXiv:2507.15759 |
| 3 | AlignUI | "AlignUI: Aligning LLM-Generated UIs with User Preferences" | arXiv:2601.17614 |
| 4 | SpecifyUI | "SpecifyUI: Structured Specifications and Generative AI for UI Design" | arXiv:2509.07334 |
| 5 | Poppins | "Poppins: Proactive Assistance via Just-In-Time Objective Inference" | arXiv:2510.14591 |
| 6 | Real-Time Guidance | Grau, L. & Blohm, I. "Real-Time Guidance Design for AI Assistants" | ICIS 2025 |
| 7 | Orca | Jiang, P. & Xia, H. "Orca: Malleable Browser Spaces for Agentic Tasks" | UCSD, github.com/peilingjiang/orca |

---

## Cross-References

- **UX Vision document**: [`../../tmp/ux-vision.md`](../../tmp/ux-vision.md) — Contains 10+ embedded academic references on symbiotic UI, cited in both `ui_adaptation_strategy` and `agentic_ui_framework` decision nodes
- **Decision nodes with research_influences sections**:
  - [`../decisions/L2-architecture/ui-adaptation-strategy.decision.yaml`](../decisions/L2-architecture/ui-adaptation-strategy.decision.yaml)
  - [`../decisions/L3-implementation/agentic-ui-framework.decision.yaml`](../decisions/L3-implementation/agentic-ui-framework.decision.yaml)
  - [`../decisions/L3-implementation/voice-agent-stack.decision.yaml`](../decisions/L3-implementation/voice-agent-stack.decision.yaml)
