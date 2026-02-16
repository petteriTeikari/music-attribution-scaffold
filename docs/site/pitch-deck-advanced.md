# Advanced Due Diligence Slides — Music Attribution Scaffold

> 18 deep-dive slides for investors, technical due diligence teams, and collective management organization (CMO) partners who want to verify technical capability, competitive positioning, unit economics, and financial viability beyond the [core pitch deck](pitch-deck.md).
>
> **Audience**: Technical due diligence teams, music tech investors, potential CMO partners, music industry analysts.
> Figure plans in [`docs/figures/repo-figures/figure-plans/`](https://github.com/petteriTeikari/music-attribution-scaffold/tree/main/docs/figures/repo-figures/figure-plans). Images generated with [Nano Banana Pro](https://nanobananapro.com/) (Google Gemini image generation).

---

## Technical Deep-Dive

### XIII. Three-Tier Attribution Architecture

The scaffold's architecture is designed to scale from a single developer running the MVP to enterprise CMO integration without architectural rewrites. Three tiers work in sequence: **(1) ETL data ingestion** pulls from Discogs, MusicBrainz, AcoustID, and file metadata through rate-limited connectors. **(2) Entity resolution** -- the competitive moat -- orchestrates six weighted signals to determine whether two metadata records refer to the same entity. **(3) Confidence-calibrated attribution** outputs A0--A3 assurance levels, calibrated confidence scores, JSON/API responses, and MCP permission queries. The entire system runs on a single PostgreSQL instance -- no microservices, no Kubernetes required at MVP stage.

![Three-tier music attribution architecture diagram — ETL data ingestion from Discogs, MusicBrainz, and file metadata; entity resolution orchestrator with six weighted signals as competitive moat; confidence-calibrated attribution output with A0-A3 assurance levels — scalable from solo developer to enterprise CMO integration](figures/fig-pitch-adv-01-architecture-three-tier.jpg)

*Three-tier attribution architecture: ETL data ingestion from multiple sources, entity resolution orchestrator with six weighted signals as the competitive moat, and confidence-calibrated attribution output with A0--A3 assurance levels -- designed to scale from single-developer MVP to enterprise CMO integration without architectural rewrites.*

---

### XIV. Entity Resolution — Six Weighted Signals

Entity resolution is what separates credible attribution from keyword matching. The scaffold uses a **six-signal weighted cascade**: identifier matching (International Standard Recording Code/International Standard Musical Work Code/International Standard Name Identifier, i.e. ISRC/ISWC/ISNI, weight 1.0), string similarity (0.6), Splink probabilistic linkage using the Fellegi-Sunter model (0.8), embedding similarity via pgvector (0.7), graph connectivity through Apache AGE (0.75), and LLM disambiguation using Claude Haiku 4.5 (0.85). Each signal can override earlier ones in the cascade. Competitors typically use one or two methods; we use all six, producing A0--A3 assurance levels rather than opaque numeric scores. This multi-signal approach is what makes the confidence calibration meaningful -- you cannot have calibrated confidence without first resolving *which entity* you are attributing to.

![Entity resolution cascade for music attribution showing six weighted signals — identifier matching (1.0), string similarity (0.6), Splink probabilistic linkage (0.8), embedding similarity (0.7), graph connectivity (0.75), LLM disambiguation (0.85) — competitive moat through multi-signal music metadata matching](figures/fig-pitch-adv-02-entity-resolution-moat.jpg)

*Entity resolution cascade: six weighted signals from identifier matching (weight 1.0) through string similarity, Splink probabilistic linkage, embedding similarity, graph connectivity, to LLM disambiguation (0.85) -- competitors use 1--2 methods; we use all six for A0--A3 assurance level determination.*

---

### XV. Conformal Prediction — The Trust Layer

Black-box confidence scores are the norm in music attribution. A competitor might claim "92% confident" -- but what does that number mean? With Adaptive Prediction Sets (APS), the scaffold provides **distribution-free coverage guarantees**: when we say "90% confident," the prediction set actually covers the true answer 90% of the time. This is not a tuning trick -- it is a statistical guarantee from conformal prediction theory (Vovk et al.). The ECE (Expected Calibration Error) reliability diagram visually proves calibration: our predictions land on the diagonal (perfect calibration) while competitors' scores cluster above it (overconfident). This trust layer is what makes EU AI Act compliance native rather than retrofitted, and what enables SLA-grade licensing where a CMO can contractually rely on the stated confidence.

![Conformal prediction calibration diagram for music attribution — Adaptive Prediction Sets (APS) with distribution-free coverage guarantees and ECE reliability diagram comparing calibrated confidence against competitors' overconfident black-box scores — trust layer for EU AI Act compliance and SLA-grade music licensing](figures/fig-pitch-adv-03-conformal-prediction-transparency.jpg)

*Calibrated confidence via Adaptive Prediction Sets (APS) with distribution-free coverage guarantees -- ECE reliability diagram shows our calibration on the diagonal versus competitors' overconfident black-box scores, providing the trust layer for EU AI Act compliance and SLA-grade licensing.*

---

### XVI. Knowledge Graph Backend — Single-Instance Evolution

The knowledge graph strategy avoids the common trap of adopting Neo4j or MongoDB alongside PostgreSQL. Instead, the scaffold evolves a **single PostgreSQL instance** through three phases: MVP (relational tables + pgvector columns for embedding storage), near-term (Apache AGE graph overlay connecting ISRC, ISWC, and ISNI identifier nodes), and future (full music ontology with composition, recording, performance, rights holder, and CMO nodes). Each phase requires zero database migration -- Apache AGE runs *on top of* PostgreSQL, not alongside it. pgvector benchmarks show 471 QPS at 99% recall, well beyond startup-scale requirements. The schema itself -- three normalized tiers (normalized_records, resolved_entities, attribution_records) -- represents defensible IP that competitors would need to reverse-engineer.

![Knowledge graph backend roadmap for music attribution — PostgreSQL with pgvector for MVP, Apache AGE graph overlay for ISRC/ISWC/ISNI identifier ontology, future expansion to full music ontology — single-instance database architecture eliminating migration overhead for scalable music metadata management](figures/fig-pitch-adv-04-knowledge-graph-backend.jpg)

*Knowledge graph backend: PostgreSQL + pgvector + Apache AGE supporting the ISRC/ISWC/ISNI identifier ontology in MVP, expanding to full music ontology (composition, recording, performance, rights holder, CMO) post-MVP -- all on a single database instance without migration overhead.*

---

### XVII. Sub-100ms Attribution Inference

Batch-only attribution systems cannot serve real-time use cases like digital audio workstation (DAW) plugins, streaming platform integrations, or live production workflows. The scaffold's inference pipeline targets **sub-100ms end-to-end**: FastAPI endpoint dispatches to pg_trgm trigram text search (~1ms exact match), pgvector Hierarchical Navigable Small World (HNSW) approximate nearest neighbor (~15ms hybrid search), and Splink probabilistic fallback (~50ms). Most queries resolve at the first or second stage -- Splink is the fallback, not the primary path. Response format is JSON. These latencies are approximate targets, but the architecture is designed so that the common case (exact identifier match) is effectively instant, while the rare case (fuzzy disambiguation) still completes well under the threshold that would block a real-time workflow.

![Sub-100ms music attribution inference pipeline — FastAPI endpoint through pg_trgm exact match (1ms), pgvector hybrid search (15ms), Splink probabilistic fallback (50ms) — real-time attribution API for DAW plugins, streaming platforms, and music production workflow integration](figures/fig-pitch-adv-05-inference-pipeline-latency.jpg)

*Sub-100ms attribution inference: FastAPI dispatches to pg_trgm exact match (1ms), pgvector hybrid search (15ms), and Splink probabilistic fallback (50ms) -- designed for real-time API embedding in DAWs, streaming platforms, and production workflows where batch-only systems cannot compete.*

---

## Competitive & Market Intelligence

### XVIII. Open-Source Neutrality as Competitive Moat

The music attribution market is fragmented across proprietary players, each locked to specific industry partners. Sureel AI (proprietary, black-box, 5 patents, STIM partnership) cannot credibly serve non-STIM CMOs. Vermillio (Sony Music's first AI investment, TraceID) cannot credibly serve Universal or Warner. Musical AI (Fairly Trained certified, Beatoven.ai integration) operates within a specific certification ecosystem. The scaffold occupies the only position in the **open-source + calibrated confidence quadrant** -- enabling simultaneous partnership with all three major labels, any CMO, and any AI platform. This is not accidental: open-source neutrality is a deliberate strategic choice that makes the scaffold the trusted infrastructure layer that proprietary competitors cannot replicate without abandoning their business models.

![Competitive positioning quadrant for music AI attribution market — open-source vs proprietary, black-box vs calibrated confidence — scaffold in unique open+calibrated position while Sureel AI, Musical AI, Vermillio, BMAT, Pex, Audible Magic cluster in proprietary quadrants — competitive moat analysis for music tech investor due diligence](figures/fig-pitch-adv-06-competitor-positioning-moat.jpg)

*Competitive moat through open-source neutrality: Sureel (proprietary, black-box), Musical AI (proprietary, partial transparency), Vermillio (enterprise, high friction), BMAT, and Pex positioned in proprietary quadrants -- scaffold uniquely occupies open-source + calibrated, enabling partnership with all three major labels simultaneously.*

---

### XIX. TAM/SAM/SOM Market Segmentation

The market sizing follows standard venture methodology. **Total Addressable Market (TAM) of $7.4B** encompasses all AI music platforms by 2035 (Goldman Sachs, Grand View Research projections). **Serviceable Addressable Market (SAM) of $300M** narrows to CMOs and indie labels that specifically need attribution infrastructure -- organizations with compliance obligations and metadata quality requirements. **Serviceable Obtainable Market (SOM) of $50M** further narrows to artists and small labels willing to pay for open-source verification tools -- the segment reachable with our distribution strategy and pricing. Revenue model maps cleanly to segments: indie artists enter via the Free tier, small labels convert to Pro ($49/month), and CMOs contract at Enterprise ($499/month). The path to $10M+ annual recurring revenue (ARR) within 5 years requires capturing less than 1% of the SAM -- achievable through the open-source acquisition funnel detailed in slide XXVII.

![TAM/SAM/SOM market pyramid for music AI attribution — total addressable market $7.4B across all AI music platforms by 2035, serviceable market $300M for CMOs and indie labels, obtainable market $50M for artists and small labels — market segmentation for music tech startup investment analysis](figures/fig-pitch-adv-07-market-segmentation-tam.jpg)

*TAM/SAM/SOM pyramid: $7.4B total market (all AI music platforms by 2035), $300M serviceable (CMOs + indie labels needing attribution), $50M obtainable (artists + small labels wanting open-source verification) -- with clear revenue model per segment and path to $10M+ ARR within 5 years.*

---

### XX. EU AI Act — Born-Compliant Advantage

The EU AI Act is the single largest regulatory catalyst for music attribution infrastructure. **July 2025**: GPAI Code of Practice finalized, establishing transparency requirements for generative AI training data. **August 2025**: General Purpose AI transparency obligations take legal effect. **2026**: Text and Data Mining (TDM) enforcement under the Digital Single Market (DSM) Directive creates opt-out compliance requirements. The scaffold is **born compliant** -- A0--A3 assurance levels provide native explainability, and conformal prediction satisfies confidence scoring requirements without retrofitting. Competitors face an estimated 18--24 month retrofit cycle. The regulation-driven purchasing opportunity is estimated at $500M+ across the compliance window, creating a defensible first-mover advantage that rewards early infrastructure investment over late scrambling.

![EU AI Act compliance timeline for music attribution — born-compliant advantage with A0-A3 assurance levels and conformal prediction vs competitors retrofitting — GPAI obligations August 2025, Code of Practice July 2025, TDM enforcement 2026 — regulatory tailwind analysis for music AI startup due diligence](figures/fig-pitch-adv-08-regulatory-tailwinds-eu-ai-act.jpg)

*EU AI Act as unfair advantage: GPAI obligations (Aug 2025) and TDM enforcement (2026) require explainability and confidence scoring -- A0--A3 assurance levels and conformal prediction provide native compliance while competitors scramble to retrofit, creating an estimated 18--24 month defensible window in $500M+ regulation-driven purchasing.*

---

### XXI. Partnership Ecosystem — Three Concentric Rings

The partnership strategy organizes stakeholders into three revenue-generating rings around the scaffold as neutral hub. **Ring 1 (API consumers)**: DAWs, streaming platforms, and AI music generators integrate via REST API and pay per-query licensing ($0.01--0.10/query). **Ring 2 (Rights holders)**: CMOs (STIM, PRS, SACEM), labels, and independent artists subscribe to SaaS tiers ($49--$499/month) for attribution verification and compliance reporting. **Ring 3 (Infrastructure partners)**: MCP servers, knowledge graph providers, and voice agent platforms engage through data licensing ($100K+/year annual contracts). Open ecosystem positioning -- no lock-in, no exclusivity requirements -- reduces partner churn and creates revenue streams from all three rings. This "neutral hub" architecture is why the scaffold can serve as the industry's shared attribution layer rather than competing with its own partners.

![Three-ring partnership ecosystem for music attribution — inner ring API consumers (DAWs, streaming platforms), middle ring rights holders (CMOs, labels, artists), outer ring infrastructure partners (MCP servers, knowledge graphs) — open ecosystem strategy for music AI platform neutral positioning](figures/fig-pitch-adv-09-partnership-ecosystem-map.jpg)

*Strategic partnership ecosystem: Ring 1 -- API consumers (DAWs, streaming platforms), Ring 2 -- rights holders (CMOs, labels, artists), Ring 3 -- infrastructure partners (MCP servers, knowledge graphs, voice agents). Open ecosystem reduces churn and creates revenue from all three rings.*

---

## Product & UX

### XXII. Premium UX — 75% Faster Attribution Review

Music attribution is inherently tedious -- reviewing metadata, correcting credits, confirming rights. The scaffold's batch review queue transforms this from a one-at-a-time chore into an efficient editorial workflow. AI-generated diffs show before/after for each attribution suggestion. "Approve All" enables bulk acceptance of high-confidence matches. A progress counter (e.g., "23/47 reviewed") shows momentum and keeps reviewers engaged. Smart sorting surfaces low-confidence items first, where human judgment adds the most value. Estimated speed improvement: **75% faster** than traditional one-at-a-time entry forms. "Premium UX first" is deliberately uncommon in music tech tools -- most competitors build for engineers, not for the artists and label administrators who actually use the product daily. This UX quality justifies premium pricing.

![Before/after UX comparison for music attribution — traditional one-at-a-time entry form vs AI-assisted batch review queue with diff highlighting, Approve All button, progress counter, and smart sorting — premium UX design reducing attribution review time by estimated 75% for music rights management](figures/fig-pitch-adv-10-review-queue-ux-efficiency.jpg)

*Premium UX: traditional attribution entry form vs. AI-assisted batch review queue with diff highlighting, Approve All for bulk acceptance, progress counter, and smart sorting -- estimated 75% faster manual review, justifying premium tier pricing through UX quality uncommon in music tech.*

---

### XXIII. Enterprise Accessibility — WCAG 2.1 AA from Day One

Accessibility is not an afterthought bolted on before an enterprise sale -- it is built into the design system from day one. The scaffold meets **Web Content Accessibility Guidelines (WCAG) 2.1 AA** with: 4.5:1 color contrast for normal text and 3:1 for large text, full keyboard navigation with visible high-contrast focus rings, Accessible Rich Internet Applications (ARIA) roles on custom components (ConfidenceGauge uses `role="meter"`, toggles use `role="radio"`), 44x44px minimum touch targets, and two-layer automated testing -- vitest-axe at the component level (runs every test suite) and Playwright with axe-core at the browser level (runs in E2E suite). This positions the scaffold for **EU EN 301 549** directive compliance, which is increasingly a hard requirement for enterprise procurement in European markets. For CMOs, accessibility compliance is not optional -- it is a checkbox on the procurement form.

![Enterprise accessibility architecture for music attribution platform — WCAG 2.1 AA compliance with 4.5:1 color contrast, keyboard navigation, ARIA roles, 44x44px touch targets, two-layer testing via vitest-axe and Playwright axe-core — EU EN 301 549 compliance as competitive differentiator for music tech enterprise sales](figures/fig-pitch-adv-11-accessibility-wcag-2-1-aa.jpg)

*WCAG 2.1 AA from day one: 4.5:1 color contrast, full keyboard navigation, ARIA roles on custom components, 44x44px touch targets, and two-layer testing (vitest-axe + Playwright axe-core) -- EU EN 301 549 compliance positions accessibility as enterprise sales differentiator.*

---

### XXIV. Voice Agent — Premium Upsell with Infrastructure Moat

Voice is not core to the attribution engine -- it is a **premium upsell** that creates a natural moat. In the MVP, voice is aspirational only: a mic animation, example queries ("What are Imogen Heap's co-writers?", "Suggest missing credits"), and an "Upgrade to Pro" banner. Full implementation launches at M9+ using Pipecat infrastructure. The pricing story: Free tier has no voice ($0/month), Pro tier includes voice at **$49/month** -- a 3x premium that is justified by the conversational convenience and batch review capabilities voice enables. Infrastructure economics: Pipecat at $0.02/conversation vs. Vapi at $0.12/conversation delivers **6x cost savings**. Revenue projection milestones: M9 (launch), M12 (100 users), M18 (meaningful ARR contribution). The defensibility argument: open-source forks can replicate the text-based attribution engine, but cannot offer hosted voice without incurring the same speech-to-text (STT), LLM, and text-to-speech (TTS) infrastructure costs.

![Voice agent premium upsell for music attribution — mic UI mockup with example queries, Free to Pro pricing tiers at $49/month, Pipecat infrastructure at $0.02/conversation vs Vapi $0.12 delivering 6x cost savings — voice as premium Pro tier feature with infrastructure moat against open-source forks](figures/fig-pitch-adv-12-voice-agent-premium-upsell.jpg)

*Voice agent as Pro tier upsell: aspirational UI in MVP (mic animation, example queries), full Pipecat implementation at M9+ with 6x cost savings over Vapi ($0.02 vs $0.12/conversation), driving 3x pricing premium at $49/month -- voice infrastructure costs create a natural moat against open-source forks.*

---

### XXV. Adaptive UI — Retention Flywheel

User retention in SaaS tools depends on progressive complexity -- beginners need simplicity, power users need full control, and the transition between the two determines whether users churn or upgrade. The scaffold implements a **per-user proficiency model** using Jotai state management and localStorage persistence. Three stages: Beginner (simplified UI, guided tooltips, curated workflows), Intermediate (more controls visible, fewer prompts), and Advanced (full dashboard, keyboard shortcuts, batch operations). PostHog analytics track engagement patterns to inform A/B testing and feature prioritization. This creates a **data-driven personalization loop**: the more a user engages, the more the UI adapts to their skill level, reducing friction at every stage. The proficiency model is entirely client-side (no ML training, no backend dependency), making it lightweight and privacy-respecting.

![Adaptive UI retention flywheel for music attribution platform — per-user proficiency model using Jotai state and localStorage, progressive feature disclosure from beginner to advanced mode, PostHog analytics tracking engagement — data-driven personalization for music tech SaaS user retention](figures/fig-pitch-adv-13-artist-mode-adaptive-ui.jpg)

*Adaptive UI retention flywheel: per-user proficiency model (Jotai + localStorage) progressively reveals features from beginner through advanced mode -- PostHog analytics track engagement to inform A/B testing, creating a data-driven personalization loop that reduces churn.*

---

## Business & Financial

### XXVI. Unit Economics by Customer Segment

The open-core model produces strong unit economics across all three segments. **Indie artists**: $0--500 average revenue per user (ARPU) through the freemium funnel, low customer acquisition cost (CAC), lifetime value to CAC (LTV:CAC) ratio viable because the Free tier feeds the Pro conversion pipeline. **Small labels**: $500--2,000 ARPU on the Pro tier ($49/month), medium CAC, LTV:CAC above 5x. **CMOs**: $5,000+ ARPU on Enterprise ($499/month), higher CAC but LTV:CAC above 10x due to multi-year contracts and low churn. Gross margins target **85%+** across all segments -- significantly above the 70--80% typical for SaaS and the 50--70% typical for music tech companies. CAC payback targets under 12 months. Open-source distribution is estimated to reduce CAC by approximately 60% versus proprietary SaaS competitors, because community-driven awareness replaces paid acquisition spend.

![Unit economics by customer segment for music attribution SaaS — indie artists $0-500 ARPU, small labels $500-2K ARPU on Pro tier, CMOs $5K+ ARPU on Enterprise — 85%+ gross margins, CAC payback under 12 months, open-source CAC reduction of 60% — music AI startup financial analysis for investor due diligence](figures/fig-pitch-adv-14-unit-economics-arpu.jpg)

*Unit economics: indie artists at $0--500 ARPU (freemium), small labels at $500--2,000 (Pro tier), CMOs at $5,000+ (Enterprise SLA) -- 85%+ gross margins, CAC payback under 12 months, with open-source distribution reducing customer acquisition costs by an estimated 60% versus proprietary competitors.*

---

### XXVII. Customer Acquisition Funnel — Open-Source Distribution

Open-source is not just a licensing choice -- it is the primary distribution channel. The acquisition funnel targets: **1,000 GitHub stars** (18-month target), driving **500 free tier signups** (50% conversion from awareness to trial), yielding **50 paid conversions** (10% free-to-paid, consistent with developer tool benchmarks), producing **5 CMO pilot programs** (10% of paid customers qualifying for enterprise evaluation), and closing **1 enterprise contract** (20% pilot-to-contract conversion). This funnel operates over the full 18-month period, not monthly. The key insight: open-source community distribution replaces expensive enterprise sales motions. CAC comparison shows open-source funnel at significantly lower cost than traditional SaaS marketing or enterprise direct sales. The 10% free-to-paid conversion rate is benchmarked against comparable open-core developer tools.

![Open-source customer acquisition funnel for music attribution — GitHub stars to free tier to paid conversion to CMO pilots to enterprise contracts — CAC reduction through community-driven distribution vs proprietary SaaS and enterprise sales — music AI startup growth strategy for investor analysis](figures/fig-pitch-adv-15-customer-acquisition-funnel.jpg)

*Open-source acquisition funnel: 1,000 GitHub stars target driving 500 free signups, 10% paid conversion to 50 Pro customers, 5 CMO pilots, and 1 enterprise contract -- open-source distribution reduces CAC by an estimated 60% versus proprietary SaaS competitors.*

---

### XXVIII. 18-Month Profit & Loss (P&L) — Three Scenarios

All three scenarios use the Helsinki + Warsaw cost base. **Conservative** (2 engineers, slow adoption): break-even at M20, requiring patience but minimal burn. **Base** (4 engineers, CMO pilot conversions): profitable by M16, the target scenario assuming the STIM pilot succeeds and 2--3 additional CMOs follow. **Upside** (4 engineers + enterprise deals): profitable by M14, triggered by a major label or large CMO signing an enterprise contract earlier than expected. Key numbers: Helsinki + Warsaw 18-month cost of approximately **$809K** versus San Francisco at **$2.3M** -- a 65% lower burn rate while maintaining equivalent engineering output. The message is **capital efficiency**, not rapid growth at all costs. Monte Carlo analysis gives P50 runway of 19 months on $1M funding, with revenue extending runway in the base and upside cases.

![18-month P&L scenarios for music attribution startup — conservative (2 engineers, break-even M20), base (4 engineers, profitable M16), upside (4 engineers + enterprise, profitable M14) — Helsinki+Warsaw cost base at $809K vs San Francisco $2.3M — capital-efficient financial projections for music AI investment](figures/fig-pitch-adv-16-18-month-financial-projections.jpg)

*18-month P&L in three scenarios: Conservative (2 engineers, break-even M20), Base (4 engineers, profitable M16), Upside (4+ engineers + enterprise, profitable M14) -- Helsinki + Warsaw delivers 65% lower burn than San Francisco with equivalent engineering output.*

---

### XXIX. Four Revenue Streams — Diversified Risk

Revenue diversification protects against single-stream dependency. **Stream 1 -- API licensing**: $0.01--0.10 per attribution query, targeting developers and integrators via REST API with rate tiers and SDK. **Stream 2 -- Enterprise SaaS**: $5K--50K monthly recurring revenue (MRR) per CMO, with service-level agreement (SLA), compliance reports, white-label options, and custom integrations. **Stream 3 -- Pro tier + voice**: $49/month per artist or small label, including voice agent queries, batch review queue, and advanced analytics. **Stream 4 -- Data licensing**: $100K+ annual contracts with large CMOs and regulators for attribution data feeds, compliance reports, and Fairly Trained certification pathway data. Projected M18 revenue mix: API (25%), Enterprise (35%), Pro + Voice (20%), Data Licensing (20%). Design principle: **no single stream exceeds 40% of revenue**, ensuring resilience.

![Four diversified revenue streams for music attribution platform — API licensing at $0.01-0.10 per query, Enterprise SaaS at $5K-50K MRR, Pro tier with voice at $49/month, Data licensing to CMOs at $100K+ annual — revenue diversification strategy for music AI startup showing projected M18 mix](figures/fig-pitch-adv-17-partnership-revenue-streams.jpg)

*Four revenue streams: API licensing ($0.01--0.10/query), Enterprise SaaS ($5K--50K MRR), Pro + Voice ($49/month), Data licensing ($100K+/year) -- projected M18 mix of 25/35/20/20%, with no single stream exceeding 40% of revenue.*

---

## Team & Execution

### XXX. Team Build-Out — Helsinki + Warsaw Cost Advantage

The hiring roadmap phases four specialized roles across the first eight months. **M0**: CTO/founder (full-stack lead, already in place). **M1**: UX/UI engineer -- first external hire, focused on the agentic interface, CopilotKit/AG-UI sidebar, and adaptive UI proficiency model. **M2**: Cloud/infrastructure engineer -- Pulumi Infrastructure as Code (IaC), k3s/Docker orchestration, CI/CD hardening, PostgreSQL + pgvector + Apache AGE operations, and observability (OpenTelemetry, Grafana). **M3**: LLM/ML engineer -- music ontology, multi-agent orchestration (PydanticAI, LangGraph), entity resolution (Splink, pgmpy), and MCP tool development. **M8**: Voice agent engineer (optional) -- sub-400ms Pipecat pipeline, STT/TTS integration, persona drift monitoring. If budget requires it, R3 and R4 merge into a single role. Helsinki salaries at 60--70% of San Francisco equivalents, total 18-month cost: **$809K** (Helsinki + Warsaw) versus **$2.3M** (San Francisco). Recruitment pipeline: Aalto University (Helsinki) and Warsaw tech ecosystem. Hiring philosophy: "Hire for scarcity, not commodities" -- LLM and voice engineering skills, not generic web development.

![Team build-out Gantt chart for music AI startup — CTO M0, UX/UI engineer M1, cloud engineer M2, LLM engineer M3, voice engineer M8 — Helsinki base salaries at 60-70% of San Francisco with Aalto University and Warsaw recruitment pipeline — 18-month hiring roadmap for music attribution venture](figures/fig-pitch-adv-18-18-month-hiring-roadmap.jpg)

*Team build-out: CTO/founder from M0, four phased hires (UX/UI M1, Cloud M2, LLM/ML M3, Voice M8) -- Helsinki salaries at 60--70% of SF equivalents, total 18-month cost $809K vs $2.3M, recruiting from Aalto University and Warsaw tech ecosystem. "Hire for scarcity, not commodities."*

---

## Back to Core Deck

Return to the **[Core Pitch Deck](pitch-deck.md)** (12 slides) for the executive summary.

---

*Companion code to: Teikari, P. (2026). Music Attribution with Transparent Confidence. [SSRN No. 6109087](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087).*
