# Geopolitical Risk Assessment: Cloud Infrastructure Sovereignty

> **Companion document to**: [FinOps Landscape](deployement-finops-landscape.md) |
> **PRD reference**: [compute-platform.decision.yaml](../prd/decisions/L4-deployment/compute-platform.decision.yaml) |
> **Figure plan**: [fig-choice-18](../figures/repo-figures/figure-plans/fig-choice-18-cloud-sovereignty.md)
>
> **Version**: 1.0 | **Created**: 2026-02-14 | **Next review**: 2026-04-14

---

## Executive Summary

European organizations building music attribution infrastructure face a **structural legal conflict**: the US CLOUD Act and FISA Section 702 grant US authorities access to data held by US-headquartered cloud providers regardless of where the data is physically stored, while GDPR requires that personal data of EU residents receives adequate protection from foreign government surveillance. This conflict has already invalidated two transatlantic data transfer frameworks (Safe Harbor in 2015, Privacy Shield in 2020), and the current EU-US Data Privacy Framework (DPF) faces a credible legal challenge (Schrems III).

For a music attribution scaffold handling artist identity data, MCP consent records, and audio fingerprints — all potentially qualifying as personal data under GDPR — the choice of cloud provider is not merely a FinOps decision. It is a **jurisdictional risk decision** with direct implications for data subject rights, regulatory compliance, and operational continuity.

**Key finding**: EU-sovereign infrastructure (Hetzner, OVHcloud, UpCloud, Scaleway) is both **cheaper** (60-93% savings vs hyperscalers) and **legally safer** (no CLOUD Act exposure) for this workload. The trade-off is fewer managed services and smaller ecosystems.

---

## Table of Contents

1. [Legal Framework: Why Jurisdiction Matters More Than Location](#1-legal-framework)
2. [Geopolitical Risk Factors](#2-geopolitical-risk-factors)
3. [European Cloud Provider Landscape](#3-european-cloud-provider-landscape)
4. [EU Sovereign Cloud Initiatives](#4-eu-sovereign-cloud-initiatives)
5. [Music Attribution: Sovereignty-Sensitive Components](#5-music-attribution-sovereignty-sensitive-components)
6. [Provider Comparison Matrix](#6-provider-comparison-matrix)
7. [Cost Analysis: EU-Sovereign vs Hyperscaler](#7-cost-analysis)
8. [Risk Assessment Matrix](#8-risk-assessment-matrix)
9. [Recommendations for the Scaffold](#9-recommendations)
10. [Impact on Probabilistic PRD](#10-impact-on-prd)

---

## 1. Legal Framework: Why Jurisdiction Matters More Than Location {#1-legal-framework}

### 1.1 The CLOUD Act (Clarifying Lawful Overseas Use of Data Act, 2018)

The single most important legal instrument for cloud sovereignty. The CLOUD Act compels US-headquartered companies to provide data to US law enforcement upon request, **regardless of where the data is physically stored**. Running AWS or Azure in `eu-central-1` does **not** provide legal sovereignty — the data remains subject to US jurisdiction through the parent company.

Key implications:
- **Extraterritorial reach**: US warrants apply to data stored in EU data centers by US companies
- **Conflict with GDPR**: Companies face impossible compliance — obey the CLOUD Act (violate GDPR) or obey GDPR (violate the CLOUD Act)
- **No notification requirement**: Data subjects may never know their data was accessed
- **Broad scope**: Applies to all data, not just communications — includes metadata, analytics, logs

**"Sovereign-Cloud-Washing"**: AWS, Azure, and GCP market "sovereign cloud" variants (AWS European Sovereign Cloud, Azure Sovereign Cloud), but these remain **legally subordinate to the CLOUD Act** because the parent company is US-headquartered. The HN community coined this "EUWashing" — the physical location of the server does not change the legal jurisdiction of the operator.

Sources: [CLOUD Act and FISA 702: Is Your Cloud Truly Sovereign?](https://www.civo.com/blog/is-your-cloud-truly-sovereign), [Why the US Cloud Act is a Problem for Europe](https://xpert.digital/en/us-cloud-act/), [CLOUD Act - What It Means for EU Data Sovereignty](https://wire.com/en/blog/cloud-act-eu-data-sovereignty)

### 1.2 FISA Section 702

The Foreign Intelligence Surveillance Act Section 702 authorizes **warrantless surveillance** of non-US persons' communications. Combined with the CLOUD Act, this creates a legal environment where:

- EU data stored on US-owned infrastructure can be surveilled without a warrant
- No judicial oversight is required for non-US persons
- The FISA Court operates in secret — no transparency about scope or targets
- In April 2024, Congress **reauthorized and expanded** Section 702 powers through 2026

Source: [US Cloud Act, FISA and the Data Privacy Framework](https://www.comex.eu/wp-content/uploads/2025/04/EN-2025-03-Factcheck-US-Cloud-Act-v1.pdf)

### 1.3 EU-US Data Privacy Framework (DPF) — The Schrems III Risk

The current DPF (adopted July 2023) is the **third attempt** at a transatlantic data transfer framework:

| Framework | Adopted | Invalidated | Duration |
|-----------|---------|-------------|----------|
| Safe Harbor | 2000 | Oct 2015 (Schrems I) | 15 years |
| Privacy Shield | 2016 | Jul 2020 (Schrems II) | 4 years |
| Data Privacy Framework | 2023 | Pending (Schrems III) | 2+ years |

**Why Schrems III is likely:**
1. **PCLOB gutted**: Trump fired all three board members of the Privacy and Civil Liberties Oversight Board (PCLOB) on January 27, 2025. The PCLOB was a **foundational pillar** of the DPF — its oversight role was cited by the European Commission as justification for the adequacy decision. Without PCLOB, the DPF's legal basis is significantly weakened.
2. **Redress mechanism hollow**: The DPF's Data Protection Review Court depends on PCLOB for its functioning. With PCLOB non-operational, the redress mechanism that distinguishes the DPF from the invalidated Privacy Shield is effectively inoperative.
3. **Latombe challenge dismissed but more coming**: The European General Court dismissed Philippe Latombe's challenge in July 2024 on procedural grounds (standing), not on substance. Max Schrems and NOYB have indicated a substantive challenge is being prepared.
4. **FTC leadership changes**: Structural changes to the Federal Trade Commission, which was expected to enforce DPF compliance, add further uncertainty.

Sources: [What the PCLOB Firings Mean for the EU-US DPF](https://cdt.org/insights/what-the-pclob-firings-mean-for-the-eu-us-data-privacy-framework/), [Schrems III Is Coming. Are You Prepared?](https://shardsecure.com/blog/schrems-iii-prepared), [Schrems Addresses Emerging Questions Around DPF](https://iapp.org/news/a/schrems-addresses-emerging-questions-around-eu-us-data-privacy-framework)

### 1.4 The Data Act (2024) and NIS2 Directive

The EU Data Act (effective September 2025) includes provisions on:
- **Free switching** between cloud services (Articles 23-31)
- **International data transfers**: safeguards against unlawful government access (Article 32)
- **Interoperability requirements**: open standards for data portability

The NIS2 Directive (effective October 2024) grants member states power to require certain "essential entities" to use only certified cloud providers — potentially EU-certified under EUCS.

### 1.5 UK Post-Brexit Data Adequacy

The UK's data adequacy status was **renewed** in 2025 following the adoption of the Data (Use and Access) Act 2025 (DUAA). However, the UK's own data transfer arrangements with the US face similar vulnerabilities to the DPF if Schrems III succeeds, potentially creating a **cascading adequacy crisis**.

Key risk: Full DUAA implementation extends into 2026, and the adequacy decision remains subject to periodic review.

Source: [UK Data Adequacy Renewed (Arnold & Porter)](https://www.arnoldporter.com/en/perspectives/advisories/2025/07/uk-remains-adequate-following-intro-of-duaa-2025)

---

## 2. Geopolitical Risk Factors {#2-geopolitical-risk-factors}

### 2.1 Executive Orders and Presidential Discretion

On February 21, 2025, President Trump issued a memorandum authorizing tariffs on countries "hindering American companies' global competitiveness." The memorandum specifically targets "foreign legal regimes that limit cross-border data flows" — a direct attack on EU data localization measures.

Source: [Trump Takes Aim at 'Overseas Extortion' of American Tech Companies](https://www.iss.europa.eu/publications/commentary/trump-takes-aim-overseas-extortion-american-tech-companies-eu-us-rift)

### 2.2 Section 301 Trade Investigation

The Trump administration is preparing a **Section 301 investigation** under the Trade Act of 1974 — the same mechanism used against China — targeting EU tech regulations (DMA, DSA). This authorizes punitive tariffs, quotas, or restrictions on European companies operating in American markets.

**Named retaliation targets** include: Spotify, DHL, Accenture, Siemens, SAP, Amadeus IT Group, Capgemini, Publicis Groupe, and Mistral AI.

The USTR warned in December 2025 that the US would deploy "every tool at its disposal" to counter what it calls discriminatory EU measures, with Trump threatening "immediate and substantial retaliation" against EU tech enforcement plans for 2026.

**Implication for music attribution**: Spotify is a named target. Any music attribution infrastructure that depends on US cloud providers could face collateral disruption if trade tensions escalate to cloud service restrictions.

Sources: [EU-US Tech Regulation Clash Intensifies](https://europeanbusinessmagazine.com/business/eu-us-tech-regulation-clash-intensifies-as-trump-administration-threatens-retaliation/), [Trump Administration Threatens EU Tech Retaliation (Fortune)](https://fortune.com/2025/12/17/trump-administration-threatens-eu-tech-regulations-retaliation-dma-dsa-digital-markets-services-act/)

### 2.3 Political Weaponization of Cloud Infrastructure

The risk is not theoretical. Cloud infrastructure controlled by companies subject to US jurisdiction can be:
- **Cut off** by executive order (TikTok divestiture precedent)
- **Throttled** through export control additions
- **Surveilled** under FISA 702 with no notification
- **Weaponized** as leverage in trade disputes

97% of German companies say the country of origin influences cloud selection, and 78% believe they are overly dependent on US cloud providers (Bitkom Cloud-Report 2025).

The European Council on Foreign Relations published "Get over your X: A European plan to escape American technology," calling for systematic de-risking from US tech dependencies.

Source: [ECFR: Get Over Your X](https://ecfr.eu/publication/get-over-your-x-a-european-plan-to-escape-american-technology/)

### 2.4 Supply Chain Dependency Depth

True sovereignty requires independence across the entire stack:

| Layer | EU-sovereign? | Notes |
|-------|---------------|-------|
| Semiconductors | Partial | ASML (NL) makes the machines; TSMC/Samsung manufacture |
| OS/Kernel | Yes | Linux (Finnish origin, global development) |
| Hypervisor | Yes | KVM, QEMU (open source) |
| Container runtime | Yes | containerd, CRI-O (open source) |
| Cloud platform | Yes | Hetzner, OVH, Scaleway, UpCloud are EU-owned |
| Database | Yes | PostgreSQL (open source, no vendor lock-in) |
| Object storage | Partial | Cloudflare R2 is US-owned; Hetzner/OVH alternatives exist |
| CDN | Partial | Cloudflare/Fastly are US; bunny.net (EU) is smaller |
| DNS | Partial | Most registrars are US-owned; Gandi (FR) exists |

---

## 3. European Cloud Provider Landscape {#3-european-cloud-provider-landscape}

### 3.1 Tier 1: Production-Ready EU-Sovereign IaaS

#### Hetzner (Germany)

| Attribute | Details |
|-----------|---------|
| **HQ** | Gunzenhausen, Germany |
| **Data Centers** | Falkenstein (FSN1), Nuremberg (NBG1), Helsinki (HEL1), Ashburn VA, Hillsboro OR, Singapore |
| **EU-only DC locations** | Germany (2), Finland (1) |
| **Revenue** | ~EUR 400M+ |
| **Pricing** | Starts at EUR 3.49/month (CX23: 2 vCPU, 4 GB RAM) |
| **Object Storage** | S3-compatible, EUR 4.90/month for 1 TB (1 TB egress included) |
| **Managed Databases** | PostgreSQL, MySQL, Redis from EUR 4.90/month |
| **GPU** | NVIDIA RTX 4000 SFF Ada ($0.34/hr), RTX 6000 Ada ($1.54/hr) |
| **Traffic** | 20+ TB egress included on most plans |
| **Kubernetes** | No native managed K8s; Ubicloud, Syself, kOps as overlays |
| **Certifications** | ISO 27001 |
| **Key strength** | Unbeatable price-performance ratio; 20+ TB free egress |
| **Key weakness** | Limited managed services; no native K8s |

#### OVHcloud (France)

| Attribute | Details |
|-----------|---------|
| **HQ** | Roubaix, France |
| **Data Centers** | 43 across 9 countries, 450,000+ servers |
| **Revenue** | Surpassed EUR 1 billion in FY 2025 |
| **SecNumCloud** | Qualified (3.2) on Bare Metal Pod |
| **Sovereignty Roadmap** | IaaS under SecNumCloud in early 2026; managed K8s/DB by end of 2026 |
| **Services** | Full IaaS/PaaS stack; VMware compatibility; object storage ~1/3 AWS price |
| **Key strength** | Most mature EU alternative; 1.6M customers; SecNumCloud certified |
| **Key weakness** | Suffered 2021 data center fire (SBG2); large but still gaps vs hyperscalers |

#### Scaleway (France / Iliad Group)

| Attribute | Details |
|-----------|---------|
| **HQ** | Paris, France (subsidiary of Iliad Group) |
| **Data Centers** | France, Netherlands, Poland; 65 PoPs worldwide |
| **GPU** | NVIDIA H100, L40S, L4, GH200 (strongest EU GPU offering) |
| **Serverless** | Functions, containers, queues (Lambda/SQS-like) |
| **PaaS partnership** | Joint PaaS with Clever Cloud on DC5 (carbon-neutral) |
| **Key strength** | Most AWS-like breadth among EU providers; strong GPU/AI infra |
| **Key weakness** | Fewer data center locations than OVH/UpCloud |

#### UpCloud (Finland)

| Attribute | Details |
|-----------|---------|
| **HQ** | Helsinki, Finland |
| **Founded** | 2011 by Joel Pihlajamaa |
| **Data Centers** | 13 across 4 continents (10 in Europe: FI, SE, DK, NO, NL, DE, UK, ES, PL) |
| **Revenue** | $20.4M in 2024 (89% YoY growth) |
| **Employees** | 51-200 |
| **SLA** | **99.999% with 50x compensation** (industry-leading) |
| **Managed Services** | PostgreSQL, MySQL, Redis, OpenSearch, Kubernetes (CNCF certified) |
| **Object Storage** | S3-compatible, ~$23.72/month per TB |
| **GPU** | NVIDIA L40S (from $1.32/hr) |
| **Certifications** | ISO 27001, CISPE, SOC 2, NIS2 aligned, DORA aligned |
| **Key strength** | Broadest EU DC coverage (10 locations); managed PG+K8s; 99.999% SLA |
| **Key weakness** | 5-17x more expensive than Hetzner for compute; small company risk |

**UpCloud vs Hetzner**: UpCloud is the "step up" from Hetzner — you pay significantly more but get managed databases, managed Kubernetes, a stronger SLA (99.999% vs 99.9%), broader EU compliance (CISPE, NIS2, DORA), and more European data center locations (10 vs 3 in EU).

| Dimension | UpCloud | Hetzner |
|-----------|---------|---------|
| Medium VM (4 vCPU, 8GB) | ~$62/month | ~$7/month |
| Managed PostgreSQL (2 vCPU) | ~$71/month | ~EUR 5/month |
| Object Storage (1 TB) | ~$24/month | ~EUR 5/month |
| SLA | 99.999% (50x compensation) | 99.9% |
| EU data centers | 10 | 3 |
| Certifications | ISO 27001, CISPE, NIS2, DORA | ISO 27001 |

### 3.2 Tier 2: EU-Sovereign PaaS / Managed Services

| Provider | Country | Focus | Key Differentiator |
|----------|---------|-------|-------------------|
| **Clever Cloud** | France (Nantes) | PaaS | ISO 27001/HDS; deploys on Scaleway, Cloud Temple, IONOS |
| **Scalingo** | France | PaaS | Close to Heroku; ISO 27001/HDS; EU hosting |
| **STACKIT** | Germany | IaaS/PaaS | Backed by Schwarz Group (Europe's largest retailer) |
| **Open Telekom Cloud** | Germany | IaaS/AI | Deutsche Telekom; Industrial AI Cloud with 10K NVIDIA GPUs |
| **IONOS** | Germany | IaaS | Former 1&1 Internet; broad services; complex cancellation |
| **Ubicloud** | Open source (Y Combinator) | IaaS overlay | Managed K8s + PG on Hetzner; 3-10x cheaper than hyperscalers |

### 3.3 Tier 3: Niche / Regional

| Provider | Country | Notes |
|----------|---------|-------|
| **Exoscale** | Austria (A1 Telekom) | 7 DCs; managed Kafka, OpenSearch, Grafana |
| **ELASTX** | Sweden | 3 Stockholm DCs; OpenStack; sustainability focus |
| **Cleura** | Sweden (ex-City Network) | Compliant cloud for regulated industries |
| **Infomaniak** | Switzerland (Geneva) | Broad SME services; Swiss data protection |
| **Atlas Cloud** | Iceland | CloudStack-based; green energy |
| **Nine** | Switzerland (Zurich) | Application platform (Deploio) |
| **Bunny.net** | EU | CDN with S3-compatible storage; edge computing |
| **Cloud Temple** | France | First Gaia-X Label Level 3 certified; SecNumCloud qualified |

### 3.4 The "Lumber Not Furniture" Problem

A recurring criticism from the developer community (across multiple HN threads): European providers sell **raw infrastructure** (VMs, block storage, networking) but lack the **managed services layer** that makes hyperscalers sticky:

- No equivalent auto-scaling groups
- No serverless compute comparable to Lambda
- No managed AI/ML pipelines at hyperscaler maturity
- Limited self-healing infrastructure
- Fewer developer experience tools

However, this gap is **narrowing**:
- Ubicloud adds managed K8s + PostgreSQL on Hetzner
- Scaleway offers functions, containers, queues (Lambda/SQS equivalents)
- Clever Cloud provides Heroku-like PaaS on EU infrastructure
- UpCloud added managed K8s, PostgreSQL, Redis, OpenSearch

### 3.5 The Free Tier Lock-In Strategy

US hyperscalers employ a deliberate loss-leader strategy that EU providers cannot match:

- AWS, GCP, and Azure offer generous free tiers (sometimes years of free usage)
- Developers build on free tiers, then organizations inherit vendor lock-in
- European providers typically charge from day one
- University partnerships provide free credits, creating a pipeline of vendor-locked graduates

This creates asymmetric competition. The scaffold's Docker-based architecture is the key mitigation: the same Docker image deploys on any provider, reducing switching costs to configuration changes.

---

## 4. EU Sovereign Cloud Initiatives {#4-eu-sovereign-cloud-initiatives}

### 4.1 EUCS (European Cloud Services Certification Scheme)

Politically deadlocked. Earlier drafts included explicit sovereignty requirements (EU headquarters, EU ownership/control) at the highest certification level that would have excluded US hyperscalers. These were removed in March 2024 under lobbying pressure. Reintroduction is possible through:

- The **Cybersecurity Act revision** (scheduled late 2025) adding "non-technical risk factors"
- The **EU Cloud and AI Development Act (CADA)** establishing EU-wide eligibility requirements
- Individual **member state complementary legislation**

While participation is formally voluntary, NIS2 grants member states power to require certain entities to use only EUCS-certified providers.

### 4.2 SecNumCloud (France) — The Gold Standard

France's ANSSI-administered SecNumCloud 3.2 is the most mature sovereignty certification:

- **S3NS** (Google/Thales): Received SecNumCloud 3.2 for "Premi3ns" trusted cloud. Google cannot hold >24% of share capital or >39% collectively. Three Paris data centers.
- **Bleu** (Microsoft/Capgemini/Orange): Launched commercial operations. Pursuing SecNumCloud 3.2. Orange migrating 70% of IT to Bleu.
- **OVHcloud**: SecNumCloud qualified on Bare Metal Pod. Full IaaS under SecNumCloud in early 2026.
- **Cloud Temple**: First Gaia-X Label Level 3 certified provider.

### 4.3 Deutsche Telekom T Cloud Public

Positions as "Europe's #1 sovereign cloud":
- Currently delivers 80% of core hyperscaler features; targeting parity by end of 2026
- **Industrial AI Cloud** launched February 2026 — Europe's largest sovereign AI infrastructure with 10,000 NVIDIA AI processors
- Broke ties with both Huawei and US Big Tech for its sovereign cloud stack

### 4.4 Gaia-X — Lessons from Failure

Gaia-X has moved from a failed infrastructure initiative to an operational governance framework:
- 180+ data spaces being developed for secure data sharing
- Trust labels at three levels (Level 3 = full sovereignty)
- Cloud Temple achieved Level 3 certification

However, Gaia-X's real value is as a **certification and interoperability standard**, not a cloud provider. The original ambition to build a European hyperscaler-equivalent failed due to bureaucratic process consuming resources that should have built technology.

---

## 5. Music Attribution: Sovereignty-Sensitive Components {#5-music-attribution-sovereignty-sensitive-components}

The music attribution scaffold has **four components with distinct sovereignty sensitivity**:

### 5.1 MCP Consent Infrastructure (CRITICAL)

The MCP permission patchbay handles machine-readable permission queries for AI training rights. This creates the most sovereignty-sensitive data:

- **Consent records**: who gave permission for what — clearly PII + contractual data
- **Permission query logs**: which AI systems asked about which works — business-sensitive
- **Rights assertions**: who claims ownership of what — legal documents

This data cannot be stored in a jurisdiction where the CLOUD Act could compel disclosure. The consent infrastructure is the **single most sovereignty-sensitive component** of the scaffold.

### 5.2 Artist Identity Data (HIGH)

Artist data qualifies as personal data under GDPR depending on context:
- ISNI identifiers, artist names, performer credits = PII
- The scaffold's A3 (Artist-verified) assurance level requires storing artist-verified identity assertions
- A2 (Multiple sources) requires cross-referencing identity data from multiple databases
- Both levels create datasets that are unambiguously personal data

Source: [GDPR Music Data Ownership (Music Tomorrow)](https://www.music-tomorrow.com/blog/gdpr-music-data-ownership-should-we-treat-artist-data-as-personal-data)

### 5.3 Audio Fingerprints and Embeddings (MODERATE)

Audio fingerprints and pgvector embeddings derived from creative works fall under both copyright and data protection regimes. Under the EU AI Act (effective August 2025), training data used for ML/embedding pipelines has transparency requirements.

### 5.4 Application Code and Frontend (LOW)

The FastAPI backend, Next.js frontend, and infrastructure configuration have no sovereignty sensitivity. These can run on any provider.

### Sovereignty Sensitivity Summary

| Component | Sensitivity | Recommendation |
|-----------|-------------|----------------|
| MCP consent infrastructure | CRITICAL | EU-sovereign only, no US jurisdictional exposure |
| Artist identity database | HIGH | EU-sovereign PostgreSQL (Hetzner, OVH, UpCloud, Neon) |
| Audio fingerprints / embeddings | MODERATE | EU-preferred, Cloudflare R2 acceptable for non-PII audio |
| Application code / frontend | LOW | Any provider acceptable |

---

## 6. Provider Comparison Matrix {#6-provider-comparison-matrix}

### 6.1 Sovereignty Assessment

| Provider | HQ | CLOUD Act Exposure | EU Data Centers | Sovereignty Rating |
|----------|-----|-------------------|-----------------|-------------------|
| **Hetzner** | Germany | None | 3 (DE x2, FI) | Sovereign |
| **OVHcloud** | France | None | 30+ (EU only) | Sovereign (SecNumCloud) |
| **Scaleway** | France | None | 3 (FR, NL, PL) | Sovereign |
| **UpCloud** | Finland | None | 10 (EU/EEA) | Sovereign (CISPE) |
| **Cloudflare** | USA | **Yes** | EU PoPs exist | Exposed |
| **Render** | USA | **Yes** | US-only | Exposed |
| **Railway** | USA | **Yes** | US-only | Exposed |
| **Fly.io** | USA | **Yes** | EU regions exist | Exposed |
| **Neon** | USA | **Yes** | EU regions (Frankfurt) | Exposed |
| **Vercel** | USA | **Yes** | EU edge PoPs | Exposed |
| **AWS** | USA | **Yes** | eu-central-1 etc. | Exposed (despite "sovereign cloud") |

### 6.2 Music Attribution Workload Fit

| Provider | Managed PG | pgvector | K8s | Object Storage | Docker Deploy | Score |
|----------|-----------|----------|-----|----------------|--------------|-------|
| Hetzner + Ubicloud | Yes (Ubicloud) | Yes | Yes (Ubicloud) | S3-compat | Kamal 2 | 5/5 |
| OVHcloud | Coming 2026 | Coming 2026 | Yes | Yes | Docker | 4/5 |
| UpCloud | Yes | Yes | Yes (CNCF) | S3-compat | Docker | 5/5 |
| Scaleway | Yes | Yes | Yes | S3-compat | Docker | 5/5 |
| Render | Yes | Yes | No | No | Git push | 3/5 |
| AWS ECS | Yes (RDS) | Yes | Yes (EKS) | S3 | Docker | 5/5 |

---

## 7. Cost Analysis: EU-Sovereign vs Hyperscaler {#7-cost-analysis}

### 7.1 Basic Music Attribution Stack (Monthly)

| Component | AWS eu-central-1 | Hetzner DE | UpCloud FI | Savings (Hetzner) |
|-----------|------------------|------------|------------|-------------------|
| Compute (2 vCPU, 4 GB) | ~EUR 30/month | EUR 3.49/month | ~$45/month | ~88% |
| PostgreSQL (managed) | ~EUR 50/month | EUR 4.90/month | ~$71/month | ~90% |
| Object Storage (1 TB) | ~EUR 25/month | EUR 4.90/month | ~$24/month | ~80% |
| Egress (1 TB) | ~EUR 90 | Included (20 TB) | ~$10/month | ~100% |
| **Total** | **~EUR 195/month** | **~EUR 13.29/month** | **~$150/month** | **~93%** |

### 7.2 UpCloud Price Positioning

UpCloud occupies a specific niche: "more managed than Hetzner, more European than AWS, more focused than OVHcloud":

| Aspect | Hetzner | UpCloud | AWS |
|--------|---------|---------|-----|
| Price | Budget leader | Mid-tier (5-17x Hetzner) | Premium |
| Managed services | Minimal | Good (PG, K8s, Redis) | Comprehensive |
| SLA | 99.9% | 99.999% | 99.99% |
| EU compliance | ISO 27001 | ISO 27001, CISPE, NIS2, DORA | SOC 2, ISO |
| CLOUD Act | No | No | **Yes** |

### 7.3 European Clouds vs US Clouds at Scale

European cloud vendors' prices are approximately 60% of US cloud prices. OVHcloud saves ~63% compared to AWS in comparable configurations.

At 100TB/month egress (relevant for audio-serving workloads), the differences are dramatic:

| Provider | Monthly Egress Cost |
|----------|-------------------|
| Cloudflare R2 | $0 |
| Hetzner Object Storage | ~EUR 100 |
| AWS S3 | ~$9,000 |
| Azure Blob | ~$8,700 |

Source: [Cloud Alternatives to AWS/Azure 2026](https://www.devilink-consulting.com/en/blog/cloud-alternatives-aws-azure-2026)

---

## 8. Risk Assessment Matrix {#8-risk-assessment-matrix}

| Risk Factor | Severity | Likelihood (by 2027) | Impact on Scaffold | Mitigation |
|-------------|----------|---------------------|---------------------|------------|
| Schrems III invalidates DPF | Critical | Medium-High | All US-hosted PII exposed | EU-sovereign infrastructure from day one |
| CLOUD Act compelled disclosure | High | Ongoing | MCP consent data, artist PII | Non-US-owned cloud provider |
| Trump executive order disrupts EU tech | High | Medium | Service availability risk | No dependency on US-controlled infrastructure |
| FISA 702 surveillance of EU data | High | Ongoing (expanded) | Artist identity data exposed | EU-sovereign storage + encryption |
| Section 301 tariffs on EU tech | Medium | Medium-High | Indirect — Spotify is a named target | Diversified supply chain |
| EUCS excludes non-EU at high levels | Medium | Medium | Regulatory tailwind for EU providers | Already using EU providers |
| UK loses data adequacy | Low-Medium | Low (renewed) | UK artist data handling | Treat UK data with EU-level care |
| EU provider acquisition by US company | Low | Low | Loss of sovereignty status | Multi-provider strategy |
| Hetzner/OVH outage (single provider risk) | Medium | Medium | Service downtime | Multi-region, multi-provider |

---

## 9. Recommendations for the Scaffold {#9-recommendations}

### 9.1 Sovereignty-Aware Deployment Architecture

```
SOVEREIGNTY TIERS

Tier 1: EU-Sovereign Only (CRITICAL data)
├── MCP consent infrastructure → Hetzner + Ubicloud managed PG (Germany)
├── Artist identity database   → Same PG instance, EU data centers only
└── Permission query logs      → Same PG instance

Tier 2: EU-Preferred (MODERATE data)
├── Audio fingerprints         → Hetzner Object Storage (EU) OR Cloudflare R2
├── pgvector embeddings        → Same PG as Tier 1
└── API responses/caching      → Cloudflare R2 acceptable (non-PII)

Tier 3: Any Provider (LOW sensitivity)
├── Frontend (Next.js)         → Vercel, Render, or Hetzner
├── CI/CD                      → GitHub Actions (code is public)
└── CDN                        → Cloudflare (content delivery, not data storage)
```

### 9.2 Phased Migration with Sovereignty Awareness

| Phase | Stack | Sovereignty Status |
|-------|-------|--------------------|
| MVP (0-6 months) | Render + Neon (Frankfurt) + R2 | **Partial** — US providers, EU data centers |
| Growth (6-18 months) | Hetzner + Ubicloud managed PG + R2 | **Sovereign** (compute + DB) |
| Scale (18+ months) | Multi-region Hetzner + OVH/UpCloud backup | **Fully sovereign** |

**Key principle**: The MVP phase on Render/Neon is acceptable because (a) the scaffold is open-source research code, not production rights infrastructure, and (b) Neon's Frankfurt region provides physical EU residency even if legal sovereignty is incomplete. When the scaffold graduates to production use handling real artist data, the migration to EU-sovereign infrastructure should be prioritized.

### 9.3 Cloudflare R2: The Sovereignty Tension

Cloudflare R2 is recommended for egress cost optimization (zero egress fees), but Cloudflare is US-headquartered and subject to the CLOUD Act. Mitigation:

- **Non-PII audio** (previews, waveforms): R2 acceptable — content delivery is less sovereignty-sensitive
- **PII/consent data**: Never on R2 — use Hetzner Object Storage (EUR 4.90/TB)
- **Long-term**: Monitor Hetzner Object Storage egress pricing evolution; if egress costs drop, eliminate R2 dependency

### 9.4 UpCloud as Premium EU Alternative

For teams that need managed services + EU sovereignty but find Hetzner's bare-bones approach insufficient:

- **Use case**: Managed PostgreSQL + Kubernetes without self-hosting
- **Trade-off**: 5-17x compute premium vs Hetzner, comparable to AWS pricing
- **Best fit**: Teams prioritizing 99.999% SLA and broad EU compliance (CISPE, NIS2, DORA) over cost optimization

### 9.5 PRD Update: Add Sovereignty-Conscious Archetype

The probabilistic PRD should add:
1. A `sovereignty_conscious_eu` archetype in `compute-platform.decision.yaml`
2. Geopolitical change drivers to the volatility section
3. Jurisdictional constraints on US-headquartered options

---

## 10. Impact on Probabilistic PRD {#10-impact-on-prd}

### 10.1 New Archetype: `sovereignty_conscious_eu`

```yaml
sovereignty_conscious_eu:
  probability_overrides:
    render: 0.05           # US-owned, MVP-only
    vercel_plus_backend: 0.00  # US-owned
    railway: 0.00          # US-owned
    fly_io: 0.00           # US-owned
    hetzner_ubicloud: 0.45 # EU-sovereign, managed services
    hetzner_baremetal: 0.20 # EU-sovereign, maximum control
    aws_ecs: 0.05          # US-owned, only with sovereign cloud variant
    upcloud: 0.15          # EU-sovereign, managed services, premium
    ovhcloud: 0.10         # EU-sovereign, SecNumCloud certified
  rationale: >
    EU data sovereignty is a hard requirement. Only EU-owned providers
    acceptable for production. Render acceptable for MVP-only phase.
    Hetzner+Ubicloud is the optimal balance of sovereignty + cost.
```

### 10.2 New Change Drivers

```yaml
change_drivers:
  # Existing drivers...
  - "Schrems III challenge to EU-US Data Privacy Framework"
  - "Section 301 US trade investigation targeting EU tech"
  - "EUCS certification scheme sovereignty requirements"
  - "PCLOB restoration or permanent dissolution"
  - "EU Cloud and AI Development Act (CADA) provisions"
```

### 10.3 New Options to Consider

| Option | Prior Probability | Rationale |
|--------|-------------------|-----------|
| `upcloud` | 0.05 | EU-sovereign, managed PG+K8s, 99.999% SLA, premium pricing |
| `ovhcloud` | 0.05 | EU-sovereign, SecNumCloud, largest EU provider, 43 DCs |
| `scaleway` | 0.03 | EU-sovereign, strongest GPU/AI, serverless functions |

These could be added as new options to `compute-platform.decision.yaml` in a future PRD update (v2.2.0).

---

## Appendix A: european.cloud Directory (Feb 2026)

The [european.cloud](https://european.cloud/) directory lists 11 EU-headquartered cloud providers across 8 countries:

| Provider | Country | Focus |
|----------|---------|-------|
| OVHcloud | France | Full-stack IaaS/PaaS |
| STACKIT | Germany | IaaS/PaaS (Schwarz Group) |
| Cyso Cloud | Netherlands | OpenStack IaaS |
| Open Telekom Cloud | Germany | IaaS/AI (Deutsche Telekom) |
| IONOS | Germany | IaaS/VPC |
| Scaleway | France | IaaS/AI/Serverless |
| UpCloud | Finland | IaaS/Managed Services |
| Exoscale | Austria | IaaS/Managed Kafka |
| ELASTX | Sweden | OpenStack IaaS |
| Nine | Switzerland | Application platform |
| Atlas Cloud | Iceland | Green energy IaaS |

**Notable absence**: Hetzner is not listed on european.cloud despite being the most frequently recommended EU alternative in developer communities.

---

## Appendix B: Reviewer Agent Insights

### Geopolitical Risk Reviewer

- The CLOUD Act + FISA 702 combination creates an **impossible compliance situation** for EU organizations using US cloud providers — no amount of contractual safeguards resolves the fundamental jurisdictional conflict
- Schrems III is not a question of "if" but "when" — the structural preconditions (PCLOB dismantling, FTC changes) have already occurred
- The Section 301 investigation targeting Spotify makes cloud sovereignty directly relevant to the music industry, not an abstract legal concern
- 97% of German companies already factor country of origin into cloud decisions (Bitkom 2025)

### Cost Optimization Reviewer

- EU-sovereign infrastructure is **cheaper**, not more expensive — Hetzner at EUR 13/month vs AWS at EUR 195/month for equivalent stack
- UpCloud fills the "managed services gap" but at a premium — evaluate whether the team needs managed PostgreSQL or can use Ubicloud on Hetzner
- The Cloudflare R2 recommendation creates a sovereignty tension that should be explicitly acknowledged in architecture decisions
- Hetzner's 20 TB free egress eliminates the need for R2 in most scaffold scenarios

### Music Domain Reviewer

- Artist data as personal data under GDPR is not hypothetical — ISNI, performer credits, and consent records are unambiguously PII
- The MCP consent infrastructure is the **sovereignty crown jewel** — it records who gave AI training permission for what works, making it both commercially sensitive and privacy-regulated
- European music rights organizations (PRS, STIM, GEMA, SACEM) increasingly require EU data residency for rights data processing
- The Imogen Heap / Auracles consent model relies on data sovereignty — the entire consent delegation chain must be EU-sovereign to be credible

### Architecture Reviewer

- The Docker-based architecture is the critical enabler — same container image runs on Render (MVP), Hetzner (growth), or UpCloud (premium), making sovereignty migration a configuration change, not a rewrite
- Separating sovereignty tiers (Critical/Moderate/Low) prevents over-engineering — the frontend and CI/CD can remain on US providers without sovereignty risk
- Consider adding a `SOVEREIGNTY_MODE` environment variable that switches database connection strings and storage backends between US-hosted (MVP) and EU-sovereign (production) configurations
- The Pulumi IaC approach supports all EU providers (Hetzner provider v1.32.0, UpCloud via bridged Terraform provider)

---

## Appendix C: Source Index

### Legal & Regulatory

| Source | URL |
|--------|-----|
| CLOUD Act and FISA 702: Is Your Cloud Truly Sovereign? | https://www.civo.com/blog/is-your-cloud-truly-sovereign |
| US Cloud Act, FISA and the Data Privacy Framework | https://www.comex.eu/wp-content/uploads/2025/04/EN-2025-03-Factcheck-US-Cloud-Act-v1.pdf |
| Why the US Cloud Act is a Problem for Europe | https://xpert.digital/en/us-cloud-act/ |
| CLOUD Act — What It Means for EU Data Sovereignty | https://wire.com/en/blog/cloud-act-eu-data-sovereignty |
| What the PCLOB Firings Mean for the EU-US DPF | https://cdt.org/insights/what-the-pclob-firings-mean-for-the-eu-us-data-privacy-framework/ |
| Schrems III Is Coming. Are You Prepared? | https://shardsecure.com/blog/schrems-iii-prepared |
| EUCS Controversial Sovereignty Issues | https://www.hoganlovells.com/en/publications/eucs-controversial-data-sovereignty-issues |
| EU Cloud Service Restrictions (ITIF) | https://itif.org/publications/2025/05/25/eu-cloud-service-restrictions/ |
| UK Data Adequacy Renewed | https://www.arnoldporter.com/en/perspectives/advisories/2025/07/uk-remains-adequate-following-intro-of-duaa-2025 |
| EU AI Act 2026 Compliance Guide | https://secureprivacy.ai/blog/eu-ai-act-2026-compliance |

### Geopolitical

| Source | URL |
|--------|-----|
| Trump Takes Aim at 'Overseas Extortion' of American Tech | https://www.iss.europa.eu/publications/commentary/trump-takes-aim-overseas-extortion-american-tech-companies-eu-us-rift |
| EU-US Tech Regulation Clash Intensifies | https://europeanbusinessmagazine.com/business/eu-us-tech-regulation-clash-intensifies-as-trump-administration-threatens-retaliation/ |
| Trump Administration Threatens EU Tech Retaliation (Fortune) | https://fortune.com/2025/12/17/trump-administration-threatens-eu-tech-regulations-retaliation-dma-dsa-digital-markets-services-act/ |
| ECFR: Get Over Your X | https://ecfr.eu/publication/get-over-your-x-a-european-plan-to-escape-american-technology/ |
| Section 301 and EU Tech Enforcement | https://europeanbusinessmagazine.com/european-news/eu-prepares-tougher-tech-enforcement-in-2026-as-trump-warns-of-retaliation/ |
| Digital Sovereignty of Europe (2026 Guide) | https://gartsolutions.com/digital-sovereignty-of-europe/ |

### European Cloud Providers

| Source | URL |
|--------|-----|
| European Cloud Providers Directory | https://european.cloud/ |
| Hetzner VPS Pricing Calculator | https://costgoat.com/pricing/hetzner |
| OVHcloud SecNumCloud Strategy | https://corporate.ovhcloud.com/en/newsroom/news/secnumcloud-strategy-acceleration/ |
| Scaleway GPU Pricing | https://www.scaleway.com/en/pricing/gpu/ |
| UpCloud European Cloud Hosting | https://upcloud.com/solutions/european-cloud/ |
| UpCloud Compliance and Security | https://upcloud.com/compliance-and-security/ |
| Ubicloud: Open Source Alternative to AWS | https://www.ubicloud.com/ |
| Clever Cloud Sovereign PaaS | https://www.clever.cloud/blog/company/2025/10/03/best-european-cloud-providers/ |
| Cloud Alternatives to AWS/Azure 2026 | https://www.devilink-consulting.com/en/blog/cloud-alternatives-aws-azure-2026 |

### Sovereign Cloud Initiatives

| Source | URL |
|--------|-----|
| S3NS SecNumCloud Certification | https://www.efficientlyconnected.com/s3ns-secnumcloud-3-2-certification-marks-a-milestone-for-sovereign-cloud-in-france/ |
| Bleu Sovereign Cloud Launch | https://www.datacenterdynamics.com/en/news/orange-capgemini-to-finally-launch-bleu-sovereign-cloud-service/ |
| Deutsche Telekom T Cloud Public Expansion | https://www.telekom.com/en/media/media-information/archive/t-cloud-public-sovereign-power-1101542 |
| Cloud Temple Gaia-X Label Level 3 | https://www.cloud-temple.com/en/press-releases/digital-sovereignty-cloud-temple-becomes-the-first-european-player-to-be-certified-gaia-x-label-level-3/ |

### Music Industry

| Source | URL |
|--------|-----|
| GDPR Music Data Ownership | https://www.music-tomorrow.com/blog/gdpr-music-data-ownership-should-we-treat-artist-data-as-personal-data |
| Global Uncertainty Reshaping Cloud Strategies | https://www.computerworld.com/article/4109029/global-uncertainty-is-reshaping-cloud-strategies-in-europe.html |

### HN Discussion Threads

| Thread | URL |
|--------|-----|
| EU Cloud Independence (2025) | https://news.ycombinator.com/item?id=43318738 |
| EU Cloud Sovereignty Debate (2026) | https://news.ycombinator.com/item?id=45604672 |
| European Cloud Providers (2025) | https://news.ycombinator.com/item?id=43394087 |

---

*Document created: 2026-02-14 (v1.0)*
*Research based on 4 parallel agent investigations covering UpCloud, EU sovereignty landscape, HN community discussions, and existing FinOps documentation.*
*Next review: 2026-04-14*
