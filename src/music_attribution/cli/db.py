"""Database management CLI commands.

Provides async functions for seed, reset, and status operations.
Can be run directly via `python -m music_attribution.cli.db <command>`.
"""

from __future__ import annotations

import asyncio
import logging
import sys

from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from music_attribution.db.models import AttributionRecordModel
from music_attribution.seed.imogen_heap import seed_imogen_heap

logger = logging.getLogger(__name__)


async def run_seed(factory: async_sessionmaker[AsyncSession]) -> None:
    """Seed the database with Imogen Heap mock data.

    Args:
        factory: Async session factory bound to the target database.
    """
    async with factory() as session:
        await seed_imogen_heap(session)
        await session.commit()
    logger.info("Seed complete: Imogen Heap attribution data loaded")


async def run_reset(factory: async_sessionmaker[AsyncSession]) -> None:
    """Clear all data from attribution tables.

    Args:
        factory: Async session factory bound to the target database.
    """
    async with factory() as session:
        await session.execute(delete(AttributionRecordModel))
        await session.commit()
    logger.info("Reset complete: all attribution records deleted")


async def run_status(factory: async_sessionmaker[AsyncSession]) -> dict[str, int]:
    """Return record counts for each table.

    Args:
        factory: Async session factory bound to the target database.

    Returns:
        Dictionary mapping table names to record counts.
    """
    counts: dict[str, int] = {}
    async with factory() as session:
        result = await session.execute(
            select(func.count()).select_from(AttributionRecordModel)
        )
        counts["attribution_records"] = result.scalar() or 0
    return counts


def _main() -> None:
    """Entry point for CLI usage."""
    import os

    from music_attribution.db.engine import async_session_factory, create_async_engine_factory

    logging.basicConfig(level=logging.INFO)

    database_url = os.environ.get("DATABASE_URL", "postgresql+psycopg://music:music@localhost:5432/music_attribution")
    engine = create_async_engine_factory(database_url)
    factory = async_session_factory(engine)

    if len(sys.argv) < 2:
        print("Usage: python -m music_attribution.cli.db <seed|reset|status>")  # noqa: T201
        sys.exit(1)

    command = sys.argv[1]

    if command == "seed":
        asyncio.run(run_seed(factory))
    elif command == "reset":
        asyncio.run(run_reset(factory))
    elif command == "status":
        counts = asyncio.run(run_status(factory))
        for table, count in counts.items():
            print(f"  {table}: {count}")  # noqa: T201
    else:
        print(f"Unknown command: {command}")  # noqa: T201
        sys.exit(1)


if __name__ == "__main__":
    _main()
