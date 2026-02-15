# Deployment & FinOps Landscape for Music Attribution Scaffold

**Status**: v2.0 — Comprehensive Multi-Hypothesis Analysis
**Created**: 2026-02-03 (v1.0)
**Updated**: 2026-02-14 (v2.0 — corrected complexity model, expanded provider coverage)
**Supersedes**: `finops-optimization-plan.md` (v1.0) — consolidated and corrected
**Target Audience**: Startup team of 2–4 engineers + 2–4 domain experts

---

## Executive Summary

This document provides a **corrected and comprehensive** deployment landscape analysis for the Music Attribution Scaffold, consolidating insights from 8+ reference documents and fresh web research (February 2026).

**Key correction from v1.0**: The original figure (`fig-choice-15`) incorrectly placed Hetzner bare-metal at the "low complexity" end of the spectrum. In reality:

| Provider | Cost | Complexity | DevOps Tax |
|----------|------|------------|------------|
| **Render** | Medium | **Lowest** | Near-zero |
| **Hetzner Cloud + Ubicloud** | Low–Medium | Medium | Low–Medium |
| **Hetzner bare-metal + K8s** | **Lowest** | **Highest** | High |
| **Big Three (AWS/GCP/Azure)** | High | Medium–High | Medium (managed) |

**Recommended path for a 2–4 engineer music startup**:

1. **MVP (months 0–6)**: Render + Neon PostgreSQL — ~€18–35/month, zero ops burden
2. **Growth (months 6–18)**: Hetzner Cloud + Ubicloud managed K8s/Postgres — ~€30–60/month
3. **Scale (18+ months)**: Multi-node Hetzner or credit-funded Big Three — ~€100–300/month

**Bayesian prior**: Hetzner preference is rational for a cost-aware, Docker-based, cloud-agnostic architecture. But the *path to Hetzner* matters — start on Render (easiest), migrate when the DevOps tax is justified by savings.

---

## Table of Contents

1. [Corrected Cost vs Complexity Model](#1-corrected-cost-vs-complexity-model)
2. [Provider Deep Dives](#2-provider-deep-dives)
3. [The DevOps Tax Framework](#3-the-devops-tax-framework)
4. [Multi-Hypothesis Scenarios (A–F)](#4-multi-hypothesis-scenarios-af)
5. [IaC Strategy: Pulumi](#5-iac-strategy-pulumi)
6. [Managed PostgreSQL Comparison](#6-managed-postgresql-comparison)
7. [Object Storage & Egress](#7-object-storage--egress)
8. [Cloud Credit Strategy](#8-cloud-credit-strategy)
9. [Container Orchestration Decision](#9-container-orchestration-decision)
10. [Local Development Parity](#10-local-development-parity)
11. [Exit Strategies & Portability](#11-exit-strategies--portability)
12. [Cost Projections by Phase](#12-cost-projections-by-phase)
13. [Recommendation & Confidence Estimates](#13-recommendation--confidence-estimates)
14. [Updated Figure Plan](#14-updated-figure-plan)
15. [Appendix A: Reference Sources](#appendix-a-reference-sources)
16. [Appendix B: Reviewer Agent Insights](#appendix-b-reviewer-agent-insights)

---

## 1. Corrected Cost vs Complexity Model

The v1.0 figure placed Hetzner at "low complexity, lowest cost." This is **wrong**. The corrected model:

```
        MONTHLY COST
           ^
           |
     €500+ |                              ┌──────────────┐
           |                              │ Big Three    │
           |                              │ AWS/GCP/Azure│
           |                              │ Full managed │
           |                              └──────────────┘
     €100  |                    ┌──────────┐
           |                    │ Fly.io   │
           |                    │ Global   │
           |                    │ Edge     │
      €50  |   ┌──────────┐    └──────────┘
           |   │ Render   │         ┌──────────────┐
           |   │ + Neon   │         │ Hetzner +    │
           |   │          │         │ Ubicloud K8s │
      €20  |   └──────────┘         └──────────────┘
           |                                    ┌──────────────┐
           |                                    │ Hetzner bare │
      €7   |                                    │ metal + K8s  │
           |                                    │ self-managed │
           |                                    └──────────────┘
           +────────────────────────────────────────────────> COMPLEXITY
          Minimal         Moderate        Significant       Expert
          (git push)      (Kamal/Pulumi)  (Managed K8s)     (Talos/K3s)
```

**Key insight**: There are now **two Hetzner paths**:

1. **Hetzner + Ubicloud** (managed K8s + managed Postgres) — moderate complexity, ~€20–50/month
2. **Hetzner bare-metal** (self-managed everything) — expert-level, ~€7–20/month

The Digital Society case study (76% savings migrating AWS→Hetzner) confirms the savings are real, but also documents significant complexity: Talos Linux, CloudNativePG, Ingress NGINX, ExternalDNS, cert-manager — all self-managed. Their team had **10 years of Kubernetes experience**.

---

## 2. Provider Deep Dives

### 2.1 Render — The Easiest Path

**What**: Managed PaaS with `git push` deployment, free tier, native Neon integration.

| Aspect | Details |
|--------|---------|
| **Free tier** | 512MB RAM, 100GB bandwidth, 1GB PostgreSQL (30-day expiry on free DB) |
| **Starter** | ~€6.50/month ($7), 512MB RAM |
| **Standard** | ~€23/month ($25), 2GB RAM |
| **Pro** | ~€46/month ($50), 4GB RAM |
| **CI/CD** | Native Git integration, auto-deploy on push |
| **IaC** | No Pulumi provider (use Render CLI + `render.yaml`) |
| **Lock-in risk** | Low — standard Docker containers |
| **SMTP change (2025)** | Free tier blocks outbound SMTP ports 25/465/587 |

**Best for**: MVP phase, musician-first teams, rapid iteration.

**Limitations**: No Pulumi provider means infrastructure is configured via `render.yaml` or dashboard, not code. Acceptable for MVP, but limits automation at scale.

### 2.2 Hetzner Cloud — The Cost Champion

**What**: European IaaS with dramatically lower compute costs than hyperscalers.

| Instance | vCPU | RAM | Storage | Monthly | vs AWS |
|----------|------|-----|---------|---------|--------|
| CX22 (shared) | 2 | 4 GB | 40 GB | **€3.79** | ~15× cheaper |
| CX32 (shared) | 4 | 8 GB | 80 GB | **€6.80** | ~10× cheaper |
| CAX21 (ARM) | 4 | 8 GB | 80 GB | **€7.49** | ~8× cheaper |
| CX42 (shared) | 8 | 16 GB | 160 GB | **€14.40** | ~7× cheaper |
| CCX23 (dedicated) | 4 | 16 GB | 80 GB | **€30.60** | ~5× cheaper |

**Two paths to Hetzner**:

#### Path A: Hetzner + Ubicloud (Managed — Recommended)

[Ubicloud](https://www.ubicloud.com/) provides an open-source AWS-alternative layer on Hetzner:

- **Managed Kubernetes**: Production-ready in <5 minutes, 2–3× cheaper than public cloud
- **Managed PostgreSQL**: pgvector supported, automated backups, failover
- **Availability**: Germany (Hetzner) and Virginia (US), preview as of Feb 2026
- **Pricing**: Pay only for nodes, no hidden networking/LB/egress fees
- **IaC**: No Pulumi provider yet (use Ubicloud CLI/API)

#### Path B: Hetzner bare-metal + self-managed K8s (Expert)

From the [Digital Society case study](https://digitalsociety.scot/migrating-to-hetzner/):
- Talos Linux + CloudNativePG + Ingress NGINX + ExternalDNS + cert-manager
- **Requires**: Experienced K8s operator (10+ years in their case)
- **Savings**: 76% vs AWS+DigitalOcean, 3.67× more capacity
- **Challenges**: Network zones ≠ availability zones, deployment automation complexity

**When to choose Path B over Path A**: Only when monthly spend exceeds €200+ AND team has dedicated DevOps capacity.

### 2.3 Big Three Hyperscalers — AWS, GCP, Azure

All three are viable but expensive. The scaffold's Docker-based architecture deploys identically on all.

#### Compute Pricing Comparison (2 vCPU, 4GB RAM equivalent)

| Provider | Service | Instance | Monthly | Notes |
|----------|---------|----------|---------|-------|
| **AWS** | ECS Fargate | 2 vCPU, 4GB | ~€70/mo | Spot: up to 70% discount |
| **AWS** | EC2 | t4g.medium | ~€56/mo | Graviton ARM |
| **GCP** | Cloud Run | 2 vCPU, 4GB | ~€45–65/mo | Scale-to-zero, per-request billing option |
| **GCP** | GKE | e2-medium | ~€55/mo | Free control plane, Autopilot mode |
| **Azure** | Container Apps | 2 vCPU, 4GB | ~€50–70/mo | 180K vCPU-seconds free/month |
| **Azure** | AKS | B2ms | ~€71/mo | Free control plane |

#### Managed PostgreSQL (2 vCPU, 4–8GB, 100GB storage)

| Provider | Service | Monthly | pgvector | Notes |
|----------|---------|---------|----------|-------|
| **AWS** | RDS db.t4g.medium | ~€48 + storage | Yes | 1yr reserved: ~€34 |
| **GCP** | Cloud SQL Enterprise | ~€65–85 | Yes | Scale-to-zero option emerging |
| **Azure** | Flexible B2s | ~€50–65 | Yes | Apache AGE also supported |

#### Egress Pricing (Critical for audio files)

| Provider | Free Tier | Per TB | Impact at 100GB/mo |
|----------|-----------|--------|---------------------|
| **AWS** | 100 GB | **$90** | ~$8/mo |
| **GCP** | 200 GB | **$85** | ~$0 (within free) |
| **Azure** | 100 GB | **$87** | ~$0 (within free) |
| **Hetzner** | 20–60 TB | **€1** | €0 |
| **Cloudflare R2** | Unlimited | **$0** | $0 |

**Egress is the hidden cost killer at scale**. For audio files (large payloads), Cloudflare R2 or Hetzner Object Storage are 80–100× cheaper than hyperscaler egress.

### 2.4 European Alternatives

| Provider | Type | Key Feature | Monthly (2 vCPU) | Notes |
|----------|------|-------------|-------------------|-------|
| **Scaleway** | IaaS+PaaS | EU sovereign, hourly billing | ~€44 | Paris, Amsterdam, Warsaw |
| **OVHcloud** | IaaS | OpenStack-based, EU | ~€20–40 | Best startup credits (€10K) |
| **Clever Cloud** | PaaS | EU PaaS, partnership with Scaleway | ~€30–50 | Auto-deploy, French company |
| **Fly.io** | Edge PaaS | Global edge deployment | ~€20–60 | Multi-region, Machines API |
| **Railway** | PaaS | Developer-friendly, usage-based | ~€5–20 | Good free tier, simpler than Render |
| **Northflank** | PaaS | Multi-cloud, K8s-native | ~€20–50 | Good DX, review environments |

### 2.5 Self-Hosting Platforms (on any VPS)

| Tool | Status | Best For | Concerns |
|------|--------|----------|----------|
| **Kamal 2** | Stable (v2.8+) | Simple Docker deploys to VPS | New Kamal Proxy (replaces Traefik), good secrets mgmt |
| **Coolify** | Patched (v4.0.0-beta.460+) | Heroku-like self-hosted | 11 critical CVEs disclosed Jan 2026, CVSS 9.4–10.0. Patches exist but trust requires caution |
| **Dokku** | Mature | Heroku clone on single server | Single-server only, no HA |
| **CapRover** | Mature | Docker Swarm GUI | Smaller community than alternatives |

**Recommendation**: Kamal 2 for Hetzner deployments. Coolify's security track record (11 critical vulnerabilities in a single disclosure) is a significant concern for a production music attribution system.

---

## 3. The DevOps Tax Framework

The "DevOps Tax" is the hidden cost of self-managing infrastructure. From the [FinOps analysis](../../dpp-agents/knowledge-base/documentation/infrastructure/deployment/rag-hosting-finops-comparison.md):

### Break-Even Calculation

```
Infrastructure savings (Hetzner vs AWS):  ~€150,000/year
Labor cost increase for self-management:   1.5 FTE × €120,000 = €180,000/year

Net at small scale: -€30,000 (LOSS)
```

**Break-even point**: ~2,000 vCPUs or >€200K annual infrastructure spend.

### DevOps Tax by Provider

| Provider | Self-Manage | Annual DevOps Tax | Break-Even Monthly Spend |
|----------|-------------|-------------------|--------------------------|
| **Render** | Nothing | €0 | N/A (fully managed) |
| **Ubicloud on Hetzner** | App deployment only | ~€5K (0.05 FTE) | N/A |
| **Kamal on Hetzner** | SSL, monitoring, backups | ~€15K (0.15 FTE) | ~€50/mo |
| **K8s on Hetzner** | Everything | ~€35K+ (0.25+ FTE) | ~€200/mo |
| **Big Three (managed)** | App deployment only | ~€5K (0.05 FTE) | N/A (but 5–10× compute cost) |

### When to Accept the DevOps Tax

| Monthly Infra Spend | Recommendation | Confidence |
|---------------------|----------------|------------|
| **<€50/mo** | Render/managed PaaS — DevOps tax exceeds savings | 95% |
| **€50–200/mo** | Consider Hetzner + Ubicloud — depends on team capacity | 70% |
| **€200–500/mo** | Hetzner + managed tools — savings justify effort | 80% |
| **>€500/mo** | Hetzner primary — clear TCO advantage | 90% |

### Self-Management Requirements Matrix

| Component | Render | Kamal+Hetzner | K8s+Hetzner | Big Three |
|-----------|--------|---------------|-------------|-----------|
| SSL/TLS | Auto | Kamal Proxy auto | cert-manager | Auto |
| Load Balancer | Auto | Kamal Proxy | Ingress NGINX | Auto (ALB/NLB) |
| Database | Managed (Neon) | External (Neon/Ubicloud) | CloudNativePG | Managed (RDS/Cloud SQL) |
| Monitoring | Built-in | Grafana Cloud free | OpenObserve/Prometheus | CloudWatch/Stackdriver |
| Backups | Auto | Manual/scripted | Manual/scripted | Auto |
| DNS | Auto | Manual (Cloudflare) | ExternalDNS | Route53/Cloud DNS |
| Zero-downtime deploys | Auto | Kamal built-in | Rolling update | Auto |

---

## 4. Multi-Hypothesis Scenarios (A–F)

### Scenario Matrix

| Scenario | Stack | Monthly Cost | Complexity | Best For |
|----------|-------|--------------|------------|----------|
| **A: Lean Managed** | Render + Neon + R2 | €0–35 | Minimal | MVP, rapid iteration |
| **B: Hybrid Hetzner** | Hetzner Cloud + Neon + R2 (Kamal deploy) | €15–40 | Moderate | Cost-conscious growth |
| **C: Managed Hetzner** | Ubicloud K8s on Hetzner + managed PG | €20–60 | Moderate | Docker-native, cloud-agnostic |
| **D: Credit-Funded Big Three** | AWS/GCP/Azure with startup credits | €0–50 | Medium | Runway extension, enterprise features |
| **E: Full Hetzner** | Bare-metal K8s + self-hosted PG | €7–30 | Expert | Maximum cost control, experienced team |
| **F: Multi-Cloud** | Render (app) + Hetzner (compute) + R2 (storage) | €30–80 | Moderate | Best-of-breed composition |

### Decision Tree

```
                                Start Here
                                    │
                         ┌──────────┼──────────┐
                         │          │          │
                   Team has K8s   Have cloud   Need global
                   experience?    credits?     edge latency?
                         │          │          │
                    ┌────┴────┐  ┌──┴──┐    ┌──┴──┐
                    │ No      │  │ Yes │    │ Yes │
                    │ → A, B  │  │ → D │    │ → Fly.io │
                    │ or C    │  │     │    │     │
                    └─────────┘  └─────┘    └─────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
         Optimize for  Optimize   Optimize for
         speed/DX?     cost?      control?
              │          │          │
         ┌────┴────┐ ┌──┴────┐ ┌──┴──────┐
         │ → A     │ │ → B/C │ │ → E     │
         │ Render  │ │ Hetzner│ │ Full    │
         │         │ │ hybrid │ │ Hetzner │
         └─────────┘ └───────┘ └─────────┘
```

### Scenario A: Lean Managed (Recommended for MVP)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MVP Architecture (~€18–35/month)                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────┐     ┌──────────────────┐                      │
│  │  Render Starter   │     │  Neon Launch     │                      │
│  │  (FastAPI +       │────▶│  (PostgreSQL +   │                      │
│  │   Next.js)        │     │   pgvector)      │                      │
│  │  €0–7/month       │     │  €17.50/month    │                      │
│  └────────┬──────────┘     └──────────────────┘                      │
│           │                                                          │
│           ▼                                                          │
│  ┌──────────────────┐     ┌──────────────────┐                      │
│  │  Cloudflare R2   │     │  Cloudflare CDN  │                      │
│  │  (Audio files)   │     │  (DNS + SSL)     │                      │
│  │  €0 (10GB free)  │     │  €0 (Free)       │                      │
│  └──────────────────┘     └──────────────────┘                      │
│                                                                      │
│  Total: ~€18–25/month (Render free tier: ~€18)                      │
│  DevOps tax: ZERO                                                    │
└─────────────────────────────────────────────────────────────────────┘
```

**Why Render for MVP**:
- Superior developer UX (10/10 in our scoring)
- `git push` deploys with auto-rollback
- Native Neon integration guides from both Render and Neon
- Free tier enables €0 compute while validating product-market fit
- Free PostgreSQL DB expires after 30 days — plan for Neon from day 1

### Scenario C: Managed Hetzner via Ubicloud (Recommended for Growth)

```
┌─────────────────────────────────────────────────────────────────────┐
│               Growth Architecture (~€30–60/month)                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────┐     ┌──────────────────┐                      │
│  │  Ubicloud K8s    │     │  Ubicloud        │                      │
│  │  on Hetzner      │────▶│  Managed Postgres │                      │
│  │  2–3× cheaper    │     │  (pgvector)      │                      │
│  │  than public K8s │     │  ~€15–25/month   │                      │
│  └────────┬─────────┘     └──────────────────┘                      │
│           │                                                          │
│           ▼                                                          │
│  ┌──────────────────┐     ┌──────────────────┐                      │
│  │  Hetzner Object  │     │  Cloudflare R2   │                      │
│  │  Storage (backup)│     │  (CDN + audio)   │                      │
│  │  €4.99/month     │     │  €0–15/month     │                      │
│  └──────────────────┘     └──────────────────┘                      │
│                                                                      │
│  Total: ~€30–50/month                                                │
│  DevOps tax: LOW (Ubicloud manages K8s + PG)                        │
└─────────────────────────────────────────────────────────────────────┘
```

**Why Ubicloud on Hetzner**:
- Open-source AWS alternative running on Hetzner infrastructure
- Managed K8s in <5 minutes (no Talos/K3s expertise needed)
- Managed PostgreSQL with pgvector (no CloudNativePG complexity)
- Docker-based = cloud-agnostic = easy migration via Pulumi
- Germany data center = EU data residency for GDPR

### Scenario D: Credit-Funded Big Three

```
┌─────────────────────────────────────────────────────────────────────┐
│              Credit-Funded Architecture (€0 for 6–18 months)        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Phase 1 (months 0–3): Use Azure credits (shortest expiry)          │
│  ├── Azure Container Apps (180K vCPU-sec free/month)                │
│  ├── Azure Database for PostgreSQL Flexible (B2s)                   │
│  └── Azure Blob Storage                                             │
│                                                                      │
│  Phase 2 (months 3–12): Switch to AWS credits                       │
│  ├── ECS Fargate (Spot: 70% discount)                               │
│  ├── RDS db.t4g.medium ($0.065/hr → ~$48/mo)                       │
│  └── S3 Standard                                                    │
│                                                                      │
│  Phase 3 (credits exhausted): Migrate to Hetzner via Pulumi         │
│  └── Same Docker containers, different infrastructure                │
│                                                                      │
│  Total: €0 (while credits last), then migrate to Scenario B/C       │
│  DevOps tax: MEDIUM (Big Three complexity, but managed services)     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. IaC Strategy: Pulumi

### Why Pulumi (Not Terraform)

| Factor | Pulumi | Terraform (IBM/HashiCorp) |
|--------|--------|---------------------------|
| **Language** | Python (same as our backend) | HCL (new DSL to learn) |
| **License** | Open source (Apache 2.0) | BSL 1.1 (no longer OSS) |
| **Ownership** | Independent startup | IBM acquired ($6.4B, Feb 2025) |
| **Hetzner provider** | Official, v1.32.0 (Jan 2026) | Community-maintained |
| **MCP integration** | Official MCP server for Claude Code/Cursor | None |
| **State backend** | Free Pulumi Cloud (individuals) OR self-hosted S3 | Terraform Cloud (paid) OR S3 |
| **AI features** | Pulumi Copilot, MCP Server, Neo | IBM watsonx integration (enterprise) |
| **GitHub stars** | 20K (167% more contributions/month than TF) | 39.2K (larger base, slower growth) |
| **Deployments** | $0.01/min, 500 free mins/month (individual) | Terraform Cloud free tier limited |

### Community & Maturity

- **Terraform**: 39.2K GitHub stars, mature ecosystem, massive provider library. But BSL license + IBM acquisition creates uncertainty for startups.
- **Pulumi**: 20K stars, 170K+ developers, 100M+ downloads. Most active IaC open-source project (117 merged PRs/month vs Terraform's lower rate).
- **OpenTofu**: Terraform fork (open-source), growing but ecosystem still catching up.

### Provider Quality Matrix

| Provider | Pulumi | Terraform | OpenTofu |
|----------|--------|-----------|----------|
| **AWS** | Excellent (official) | Excellent (official) | Excellent (fork) |
| **GCP** | Excellent (official) | Excellent (official) | Excellent (fork) |
| **Azure** | Excellent (official) | Excellent (official) | Excellent (fork) |
| **Hetzner** | Good (official v1.32) | Good (community) | Good (community) |
| **Render** | None | None | None |
| **Neon** | None | Community | None |
| **Ubicloud** | None | None | None |
| **Cloudflare** | Good (official) | Good (official) | Good |

**Key gap**: Neither Render nor Ubicloud have Pulumi providers. For MVP (Render) and Growth (Ubicloud), infrastructure is managed via their respective CLIs/dashboards. Pulumi becomes essential when migrating to Big Three or managing Hetzner directly.

### MCP Integration (Compelling for our Stack)

Pulumi's [MCP Server](https://www.pulumi.com/docs/iac/guides/ai-integration/mcp-server/) integrates directly with Claude Code:

```bash
# In Claude Code: /mcp → select "pulumi" → authenticate
# Then ask: "What resources are in my production stack?"
# Or: "Deploy a new Hetzner CX32 with pgvector"
```

This aligns perfectly with our AG-UI agentic architecture — the same Claude agent that queries music attribution data can also manage infrastructure.

### Reference Implementation: UAD Copilot (KusiKasa)

The `uad-copilot` project provides a real-world Pulumi + Azure Container Apps reference. Key patterns to adopt:

**Strengths to replicate**:
- Clean dev/staging/prod stack separation via `Pulumi.{env}.yaml`
- Managed identities for secure Azure authentication (no long-lived credentials)
- Doppler integration for centralized secrets management
- GitHub Actions OIDC-based deployment (no stored secrets)
- Infrastructure tests with mocks + integration checks

**Anti-patterns to avoid** (lessons learned):
- Hardcoded tenant IDs, resource group names — externalize to config
- Mixed cloud provider code (GCP leftovers) — clean separation from day 1
- Key Vault provisioned but unused — provision only what's needed
- Public defaults in fallback chains (Grafana user IDs) — require explicit config
- No CrossGuard/Policy-as-Code — add Azure policies from the start
- Force deployment ID workaround — use proper container versioning

### Recommended Pulumi Structure

```
infrastructure/
├── __main__.py           # Entry point
├── Pulumi.yaml           # Project config
├── Pulumi.dev.yaml       # Local Docker environment
├── Pulumi.staging.yaml   # Hetzner staging
├── Pulumi.prod.yaml      # Production
├── modules/
│   ├── __init__.py
│   ├── compute.py        # Cloud-agnostic compute abstraction
│   ├── database.py       # PostgreSQL (Neon/Ubicloud/RDS)
│   ├── storage.py        # S3-compatible (R2/Hetzner/S3)
│   └── network.py        # Firewall/DNS
└── tests/
    └── test_infra.py     # pytest infrastructure tests
```

### Cloud Migration with Pulumi

```python
# Same patterns, different providers — swap with config
if config.get("cloud_provider") == "hetzner":
    import pulumi_hcloud as cloud
    server = cloud.Server(...)
elif config.get("cloud_provider") == "aws":
    import pulumi_aws as cloud
    server = cloud.ec2.Instance(...)
elif config.get("cloud_provider") == "gcp":
    import pulumi_gcp as cloud
    server = cloud.compute.Instance(...)
```

---

## 6. Managed PostgreSQL Comparison

### Cost Comparison (10GB data, pgvector required)

| Provider | Plan | Monthly | pgvector | Scale-to-zero | Free Tier | EU Data |
|----------|------|---------|----------|---------------|-----------|---------|
| **Neon** | Launch | €17–22 | Yes | Yes | 0.5GB | Frankfurt |
| **Render** | Starter | €6–10 | Yes | No | 1GB (30-day) | Yes |
| **Ubicloud** | Managed | €11–15 | Yes | No | No | Germany |
| **Supabase** | Pro | €23–25 | Yes | No | 500MB | Frankfurt |
| **AWS RDS** | db.t4g.medium | ~€48 | Yes | No | 12-mo free tier | eu-west-1 |
| **GCP Cloud SQL** | Enterprise | ~€65–85 | Yes | Emerging | $300 credit | europe-west1 |
| **Azure Flexible** | B2s | ~€50–65 | Yes | No | 12-mo free tier | westeurope |

### Recommendation: Start with Neon

1. **Scale-to-zero**: Don't pay when not querying (perfect for MVP)
2. **Database branching**: Test schema changes without affecting production
3. **pgvector optimized**: Required for music attribution embeddings
4. **EU data residency**: Frankfurt data center
5. **Standard PostgreSQL**: No lock-in, easy `pg_dump` migration

### Cost at Scale

| Data Size | Neon | Ubicloud | AWS RDS | Self-hosted (Hetzner) |
|-----------|------|----------|---------|-----------------------|
| 10GB (MVP) | €17–22 | €11–15 | ~€48 | €0 (on VPS) |
| 100GB (Growth) | €50–65 | €30–50 | ~€80 | €0 (on VPS) |
| 1TB (Scale) | €350–400 | €150–250 | ~€250 | €0 (on VPS) |

---

## 7. Object Storage & Egress

### Why This Matters for Music Attribution

Audio files are large (3–10MB per track). At scale, serving 10,000 tracks/day = 30–100GB egress/day. On AWS at $0.09/GB, that's $2,700–9,000/month in egress alone.

### Provider Comparison

| Provider | Storage/GB/mo | Egress/TB | Free Tier | S3-compatible | Notes |
|----------|---------------|-----------|-----------|---------------|-------|
| **Cloudflare R2** | $0.015 | **$0** | 10GB storage | Yes | Zero egress. Best for audio CDN. |
| **Hetzner Object** | €0.005 | €1/TB | 1TB egress incl. in base (€4.99/mo) | Yes | Intra-Hetzner egress free |
| **Backblaze B2** | $0.005 | $0.01/GB via Cloudflare | 10GB | Yes | Good for cold backups |
| **AWS S3** | $0.021 | $0.09/GB | 100GB/mo (free tier) | Native | Most features, most expensive egress |
| **GCP GCS** | $0.020 | $0.085/GB | 5GB/mo (free tier) | Via interop | Slightly cheaper egress than AWS |
| **Azure Blob** | $0.018 | $0.087/GB | 5GB/mo (free tier) | No (proprietary API) | Azure-only ecosystem |

### Recommendation

**Cloudflare R2** for all object storage (audio files, embeddings exports, static assets). Zero egress is the single most impactful FinOps decision for a music platform.

**Hetzner Object Storage** as secondary/backup if running on Hetzner infrastructure (intra-network traffic is free).

---

## 8. Cloud Credit Strategy

### Realistic Credits for a UK/EU Music Startup

| Program | Amount | Duration | Application Priority |
|---------|--------|----------|---------------------|
| **NVIDIA Inception** | Unlocks higher tiers | Ongoing | **1st — Apply immediately** |
| **Azure Founders Hub** | €920–4,600 | 90–180 days | 2nd (use first — expires fastest) |
| **AWS Activate Founders** | €920 ($1,000) | 12–24 months | 3rd |
| **OVHcloud START** | **€10,000** | 12 months | 4th (best value for bootstrapped) |
| **GCP for Startups** | €1,840 ($2,000) | 12 months | 5th |
| **Scaleway Founders** | €1,000 | 12 months | 6th |

**Total realistic credits**: ~€17,000–27,000

### Credit Stacking Timeline

```
Week 1–2:  Apply NVIDIA Inception (unlocks higher AWS tier)
           Apply Azure Founders Hub (€920 instant, shortest expiry)
           Apply AWS Activate (€920)

Week 3–4:  Apply OVHcloud START (€10,000 — best value)
           Apply Scaleway (€1,000)

Month 2:   Re-apply AWS via NVIDIA Inception (upgrade to €9,200+)
           Apply GCP (€1,840)

Ongoing:   Use Azure credits FIRST (90–180 day expiration)
           Then AWS/GCP (12–24 month expiration)
           Save Hetzner for post-credit production
```

### Credit Gotchas

| Issue | Mitigation |
|-------|------------|
| Azure 90–180 day expiration | Use Azure immediately upon receipt |
| AWS region-locked credits | Verify eu-west-1 availability before architecting |
| No retroactive application | Apply BEFORE major spend events |
| Personal email rejection | Always use company domain |
| NVIDIA 6-month profile update | Set calendar reminder |

---

## 9. Container Orchestration Decision

### Decision Matrix

| Factor | Render | Kamal 2 | Ubicloud K8s | Full K8s (self-hosted) | Fly.io |
|--------|--------|---------|--------------|------------------------|--------|
| **DevEx (2–4 person)** | 10/10 | 7/10 | 8/10 | 5/10 | 8/10 |
| **Operational simplicity** | 10/10 | 7/10 | 8/10 | 4/10 | 8/10 |
| **Cost control** | 7/10 | 10/10 | 9/10 | 10/10 | 7/10 |
| **Vendor lock-in** | Low | None | Low | None | Medium |
| **Security** | 10/10 | 8/10 | 8/10 | 7/10 | 9/10 |
| **Production readiness** | 5/5 | 4/5 | 4/5 | 5/5 (if operated well) | 5/5 |
| **Pulumi support** | None | N/A | None | Via Hetzner provider | None |

### Recommendation by Phase

| Phase | Tool | Monthly Cost | Rationale |
|-------|------|--------------|-----------|
| **MVP** | Render | €0–7 | Best UX, free tier, zero DevOps tax |
| **Growth** | Kamal 2 on Hetzner OR Ubicloud K8s | €15–40 | Full control, managed options available |
| **Scale** | Ubicloud K8s or self-hosted K8s | €50+ | HA requirements, cost optimization |

### Kamal 2 Configuration (for Hetzner path)

```yaml
# config/deploy.yml — Kamal 2 format
service: attribution
image: ghcr.io/music-attribution/scaffold

servers:
  web:
    hosts:
      - attribution-web-1.hetzner.com

proxy:
  ssl: true
  host: api.your-domain.com

registry:
  server: ghcr.io
  username:
    - KAMAL_REGISTRY_USERNAME
  password:
    - KAMAL_REGISTRY_PASSWORD

env:
  secret:
    - DATABASE_URL
    - ANTHROPIC_API_KEY
```

**Kamal 2 improvements** (released Sept 2024):
- Replaced Traefik with custom Kamal Proxy (simpler config, better errors)
- `.kamal/secrets` replaces `.env` for secrets (no conflicts with other tools)
- Automatic Let's Encrypt SSL
- Maintenance mode and canary deployments coming

---

## 10. Local Development Parity

**Principle**: Same `docker-compose.yml` works locally AND approximates production.

```yaml
# docker-compose.yml
services:
  app:
    build: .
    image: ghcr.io/music-attribution/scaffold:${TAG:-latest}
    environment:
      - DATABASE_URL=${DATABASE_URL:-postgresql://postgres:postgres@postgres:5432/attribution}  # pragma: allowlist secret
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    ports:
      - "${PORT:-8000}:8000"
    depends_on:
      postgres:
        condition: service_healthy

  frontend:
    build: ./frontend
    ports:
      - "${FRONTEND_PORT:-3000}:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000

  postgres:
    image: pgvector/pgvector:pg16
    environment:
      POSTGRES_DB: attribution
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  # Dev-only services
  pgadmin:
    image: dpage/pgadmin4
    profiles: ["dev"]
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@attribution.local
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"

volumes:
  postgres_data:
```

```bash
# Development (with pgadmin)
docker compose --profile dev up -d

# Staging-like (production config)
docker compose up -d

# Production deploy via Kamal
kamal deploy
```

---

## 11. Exit Strategies & Portability

### Migration Effort Matrix

| From → To | Effort | Downtime | Notes |
|-----------|--------|----------|-------|
| Render → Hetzner (Kamal) | Low | <1 hour | Same Docker image |
| Render → Ubicloud K8s | Low | <1 hour | Write K8s manifests |
| Neon → Ubicloud PG | Low | <1 hour | `pg_dump` / `pg_restore` |
| Hetzner → AWS | Medium | 2–4 hours | Pulumi provider swap |
| AWS → Hetzner | Medium | 2–4 hours | Pulumi provider swap |
| Cloudflare R2 → S3 | Low | <1 hour | `rclone sync` |
| Any → Any (PostgreSQL) | Low | <1 hour | Standard `pg_dump` — pgvector data is standard arrays |

### Portability Checklist

- [x] **Containerized**: All services run in Docker
- [x] **Standard PostgreSQL**: pgvector, no proprietary extensions
- [x] **S3-compatible storage**: R2/Hetzner/S3 all compatible
- [x] **Pulumi IaC**: Same patterns across clouds (when provider exists)
- [x] **No serverless lock-in**: Containers over Lambda/Cloud Functions
- [x] **Open protocols**: Standard HTTP APIs, no proprietary SDKs
- [x] **No cloud-specific services**: No DynamoDB, no Firestore, no proprietary queues

### Emergency Migration Playbook

```bash
# 1. Export database
pg_dump -Fc $CURRENT_DB_URL > backup.dump

# 2. Export object storage
rclone sync r2:attribution-data s3:attribution-backup

# 3. Deploy to new provider (if using Pulumi)
cd infrastructure && pulumi stack select new-provider
pulumi up

# 4. Restore database
pg_restore -d $NEW_DB_URL backup.dump

# 5. Update DNS (Cloudflare → new IP, TTL: 60s)

# 6. Verify
curl -I https://api.your-domain.com/health
```

---

## 12. Cost Projections by Phase

### Phase-by-Phase Summary

| Phase | Monthly Cost | Annual Cost | Stack | DevOps Tax |
|-------|--------------|-------------|-------|------------|
| **MVP (0–6 mo)** | €0–35 | €0–420 | Render + Neon + R2 | Zero |
| **Growth (6–18 mo)** | €30–80 | €360–960 | Hetzner + Ubicloud/Kamal + Neon + R2 | Low |
| **Scale (18+ mo)** | €100–300 | €1,200–3,600 | Multi-node Hetzner + managed PG | Medium |
| **Enterprise (24+ mo)** | €300–1,000 | €3,600–12,000 | Multi-cloud, HA, multi-region | Medium–High |

### Cost at Volume (per-query economics)

| Volume | MVP (Render) | Growth (Hetzner) | Scale (Multi-node) |
|--------|-------------|-------------------|---------------------|
| 1K queries/day | €0.001/query | €0.001/query | €0.003/query |
| 10K queries/day | €0.001/query | €0.001/query | €0.001/query |
| 100K queries/day | €0.001/query | €0.0003/query | €0.0003/query |

### Savings vs All-Hyperscaler Path

| Phase | Hetzner-path Cost | All-AWS Cost | Savings |
|-------|-------------------|-------------|---------|
| MVP | €25/mo | €150/mo | **83%** |
| Growth | €50/mo | €300/mo | **83%** |
| Scale | €200/mo | €1,000/mo | **80%** |

---

## 13. Recommendation & Confidence Estimates

### For a Music Attribution Startup (2–4 engineers, 2–4 domain experts)

| Decision | Recommendation | Confidence | Alternatives |
|----------|----------------|------------|-------------|
| **MVP compute** | Render (PaaS) | **95%** | Railway, Fly.io |
| **MVP database** | Neon (managed PostgreSQL) | **90%** | Supabase, Render PG |
| **Growth compute** | Hetzner Cloud + Kamal 2 or Ubicloud | **80%** | Remain on Render if <€50/mo |
| **Growth database** | Neon or Ubicloud managed PG | **85%** | Self-hosted CloudNativePG |
| **Object storage** | Cloudflare R2 (zero egress) | **95%** | Hetzner Object Storage |
| **IaC tool** | Pulumi (Python) | **85%** | OpenTofu (if BSL concerns) |
| **Container deploy** | Kamal 2 (growth) → K8s (scale) | **75%** | Ubicloud K8s from the start |
| **DNS/CDN** | Cloudflare (free tier) | **95%** | Route53 (if all-AWS) |
| **CI/CD** | GitHub Actions | **90%** | Pulumi Deployments |
| **Monitoring** | Grafana Cloud (free tier) + PostHog | **80%** | OpenObserve on Hetzner |

### Phased Migration Path (Most Likely)

```
Month 0 ──── Render + Neon + R2 (€18/mo, zero ops)
              │
Month 3 ──── Apply for all cloud credits (€17K–27K)
              │
Month 6 ──── Evaluate: if cost >€50/mo on Render, begin Hetzner pilot
              │
Month 9 ──── Kamal 2 on Hetzner Cloud + Neon (€30–50/mo)
              │  OR stay on Render if cost is acceptable
              │
Month 12 ─── Evaluate: Ubicloud K8s maturity, team K8s comfort
              │
Month 18 ─── Scale decision: Ubicloud K8s OR self-hosted K8s
              │  Credit-funded Big Three for compliance customers
              │
Month 24+ ── Multi-cloud: Hetzner primary, Big Three for enterprise
```

### Hetzner as Bayesian Prior

The user's instinct to default to Hetzner is well-founded:

**Prior probability of Hetzner as optimal long-term choice**: ~70%

| Evidence | Effect on Posterior |
|----------|---------------------|
| 76% cost savings (Digital Society case study) | Increases ↑ |
| Docker-based = cloud-agnostic (no lock-in) | Increases ↑ |
| EU data residency (GDPR compliance) | Increases ↑ |
| Ubicloud reduces DevOps tax | Increases ↑ |
| No managed K8s from Hetzner (yet) | Decreases ↓ slightly |
| Pulumi provider exists (official) | Increases ↑ |
| Network zones ≠ availability zones | Decreases ↓ slightly |
| Small team (2–4 engineers) has limited DevOps capacity | Decreases ↓ (for bare-metal path) |

**Updated posterior**: ~75% for Hetzner as long-term primary, BUT with Render as the correct starting point (not Hetzner from day 1).

**The key insight**: Start where the DevOps tax is zero (Render), migrate when savings justify the tax (Hetzner). The Docker-based, cloud-agnostic architecture ensures this migration is low-effort when the time comes.

---

## 14. Updated Figure Plan

The corrected `fig-choice-15` should reflect:

1. **X-axis (Complexity)**: Render (lowest) → Ubicloud on Hetzner → Big Three → Hetzner bare-metal (highest)
2. **Y-axis (Monthly Cost)**: Hetzner bare-metal (lowest) → Hetzner+Ubicloud → Render → Big Three (highest)
3. **Two Hetzner dots**: Managed (Ubicloud) and bare-metal (self-hosted)
4. **Big Three as single region**: AWS, GCP, Azure clustered together (similar pricing)
5. **Migration arrows**: Render → Hetzner+Ubicloud → Hetzner bare-metal

Updated archetype mapping:
- **Musician-First Team** → Render (zero DevOps tax)
- **Budget-Conscious Startup** → Hetzner + Ubicloud (managed, affordable)
- **Solo Hacker (K8s expert)** → Hetzner bare-metal (cheapest, expert-level ops)
- **Well-Funded / Enterprise** → Big Three (credits, compliance, managed)

---

## Appendix A: Reference Sources

### Internal Documentation

| Document | Key Insight |
|----------|-------------|
| `docs/planning/finops-optimization-plan.md` | Original 5-scenario analysis, Render+Neon recommended for MVP |
| `dpp-agents/.../rag-hosting-finops-comparison.md` | Hetzner €4.50 vs Azure $77.85, DevOps tax break-even at 2,000 vCPUs |
| `dpp-agents/.../azure-finops-guide.md` | Azure B2 ~$85/mo baseline, optimization to $5–10 possible |
| `dpp-agents/.../voice-ai-finops-expansion-roadmap.md` | Multi-tier scaling: Demo ($50–100) → Beta ($300–500) → Traction ($1K–2K) |
| `sci-llm-writer/biblio/.../Digital Society - Migrating to Hetzner.md` | 76% savings, but required K8s expertise (Talos, CloudNativePG) |

### External Research (February 2026)

| Topic | Finding |
|-------|---------|
| Hetzner managed K8s | No native offering yet. Ubicloud, Cloudfleet, Syself provide managed K8s on Hetzner |
| Ubicloud | Open-source AWS alternative. Managed K8s + PostgreSQL on Hetzner. Preview in Germany + Virginia |
| Render free tier | Still available (Feb 2026). Free PG DB expires after 30 days (was 90). SMTP ports blocked on free tier |
| Kamal 2 | Stable at v2.8+. Custom Kamal Proxy replaced Traefik. Better secrets mgmt (.kamal/secrets) |
| Coolify security | 11 critical CVEs (CVSS 9.4–10.0) disclosed Jan 2026. Patches in v4.0.0-beta.420.7+. Use with caution |
| Hetzner Object Storage | GA. €4.99/mo base includes 1TB storage + 1TB egress. Additional egress: €1/TB |
| Pulumi vs Terraform | Pulumi: 20K stars, 170K devs, most active IaC OSS project. Terraform: 39.2K stars, IBM acquisition |
| IBM + HashiCorp | Completed Feb 2025 for $6.4B. Terraform under BSL. IBM integrating with watsonx (Project Infragraph) |
| Pulumi MCP Server | Official integration with Claude Code and Cursor. Remote MCP server at mcp.ai.pulumi.com |
| Pulumi state | Free for individuals. DIY backends (S3/GCS/Azure Blob) fully open source |
| SST | Development paused (team pivoted to OpenCode AI agent). In maintenance mode, not recommended for new projects |
| AWS RDS pricing | db.t4g.medium: $0.065/hr (~$48/mo). Reserved: ~$34/mo. Fargate Spot: up to 70% discount |
| GCP Cloud Run | Scale-to-zero, per-request billing. Min instance: ~$10–12/mo. Recommender auto-suggests billing model |
| Azure Container Apps | 180K vCPU-seconds free/month. Consumption plan scales to zero |
| Egress costs | AWS $0.09/GB, GCP $0.085/GB (cheapest of Big Three), Azure $0.087/GB |
| European clouds | Scaleway+Clever Cloud partnership (EU sovereign PaaS). OVHcloud €10K startup credits. Northflank multi-cloud PaaS |

---

## Appendix B: Reviewer Agent Insights

### Cost Optimization Reviewer

- Cloudflare R2 zero egress is the single highest-impact FinOps decision for a music platform
- Neon scale-to-zero saves €10–15/mo during MVP when database is idle 95% of the time
- Cloud credits (€17K–27K) provide 12–18 months of runway on hyperscaler infrastructure for free
- The €4.99/mo Hetzner Object Storage base plan includes enough egress for MVP

### Architecture Reviewer

- The "two Hetzner paths" distinction is critical — bare-metal K8s requires fundamentally different team skills than Ubicloud managed
- Pulumi's lack of Render and Ubicloud providers creates a gap in the IaC story for months 0–12
- The Docker-based architecture is the correct foundation — it makes the entire migration path viable
- Consider `render.yaml` (Blueprint Spec) as IaC-lite for the Render phase

### Startup Strategy Reviewer

- A 2–4 engineer team should spend ZERO time on infrastructure in months 0–6 — product-market fit is the only priority
- Hetzner is the correct long-term bet, but premature optimization into self-managed infra kills startups
- The credit stacking strategy (€17K–27K free) is under-utilized by most bootstrapped startups
- Coolify's security issues are a dealbreaker for a music attribution platform handling rights data

### Music Domain Reviewer

- Audio file egress is the hidden cost that makes or breaks FinOps for music platforms
- GDPR/EU data residency is a competitive advantage for music attribution (EU creators trust EU infrastructure)
- The MCP permission patchbay means AI companies will query the API at scale — plan for burst traffic patterns
- Hetzner's German data centers align with the European music rights organizations (PRS, STIM, GEMA)

---

*Document created: 2026-02-03 (v1.0)*
*Updated: 2026-02-14 (v2.0 — corrected complexity model, added Big Three coverage, Ubicloud path, Bayesian analysis)*
*Next review: 2026-03-14*
