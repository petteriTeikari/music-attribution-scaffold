# Advanced Due Diligence Slides

> 18 deep-dive slides for investors and collaborators who want to verify technical capability, competitive positioning, and financial viability beyond the [core pitch deck](pitch-deck.md).
>
> **Audience**: Technical due diligence teams, music tech investors, potential CMO partners.
> Figure plans in [`docs/figures/repo-figures/figure-plans/`](https://github.com/petteriTeikari/music-attribution-scaffold/tree/main/docs/figures/repo-figures/figure-plans). Images will be generated with [Nano Banana Pro](https://nanobananapro.com/).

---

## Technical Deep-Dive

### XIII. Three-Tier Attribution Architecture

![Three-tier attribution architecture: ETL data ingestion, entity resolution orchestrator, and confidence-calibrated attribution output scaling to enterprise](figures/fig-pitch-adv-01-architecture-three-tier.jpg)

*Three-tier attribution architecture -- ETL ingestion from Discogs, MusicBrainz, and file metadata; entity resolution orchestrator with six weighted signals; and confidence-calibrated attribution output -- designed to scale from single-developer MVP to enterprise CMO integration without architectural rewrites.*

---

### XIV. Entity Resolution: Six Weighted Signals

![Entity resolution cascade: six weighted signals from identifiers through string similarity, Splink, embeddings, graph, and LLM disambiguation](figures/fig-pitch-adv-02-entity-resolution-moat.jpg)

*Entity resolution as the confidence foundation -- a six-signal weighted cascade from identifier matching (ISRC/ISWC/ISNI, weight 1.0), through string similarity (0.6), Splink probabilistic linkage (0.8), embedding similarity (0.7), graph connectivity (0.75), to LLM disambiguation (0.85) -- each signal contributing to A0--A3 assurance levels. Competitors use 1--2 methods; we use six.*

---

### XV. Conformal Prediction: The Trust Layer

![Conformal prediction: APS method and ECE reliability diagram showing calibrated confidence vs competitors' black-box scores](figures/fig-pitch-adv-03-conformal-prediction-transparency.jpg)

*Calibrated confidence via Adaptive Prediction Sets (APS) with distribution-free coverage guarantees -- when we say "90% confident," it means 90% coverage, not overconfident marketing. ECE reliability diagram contrasts our calibration against competitors' black-box confidence scores. This is the technical basis for EU AI Act compliance and SLA-grade licensing.*

---

### XVI. Knowledge Graph Backend

![PostgreSQL + pgvector + Apache AGE supporting ISRC/ISWC/ISNI ontology with future music ontology expansion](figures/fig-pitch-adv-04-knowledge-graph-backend.jpg)

*Knowledge graph backend roadmap: PostgreSQL + pgvector + Apache AGE supporting the ISRC/ISWC/ISNI identifier ontology in MVP, expanding to full music ontology nodes (composition, recording, performance, rights holder, CMO) post-MVP -- defensible IP in graph schema and embedding strategies.*

---

### XVII. Sub-100ms Attribution Inference

![Request flow: FastAPI endpoint to pg_trgm exact match to pgvector hybrid search to Splink fallback with latency annotations](figures/fig-pitch-adv-05-inference-pipeline-latency.jpg)

*Sub-100ms attribution inference pipeline: FastAPI endpoint dispatches to pg_trgm exact match (1ms), pgvector hybrid search (15ms), and Splink probabilistic fallback (50ms) -- designed for real-time API embedding in DAWs, streaming platforms, and production workflows where batch-only systems cannot compete.*

---

## Competitive & Market Intelligence

### XVIII. Open-Source Neutrality Moat

![Quadrant chart: open-source vs proprietary, black-box vs calibrated -- competitors positioned with scaffold in open+calibrated quadrant](figures/fig-pitch-adv-06-competitor-positioning-moat.jpg)

*Competitive moat through open-source neutrality: quadrant positioning (Open-Source vs. Proprietary, Black-Box vs. Calibrated Confidence) maps Sureel (proprietary, black-box), Musical AI (proprietary, partial transparency), and Vermillio (enterprise, high friction) against the scaffold's unique open-source + calibrated position -- enabling partnership with all three major labels simultaneously.*

---

### XIX. TAM/SAM/SOM Segmentation

![Market pyramid: TAM $7.4B all AI music platforms, SAM $300M CMOs and indie labels, SOM $50M artists and small labels](figures/fig-pitch-adv-07-market-segmentation-tam.jpg)

*TAM/SAM/SOM pyramid: TAM of $7.4B (all AI music platforms by 2035), SAM of $300M (CMOs and indie labels needing attribution infrastructure), SOM of $50M (artists and small labels willing to pay for open-source verification) -- with revenue model mapped per segment and a clear path to $10M+ ARR within 5 years.*

---

### XX. EU AI Act as Unfair Advantage

![EU AI Act timeline: born-compliant advantage with A0-A3 and conformal prediction vs competitors scrambling post-hoc](figures/fig-pitch-adv-08-regulatory-tailwinds-eu-ai-act.jpg)

*Regulatory tailwind: EU AI Act (GPAI obligations Aug 2025, TDM enforcement 2026) requires explainability and confidence scoring -- our A0--A3 assurance levels and conformal prediction provide native compliance while competitors scramble to retrofit. Estimated $500M+ in regulation-driven purchasing creates an 18--24 month defensible window.*

---

### XXI. Partnership Ecosystem: Three Rings

![Three concentric rings: API consumers (DAWs, streaming), rights holders (CMOs, labels), infrastructure (MCP, knowledge graphs)](figures/fig-pitch-adv-09-partnership-ecosystem-map.jpg)

*Strategic partnership ecosystem in three concentric rings: Ring 1 -- API consumers (DAWs, streaming platforms), Ring 2 -- rights holders (CMOs, labels, artists), Ring 3 -- infrastructure partners (MCP servers, knowledge graphs, voice agents). Open ecosystem positioning reduces churn and creates revenue streams from all three rings.*

---

## Product & UX

### XXII. Premium UX: 75% Faster Review

![Before/after: traditional attribution form vs batch review queue with AI diffs, Approve All, and progress counter](figures/fig-pitch-adv-10-review-queue-ux-efficiency.jpg)

*Premium UX reduces attribution friction: batch review queue with AI-generated diffs (before/after), "Approve All" for bulk acceptance, progress counter showing momentum, and smart sorting by review priority -- estimated 75% faster than traditional one-at-a-time entry forms. "Premium UX first" is uncommon in music tech and justifies premium pricing.*

---

### XXIII. Enterprise Accessibility: WCAG 2.1 AA

![Accessibility architecture: color contrast ratios, keyboard navigation, ARIA roles, touch targets, vitest-axe and Playwright coverage](figures/fig-pitch-adv-11-accessibility-wcag-2-1-aa.jpg)

*Enterprise-grade accessibility from day one: WCAG 2.1 AA compliance with 4.5:1 color contrast, full keyboard navigation, ARIA roles on custom components (ConfidenceGauge as role="meter"), 44x44px touch targets, and two-layer testing (vitest-axe component-level + Playwright browser-level). EU EN 301 549 accessibility directive compliance as a defensible differentiator.*

---

### XXIV. Voice Agent Upsell Path

![Voice UI mockup with mic button, example queries, pricing tiers Free to Pro, and projected voice tier revenue](figures/fig-pitch-adv-12-voice-agent-premium-upsell.jpg)

*Voice agent as premium Pro upsell: mic animation with example queries ("What are Imogen Heap's co-writers?"), pricing progression from Free to Pro tier, and projected revenue from voice-specific features. In MVP, voice is aspirational UI only (upsell surface) -- full implementation at M9+ with Pipecat infrastructure delivering 6x cost savings over Vapi.*

---

### XXV. Adaptive UI Retention Flywheel

![Proficiency model: Jotai + localStorage scoring, adaptive UI layers from basic to pro mode, engagement analytics](figures/fig-pitch-adv-13-artist-mode-adaptive-ui.jpg)

*Adaptive UI as retention flywheel: per-user proficiency model (Jotai + localStorage) progressively reveals advanced features as users demonstrate mastery -- basic mode hides complexity, pro mode expands full controls. PostHog analytics track engagement and inform A/B testing, creating a data-driven personalization loop that reduces churn and is hard for competitors to replicate.*

---

## Business & Financial

### XXVI. Unit Economics by Segment

![ARPU table: indie artists $0-500, small labels $500-2000, CMOs $5000+ enterprise, with CAC payback and gross margin](figures/fig-pitch-adv-14-unit-economics-arpu.jpg)

*Unit economics by customer segment: indie artists at $0--500 ARPU (freemium funnel), small labels at $500--2,000 (Pro tier), CMOs at $5,000+ (Enterprise SLA), with CAC payback under 12 months and gross margins above 85% -- LTV:CAC ratios that support venture-scale growth across all three segments.*

---

### XXVII. Customer Acquisition Funnel

![Funnel: GitHub stars to free tier to paid conversion to CMO pilots to enterprise contracts, with CAC reduction from open-source](figures/fig-pitch-adv-15-customer-acquisition-funnel.jpg)

*Open-source acquisition funnel: 1,000 GitHub stars target driving 500 free tier signups, 10% paid conversion to 50 Pro customers, 5 CMO pilot programs, and 1 enterprise contract -- open-source distribution reduces CAC by an estimated 60% versus proprietary SaaS competitors through community-driven awareness and trust.*

---

### XXVIII. 18-Month P&L Scenarios

![Three scenarios: conservative (2 engineers), base (4 engineers, CMO pilots), upside (enterprise deals) with MRR and burn rate](figures/fig-pitch-adv-16-18-month-financial-projections.jpg)

*18-month P&L in three scenarios: Conservative (2 engineers, slow adoption, break-even at M20), Base (4 engineers, CMO pilots, profitable by M16), Upside (4 engineers + enterprise deals, profitable by M14) -- showing capital efficiency with Helsinki + Warsaw cost base and disciplined burn management.*

---

### XXIX. Four Revenue Streams

![Four revenue boxes: API licensing, enterprise SaaS, voice tier, data licensing to CMOs with 2026 projection](figures/fig-pitch-adv-17-partnership-revenue-streams.jpg)

*Four diversified revenue streams: API licensing ($0.01--0.10 per attribution query), Enterprise SaaS ($5K--50K MRR per CMO), Voice Pro tier ($29 ARPU with infrastructure moat), and Data licensing to CMOs ($100K+ annual) -- reducing single-stream risk and leveraging defensible IP across each channel.*

---

### XXX. Team Build-Out & Hiring Roadmap

![Gantt: CTO M0, UX/UI M1, Cloud M2, LLM M3, Voice M8, with Helsinki salary ranges and recruitment timeline](figures/fig-pitch-adv-18-18-month-hiring-roadmap.jpg)

*Team build-out: CTO/founder from M0, four phased hires (UX/UI engineer M1, cloud/infrastructure M2, LLM/ML engineer M3, optional voice agent M8) -- Helsinki base salaries at 60--70% of SF equivalents, recruiting from Aalto University and Warsaw tech ecosystem, growing to 5 people with each hire timed to the roadmap phase that needs their specialization.*

---

## Back to Core Deck

Return to the **[Core Pitch Deck](pitch-deck.md)** (12 slides) for the executive summary.

---

*Companion code to: Teikari, P. (2026). Music Attribution with Transparent Confidence. [SSRN No. 6109087](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087).*
