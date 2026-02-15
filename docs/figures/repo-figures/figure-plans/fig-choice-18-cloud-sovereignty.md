# fig-choice-18: Cloud Sovereignty — EU-Owned vs US-Owned Providers

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-18 |
| **Title** | Cloud Sovereignty: EU-Owned vs US-Owned for Music Rights Infrastructure |
| **Audience** | L2 (Technical Manager) |
| **Complexity** | L2 (cross-cutting decision) |
| **Location** | docs/planning/deployement-finops-landscape-geopolitical-risk-assessment.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains why cloud provider jurisdiction — not just data center location — determines data sovereignty for music attribution infrastructure. The CLOUD Act means running AWS in Frankfurt still exposes data to US government access. Shows the four EU-sovereign alternatives (Hetzner, OVHcloud, UpCloud, Scaleway) mapped against the three sovereignty-sensitive components of the scaffold (MCP consent, artist identity, audio fingerprints), with cost comparison proving EU providers are both cheaper and legally safer.

The key message is: "Where your cloud provider is headquartered matters more than where your server physically sits. EU-sovereign providers eliminate CLOUD Act exposure while saving 60-93% versus hyperscalers — and the scaffold's Docker architecture makes migration a configuration change, not a rewrite."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  CLOUD SOVEREIGNTY                                             |
|  ■ EU-Owned vs US-Owned for Music Rights Infrastructure       |
+---------------------------------------------------------------+
|                                                                |
|  THE JURISDICTION PROBLEM                                      |
|  ────────────────────────                                      |
|  Physical location ≠ legal jurisdiction.                       |
|  AWS eu-central-1 (Frankfurt) is still US jurisdiction.        |
|                                                                |
|  ┌──────────────────────────────────┐                         |
|  │  CLOUD Act + FISA 702           │                          |
|  │  US can compel data access from │                          |
|  │  US-owned providers, regardless │                          |
|  │  of where data is stored.       │                          |
|  └──────────────────────────────────┘                         |
|                                                                |
|  SOVEREIGNTY TIERS FOR MUSIC ATTRIBUTION                       |
|  ────────────────────────────────────                          |
|  ■ CRITICAL  MCP consent infra    → EU-sovereign only         |
|  ■ HIGH      Artist identity (PII) → EU-sovereign only        |
|  ■ MODERATE  Audio fingerprints    → EU-preferred             |
|  ■ LOW       Frontend / CI/CD      → Any provider             |
|                                                                |
|  EU-SOVEREIGN PROVIDERS                                        |
|  ────────────────────────                                      |
|  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        |
|  │ Hetzner  │ │ OVHcloud │ │ UpCloud  │ │ Scaleway │        |
|  │ Germany  │ │ France   │ │ Finland  │ │ France   │        |
|  │──────────│ │──────────│ │──────────│ │──────────│        |
|  │ €13/mo   │ │ €30/mo   │ │ $150/mo  │ │ €25/mo   │        |
|  │ 3 EU DCs │ │ 30+ DCs  │ │ 10 EU DC │ │ 3 EU DCs │        |
|  │ ISO27001 │ │ SecNum   │ │ CISPE    │ │ ISO27001 │        |
|  │          │ │ Cloud    │ │ NIS2     │ │          │        |
|  │ Budget   │ │ Enter-   │ │ Premium  │ │ GPU/AI   │        |
|  │ leader   │ │ prise    │ │ managed  │ │ focus    │        |
|  └──────────┘ └──────────┘ └──────────┘ └──────────┘        |
|                                                                |
|  vs US-HEADQUARTERED (CLOUD Act exposed)                       |
|  ┌──────────┐ ┌──────────┐ ┌──────────┐                     |
|  │ AWS      │ │ Render   │ │ Neon     │                      |
|  │ $195/mo  │ │ $35/mo   │ │ $0-19/mo │                      |
|  │ Broadest │ │ Simplest │ │ Scale-   │                      |
|  │ services │ │ deploy   │ │ to-zero  │                      |
|  │──────────│ │──────────│ │──────────│                      |
|  │ ⚠ CLOUD  │ │ ⚠ CLOUD  │ │ ⚠ CLOUD  │                    |
|  │ Act      │ │ Act      │ │ Act      │                      |
|  └──────────┘ └──────────┘ └──────────┘                     |
|                                                                |
|  Docker image → same container, any provider → sovereignty    |
|  is a configuration change, not a rewrite                      |
|                                                                |
+---------------------------------------------------------------+
|  Schrems III + Section 301 + PCLOB dissolution = rising risk  |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "CLOUD SOVEREIGNTY" with coral accent square |
| Jurisdiction problem | `callout_box` | Physical location ≠ legal jurisdiction; CLOUD Act + FISA 702 |
| Sovereignty tiers | `feature_list` | Four tiers (Critical/High/Moderate/Low) mapped to scaffold components |
| Hetzner card | `selected_option` | Budget leader, EUR 13/month, 3 EU DCs, ISO 27001 |
| OVHcloud card | `deferred_option` | Enterprise, SecNumCloud, 30+ DCs, EUR 30/month |
| UpCloud card | `deferred_option` | Premium managed, CISPE/NIS2, 10 EU DCs, $150/month |
| Scaleway card | `deferred_option` | GPU/AI focus, 3 EU DCs, EUR 25/month |
| US providers row | `warning_box` | AWS, Render, Neon with CLOUD Act warning badges |
| Docker portability callout | `callout_bar` | Same container, any provider — sovereignty as configuration |
| Risk footer | `callout_bar` | Schrems III + Section 301 + PCLOB = rising risk |

## Anti-Hallucination Rules

1. The CLOUD Act (2018) compels US-headquartered companies to provide data to US government regardless of physical storage location. This is the law, not speculation.
2. FISA Section 702 was reauthorized and expanded by Congress in April 2024 through 2026.
3. Schrems III has NOT been filed yet — NOYB has indicated preparation but no formal challenge exists as of Feb 2026.
4. Trump fired all three PCLOB board members on January 27, 2025. The PCLOB was a foundational pillar of the DPF adequacy decision.
5. Section 301 investigation targets include Spotify — this is documented in Fortune, December 2025.
6. Hetzner basic stack (compute + PG + object storage) is ~EUR 13/month. AWS equivalent is ~EUR 195/month. The 93% savings figure comes from this comparison.
7. UpCloud is Finnish-owned (Helsinki), has 13 DCs (10 in EU), ISO 27001 + CISPE + NIS2/DORA certified, 99.999% SLA with 50x compensation. Revenue ~$20M (2024).
8. OVHcloud surpassed EUR 1 billion revenue in FY 2025. SecNumCloud 3.2 qualified.
9. european.cloud lists 11 EU providers across 8 countries. Hetzner is notably absent from this directory.
10. Background must be warm cream (#f6f3e6).

## Alt Text

Architecture decision: cloud sovereignty assessment for music attribution scaffold comparing four EU-sovereign providers — Hetzner (Germany, budget leader), OVHcloud (France, SecNumCloud enterprise), UpCloud (Finland, premium managed services with CISPE certification), and Scaleway (France, GPU and AI focus) — against US-headquartered providers exposed to the CLOUD Act and FISA Section 702, with four sovereignty tiers mapping MCP consent infrastructure and artist identity data to EU-only hosting requirements in the open-source attribution platform.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture decision: cloud sovereignty assessment for music attribution scaffold comparing four EU-sovereign providers — Hetzner (Germany, budget leader), OVHcloud (France, SecNumCloud enterprise), UpCloud (Finland, premium managed services with CISPE certification), and Scaleway (France, GPU and AI focus) — against US-headquartered providers exposed to the CLOUD Act and FISA Section 702, with four sovereignty tiers mapping MCP consent infrastructure and artist identity data to EU-only hosting requirements in the open-source attribution platform.](docs/figures/repo-figures/assets/fig-choice-18-cloud-sovereignty.jpg)

*Cloud sovereignty for music attribution: EU-sovereign providers (Hetzner, OVHcloud, UpCloud, Scaleway) eliminate CLOUD Act exposure while saving 60-93% versus hyperscalers. The scaffold's Docker architecture makes sovereignty a configuration change — same container image deploys on any provider (PRD geopolitical risk assessment, volatility: shifting).*

### From this figure plan (relative)

![Architecture decision: cloud sovereignty assessment for music attribution scaffold comparing four EU-sovereign providers — Hetzner (Germany, budget leader), OVHcloud (France, SecNumCloud enterprise), UpCloud (Finland, premium managed services with CISPE certification), and Scaleway (France, GPU and AI focus) — against US-headquartered providers exposed to the CLOUD Act and FISA Section 702, with four sovereignty tiers mapping MCP consent infrastructure and artist identity data to EU-only hosting requirements in the open-source attribution platform.](../assets/fig-choice-18-cloud-sovereignty.jpg)
