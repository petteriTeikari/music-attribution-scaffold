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

This figure shows the deployment pipeline from Docker build to production, highlighting that the scaffold supports four deployment paths (Render, Hetzner via Kamal or Ubicloud, Big Three hyperscalers). Updated to reflect PRD v2.1.0 with Kamal 2 as a bridge between Docker Compose and Kubernetes, and two distinct Hetzner paths. It answers: "How do I take this scaffold from local development to a running production service?"

The key message is: "The scaffold ships as a production-ready Docker image with Prometheus metrics and health checks. Deployment follows five steps: build, configure, push, deploy, and verify -- with four branching paths from PaaS simplicity (Render) to bare-metal efficiency (Hetzner), including Kamal 2 as the recommended middle ground."

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
|  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐     |
|  │ RENDER    │ │ KAMAL 2   │ │ HETZNER + │ │ BIG THREE │     |
|  │ ──────── │ │ ──────── │ │ UBICLOUD  │ │ ──────── │     |
|  │ render.   │ │ kamal     │ │ managed   │ │ ECS/Cloud │     |
|  │ yaml auto │ │ deploy    │ │ K8s +     │ │ Run via   │     |
|  │ deploy    │ │ (Docker   │ │ managed   │ │ Pulumi /  │     |
|  │ from Git  │ │  without  │ │ PG        │ │ Terraform │     |
|  │           │ │  K8s)     │ │           │ │           │     |
|  │ (managed) │ │ (bridge)  │ │ (managed) │ │ (managed) │     |
|  └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘     |
|         └──────────────┴─────────────┴─────────────┘           |
|                            v                                    |
|  V. VERIFY                                                     |
|  ─────────                                                     |
|  ┌─────────────────────────────────────────────┐              |
|  │ ■ GET /api/v1/health       → 200 OK         │              |
|  │ ■ GET /metrics              → Prometheus OK  │              |
|  │ ■ Grafana dashboard         → Panels green   │              |
|  └─────────────────────────────────────────────┘              |
|                                                                |
+---------------------------------------------------------------+
|  Start on Render, migrate to Hetzner when savings justify ops  |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO DEPLOY TO PRODUCTION" with coral accent square |
| Subtitle | `label_editorial` | "Docker Image to Running Service" |
| Step I: Build | `processing_stage` | Docker build command using Dockerfile.prod |
| Step II: Configure | `processing_stage` | Required environment variables list |
| Step III: Push | `processing_stage` | Docker push to container registry |
| Step IV: Deploy options | `branching_path` | Four alternative deployment targets as parallel boxes |
| Render option | `selected_option` | Managed PaaS with auto-deploy from Git (simplest path) |
| Kamal 2 option | `selected_option` | Docker deployment without K8s (37signals), bridge path |
| Hetzner+Ubicloud option | `deferred_option` | Managed K8s + managed PG on Hetzner (budget-conscious) |
| Big Three option | `deferred_option` | AWS/GCP/Azure managed container services (enterprise) |
| Step V: Verify | `processing_stage` | Three health check endpoints to confirm deployment |
| Health endpoint | `api_endpoint` | /api/v1/health returning 200 OK |
| Metrics endpoint | `api_endpoint` | /metrics for Prometheus scraping |
| Grafana dashboard | `solution_component` | Visual confirmation of service health |
| Flow arrows | `data_flow` | Vertical and branching arrows through steps |
| Roman numerals I-V | `section_numeral` | Step headers in editorial style |
| Footer callout | `callout_box` | Migration path: Render → Hetzner when savings justify ops |

## Anti-Hallucination Rules

1. The production Dockerfile is `docker/Dockerfile.prod` -- not `Dockerfile` in the repo root.
2. The scaffold includes Prometheus metrics and a Grafana dashboard -- these are real, not aspirational.
3. Four deployment paths reflect PRD v2.1.0: Render (PaaS), Kamal 2 (Docker without K8s), Hetzner+Ubicloud (managed K8s), Big Three (enterprise managed).
4. Kamal 2 is from 37signals (makers of Basecamp/HEY). It uses a custom Kamal Proxy (replaced Traefik in v2.8+) for zero-downtime deploys of Docker containers without K8s.
5. Hetzner+Ubicloud provides managed K8s and managed PostgreSQL on Hetzner Cloud. Ubicloud is open-source; K8s preview available Feb 2026.
6. Environment variables shown (DATABASE_URL, SECRET_KEY, ALLOWED_ORIGINS, SENTRY_DSN) are illustrative -- the actual required set is in the deployment docs.
7. The health endpoint is at `/api/v1/health` -- not `/health` or `/healthz`.
8. This is a SCAFFOLD -- no single deployment path is "correct." Recommended migration: Render → Hetzner+Ubicloud.
9. There is also a fifth path (Hetzner bare-metal self-managed K8s) but it is NOT shown here as it requires expert K8s knowledge and is not a how-to.
10. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Step-by-step guide: five-step production deployment pipeline for the open-source music attribution scaffold, from Docker build through environment configuration and registry push to a branching deploy step with four paths -- Render PaaS, Kamal 2 Docker deployment, Hetzner with Ubicloud managed Kubernetes, and Big Three hyperscalers -- concluding with health check and Prometheus metrics verification, reflecting the scaffold philosophy that deployment paths vary by team archetype.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Step-by-step guide: five-step production deployment pipeline for the open-source music attribution scaffold, from Docker build through environment configuration and registry push to a branching deploy step with four paths -- Render PaaS, Kamal 2 Docker deployment, Hetzner with Ubicloud managed Kubernetes, and Big Three hyperscalers -- concluding with health check and Prometheus metrics verification, reflecting the scaffold philosophy that deployment paths vary by team archetype.](docs/figures/repo-figures/assets/fig-howto-07-deploy-to-production.jpg)

*Production deployment pipeline for the Music Attribution Scaffold. Four deployment paths reflect PRD v2.1.0: Render for PaaS simplicity, Kamal 2 for Docker-without-K8s, Hetzner+Ubicloud for managed infrastructure at budget prices, and Big Three for enterprise compliance -- all converging on the same health and metrics verification endpoints (Teikari, 2026).*

### From this figure plan (relative)

![Step-by-step guide: five-step production deployment pipeline for the open-source music attribution scaffold, from Docker build through environment configuration and registry push to a branching deploy step with four paths -- Render PaaS, Kamal 2 Docker deployment, Hetzner with Ubicloud managed Kubernetes, and Big Three hyperscalers -- concluding with health check and Prometheus metrics verification, reflecting the scaffold philosophy that deployment paths vary by team archetype.](../assets/fig-howto-07-deploy-to-production.jpg)
