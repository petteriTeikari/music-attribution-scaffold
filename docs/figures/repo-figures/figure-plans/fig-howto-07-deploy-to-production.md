# fig-howto-07: How to Deploy to Production

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-07 |
| **Title** | How to Deploy to Production |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/guides/deployment.md, docs/architecture/ |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the deployment pipeline from Docker build to production, highlighting that the scaffold supports multiple deployment targets (Hetzner, Render, AWS). It answers: "How do I take this scaffold from local development to a running production service?"

The key message is: "The scaffold ships as a production-ready Docker image with Prometheus metrics and health checks. Deployment follows five steps: build, configure, push, deploy, and verify -- with branching paths for different cloud providers."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO DEPLOY TO PRODUCTION                                   |
|  ■ Docker Image to Running Service                             |
+---------------------------------------------------------------+
|                                                                |
|  I. BUILD                           II. CONFIGURE              |
|  ────────                           ────────────               |
|  ┌───────────────────┐             ┌───────────────────┐      |
|  │ docker build       │             │ Environment vars:  │      |
|  │  -f docker/        │             │ ──────────────    │      |
|  │  Dockerfile.prod   │     ──>     │ DATABASE_URL      │      |
|  │  -t music-attr:    │             │ SECRET_KEY        │      |
|  │  latest .          │             │ ALLOWED_ORIGINS   │      |
|  └─────────┬─────────┘             │ SENTRY_DSN        │      |
|             │                       └─────────┬─────────┘      |
|             v                                  │               |
|  III. PUSH TO REGISTRY                        │               |
|  ─────────────────────                        │               |
|  ┌───────────────────┐                        │               |
|  │ docker push        │                        │               |
|  │  registry/music-   │                        │               |
|  │  attr:latest       │                        │               |
|  └─────────┬─────────┘                        │               |
|             │                                  │               |
|             └──────────────┬───────────────────┘               |
|                            v                                    |
|  IV. DEPLOY (CHOOSE YOUR PATH)                                 |
|  ─────────────────────────────                                 |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │  ■ HETZNER   │ │  ■ RENDER    │ │  ■ AWS/GCP   │          |
|  │  ──────────  │ │  ──────────  │ │  ──────────  │          |
|  │  docker      │ │  render.yaml │ │  ECS/Cloud   │          |
|  │  compose up  │ │  auto-deploy │ │  Run config  │          |
|  │  -d          │ │  from Git    │ │              │          |
|  │  (self-host) │ │  (managed)   │ │  (managed)   │          |
|  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘          |
|          └────────────────┼────────────────┘                   |
|                           v                                    |
|  V. VERIFY                                                     |
|  ─────────                                                     |
|  ┌─────────────────────────────────────────────┐              |
|  │ ■ GET /api/v1/health       → 200 OK         │              |
|  │ ■ GET /metrics              → Prometheus OK  │              |
|  │ ■ Grafana dashboard         → Panels green   │              |
|  └─────────────────────────────────────────────┘              |
|                                                                |
+---------------------------------------------------------------+
|  ■ Scaffold, not SaaS — choose the deployment that fits       |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO DEPLOY TO PRODUCTION" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Docker Image to Running Service" in Plus Jakarta Sans caps |
| Step I: Build | `processing_stage` | Docker build command using Dockerfile.prod |
| Step II: Configure | `processing_stage` | Required environment variables list |
| Step III: Push | `processing_stage` | Docker push to container registry |
| Step IV: Deploy options | `branching_path` | Three alternative deployment targets as parallel boxes |
| Hetzner option | `selected_option` | Self-hosted with docker compose (engineer-heavy archetype) |
| Render option | `deferred_option` | Managed platform with render.yaml auto-deploy |
| AWS/GCP option | `deferred_option` | Cloud provider managed container services |
| Step V: Verify | `processing_stage` | Three health check endpoints to confirm deployment |
| Health endpoint | `api_endpoint` | /api/v1/health returning 200 OK |
| Metrics endpoint | `api_endpoint` | /metrics for Prometheus scraping |
| Grafana dashboard | `solution_component` | Visual confirmation of service health |
| Flow arrows | `data_flow` | Vertical and branching arrows through steps |
| Roman numerals I-V | `section_numeral` | Step headers in editorial style |
| Footer callout | `callout_box` | "Scaffold, not SaaS" reminder about deployment flexibility |

## Anti-Hallucination Rules

1. The production Dockerfile is `docker/Dockerfile.prod` -- not `Dockerfile` in the repo root.
2. The scaffold includes Prometheus metrics and a Grafana dashboard -- these are real, not aspirational.
3. Three deployment targets (Hetzner, Render, AWS) reflect the PRD archetype system -- engineer-heavy teams may self-host, musician-heavy teams may use managed platforms.
4. Environment variables shown (DATABASE_URL, SECRET_KEY, ALLOWED_ORIGINS, SENTRY_DSN) are illustrative -- the actual required set is in the deployment docs.
5. The health endpoint is at `/api/v1/health` -- not `/health` or `/healthz`.
6. This is a SCAFFOLD -- no single deployment path is "correct." The branching paths are intentional.
7. Do NOT show Kubernetes/Helm -- that is not part of the current scaffold scope.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Step-by-step guide: five-step production deployment pipeline for the open-source music attribution scaffold, from Docker build through environment configuration and registry push to a branching deploy step with Hetzner, Render, and AWS options, concluding with health check and Prometheus metrics verification -- reflecting the scaffold philosophy that deployment paths vary by team archetype.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Step-by-step guide: five-step production deployment pipeline for the open-source music attribution scaffold, from Docker build through environment configuration and registry push to a branching deploy step with Hetzner, Render, and AWS options, concluding with health check and Prometheus metrics verification -- reflecting the scaffold philosophy that deployment paths vary by team archetype.](docs/figures/repo-figures/assets/fig-howto-07-deploy-to-production.jpg)

*Production deployment pipeline for the Music Attribution Scaffold. The branching deploy step reflects the PRD archetype system: engineer-heavy teams may self-host on Hetzner, while musician-heavy teams may prefer managed platforms like Render, all converging on the same health and metrics verification endpoints (Teikari, 2026).*

### From this figure plan (relative)

![Step-by-step guide: five-step production deployment pipeline for the open-source music attribution scaffold, from Docker build through environment configuration and registry push to a branching deploy step with Hetzner, Render, and AWS options, concluding with health check and Prometheus metrics verification -- reflecting the scaffold philosophy that deployment paths vary by team archetype.](../assets/fig-howto-07-deploy-to-production.jpg)
