# Music Tech Landscape — Figure Coverage Plan

> **Version:** 1.0.0
> **Created:** 2026-02-15
> **Scope:** 32 new figure plans covering the music AI attribution landscape at category level
> **Prefix:** `fig-landscape-*`
> **Source material:** `docs/planning/music-tech-landscape/` (10 sub-files)

---

## Rationale

The repo already has **169 figure plans** across 12 prefixes. Existing figures focus on this scaffold's integration with specific companies/protocols. These 32 new figures fill a different niche:

- **Category-level problem taxonomies** (not individual company profiles)
- **Academic literature lineage** (how papers become products)
- **Cross-domain synthesis** connecting music attribution to supply chain, pharma, finance
- **Audience:** investors doing due diligence, founders building decks, researchers surveying the field

### The Nikola T. Markov Rule

Figures progress through four phases:

| Phase | Figures | What It Does |
|-------|---------|-------------|
| **Explain** | 01-08 | Define the problem space, map the territory |
| **Contextualize** | 09-16 | Situate methods within their technical traditions |
| **Synthesize** | 17-24 | Connect industry dynamics to economic models |
| **Speculate** | 25-32 | Forecast convergences, cross-domain transfers, open problems |

---

## Anti-Overlap Design

Each new figure is designed to complement, not duplicate, existing figures:

| Existing Figure | Focus | New Figures | Different Focus |
|----------------|-------|-------------|-----------------|
| fig-repo-16 | Maps companies to 4 tiers | fig-landscape-01 to -08 | Maps 12 problem categories by depth, no individual companies |
| fig-ecosystem-04 | Maps TDA providers (companies) | fig-landscape-09 to -16 | Maps TDA methods (techniques) with academic provenance |
| fig-trends-07 | STIM flow (single model) | fig-landscape-17 to -24 | Compares multiple licensing models side by side |
| fig-repo-24 | General protocol landscape | fig-landscape-25 to -32 | Music-specific future directions with cross-domain synthesis |

---

## Master Index

### Group 1: Problem Taxonomy & Market Map (Explain)

| # | ID | Title | Aud | Pri | Layout | Novelty |
|---|-----|-------|-----|-----|--------|---------|
| 01 | fig-landscape-01 | Music AI Problem Taxonomy: 12 Categories | L2 | P0 | B | 2/5 |
| 02 | fig-landscape-02 | Where the Money Went: $500M+ by Category | L1 | P0 | D | 2/5 |
| 03 | fig-landscape-03 | Papers to Products: Academic-to-Industry Pipeline | L2 | P0 | C | 3/5 |
| 04 | fig-landscape-04 | AI Disruption Points in the Music Value Chain | L1 | P1 | C | 3/5 |
| 05 | fig-landscape-05 | Market Maturity Spectrum: TRL x Adoption x Regulation | L2 | P1 | B | 3/5 |
| 06 | fig-landscape-06 | Founder Decision Framework: Which Attribution Approach | L3 | P1 | E | 2/5 |
| 07 | fig-landscape-07 | Same Landscape, Four Perspectives: Misaligned Incentives | L1 | P1 | B | 3/5 |
| 08 | fig-landscape-08 | Geographic Regulatory Fragmentation: Five Jurisdictions | L2 | P1 | B | 2/5 |

### Group 2: Attribution & Provenance Methods (Contextualize)

| # | ID | Title | Aud | Pri | Layout | Novelty |
|---|-----|-------|-----|-----|--------|---------|
| 09 | fig-landscape-09 | Seven TDA Methods: What Each Actually Measures | L4 | P0 | B | 2/5 |
| 10 | fig-landscape-10 | Post-hoc vs By-Design: Two Paradigms Converging | L2 | P0 | D | 3/5 |
| 11 | fig-landscape-11 | Audio Watermarking: 22 Schemes, 22 Attacks, None Robust | L4 | P1 | B | 2/5 |
| 12 | fig-landscape-12 | Content ID Evolution: From Shazam to AI Detection | L3 | P1 | E | 3/5 |
| 13 | fig-landscape-13 | The Metadata Mess: 6 Standards That Don't Connect | L2 | P0 | A | 3/5 |
| 14 | fig-landscape-14 | On-Chain vs Off-Chain Provenance Trade-offs | L3 | P2 | B | 4/5 |
| 15 | fig-landscape-15 | Evidence Chain: Detection to Forensics to Legal Claim | L4 | P1 | C | 3/5 |
| 16 | fig-landscape-16 | UQ in Attribution: From Medical Diagnosis to Music Credits | L4 | P0 | D | **5/5** |

### Group 3: Industry & Economic Models (Synthesize)

| # | ID | Title | Aud | Pri | Layout | Novelty |
|---|-----|-------|-----|-----|--------|---------|
| 17 | fig-landscape-17 | Five Licensing Models: Economics at Scale | L1 | P0 | B | 3/5 |
| 18 | fig-landscape-18 | CMO Digital Transformation: Four Phases | L2 | P1 | E | 3/5 |
| 19 | fig-landscape-19 | Ethical Certification: Binary vs Graduated vs Regulatory | L2 | P1 | B | 4/5 |
| 20 | fig-landscape-20 | Voice Rights & Identity Protection: 5-Layer Stack | L2 | P1 | C | 4/5 |
| 21 | fig-landscape-21 | 25 Years of MIR: How Research Became Infrastructure | L2 | P0 | C | 4/5 |
| 22 | fig-landscape-22 | Platform Evolution: Consumer Toy to Attribution-Integrated | L1 | P1 | E | 3/5 |
| 23 | fig-landscape-23 | Founder's Build-vs-Buy-vs-Partner Decision Map | L3 | P1 | D | 3/5 |
| 24 | fig-landscape-24 | $7.4B Revenue Distribution: With vs Without Attribution | L1 | P2 | A | 3/5 |

### Group 4: Future Directions & Cross-Domain Synthesis (Speculate)

| # | ID | Title | Aud | Pri | Layout | Novelty |
|---|-----|-------|-----|-----|--------|---------|
| 25 | fig-landscape-25 | Research Priority Forecast 2026-2028 | L4 | P0 | B | 4/5 |
| 26 | fig-landscape-26 | Cross-Domain Method Transfer: Supply Chain / Pharma / Finance to Music | L2 | P0 | A | **5/5** |
| 27 | fig-landscape-27 | Agentic Music Attribution: When AI Agents Query & Pay | L3 | P1 | C | 4/5 |
| 28 | fig-landscape-28 | Five Emerging Service Categories 2026 | L1 | P1 | B | 4/5 |
| 29 | fig-landscape-29 | Regulatory Cascade: EU AI Act to Architecture Requirements | L3 | P1 | C | 3/5 |
| 30 | fig-landscape-30 | The Convergence Thesis: MIR + XAI + UQ = Attribution | L4 | P0 | A | **5/5** |
| 31 | fig-landscape-31 | Open Problems: Solvable (2yr) / Hard (5yr) / Fundamental | L4 | P1 | B | 4/5 |
| 32 | fig-landscape-32 | From Landscape to Product: The Meta-Loop | L3 | P1 | C | 3/5 |

---

## Markovian Novelty Highlights (the "Trinity")

Three signature figures (5/5 novelty) constitute the intellectual contribution:

1. **fig-landscape-16** -- UQ cross-domain: medical diagnosis, autonomous driving, financial risk --> music attribution
2. **fig-landscape-26** -- Method transfer: supply chain (GS1), pharma (EU FMD), finance (SOX), game theory (Shapley) --> music
3. **fig-landscape-30** -- Field convergence: MIR (25yr) + XAI (post-2016) + UQ (conformal prediction) = new discipline

---

## Academic Sources Across 32 Figures

| Research Tradition | Key Papers | Figures Referenced In |
|-------------------|------------|----------------------|
| TDA / Influence Functions | Koh & Liang (2017), Mlodozeniec (2024), Choi et al. Sony NeurIPS (2025) | 03, 09, 10, 15 |
| Attribution-by-Design | Morreale et al. (2025) | 03, 10, 30 |
| Embedding Similarity | Barnett et al. CLMR/CLAP (2024), 25yr MIR survey (2025) | 03, 09, 12, 21, 30 |
| Watermarking | SoK (Wen et al. 2025), AudioSeal, SynthID, Epple (2024) | 11, 14 |
| Detection / Forensics | Afchar ICASSP (2025), MiRA (2024), SSIMuse (2025) | 12, 15 |
| Copyright / Legal | Dornis & Stober TISMIR (2025), Computational Copyright (Deng, 2023/2025) | 08, 15, 29 |
| Economics | Waldfogel, Arrieta-Ibarra Data Dividends, NBER Genius on Demand | 02, 04, 17, 24 |
| Responsible AI | de Berardinis et al. (2025), artist opinion surveys | 07, 19 |
| UQ / Conformal | Vovk (2005), Beigi LLM UQ taxonomy (2024), SConU | 16, 30, 25 |
| Cross-Domain | GS1 EPCIS, EU FMD, SOX, Shapley values, DPP/AI Passport manuscripts | 14, 19, 26 |

---

## Priority Distribution

| Priority | Count | Figures |
|----------|-------|---------|
| P0 (Critical) | 12 | 01, 02, 03, 09, 10, 13, 16, 17, 21, 25, 26, 30 |
| P1 (High) | 18 | 04, 05, 06, 07, 08, 11, 12, 15, 18, 19, 20, 22, 23, 27, 28, 29, 31, 32 |
| P2 (Medium) | 2 | 14, 24 |

---

## File Structure

- **This document:** `docs/planning/music-tech-figure-coverage-plan.md`
- **Figure plans:** `docs/figures/repo-figures/figure-plans/fig-landscape-{01..32}-*.md`
- **Template:** `docs/figures/repo-figures/CONTENT-TEMPLATE-REPO.md`
- **Style guide:** `docs/figures/repo-figures/STYLE-GUIDE-REPO.md`

---

*Music Attribution Scaffold -- Music Tech Landscape Figure Coverage Plan v1.0.0*
