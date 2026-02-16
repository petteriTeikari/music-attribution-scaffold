# Investor Pitch Deck

> 12 slides presenting the Music Attribution Scaffold as an investable platform -- from market opportunity through competitive moat to partnership strategy.
>
> **Audience**: Music industry executives, investors, potential collaborators.
> Figures generated with [Nano Banana Pro](https://nanobananapro.com/) (Google Gemini image generation). Figure plans in [`docs/figures/repo-figures/figure-plans/`](https://github.com/petteriTeikari/music-attribution-scaffold/tree/main/docs/figures/repo-figures/figure-plans).

---

## I. Market Opportunity

![Generative music market waterfall from $558M to $7.4B with attribution infrastructure TAM breakdown](figures/fig-pitch-01-market-opportunity.jpg)

*Generative music market growing from $558M (2024) to $7.4B (2035), with the attribution infrastructure TAM broken out across AI music platforms, CMO compliance tools, and independent artist verification -- a rising tide where every AI-generated track needs provenance.*

---

## II. Competitive Positioning

![Quadrant chart: open vs closed, black box vs calibrated -- scaffold alone in open+calibrated position](figures/fig-pitch-02-competitive-positioning.jpg)

*Competitive landscape on two axes: open-source vs. proprietary and black-box vs. calibrated confidence. 12+ companies mapped -- Sureel, Musical AI, Vermillio, BMAT, Pex, and others -- with the attribution scaffold uniquely positioned as the only open-source system with calibrated confidence scoring via conformal prediction.*

---

## III. Technical Architecture

![Five-pipeline architecture with unified PostgreSQL handling relational, vector, and graph data](figures/fig-pitch-03-architecture.jpg)

*Five-pipeline architecture -- ETL, entity resolution, attribution engine, API/MCP server, and agentic chat -- unified on a single PostgreSQL instance with relational tables, pgvector embeddings, and Apache AGE graph queries, eliminating multi-database operational overhead.*

---

## IV. Assurance Levels (A0--A3)

![Four ascending steps from A0 Unknown to A3 Artist-Verified showing tiered provenance progression](figures/fig-pitch-04-assurance-levels.jpg)

*Four-tier provenance framework ascending from A0 (Unknown -- no metadata) through A1 (Single Source), A2 (Corroborated -- multiple sources agree), to A3 (Artist-Verified -- identity-confirmed provenance), mapping directly to ISRC, ISWC, and ISNI registry standards.*

---

## V. Team & Hiring Plan

![Gantt chart: CTO at M0, plus four phased hires growing to 5](figures/fig-pitch-05-team-hiring.jpg)

*Phased hiring plan: CTO/founder from M0, UX/UI engineer at M1, cloud/infrastructure engineer at M2, LLM/ML engineer at M3, and optional voice agent engineer at M8 -- growing from solo founder to a 5-person team with four specialized roles, each timed to the roadmap phase that needs them.*

---

## VI. Milestone Roadmap

![Three-phase roadmap: Foundation M0-M6, Scale M6-M12, Ecosystem M12-M18, with go/no-go gates](figures/fig-pitch-06-milestone-roadmap.jpg)

*Three-phase 18-month roadmap: Foundation (M0--M6, core platform + STIM pilot), Scale (M6--M12, Pro tier + 3 CMO integrations), Ecosystem (M12--M18, voice agent + marketplace), with go/no-go gates at each phase boundary tied to specific KPIs.*

---

## VII. Financial Scenarios

![Stacked bar comparison: Helsinki+Warsaw $809K, London+Helsinki $1.4M, San Francisco $2.3M for 18 months](figures/fig-pitch-07-financial-scenarios.jpg)

*18-month total cost comparison across three geography scenarios: Helsinki + Warsaw at $809K (3x engineering per dollar), London + Helsinki at $1.4M, and San Francisco at $2.3M -- demonstrating how Nordic + CEE talent delivers equivalent capability at 65% lower burn.*

---

## VIII. Revenue Model

![Three-tier pricing: Free for researchers, Pro $49/mo for artists, Enterprise $499/mo for CMOs, with revenue curve](figures/fig-pitch-08-revenue-model.jpg)

*Three-tier open-core revenue model: Free (researchers, core attribution + rate-limited API), Pro at $49/month (artists, voice agent + batch review), Enterprise at $499/month (CMOs, SLA + compliance reports + white-label), with revenue projection from first revenue at M12 to 3 enterprise clients by M18.*

---

## IX. Competitive Moat

![Hexagonal radar with 6 moat advantages: open-source, calibrated confidence, MCP, neutral, PRD, EU AI Act](figures/fig-pitch-09-moat-defensibility.jpg)

*Six reinforcing competitive advantages forming a defensive moat: open-source trust (auditability), calibrated confidence (conformal prediction), MCP-native consent queries, neutral positioning (not owned by any platform), probabilistic PRD architecture, and EU AI Act compliance readiness -- no single competitor has more than two.*

---

## X. Voice Agent Pipeline

![Voice pipeline: User, STT, LLM, Attribution Tools, TTS, User -- under 400ms, Pipecat 6x cheaper than Vapi](figures/fig-pitch-10-voice-agent.jpg)

*Voice attribution pipeline flowing from user speech through STT, LLM (Haiku 4.5), attribution tool calls, and TTS in under 400ms end-to-end. Pipecat delivers 6x cost savings ($0.02/conversation) over Vapi ($0.12/conversation) as a premium Pro tier feature.*

---

## XI. Regulatory Tailwind

![EU AI Act timeline: GPAI obligations and TDM enforcement creating rising mandatory attribution demand](figures/fig-pitch-11-regulatory-tailwind.jpg)

*EU AI Act regulatory timeline showing how GPAI obligations (Aug 2025), Code of Practice (Jul 2025), TDM enforcement, and the STIM pilot create escalating mandatory demand for attribution infrastructure -- each compliance deadline accelerates customer acquisition.*

---

## XII. Partnership Strategy

![Hub-and-spoke: scaffold at center connecting CMOs, platforms, providers, registries, certifiers bidirectionally](figures/fig-pitch-12-partnership-strategy.jpg)

*Hub-and-spoke partnership architecture with the attribution scaffold as the neutral center -- "Switzerland of music attribution" -- connecting CMOs (STIM, PRS, SACEM), platforms (Spotify, YouTube, AI platforms), attribution providers (Pex, BMAT, Audible Magic), registries (ISRC, ISWC, ISNI, DDEX), and certifiers (Fairly Trained, C2PA) with bidirectional data flows, trusted by all parties because it is not owned by any single one.*

---

## Next: Advanced Due Diligence Slides

For investors and collaborators seeking deeper technical and financial detail, see the **[Advanced Pitch Deck](pitch-deck-advanced.md)** -- 18 additional slides covering:

- **Technical Deep-Dive** (5 slides): Architecture scaling, entity resolution moat, conformal prediction, knowledge graph roadmap, inference latency
- **Competitive & Market Intelligence** (4 slides): Positioning moat, TAM/SAM/SOM, regulatory tailwinds, partnership ecosystem
- **Product & UX** (4 slides): Review queue efficiency, WCAG 2.1 AA accessibility, voice agent upsell, adaptive UI retention
- **Business & Financial** (4 slides): Unit economics, acquisition funnel, 18-month P&L scenarios, revenue stream diversification
- **Team & Execution** (1 slide): Hiring roadmap and cost-efficient talent strategy

---

*Companion code to: Teikari, P. (2026). Music Attribution with Transparent Confidence. [SSRN No. 6109087](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087).*
