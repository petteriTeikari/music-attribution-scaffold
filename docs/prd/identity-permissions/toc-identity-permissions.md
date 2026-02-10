---
id: identity-permissions/toc-identity-permissions
title: Identity & Permissions - Table of Contents
status: active
version: 0.1.0
last_updated: 2026-02-04
priority: high

requires:
  - vision-v1.md#executive-summary
  - llm-context.md

cross_refs:
  - mcp-server/toc-mcp-server.md
  - voice-agent/voice-consent.md
  - security/toc-security.md

tags:
  - identity
  - permissions
  - artist-id
  - ai-consent

changelog:
  - version: "0.1.0"
    date: 2026-02-04
    changes: "Initial structure for identity and permission management"
---

# Identity & Permissions

**Purpose**: Artist identity verification and AI permission management

**Key Concept**: ArtistID - A verified artist identity that controls attribution data and AI permissions

---

## Overview

Identity & Permissions enables artists to:
1. Establish verified digital identity (ArtistID)
2. Control how their work is used by AI platforms
3. Set granular permissions per work, per platform, per use case

## Core Capabilities

| Capability | Description | PRD |
|------------|-------------|-----|
| **ArtistID** | Verified artist identity system | [artist-id.md](artist-id.md) |
| **AI Permissions** | Granular AI training/use permissions | [ai-permissions.md](ai-permissions.md) |
| **Verification Flow** | Identity verification process | [verification-flow.md](verification-flow.md) |
| **Permission Dashboard** | UI for managing permissions | [permission-dashboard.md](permission-dashboard.md) |
| **Delegation** | Manager/label delegation support | [delegation.md](delegation.md) |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   IDENTITY & PERMISSIONS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                      ArtistID                           │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │   │
│  │  │ Verification│  │  Identity   │  │ Delegation  │     │   │
│  │  │   Status    │  │   Claims    │  │   Tree      │     │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   Permission Matrix                      │   │
│  │                                                         │   │
│  │         │ AI Training │ AI Output │ Sampling │ Remix   │   │
│  │  ───────┼─────────────┼───────────┼──────────┼─────────│   │
│  │  Work A │     ✓       │     ✓     │    ✗     │   ✓     │   │
│  │  Work B │     ✗       │     ✗     │    ✗     │   ✗     │   │
│  │  All    │   Default   │  Default  │ Default  │ Default │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Exposed via MCP Server                      │   │
│  │       (AI platforms query permissions before use)        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Permission Types

| Permission | Description | Default |
|------------|-------------|---------|
| `ai_training` | Allow use in AI model training | Opt-in |
| `ai_generation` | Allow AI to generate content in style | Opt-in |
| `ai_sampling` | Allow AI to sample/reference work | Opt-in |
| `ai_remix` | Allow AI-assisted remixes | Opt-in |
| `data_sharing` | Share attribution data publicly | Opt-in (basic) |
| `voice_clone` | Allow voice synthesis | Opt-in |

## Verification Levels

| Level | Requirements | Unlocks |
|-------|--------------|---------|
| **Basic** | Email verification | View/edit own data |
| **Verified** | ID + existing catalog link | Set AI permissions, MCP exposure |
| **Pro** | Contracts, label verification | Multi-artist management, API access |

## Implementation Priority

1. **artist-id.md** - Core identity system
2. **ai-permissions.md** - Permission framework
3. **verification-flow.md** - Verification process
4. **permission-dashboard.md** - User interface
5. **delegation.md** - Manager/label support

## Cross-Cutting Dependencies

| Concern | Integration Point |
|---------|-------------------|
| **MCP Server** | Exposes permissions to AI platforms |
| **Voice Agent** | Voice consent ties to identity |
| **Security** | Authentication, authorization |
| **Attribution Engine** | Artist-confirmed data tied to identity |

## Related Documents

- [vision-v1.md](../vision-v1.md) - Product vision
- [mcp-server/permission-verification.md](../mcp-server/permission-verification.md) - How MCP checks permissions
- [voice-agent/voice-consent.md](../voice-agent/voice-consent.md) - Voice-specific consent
- [security/toc-security.md](../security/toc-security.md) - Security requirements

---

## Cross-Domain Impact Diagram

Identity & Permissions is a foundational cross-cutting concern that affects every domain in the system platform.

```mermaid
flowchart TB
    subgraph Identity["Identity & Permissions"]
        AID[ArtistID]
        PM[Permission Matrix]
        VF[Verification Flow]
        DEL[Delegation]
    end

    subgraph Domains["All Platform Domains"]
        AE[Attribution Engine]
        CI[Chat Interface]
        VA[Voice Agent]
        MCP[MCP Server]
        DL[Data Layer]
        OBS[Observability]
        SEC[Security]
        INF[Infrastructure]
    end

    subgraph External["External Systems"]
        AI_PLAT[AI Platforms<br/>OpenAI, Anthropic, etc.]
        LABELS[Labels & Rights Orgs]
        ARTISTS[Individual Artists]
    end

    AID -->|"Owns attribution data"| AE
    AID -->|"Session identity"| CI
    AID -->|"Voice consent binding"| VA
    PM -->|"Permission checks"| MCP
    PM -->|"Access control"| DL
    VF -->|"Auth events"| OBS
    VF -->|"Identity verification"| SEC
    DEL -->|"Multi-tenant access"| INF

    AI_PLAT -->|"Query permissions via MCP"| PM
    LABELS -->|"Delegate permissions"| DEL
    ARTISTS -->|"Verify identity"| VF
    ARTISTS -->|"Set permissions"| PM

    style Identity fill:#e1f5fe,stroke:#01579b
    style AID fill:#fff9c4,stroke:#f57f17
    style PM fill:#fff9c4,stroke:#f57f17
```

### Domain-by-Domain Impact

| Domain | How Identity & Permissions Affects It |
|--------|---------------------------------------|
| **Attribution Engine** | All attribution data is tied to a verified ArtistID; confidence scoring considers verification level |
| **Chat Interface** | Session context includes artist identity; prompts can request permission changes |
| **Voice Agent** | Voice consent creates legally-binding permission records tied to ArtistID |
| **MCP Server** | Every API request is validated against the permission matrix before data is returned |
| **Data Layer** | Row-level security policies enforce ArtistID-based access control |
| **Observability** | Verification events, permission changes, and delegation actions are all logged |
| **Security** | Authentication and authorization are built on ArtistID verification levels |
| **Infrastructure** | Multi-tenant isolation maps directly to delegation hierarchies |

---

## For Domain Experts (Imogen/Andy)

### Business Impact Summary

**Why This Matters for Artist Relations (Imogen):**
- ArtistID is how artists "own" their data on the system - it's their identity in the music metadata ecosystem
- Permission controls give artists unprecedented agency over how AI uses their work
- Delegation allows managers and labels to act on behalf of artists without full account access
- Verification levels create trust tiers that can unlock premium features or partnerships

**Why This Matters for Strategy (Andy):**
- AI platforms (OpenAI, Anthropic, Google) need a standardized way to check permissions - ArtistID + MCP is our moat
- Permission granularity (per-work, per-platform, per-use-case) is a competitive differentiator
- Enterprise deals with labels require delegation and multi-tenant support
- Verification levels can tier pricing and access

### Business Metrics Tied to Identity

| Metric | Business Meaning |
|--------|------------------|
| Verified artists | Market penetration among established artists |
| Permission opt-in rates | Artist trust in platform |
| Delegation chains | Label/management partnerships |
| MCP permission queries | AI platform integration adoption |

---

## Known Unknowns

These are identified gaps requiring research or executive decisions:

| Unknown | Impact | Research Needed |
|---------|--------|-----------------|
| **Identity verification cost** | Per-artist verification via ID services has real costs ($0.50-$2/verification) | Need to model break-even at different artist counts |
| **Permission inheritance rules** | When labels delegate, do sub-permissions propagate? How deep? | Legal review of standard management contracts |
| **Cross-platform identity linking** | Can an ArtistID link to Spotify for Artists, Apple Music for Artists, etc.? | API access negotiations with DSPs |
| **Permission revocation latency** | How fast must AI platforms honor permission changes? Real-time? Daily? | Industry standard research, legal requirements |
| **International ID verification** | ID verification services vary by country - coverage gaps? | Market analysis for target regions |
| **Deceased artist handling** | Who controls permissions for estates? How is this verified? | Legal consultation required |

---

## Executive Decision Impact

Technical choices in Identity & Permissions directly affect business strategy.

```mermaid
flowchart LR
    subgraph Tech["Technical Decisions"]
        T1[Verification Provider<br/>Stripe Identity vs. Persona]
        T2[Permission Storage<br/>Centralized vs. Federated]
        T3[Delegation Depth<br/>1-level vs. N-level]
        T4[Session Duration<br/>Hours vs. Days]
    end

    subgraph Biz["Business Impact"]
        B1[Cost per Artist<br/>$0.50-$2.00]
        B2[Data Sovereignty<br/>GDPR compliance]
        B3[Enterprise Sales<br/>Label complexity]
        B4[User Experience<br/>Re-login frequency]
    end

    subgraph Strategy["Strategic Implications"]
        S1[Pricing Model]
        S2[Market Expansion]
        S3[Partnership Types]
        S4[Competitive Position]
    end

    T1 --> B1 --> S1
    T2 --> B2 --> S2
    T3 --> B3 --> S3
    T4 --> B4 --> S4

    style Tech fill:#e3f2fd,stroke:#1565c0
    style Biz fill:#fff3e0,stroke:#ef6c00
    style Strategy fill:#f3e5f5,stroke:#7b1fa2
```

### Decision Matrix

| Technical Choice | Options | Business Trade-off |
|------------------|---------|-------------------|
| **Verification provider** | Stripe Identity, Persona, Jumio | Cost vs. coverage vs. integration complexity |
| **Permission model** | Opt-in default vs. opt-out default | Artist trust vs. AI platform adoption |
| **Delegation depth** | Single-level vs. hierarchical | Simplicity vs. enterprise label structures |
| **Permission granularity** | Per-catalog vs. per-work vs. per-platform | UX simplicity vs. artist control |
| **Verification tiers** | 2-tier vs. 3-tier vs. continuous | Onboarding friction vs. security |

### Recommendations for Executive Review

1. **Start with opt-in default** for AI permissions - builds artist trust, differentiates from competitors who assume consent
2. **Two-level delegation** (artist -> manager/label -> the system) covers 90% of use cases without complexity
3. **Per-catalog permissions** as default, with per-work override for power users - balances UX and control
4. **Stripe Identity** for verification - already integrated, good international coverage, known costs
