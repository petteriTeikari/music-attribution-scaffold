"""Health check endpoint for the Music Attribution API.

Provides a minimal ``GET /health`` endpoint used by container
orchestrators (Docker health checks, Kubernetes liveness probes) and
uptime monitors to verify the service is running.

The endpoint does not check database connectivity — it only confirms
that the FastAPI process is alive and able to serve HTTP responses.
For deeper health checks, see the ``/metrics`` endpoint.
"""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Return a simple health status for the service.

    ``GET /health``

    Returns a static JSON object confirming the service is alive.
    This endpoint is intentionally cheap — no database queries, no
    external calls.

    Returns
    -------
    dict[str, str]
        Dictionary with ``status`` (always ``"healthy"``) and
        ``service`` (always ``"music-attribution-api"``).

    Examples
    --------
    >>> import httpx
    >>> resp = httpx.get("http://localhost:8000/health")
    >>> resp.json()
    {'status': 'healthy', 'service': 'music-attribution-api'}
    """
    return {"status": "healthy", "service": "music-attribution-api"}
