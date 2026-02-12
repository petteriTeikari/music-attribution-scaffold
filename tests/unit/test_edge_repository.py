"""Tests for async PostgreSQL edge repository with recursive CTE graph traversal."""

from __future__ import annotations

import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from music_attribution.db.models import EdgeModel


@pytest.fixture
async def async_session():
    """Create an in-memory async SQLite database with edges table."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(EdgeModel.__table__.create)

    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with session_factory() as session:
        yield session

    await engine.dispose()


class TestAsyncEdgeRepository:
    """Tests for AsyncEdgeRepository."""

    async def test_add_edge(self, async_session: AsyncSession) -> None:
        """Add an edge between two entities."""
        from music_attribution.resolution.edge_repository import AsyncEdgeRepository

        repo = AsyncEdgeRepository()
        from_id = uuid.uuid4()
        to_id = uuid.uuid4()

        edge_id = await repo.add_edge(
            from_entity_id=from_id,
            to_entity_id=to_id,
            relationship_type="PERFORMED",
            confidence=0.95,
            session=async_session,
        )
        assert isinstance(edge_id, uuid.UUID)

    async def test_get_neighbors_depth_1(self, async_session: AsyncSession) -> None:
        """Get direct neighbors (depth 1)."""
        from music_attribution.resolution.edge_repository import AsyncEdgeRepository

        repo = AsyncEdgeRepository()
        a, b, c = uuid.uuid4(), uuid.uuid4(), uuid.uuid4()

        await repo.add_edge(a, b, "PERFORMED", 0.9, session=async_session)
        await repo.add_edge(a, c, "WROTE", 0.8, session=async_session)

        neighbors = await repo.get_neighbors(a, depth=1, session=async_session)
        neighbor_ids = {n.to_entity_id for n in neighbors}
        assert b in neighbor_ids
        assert c in neighbor_ids

    async def test_get_neighbors_depth_2(self, async_session: AsyncSession) -> None:
        """Get 2-hop neighbors via recursive CTE."""
        from music_attribution.resolution.edge_repository import AsyncEdgeRepository

        repo = AsyncEdgeRepository()
        a, b, c, d = uuid.uuid4(), uuid.uuid4(), uuid.uuid4(), uuid.uuid4()

        # a -> b -> c, a -> d
        await repo.add_edge(a, b, "PERFORMED", 0.9, session=async_session)
        await repo.add_edge(b, c, "PERFORMED", 0.8, session=async_session)
        await repo.add_edge(a, d, "WROTE", 0.7, session=async_session)

        # Depth 1: should find b, d
        depth1 = await repo.get_neighbors(a, depth=1, session=async_session)
        depth1_targets = {n.to_entity_id for n in depth1}
        assert b in depth1_targets
        assert d in depth1_targets
        assert c not in depth1_targets

        # Depth 2: should also find c
        depth2 = await repo.get_neighbors(a, depth=2, session=async_session)
        depth2_targets = {n.to_entity_id for n in depth2}
        assert c in depth2_targets

    async def test_find_related_by_type(self, async_session: AsyncSession) -> None:
        """Filter neighbors by relationship_type."""
        from music_attribution.resolution.edge_repository import AsyncEdgeRepository

        repo = AsyncEdgeRepository()
        a, b, c = uuid.uuid4(), uuid.uuid4(), uuid.uuid4()

        await repo.add_edge(a, b, "PERFORMED", 0.9, session=async_session)
        await repo.add_edge(a, c, "WROTE", 0.8, session=async_session)

        performed = await repo.get_neighbors(a, depth=1, rel_type="PERFORMED", session=async_session)
        assert len(performed) == 1
        assert performed[0].to_entity_id == b

    async def test_cycle_prevention(self, async_session: AsyncSession) -> None:
        """Recursive CTE doesn't infinite loop on cycles."""
        from music_attribution.resolution.edge_repository import AsyncEdgeRepository

        repo = AsyncEdgeRepository()
        a, b, c = uuid.uuid4(), uuid.uuid4(), uuid.uuid4()

        # Create a cycle: a -> b -> c -> a
        await repo.add_edge(a, b, "RELATED", 0.9, session=async_session)
        await repo.add_edge(b, c, "RELATED", 0.8, session=async_session)
        await repo.add_edge(c, a, "RELATED", 0.7, session=async_session)

        # Should terminate and find b, c (not revisit a)
        neighbors = await repo.get_neighbors(a, depth=5, session=async_session)
        target_ids = {n.to_entity_id for n in neighbors}
        assert b in target_ids
        assert c in target_ids
        # Should not contain start node
        assert a not in target_ids

    async def test_get_edges_for_entity(self, async_session: AsyncSession) -> None:
        """Get all edges where entity is from or to."""
        from music_attribution.resolution.edge_repository import AsyncEdgeRepository

        repo = AsyncEdgeRepository()
        a, b, c = uuid.uuid4(), uuid.uuid4(), uuid.uuid4()

        await repo.add_edge(a, b, "PERFORMED", 0.9, session=async_session)
        await repo.add_edge(c, a, "WROTE", 0.8, session=async_session)

        edges = await repo.get_edges(a, session=async_session)
        assert len(edges) == 2
