"""Token bucket rate limiter for API compliance."""

from __future__ import annotations

import asyncio
import time


class TokenBucketRateLimiter:
    """Async token bucket rate limiter.

    Enforces a maximum request rate to comply with API rate limits.
    MusicBrainz: 1 req/s. Discogs: 60 req/min authenticated.

    Args:
        rate: Tokens added per second.
        capacity: Maximum bucket capacity (burst size).
    """

    def __init__(self, rate: float = 1.0, capacity: int = 1) -> None:
        self._rate = rate
        self._capacity = capacity
        self._tokens = float(capacity)
        self._last_refill = time.monotonic()
        self._lock = asyncio.Lock()

    async def acquire(self) -> bool:
        """Acquire a token, waiting if necessary.

        Returns:
            True when a token has been acquired.
        """
        async with self._lock:
            self._refill()
            if self._tokens >= 1.0:
                self._tokens -= 1.0
                return True
            wait_time = (1.0 - self._tokens) / self._rate
            await asyncio.sleep(wait_time)
            self._refill()
            self._tokens -= 1.0
            return True

    def _refill(self) -> None:
        """Add tokens based on elapsed time."""
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self._capacity, self._tokens + elapsed * self._rate)
        self._last_refill = now
