# fig-repo-09: Docker Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-09 |
| **Title** | Docker Architecture: Six-Service Development Stack |
| **Audience** | Technical (developers, DevOps) |
| **Complexity** | L2 (infrastructure) |
| **Location** | docs/architecture/docker.md, README.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

The development environment runs six services via Docker Compose, with two optional monitoring services. This figure shows the container topology, port mappings, health checks, and volume mounts. It helps developers understand the local infrastructure and debug connectivity issues.

The key message is: "Six always-on services (postgres, pgbouncer, valkey, backend, frontend) plus opt-in monitoring (Prometheus + Grafana) -- all managed by a single `make dev` command."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  DOCKER ARCHITECTURE                                                   |
|  ■ Six-Service Development Stack                                       |
+-----------------------------------------------------------------------+
|                                                                        |
|  $ make dev  (docker-compose.dev.yml)                                  |
|                                                                        |
|  ┌─────────────────── CORE SERVICES ──────────────────────────────┐   |
|  │                                                                 │   |
|  │  ┌───────────────┐    ┌───────────┐    ┌───────────┐           │   |
|  │  │  POSTGRESQL   │    │ PGBOUNCER │    │  VALKEY   │           │   |
|  │  │  17 + pgvector│───▶│  :6432    │    │  :6379    │           │   |
|  │  │  :5432        │    │ tx pool   │    │  cache    │           │   |
|  │  │  ■ healthcheck│    │ max 200   │    │  alpine   │           │   |
|  │  └───────────────┘    └─────┬─────┘    └───────────┘           │   |
|  │                             │                                   │   |
|  │  ┌──────────────────────────┴────────────────────────────┐     │   |
|  │  │              BACKEND (FastAPI)  :8000                  │     │   |
|  │  │              Dockerfile.dev  │  hot-reload             │     │   |
|  │  │              volumes: src/, alembic/                   │     │   |
|  │  └──────────────────────────┬────────────────────────────┘     │   |
|  │                             │                                   │   |
|  │  ┌──────────────────────────┴────────────────────────────┐     │   |
|  │  │              FRONTEND (Next.js 15)  :3000              │     │   |
|  │  │              node:22-slim  │  npm run dev              │     │   |
|  │  │              NEXT_PUBLIC_API_URL=backend:8000          │     │   |
|  │  └────────────────────────────────────────────────────────┘     │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  ┌─── MONITORING (opt-in: --profile monitoring) ──────────────────┐   |
|  │  Prometheus :9090  ───▶  Grafana :3001 (anonymous admin)       │   |
|  └────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  Volumes: postgres_data (persistent), frontend_node_modules (cache)   |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "DOCKER ARCHITECTURE" Instrument Serif ALL-CAPS |
| make dev trigger | `data_mono` | Command that starts everything |
| Core services box | `zone_core` | Main container group with coral border |
| PostgreSQL container | `container_box` | pgvector/pgvector:pg17, port 5432 |
| PgBouncer container | `container_box` | Connection pooler, port 6432 |
| Valkey container | `container_box` | Cache layer, port 6379 |
| Backend container | `container_box` | FastAPI, port 8000, hot-reload |
| Frontend container | `container_box` | Next.js, port 3000 |
| Monitoring zone | `zone_optional` | Dashed border, opt-in profile |
| Port labels | `data_mono` | :5432, :6432, :6379, :8000, :3000, :9090, :3001 |
| Health check indicators | `accent_square` | Small coral squares on containers with health checks |
| Volume labels | `label_editorial` | postgres_data, frontend_node_modules |
| Dependency arrows | `primary_pathway` | Showing startup order and connections |

## Anti-Hallucination Rules

1. The compose file is `docker-compose.dev.yml`, not `docker-compose.yml`.
2. PostgreSQL image is `pgvector/pgvector:pg17` (PostgreSQL 17 with pgvector).
3. PgBouncer image is `edoburu/pgbouncer:1.23.1`, pool mode is "transaction", max 200 connections.
4. Valkey image is `valkey/valkey:8-alpine` (not Redis -- Valkey is the Redis-compatible fork).
5. Frontend uses `node:22-slim` image, not a custom Dockerfile.
6. Backend uses `docker/Dockerfile.dev` and mounts `src/`, `alembic/`, `alembic.ini`.
7. Monitoring is opt-in via `--profile monitoring` (Prometheus v2.54.1, Grafana 11.4.0).
8. Grafana runs on port 3001 (not 3000, which is frontend), with anonymous admin access.
9. There are exactly two named volumes: `postgres_data` and `frontend_node_modules`.
10. Backend depends on postgres (healthy), frontend depends on backend (healthy).

## Alt Text

Docker Compose architecture: six core services (PostgreSQL+pgvector, PgBouncer, Valkey, FastAPI backend, Next.js frontend) with opt-in Prometheus+Grafana monitoring stack.
