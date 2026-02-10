# Music Attribution Scaffold

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)
[![Package manager: uv](https://img.shields.io/badge/package%20manager-uv-blueviolet.svg)](https://docs.astral.sh/uv/)

**Open-source research scaffold for music attribution with transparent confidence scoring.**

Companion code to: **Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.**
[Read the preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087)

This scaffold demonstrates how to build a multi-source music attribution system with per-field confidence scores, entity resolution, and AI-ready permissions via the MCP protocol.

---

## Who We Build For

![Mogen, Andy & Friends — The People We Build For](docs/figures/assets/fig-vis-01-mogen-andy-and-friends.jpg)
*Artists, producers, session musicians, and the creative teams who deserve proper credit.*

---

## What You Get

![What You Get — From Chaos to Clarity](docs/figures/assets/fig-rm-09-what-you-get.jpg)
*From invisible to verified. From chaos to control.*

---

## The Problem

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C', 'textColor': '#2C2C2C'}}}%%
graph TD
    subgraph silos[" Data Silos "]
        L[("Labels<br/>30% coverage")]
        S[("Streaming<br/>40% coverage")]
        R[("Rights Orgs<br/>25% coverage")]
    end

    silos --> PROBLEM["No Single Source of Truth"]
    PROBLEM --> C1["$2.5B+ unclaimed royalties"]
    PROBLEM --> C2["Artists can't prove credits"]
    PROBLEM --> C3["AI trains without consent"]

    style PROBLEM fill:#C75050,color:#fff,stroke:#C75050
    style C1 fill:#8B8B8B,color:#fff
    style C2 fill:#8B8B8B,color:#fff
    style C3 fill:#8B8B8B,color:#fff
    style L fill:#D4A03C,color:#000
    style S fill:#D4A03C,color:#000
    style R fill:#D4A03C,color:#000
```

**40%+ of music metadata is wrong.** Labels, streaming platforms, and rights organizations each hold partial data. No single source has the complete picture — and artists pay the price.

---

## The Solution

![Sound Sources Unite — How Attribution Brings It Together](docs/figures/assets/fig-rm-02-sound-sources-unite.jpg)
*Multiple sources in. One verified truth out.*

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C', 'textColor': '#2C2C2C'}}}%%
graph LR
    subgraph sources[" Sources "]
        D[Discogs]
        M[MusicBrainz]
        U[User Input]
    end

    subgraph engine[" Attribution System "]
        ER[Entity<br/>Resolution]
        CS[Confidence<br/>Scoring]
        DB[(Unified<br/>Database)]
    end

    subgraph output[" Output "]
        API[MCP API]
        WEB[Web App]
    end

    D --> ER
    M --> ER
    U --> ER
    ER --> CS
    CS --> DB
    DB --> API
    DB --> WEB

    style ER fill:#1E3A5F,color:#fff
    style CS fill:#1E3A5F,color:#fff
    style DB fill:#4A7C59,color:#fff
    style API fill:#2E7D7B,color:#fff
    style WEB fill:#D4A03C,color:#000
    style D fill:#8B8B8B,color:#fff
    style M fill:#8B8B8B,color:#fff
    style U fill:#8B8B8B,color:#fff
```

The system **aggregates multiple sources** through entity resolution, producing unified records with **per-field confidence scores** and full provenance tracking.

---

## Attribution Levels

![From Unknown to Verified — The Trust Progression](docs/figures/assets/fig-rm-03-from-unknown-to-verified.jpg)
*Your word matters. When YOU claim a credit, that's the start of verification — not the end.*

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'lineColor': '#5C5C5C'}}}%%
stateDiagram-v2
    direction LR
    [*] --> A0: New data
    A0 --> A1: Artist claims
    A1 --> A2: Source confirms
    A2 --> A3: Multiple sources agree

    A0: A0 Unknown
    A1: A1 Claimed
    A2: A2 Corroborated
    A3: A3 Verified
```

Every attribution progresses through **four trust levels**:
- **A0 Unknown**: Data exists but unverified
- **A1 Claimed**: Artist asserts the credit
- **A2 Corroborated**: One external source confirms
- **A3 Verified**: Multiple sources agree with high confidence

---

## How Sure Are We?

![How Sure Are We? — Confidence Scores Explained](docs/figures/assets/fig-rm-07-how-sure-are-we.jpg)
*Every credit comes with a number. Higher = more trustworthy.*

---

## A Day with the System

![A Day in the Life — Check, Fix, Decide](docs/figures/assets/fig-rm-04-mogen-and-andys-day.jpg)
*Check. Fix. Decide. That's it.*

---

## Two-Way Conversation

![Two-Way Conversation — Input Your Data, Let Others Query It](docs/figures/assets/fig-rm-05-two-way-conversation.jpg)
*You control what goes in. You control who asks.*

---

## AI Asks Permission

![AI Asks Permission — How the MCP Protocol Protects Your Music](docs/figures/assets/fig-rm-06-ai-asks-permission.jpg)
*AI can't just take your music. They have to ask — and YOU decide.*

---

## Your Music, Your Rules

![Your Music, Your Rules — Control Who Accesses Your Data](docs/figures/assets/fig-rm-08-your-music-your-rules.jpg)
*Turn access on or off. It's your call.*

---

## System Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TB
    subgraph external[" External APIs "]
        DIS[Discogs]
        MB[MusicBrainz]
    end

    subgraph core[" Attribution Core "]
        AE[Attribution Engine]
        MCP[MCP Server]
        CHAT[Chat Interface]
        DB[(PostgreSQL<br/>+ pgvector)]
    end

    subgraph clients[" Clients "]
        AI[AI Platforms<br/>Tier 2-3]
        WEB[Web App<br/>Artists]
        INT[Internal Apps<br/>Tier 1]
    end

    DIS --> AE
    MB --> AE
    AE --> DB
    DB --> MCP
    DB --> CHAT
    MCP --> AI
    CHAT --> WEB
    MCP --> INT

    style AE fill:#1E3A5F,color:#fff
    style MCP fill:#2E7D7B,color:#fff
    style CHAT fill:#D4A03C,color:#000
    style DB fill:#4A7C59,color:#fff
    style DIS fill:#8B8B8B,color:#fff
    style MB fill:#8B8B8B,color:#fff
    style AI fill:#8B8B8B,color:#fff
    style WEB fill:#8B8B8B,color:#fff
    style INT fill:#8B8B8B,color:#fff
```

| Component | Purpose |
|-----------|---------|
| **Attribution Engine** | Multi-source aggregation with entity resolution |
| **MCP Server** | AI-friendly API with three-tier access control |
| **Chat Interface** | Conversational gap-filling for artists |
| **PostgreSQL + pgvector** | Vector-enabled database for similarity search |

## Key Features

- **Multi-source truth**: Aggregate Discogs, MusicBrainz, and user contributions
- **Transparent confidence**: Every field has a confidence score with provenance
- **Calibrated uncertainty**: Conformal prediction for statistically valid bounds
- **AI-ready**: MCP protocol for ethical AI training with consent

## Documentation

| Document | Description |
|----------|-------------|
| [Vision PRD](docs/prd/vision-v1.md) | Product vision and strategy |
| [Architecture](docs/architecture/README.md) | System design, ADRs, and technical diagrams |
| [Knowledge Base](docs/knowledge-base/README.md) | Domain and technical knowledge |
| [Figures](docs/figures/README.md) | Visual documentation gallery |

## Quick Start

```bash
# Install dependencies (requires uv)
uv sync

# Run tests
make test

# Run linting
make lint
```

> **Note**: This project uses [uv](https://docs.astral.sh/uv/) for package management. pip/conda are not supported.

## Development

```bash
# Install dev dependencies
make install-dev

# Run tests with coverage
make test-cov

# Run CI locally (Docker)
make ci-docker
```

## Tech Stack

| Category | Choice |
|----------|--------|
| Language | Python 3.13 |
| Package Manager | uv (only) |
| Database | PostgreSQL + pgvector |
| Uncertainty | MAPIE (conformal prediction) |
| AI Integration | MCP protocol |
| Linting | Ruff |
| Type Checking | mypy |

## Citation

If you use this scaffold in your research, please cite:

```bibtex
@article{teikari2026music,
  title={Music Attribution with Transparent Confidence},
  author={Teikari, Petteri},
  journal={SSRN},
  number={6109087},
  year={2026}
}
```

## License

MIT
