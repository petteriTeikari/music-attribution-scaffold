# Investor Pitch Deck — Music Attribution Scaffold

> 12 slides presenting the Music Attribution Scaffold as an investable open-source platform for AI music attribution -- from market opportunity and technical architecture through competitive moat and partnership strategy.
>
> **Audience**: Music industry executives, investors, CMO leadership, potential collaborators.
> Figures generated with [Nano Banana Pro](https://nanobananapro.com/) (Google Gemini image generation). Figure plans in [`docs/figures/repo-figures/figure-plans/`](https://github.com/petteriTeikari/music-attribution-scaffold/tree/main/docs/figures/repo-figures/figure-plans).

---

## I. Market Opportunity — $7.4B by 2035

The generative music market is the fastest-growing segment in the broader music industry, projected to expand from **$558M in 2024 to $7.4B by 2035** at a 26.5% compound annual growth rate (CAGR) (Goldman Sachs, Grand View Research). Every AI-generated track requires provenance metadata -- who trained the model, which samples were used, and what rights apply. Attribution infrastructure is the "picks-and-shovels" play in this expansion, serving AI music platforms, collective management organizations (CMOs), and independent artists alike.

![Infographic showing generative music market growth from $558M in 2024 to $7.4B by 2035 at 26.5% CAGR, with attribution infrastructure TAM breakdown across AI music platforms, CMO compliance tools, and artist verification — music AI market sizing for investor due diligence](figures/fig-pitch-01-market-opportunity.jpg)

*Generative music market growing from $558M (2024) to $7.4B (2035) at 26.5% CAGR, with the attribution infrastructure total addressable market (TAM) broken out across AI music platforms, CMO compliance tools, and independent artist verification.*

---

## II. Competitive Positioning — The Only Open + Calibrated System

Over $300M in equity funding has flowed into music AI attribution companies -- Suno ($250M), ProRata.ai ($40M), Vermillio ($16M, Sony Music's first AI investment), Musical AI ($6M, Fairly Trained certified). Yet no competitor offers both **open-source transparency** and **calibrated confidence scoring**. Sureel AI uses proprietary gradient tracking; Musical AI uses proprietary influence functions; BMAT and Pex focus on content identification. The scaffold uniquely occupies the open-source + calibrated quadrant, enabled by conformal prediction with distribution-free coverage guarantees.

![Competitive positioning quadrant for music AI attribution startups — open-source vs proprietary on x-axis, black-box vs calibrated confidence on y-axis — scaffold uniquely positioned in open+calibrated quadrant while Sureel, Musical AI, Vermillio, BMAT, Pex cluster in proprietary positions](figures/fig-pitch-02-competitive-positioning.jpg)

*Competitive landscape on two axes: open-source vs. proprietary and black-box vs. calibrated confidence. Sureel, Musical AI, Vermillio, BMAT, Pex, Auracles, and Orfium mapped -- with the attribution scaffold uniquely positioned as the only open-source system with calibrated confidence scoring via conformal prediction.*

---

## III. Technical Architecture — Unified PostgreSQL Stack

The scaffold runs five pipelines -- ETL ingestion, entity resolution, attribution scoring, REST API/MCP server, and agentic chat -- on a **single PostgreSQL 17 instance** handling relational data, pgvector embeddings, and Apache AGE graph queries. This eliminates the multi-database operational overhead that plagues competitors using separate systems for relational, vector, and graph workloads. The frontend is Next.js 15 (App Router) with a PydanticAI agent communicating via the AG-UI protocol.

![Five-pipeline music attribution architecture diagram — ETL, entity resolution, attribution engine, API/MCP server, and agentic chat — unified on single PostgreSQL 17 instance with pgvector embeddings and Apache AGE graph queries for scalable music metadata processing](figures/fig-pitch-03-architecture.jpg)

*Five-pipeline architecture unified on a single PostgreSQL 17 instance with relational tables, pgvector embeddings, and Apache AGE graph queries, eliminating multi-database operational overhead while powering ETL, entity resolution, attribution scoring, API/MCP, and agentic chat.*

---

## IV. Assurance Levels (A0--A3) — Tiered Provenance Trust

Attribution trust is not binary. The scaffold defines four **assurance levels** that map directly to music industry identifier standards (ISRC for recordings, ISWC for compositions, ISNI for creators). A0 (Unknown) means no provenance data -- like a blank page. A1 (Claimed) is single-source, self-reported metadata -- like a resume. A2 (Corroborated) requires multiple independent sources agreeing (MusicBrainz + Discogs + AcoustID) -- like a background check. A3 (Verified) means the artist has directly confirmed the attribution -- like a notarized deed. This graduated framework gives CMOs and regulators the granularity they need for compliance decisions.

![Four-tier provenance framework for music attribution — A0 Unknown through A1 Claimed, A2 Corroborated, to A3 Artist-Verified — mapping to ISRC, ISWC, and ISNI registry standards for transparent confidence scoring in music rights management](figures/fig-pitch-04-assurance-levels.jpg)

*Four assurance levels ascending from A0 (Unknown) through A1 (Claimed -- single source), A2 (Corroborated -- MusicBrainz + Discogs + AcoustID agree), to A3 (Artist-Verified -- identity-confirmed provenance), mapping directly to ISRC, ISWC, and ISNI registry standards.*

---

## V. Team & Hiring Plan — 4 Specialized Roles

The team grows from solo CTO/founder to five people over eight months, with each hire timed to the roadmap phase that requires their expertise. UX/UI engineer at M1 (agentic interface craft), cloud/infrastructure engineer at M2 (Pulumi IaC, Kubernetes), LLM/ML engineer at M3 (entity resolution, knowledge graphs), and an optional voice agent engineer at M8 (Pipecat audio pipeline). If budget is tight, R3 and R4 can merge into a single generalist role. Recruiting targets Aalto University (Helsinki) and the Warsaw tech ecosystem for specialized AI/ML talent at 60--70% of San Francisco salary equivalents.

![Gantt chart showing phased hiring plan for music AI startup — CTO at M0, UX/UI engineer M1, cloud engineer M2, LLM engineer M3, voice engineer M8 — growing from solo founder to 5-person team with Helsinki and Warsaw talent pipeline](figures/fig-pitch-05-team-hiring.jpg)

*Phased hiring plan: CTO/founder from M0, UX/UI engineer at M1, cloud/infrastructure engineer at M2, LLM/ML engineer at M3, and optional voice agent engineer at M8 -- growing from solo founder to 5-person team, each hire timed to the roadmap phase that needs them.*

---

## VI. Milestone Roadmap — Foundation, Scale, Ecosystem

Three phases with **go/no-go gates** at each boundary. Phase 1 (Foundation, M0--M6): production-ready attribution API, agentic UI, MCP server, and MVP demo -- culminating in a STIM (Swedish CMO) pilot observer engagement. Phase 2 (Scale, M6--M12): first paying customers, Pro tier launch with voice agent beta, 3 data source integrations, and EU AI Act compliance documentation. Phase 3 (Ecosystem, M12--M18): CMO pilot integration, voice agent production, 10+ data sources, partnership network, and Series A readiness materials. Each gate is tied to specific KPIs -- not time alone.

![Three-phase 18-month product roadmap for music attribution platform — Foundation M0-M6 with MVP demo gate, Scale M6-M12 with first revenue gate, Ecosystem M12-M18 with Series A readiness gate — milestone-driven startup execution plan](figures/fig-pitch-06-milestone-roadmap.jpg)

*Three-phase 18-month roadmap: Foundation (M0--M6, MVP demo), Scale (M6--M12, first revenue + Pro tier), Ecosystem (M12--M18, Series A readiness), with go/no-go gates at each phase boundary tied to specific KPIs.*

---

## VII. Financial Scenarios — 65% Lower Burn Than SF

Capital efficiency is the key message. Three geographic hiring scenarios compared over 18 months: **Helsinki + Warsaw at $809K** (recommended), London + Helsinki at $1.4M, and San Francisco at $2.3M. The Nordic + CEE cost base delivers equivalent engineering output at roughly 2.8x advantage. People costs account for 65--75% of total burn, with infrastructure (Hetzner EU data centers) at 15--20% and operations at 10--15%. Monte Carlo sensitivity analysis shows P50 runway of 19 months on $1M funding -- comfortable path to Series A with revenue extending runway.

![Stacked bar chart comparing 18-month startup costs across three geographies — Helsinki+Warsaw $809K vs London+Helsinki $1.4M vs San Francisco $2.3M — demonstrating Nordic and CEE talent cost advantage for music AI venture capital efficiency](figures/fig-pitch-07-financial-scenarios.jpg)

*18-month total cost comparison: Helsinki + Warsaw at $809K, London + Helsinki at $1.4M, San Francisco at $2.3M -- Nordic + CEE talent delivers equivalent engineering capability at 65% lower burn rate.*

---

## VIII. Revenue Model — Open-Core with Three Tiers

An open-core model captures value at every market segment. **Free tier** ($0): researchers and the open-source community get core attribution with rate-limited API access and an agent sidebar. **Pro tier** ($49/month): independent artists and small labels get voice agent queries, batch review queue, priority support, and advanced analytics. **Enterprise tier** ($499/month): CMOs and distributors get service-level agreement (SLA)-backed support, custom integrations, compliance reports, and white-label options. Target: first revenue at M10--M12, 30--80 Pro users and 3--5 enterprise clients by M18, with projected annual recurring revenue (ARR) of $50K--$150K validating the model.

![Three-tier open-core revenue model for music attribution SaaS — Free for researchers, Pro at $49/month for artists with voice agent, Enterprise at $499/month for CMOs with SLA and compliance — pricing strategy for music AI startup monetization](figures/fig-pitch-08-revenue-model.jpg)

*Three-tier open-core pricing: Free (researchers, rate-limited API), Pro at $49/month (artists, voice + batch review), Enterprise at $499/month (CMOs, SLA + compliance + white-label), with first revenue at M10--M12 scaling to 3--5 enterprise clients by M18.*

---

## IX. Competitive Moat — Six Reinforcing Advantages

Six advantages that compound into a defensible moat. **(1) Open-source trust**: full auditability builds confidence with CMOs and regulators who distrust black boxes. **(2) Calibrated confidence**: conformal prediction with distribution-free coverage guarantees -- not marketing confidence scores. **(3) MCP-native**: Model Context Protocol consent queries for machine-readable AI training permissions. **(4) Neutral positioning**: not owned by any platform, label, or CMO -- enabling partnership with all three major labels simultaneously. **(5) Probabilistic PRD**: branching-path architecture supporting multiple deployment scenarios. **(6) EU AI Act compliance**: born-compliant with A0--A3 assurance levels. No single competitor has more than two of these advantages.

![Hexagonal radar diagram showing six competitive moat advantages for music attribution — open-source trust, calibrated confidence via conformal prediction, MCP-native consent, neutral platform positioning, probabilistic PRD architecture, EU AI Act compliance — defensibility analysis for music AI investment](figures/fig-pitch-09-moat-defensibility.jpg)

*Six reinforcing competitive advantages: open-source trust (auditability), calibrated confidence (conformal prediction), MCP-native consent queries, neutral positioning, probabilistic PRD architecture, and EU AI Act compliance -- no single competitor has more than two.*

---

## X. Voice Agent Pipeline — Sub-400ms, 6x Cost Savings

Voice is the premium upsell that creates infrastructure-level defensibility. The attribution voice agent pipeline flows from user speech through speech-to-text (STT), LLM (Claude Haiku 4.5 via PydanticAI), attribution tool calls, and text-to-speech (TTS) in **under 400ms end-to-end**. Pipecat delivers **6x cost savings** at $0.02 per conversation versus Vapi at $0.12/conversation. In the MVP, voice is aspirational only (mic animation, example queries, "Upgrade to Pro" banner). Full implementation launches at M9+ with Pipecat infrastructure. Open-source forks cannot replicate the hosted voice service without incurring the same infrastructure costs -- a natural moat.

![Voice attribution pipeline architecture — user speech through STT, Claude Haiku 4.5 LLM, PydanticAI attribution tools, and TTS in under 400ms — Pipecat infrastructure at $0.02 per conversation vs Vapi $0.12, music AI voice agent for premium Pro tier upsell](figures/fig-pitch-10-voice-agent.jpg)

*Voice attribution pipeline: STT, LLM (Haiku 4.5), attribution tool calls, and TTS in under 400ms end-to-end. Pipecat at $0.02/conversation (6x cheaper than Vapi at $0.12) as a premium Pro tier feature.*

---

## XI. Regulatory Tailwind — EU AI Act as Unfair Advantage

The EU AI Act transforms attribution from nice-to-have to mandatory. **July 2025**: Code of Practice for General Purpose AI (GPAI) finalized. **August 2025**: GPAI transparency obligations take effect. **2026**: Text and Data Mining (TDM) enforcement under the Digital Single Market (DSM) Directive. Each compliance deadline is a customer acquisition accelerator. The scaffold is **born compliant** -- A0--A3 assurance levels and conformal prediction provide native explainability and confidence scoring, while competitors scramble to retrofit proprietary systems. The STIM (Swedish CMO) pilot positions us as the reference implementation for Nordic regulatory compliance. Estimated $500M+ in regulation-driven purchasing over 18--24 months creates a defensible first-mover window.

![EU AI Act regulatory timeline showing compliance deadlines driving mandatory demand for music attribution infrastructure — GPAI obligations August 2025, Code of Practice July 2025, TDM enforcement 2026 — born-compliant advantage for music AI startup regulatory strategy](figures/fig-pitch-11-regulatory-tailwind.jpg)

*EU AI Act timeline: Code of Practice (Jul 2025), GPAI obligations (Aug 2025), TDM enforcement (2026), and STIM pilot creating escalating mandatory demand for attribution infrastructure -- each deadline accelerates customer acquisition.*

---

## XII. Partnership Strategy — The Neutral Hub

The scaffold is positioned as the **"Switzerland of music attribution"** -- trusted by all parties because it is not owned by any single one. Five stakeholder categories connect bidirectionally through the hub: CMOs (STIM, PRS, SACEM) send licenses and claims, receive confidence reports. Platforms (Spotify, YouTube, AI music generators) send usage data and training rights, receive attribution records. Registries (ISRC, ISWC, ISNI, Digital Data Exchange/DDEX) provide identifiers and metadata. Certifiers (Fairly Trained, Coalition for Content Provenance and Authenticity/C2PA) provide compliance status. Attribution providers (Pex, BMAT, Audible Magic) contribute confidence scores. Open-source neutrality is what enables simultaneous partnership with Universal, Sony, and Warner -- something no proprietary competitor can achieve.

![Hub-and-spoke partnership architecture for music attribution — scaffold as neutral center connecting CMOs (STIM, PRS, SACEM), platforms (Spotify, YouTube), attribution providers (Pex, BMAT), registries (ISRC, ISWC, ISNI, DDEX), and certifiers (Fairly Trained, C2PA) with bidirectional data flows](figures/fig-pitch-12-partnership-strategy.jpg)

*Hub-and-spoke partnership architecture: the scaffold as neutral center connecting CMOs (STIM, PRS, SACEM), platforms, attribution providers (Pex, BMAT, Audible Magic), registries (ISRC, ISWC, ISNI, DDEX), and certifiers (Fairly Trained, C2PA) with bidirectional data flows.*

---

## Next: Advanced Due Diligence Slides

For investors and collaborators seeking deeper technical and financial detail, see the **[Advanced Pitch Deck](pitch-deck-advanced.md)** -- 18 additional slides covering:

- **Technical Deep-Dive** (5 slides): Three-tier architecture scaling, entity resolution with six weighted signals, conformal prediction calibration, knowledge graph backend roadmap, sub-100ms inference pipeline
- **Competitive & Market Intelligence** (4 slides): Open-source neutrality moat, TAM/SAM/SOM segmentation ($7.4B / $300M / $50M), EU AI Act born-compliant advantage, three-ring partnership ecosystem
- **Product & UX** (4 slides): 75% faster review queue, WCAG 2.1 AA enterprise accessibility, voice agent premium upsell, adaptive UI retention flywheel
- **Business & Financial** (4 slides): Unit economics by segment (85%+ gross margins), open-source acquisition funnel (60% lower customer acquisition cost), 18-month P&L scenarios, four diversified revenue streams
- **Team & Execution** (1 slide): Phased hiring roadmap with Helsinki + Warsaw cost advantage

---

*Companion code to: Teikari, P. (2026). Music Attribution with Transparent Confidence. [SSRN No. 6109087](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087).*
