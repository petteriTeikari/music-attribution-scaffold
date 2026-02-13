# Getting Started

Get the Music Attribution Scaffold running on your machine in under 5 minutes.

## Prerequisites

| Requirement | Version | Check Command |
|------------|---------|---------------|
| Python | 3.13+ | `python --version` |
| uv | Latest | `uv --version` |
| Node.js | 22+ | `node --version` |
| Docker | Latest | `docker --version` |
| PostgreSQL | 16+ (via Docker) | `docker compose ps` |

!!! tip "Don't have uv?"
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

## Quick Path

```bash
git clone https://github.com/petteriTeikari/music-attribution-scaffold.git
cd music-attribution-scaffold
make setup        # Install deps, start PostgreSQL, run migrations, seed data
make agent &      # Start FastAPI backend on :8000
make dev-frontend # Start Next.js frontend on :3000
```

Open [http://localhost:3000](http://localhost:3000) to see the attribution dashboard.

## What's Next?

- [Installation](installation.md) — Detailed setup guide with troubleshooting
- [Quick Start](quickstart.md) — Walkthrough of the running application
- [Concepts](../concepts/index.md) — Understand the theory behind the scaffold
