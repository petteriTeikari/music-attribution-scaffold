#!/usr/bin/env bash
set -euo pipefail

echo "==> Waiting for PostgreSQL to accept connections..."
# DATABASE_URL is required — fail loudly if missing
: "${DATABASE_URL:?DATABASE_URL must be set}"

echo "==> Running Alembic migrations..."
uv run alembic upgrade head

echo "==> Seeding demo data..."
uv run python -c "
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from music_attribution.seed.imogen_heap import seed_imogen_heap

async def seed():
    import os
    engine = create_async_engine(os.environ['DATABASE_URL'], echo=False)
    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with factory() as session:
        from sqlalchemy import text
        result = await session.execute(text('SELECT COUNT(*) FROM attribution_records'))
        count = result.scalar_one()
        if count == 0:
            await seed_imogen_heap(session)
            await session.commit()
            print(f'  Seeded {8} Imogen Heap records')
        else:
            print(f'  Database already has {count} records, skipping seed')
    await engine.dispose()

asyncio.run(seed())
"

echo "==> Starting uvicorn with hot-reload..."
exec uv run uvicorn music_attribution.api.app:create_app \
    --factory \
    --host 0.0.0.0 \
    --port 8000 \
    --reload \
    --reload-dir /app/src
