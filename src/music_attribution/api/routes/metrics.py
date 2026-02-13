"""Prometheus metrics endpoint for the attribution API.

Exposes /metrics in Prometheus exposition format for scraping by
Prometheus, Grafana Agent, or any compatible collector.
"""

from __future__ import annotations

from fastapi import APIRouter, Response
from prometheus_client import REGISTRY, generate_latest

router = APIRouter(tags=["observability"])


@router.get("/metrics", include_in_schema=False)
async def metrics() -> Response:
    """Prometheus metrics endpoint.

    Returns:
        Prometheus exposition format text.
    """
    return Response(
        content=generate_latest(REGISTRY),
        media_type="text/plain; version=0.0.4; charset=utf-8",
    )
