"""Prometheus metrics endpoint for the Music Attribution API.

Exposes ``GET /metrics`` in Prometheus exposition format for scraping
by Prometheus, Grafana Agent, or any OpenMetrics-compatible collector.

The endpoint is excluded from the OpenAPI schema
(``include_in_schema=False``) so it does not appear in the Swagger UI
or auto-generated client stubs.

Notes
-----
Metrics are collected via the ``prometheus_client`` default registry
(``REGISTRY``).  Custom counters and histograms for attribution
pipeline stages can be registered elsewhere and will automatically
appear here.
"""

from __future__ import annotations

from fastapi import APIRouter, Response
from prometheus_client import REGISTRY, generate_latest

router = APIRouter(tags=["observability"])


@router.get("/metrics", include_in_schema=False)
async def metrics() -> Response:
    """Serve Prometheus metrics in exposition format.

    ``GET /metrics``

    Serialises all registered Prometheus collectors into the plain-text
    exposition format (version 0.0.4).  The response content type is
    set to ``text/plain; version=0.0.4; charset=utf-8`` as required by
    the Prometheus scraping protocol.

    Returns
    -------
    Response
        FastAPI ``Response`` with Prometheus-formatted metrics body and
        the correct content type header.

    Notes
    -----
    This endpoint is hidden from the OpenAPI schema to avoid cluttering
    the public API documentation.
    """
    return Response(
        content=generate_latest(REGISTRY),
        media_type="text/plain; version=0.0.4; charset=utf-8",
    )
