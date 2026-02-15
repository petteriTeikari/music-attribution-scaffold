# Product Requirements Documents

This directory contains PRDs for the Music Attribution Scaffold.

---

## The Problem We're Solving

![Overview of the Music Attribution Scaffold: editorial frontend with confidence gauges, assurance badges, review queue, and agentic sidebar.](../figures/repo-figures/assets/fig-repo-01-hero-overview.jpg)

*40%+ of music metadata is wrong, causing $2.5B+ in unclaimed royalties annually. The scaffold unifies fragmented metadata into confidence-scored attribution records.*

---

## 🎯 For Imogen & Andy: We Need Your Input!

> **Before we build, we need your expertise.**
>
> We've created a structured questionnaire with questions that **only domain experts can answer**. Your input directly shapes our technical architecture and prevents costly rework later.

### 📋 [**→ UNKNOWNS-FOR-DOMAIN-EXPERTS.md**](UNKNOWNS-FOR-DOMAIN-EXPERTS.md)

| Section | Key Questions |
|---------|---------------|
| **Confidence & Trust** | What makes you trust automated data? When do you verify? |
| **Workflow & Scale** | How do you track credits today? How big is your catalog? |
| **Business & Revenue** | Cost of wrong credits? Who else needs this data? |
| **Edge Cases** | Pseudonyms? Uncredited work? AI contributions? |
| **Permissions & AI** | What can AI do without asking? What requires permission? |
| **Unknown Unknowns** | What questions should we have asked but didn't? |

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F'}}}%%
flowchart LR
    subgraph input["Your Expertise"]
        I1[Answer<br/>Questions]
        I2[Flag Missing<br/>Questions]
    end

    subgraph output["What We Build"]
        O1[Right<br/>Architecture]
        O2[No Surprise<br/>Rework]
    end

    I1 --> O1
    I2 --> O2

    style I1 fill:#D4A03C,color:#000
    style I2 fill:#D4A03C,color:#000
    style O1 fill:#4A7C59,color:#fff
    style O2 fill:#4A7C59,color:#fff
```

**⏰ Earlier input = more influence on what we build.**

---

### How the Attribution System Creates Value

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
flowchart TB
    subgraph problem[" Current State: Fragmented Data "]
        P1[40% wrong<br/>metadata]
        P2[$2.5B lost<br/>royalties]
        P3[No AI consent<br/>framework]
    end

    subgraph attribution[" Attribution Solution "]
        A1[Multi-source<br/>Aggregation]
        A2[Artist-verified<br/>Attribution]
        A3[Machine-readable<br/>Permissions]
    end

    subgraph value[" Delivered Value "]
        V1[Accurate<br/>Credits]
        V2[Proper<br/>Royalties]
        V3[AI Training<br/>Consent]
    end

    P1 -->|solved by| A1
    P2 -->|solved by| A2
    P3 -->|solved by| A3

    A1 --> V1
    A2 --> V2
    A3 --> V3

    style P1 fill:#C75050,color:#fff
    style P2 fill:#C75050,color:#fff
    style P3 fill:#C75050,color:#fff
    style A1 fill:#1E3A5F,color:#fff
    style A2 fill:#1E3A5F,color:#fff
    style A3 fill:#1E3A5F,color:#fff
    style V1 fill:#4A7C59,color:#fff
    style V2 fill:#4A7C59,color:#fff
    style V3 fill:#4A7C59,color:#fff
```

**For Stakeholders**: Each problem has a corresponding solution and delivered value. The system addresses all three critical pain points in the music industry.

**For Engineers**: Each value proposition maps to specific technical components. Multi-source aggregation is the Attribution Engine; artist verification is the Chat Interface; permissions are the MCP Server.

---

## Quick Navigation (For Both Audiences)

**For Stakeholders**: Start with the problem/solution overview above, then [UNKNOWNS-FOR-DOMAIN-EXPERTS.md](UNKNOWNS-FOR-DOMAIN-EXPERTS.md) to provide input.

**For Engineers**: Start with [llm-context.md](llm-context.md) for system context, then dive into specific domain TOCs.

---

## PRD Ecosystem

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TB
    subgraph level1[" L1: Vision & Context "]
        V[decisions/<br/>PRD NETWORK]
        LLM[llm-context.md<br/>System Context]
        SYN[SYNTHESIS.md<br/>Cross-cutting]
    end

    subgraph level2[" L2: Legacy PRDs "]
        AE[attribution-engine-prd.md]
        CI[chat-interface-prd.md]
        MCP[mcp-server-prd.md]
    end

    subgraph level2h[" L2: Hierarchical PRDs "]
        AET[attribution-engine/]
        CIT[chat-interface/]
        MCPT[mcp-server/]
        DL[data-layer/]
        VA[voice-agent/]
    end

    subgraph cross[" Cross-Cutting "]
        UQ[uncertainty/]
        OBS[observability/]
        SEC[security/]
        IP[identity-permissions/]
        INF[infrastructure/]
    end

    subgraph support[" Support Docs "]
        REJ[REJECTED.md]
        UNK[UNKNOWNS-FOR-DOMAIN-EXPERTS.md]
    end

    V --> AE
    V --> CI
    V --> MCP
    AE -.->|Details in| AET
    CI -.->|Details in| CIT
    MCP -.->|Details in| MCPT

    AET --> UQ
    AET --> OBS
    CIT --> UQ
    MCPT --> SEC
    MCPT --> IP

    style V fill:#1E3A5F,color:#fff
    style LLM fill:#1E3A5F,color:#fff
    style AE fill:#2E7D7B,color:#fff
    style CI fill:#D4A03C,color:#000
    style MCP fill:#4A7C59,color:#fff
    style AET fill:#2E7D7B,color:#fff
    style CIT fill:#D4A03C,color:#000
    style MCPT fill:#4A7C59,color:#fff
    style UQ fill:#C75050,color:#fff
    style SEC fill:#C75050,color:#fff
```

---

## PRD Index

### L1: Vision Documents

| PRD | Description | Status | Last Updated |
|-----|-------------|--------|--------------|
| *(vision content integrated into PRD decisions)* | Master vision and product strategy | Merged | 2026-02-14 |
| [llm-context.md](llm-context.md) | System prompt for AI assistants | Active | 2026-02-04 |
| [SYNTHESIS.md](SYNTHESIS.md) | Cross-PRD insights and decisions | Active | 2026-02-04 |

### L2: Legacy PRDs (Component Overviews)

| PRD | Description | Status | Last Updated |
|-----|-------------|--------|--------------|
| [attribution-engine-prd.md](attribution-engine-prd.md) | Multi-source attribution with confidence | Draft v0.8 | 2026-02-04 |
| [chat-interface-prd.md](chat-interface-prd.md) | Conversational gap-filling UX | Draft v0.8 | 2026-02-04 |
| [mcp-server-prd.md](mcp-server-prd.md) | MCP API for AI platforms | Draft v0.8 | 2026-02-04 |

### L2: Hierarchical PRD Domains

| Domain | TOC | Description |
|--------|-----|-------------|
| Attribution Engine | [toc-attribution-engine.md](attribution-engine/toc-attribution-engine.md) | Core data aggregation |
| Chat Interface | [toc-chat-interface.md](chat-interface/toc-chat-interface.md) | Gap-filling UX |
| MCP Server | [toc-mcp-server.md](mcp-server/toc-mcp-server.md) | AI platform API |
| Data Layer | [toc-data-layer.md](data-layer/toc-data-layer.md) | Database architecture |
| Voice Agent | [toc-voice-agent.md](voice-agent/toc-voice-agent.md) | Voice-first interface |

### Cross-Cutting PRD Domains

| Domain | TOC | Description |
|--------|-----|-------------|
| Uncertainty | [toc-uncertainty.md](uncertainty/toc-uncertainty.md) | Conformal prediction, calibration |
| Observability | [toc-observability.md](observability/toc-observability.md) | Langfuse, metrics |
| Security | [toc-security.md](security/toc-security.md) | MCP security, multi-tenancy |
| Identity & Permissions | [toc-identity-permissions.md](identity-permissions/toc-identity-permissions.md) | ArtistID, consent |
| Infrastructure | [toc-infrastructure.md](infrastructure/toc-infrastructure.md) | Deployment, ops |

### Support Documents

| Document | Description |
|----------|-------------|
| [REJECTED.md](REJECTED.md) | Why NOT to use certain technologies |
| [UNKNOWNS-FOR-DOMAIN-EXPERTS.md](UNKNOWNS-FOR-DOMAIN-EXPERTS.md) | Questions for Imogen/Andy |
| [defaults.yaml](defaults.yaml) | Current active configuration |
| [schema.yaml](schema.yaml) | PRD frontmatter schema |

---

## Document Reading Order by Role

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
flowchart LR
    subgraph stakeholder[" Stakeholder Path "]
        S1[README.md<br/>YOU ARE HERE] --> S3[UNKNOWNS-FOR-DOMAIN-EXPERTS.md]
    end

    subgraph engineer[" Engineer Path "]
        E1[llm-context.md] --> E2[SYNTHESIS.md]
        E2 --> E3[Domain TOC files]
    end

    subgraph devops[" DevOps Path "]
        D1[infrastructure/] --> D2[observability/]
        D2 --> D3[security/]
    end

    style S1 fill:#D4A03C,color:#000
    style E1 fill:#1E3A5F,color:#fff
    style D1 fill:#4A7C59,color:#fff
```

**For Stakeholders**: Follow the yellow path. Start here, then read the vision document, then provide feedback via the unknowns document.

**For Engineers**: Follow the blue path. Start with system context, then cross-cutting synthesis, then dive into specific domains.

---

## Cross-PRD Dependencies

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph LR
    subgraph core[" Core Dependencies "]
        AE[attribution-engine]
        MCP[mcp-server]
        CI[chat-interface]
    end

    subgraph data[" Data Flow "]
        AE -->|exposes data| MCP
        AE -->|provides data| CI
        CI -->|contributes data| AE
    end

    style AE fill:#1E3A5F,color:#fff
    style MCP fill:#4A7C59,color:#fff
    style CI fill:#D4A03C,color:#000
```

---

## Implementation Roadmap

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
gantt
    title Music Attribution Roadmap
    dateFormat  YYYY-MM-DD
    section Phase 1: MVP
        Attribution Engine Core     :a1, 2026-02-10, 2w
        MCP Server (Read-only)      :a2, after a1, 1w
        Confidence Scoring          :a3, 2026-02-10, 2w
    section Phase 2: Identity
        Chat Interface              :b1, after a2, 2w
        ArtistID System            :b2, after a2, 2w
        MCP Write Operations        :b3, after b1, 1w
    section Phase 3: Ecosystem
        Partner Integrations        :c1, after b3, 4w
        Calibrated Confidence       :c2, after b3, 2w
        Voice Agent                 :c3, after b1, 4w
```

---

---

## Stakeholder Journey Map

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
journey
    title Artist Journey with the Attribution System
    section Discovery
      Hear about the system: 3: Artist
      Visit website: 3: Artist
      Understand value proposition: 4: Artist
    section Onboarding
      Create ArtistID: 5: Artist, System
      Connect existing accounts: 4: Artist, System
      Review imported catalog: 4: Artist
    section Verification
      Chat to fill gaps: 5: Artist, Chat Interface
      Confirm credits: 5: Artist
      Set AI permissions: 4: Artist
    section Value Realization
      AI platform queries permissions: 5: AI Platform, MCP
      Receive proper attribution: 5: Artist
      Collect royalties: 5: Artist
```

**For Stakeholders**: This shows the artist's emotional journey. High satisfaction (5) in chat-based gap-filling and value realization; medium satisfaction (3-4) in early discovery phases.

**For Engineers**: Low-satisfaction phases (Discovery, Onboarding) need UX optimization. High-satisfaction phases (Verification, Value) validate our core approach.

---

## Unknown Unknowns: What We Don't Know We Don't Know

This section captures fundamental uncertainties that could invalidate our assumptions.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
mindmap
  root((PRD-Level<br/>Unknowns))
    Market Assumptions
      Will AI platforms honor permissions?
      Is there willingness to pay?
      Will major labels compete directly?
    Technical Assumptions
      Can entity resolution scale?
      Will MCP protocol stabilize?
      Are confidence calibrations achievable?
    User Assumptions
      Will artists engage long-term?
      Can heritage artists use digital tools?
      Is chat the right modality?
    Regulatory Assumptions
      Will EU AI Act enforcement be strong?
      Will US follow with similar laws?
      How will PROs respond?
```

### Critical Questions by Category

| Category | Question | Why It Matters | Monitoring Approach |
|----------|----------|----------------|---------------------|
| **Market** | Will AI platforms actually honor permissions? | If ignored, core value prop collapses | Track platform adoption, legal developments |
| **Market** | Will major labels build competing systems? | Could fragment ecosystem | Competitive intelligence, partnership outreach |
| **Technical** | Can entity resolution handle 100M+ records? | Scale determines viability | Load testing, architecture reviews |
| **Technical** | Will confidence calibration work with limited data? | Affects API usefulness | Calibration experiments, domain expert validation |
| **User** | Is conversational gap-filling engaging enough? | User retention depends on UX | Session analytics, A/B testing, dropout analysis |
| **Regulatory** | How strictly will EU AI Act be enforced? | Determines compliance urgency | Legal monitoring, industry working groups |

### Questions Only Domain Experts Can Answer

1. **Imogen/Andy**: What percentage of your catalog has incorrect credits that matter to you?
2. **Imogen/Andy**: Would you actually use a chat interface weekly, or prefer bulk upload?
3. **Rights Orgs**: Would you accept the system's data as an authoritative source?
4. **AI Platforms**: What level of attribution confidence would you require for training consent?

See [UNKNOWNS-FOR-DOMAIN-EXPERTS.md](UNKNOWNS-FOR-DOMAIN-EXPERTS.md) for the complete list.

---

## Probabilistic PRD System

The PRD system extends beyond traditional linear documents into a **Bayesian decision network** with conditional probabilities, team archetype modulation, and cross-domain applicability.

| Directory | Contents |
|-----------|----------|
| [decisions/](decisions/) | 23 decision nodes across 5 levels (L1 Business → L5 Operations) with conditional probability tables |
| [decisions/REPORT.md](decisions/REPORT.md) | Visual report with mermaid diagrams showing network topology, archetype comparisons, and scenario paths |
| [archetypes/](archetypes/) | 4 team profiles (engineer-heavy, musician-first, solo hacker, well-funded) that modulate decision probabilities |
| [scenarios/](scenarios/) | 3 composed paths through the network (music MVP, solo musician, DPP enterprise) |
| [domains/](domains/) | Domain overlay system — music attribution and DPP traceability share the same architecture |

Start with [decisions/README.md](decisions/README.md) for the conceptual model, or [decisions/REPORT.md](decisions/REPORT.md) for visual summaries.

---

## See Also

- [SYNTHESIS.md](SYNTHESIS.md) - Cross-PRD insights and decisions
- [REJECTED.md](REJECTED.md) - Why NOT to use certain technologies
- [UNKNOWNS-FOR-DOMAIN-EXPERTS.md](UNKNOWNS-FOR-DOMAIN-EXPERTS.md) - Questions for domain experts
- [../knowledge-base/](../knowledge-base/) - Domain and technical knowledge
- [../planning/probabilistic-prd-design.md](../planning/probabilistic-prd-design.md) - Probabilistic PRD design rationale
