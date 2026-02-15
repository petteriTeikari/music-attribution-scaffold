# fig-repo-13: Environment Variables

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-13 |
| **Title** | Environment Variables: Configuration Map |
| **Audience** | Technical (developers, deployers) |
| **Complexity** | L2 (configuration reference) |
| **Location** | docs/architecture/configuration.md, README.md |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

The application is configured via environment variables, following 12-factor app principles. This figure maps all environment variables by service, showing which are required vs. optional, their default values, and which services consume them. It serves as a quick reference when setting up a new environment or debugging configuration issues.

The key message is: "All configuration flows through environment variables -- no config files to manage, no secrets in code. The Docker Compose file sets sensible defaults for development."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  ENVIRONMENT VARIABLES                                                 |
|  ■ Configuration Map: What Goes Where                                  |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. BACKEND (FastAPI)                                                  |
|  ────────────────────                                                  |
|                                                                        |
|  Variable                    Default (dev)              Required       |
|  ──────────────────────────  ─────────────────────────  ────────       |
|  DATABASE_URL                postgresql+psycopg://...   ■ YES          |
|  CORS_ORIGINS                http://localhost:3000      ■ YES          |
|  ATTRIBUTION_AGENT_MODEL     anthropic:claude-haiku-4-5 optional       |
|  ANTHROPIC_API_KEY           (none)                     for agent      |
|                                                                        |
|  II. POSTGRESQL                                                        |
|  ──────────────                                                        |
|                                                                        |
|  POSTGRES_DB                 music_attribution          ■ YES          |
|  POSTGRES_USER               musicattr                  ■ YES          |
|  POSTGRES_PASSWORD           musicattr_dev              ■ YES          |
|                                                                        |
|  III. PGBOUNCER                                                        |
|  ──────────────                                                        |
|                                                                        |
|  POOL_MODE                   transaction                ■ YES          |
|  MAX_CLIENT_CONN             200                        optional       |
|  DEFAULT_POOL_SIZE           20                         optional       |
|                                                                        |
|  IV. FRONTEND (Next.js)                                                |
|  ──────────────────────                                                |
|                                                                        |
|  NEXT_PUBLIC_API_URL          http://localhost:8000     ■ YES          |
|                                                                        |
|  ─────────────────────────────────────────────────────────             |
|  ■ Dev defaults in docker-compose.dev.yml                              |
|  ■ Production: inject via orchestrator (K8s secrets, Render env)       |
|  ■ NEVER commit real credentials -- detect-secrets enforced            |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "ENVIRONMENT VARIABLES" Instrument Serif ALL-CAPS |
| Service sections (I-IV) | `section_numeral` | Roman numerals per service group |
| Variable names | `data_mono` | IBM Plex Mono, left-aligned |
| Default values | `data_mono` | IBM Plex Mono, center column |
| Required indicators | `accent_square` | Coral squares for required, open for optional |
| Section headers | `label_editorial` | Plus Jakarta Sans service names |
| Horizontal dividers | `accent_line` | Separating service groups |
| Footer notes | `callout_tip` | Dev defaults, production guidance, security note |
| Table grid lines | `grid_line` | Subtle lines separating rows |

## Anti-Hallucination Rules

1. DATABASE_URL format is `postgresql+psycopg://` (psycopg3 async driver), not `postgresql://` or `postgres://`.
2. Dev database credentials are: user=musicattr, password=musicattr_dev, db=music_attribution -- these are in the public docker-compose.dev.yml (not secrets).
3. CORS_ORIGINS is a backend env var, not a frontend one.
4. NEXT_PUBLIC_API_URL is the only required frontend env var for backend connection.
5. ANTHROPIC_API_KEY is only needed when using the AI agent feature -- not for basic CRUD.
6. PgBouncer AUTH_TYPE is scram-sha-256 -- not md5 or trust.
7. Valkey does not require authentication in the dev setup.
8. detect-secrets pre-commit hook prevents credential commits.
9. Do NOT list AWS, GCP, or Azure credentials -- the project does not mandate a cloud provider.
10. Configuration is managed via pydantic-settings (config.py), not dotenv files.

## Alt Text

Reference card: environment variable configuration map for the music attribution scaffold organized by service -- FastAPI backend requiring DATABASE_URL with psycopg3 async driver and CORS_ORIGINS, PostgreSQL 17 database credentials, PgBouncer transaction pooling settings, and Next.js 15 frontend API URL, following 12-factor app principles with detect-secrets pre-commit enforcement preventing credential leaks in the open-source repository.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Reference card: environment variable configuration map for the music attribution scaffold organized by service -- FastAPI backend requiring DATABASE_URL with psycopg3 async driver and CORS_ORIGINS, PostgreSQL 17 database credentials, PgBouncer transaction pooling settings, and Next.js 15 frontend API URL, following 12-factor app principles with detect-secrets pre-commit enforcement preventing credential leaks in the open-source repository.](docs/figures/repo-figures/assets/fig-repo-13-environment-variables.jpg)

*Figure 13. All configuration flows through environment variables following 12-factor app principles, with sensible development defaults in docker-compose.dev.yml and pydantic-settings managing validation -- detect-secrets pre-commit hooks ensure no credentials are ever committed.*

### From this figure plan (relative)

![Reference card: environment variable configuration map for the music attribution scaffold organized by service -- FastAPI backend requiring DATABASE_URL with psycopg3 async driver and CORS_ORIGINS, PostgreSQL 17 database credentials, PgBouncer transaction pooling settings, and Next.js 15 frontend API URL, following 12-factor app principles with detect-secrets pre-commit enforcement preventing credential leaks in the open-source repository.](../assets/fig-repo-13-environment-variables.jpg)
