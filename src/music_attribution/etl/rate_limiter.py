"""Token-bucket rate limiter for external API compliance.

Provides an async-safe ``TokenBucketRateLimiter`` that enforces per-source
request rate limits to avoid API bans.  Used by all ETL connectors
(MusicBrainz, Discogs, AcoustID) to throttle outbound requests.

The token-bucket algorithm allows controlled bursts (up to ``capacity``
requests) while maintaining a steady-state rate of ``rate`` requests per
second.  Each ``acquire()`` call blocks until a token is available.

Notes
-----
The implementation uses ``time.monotonic()`` for clock-skew-resistant
timing and ``asyncio.Lock()`` for thread-safety within the async
event loop.
"""

from __future__ import annotations

import asyncio
import time


class TokenBucketRateLimiter:
    """Async token-bucket rate limiter.

    Enforces a maximum request rate to comply with external API rate
    limits.  Common configurations:

    * MusicBrainz: ``rate=1.0, capacity=1`` (1 req/s)
    * Discogs authenticated: ``rate=1.0, capacity=1`` (60 req/min)
    * Discogs unauthenticated: ``rate=0.42, capacity=1`` (25 req/min)
    * AcoustID: ``rate=3.0, capacity=3`` (3 req/s)

    Parameters
    ----------
    rate : float, optional
        Tokens added per second (steady-state request rate), by default
        1.0.
    capacity : int, optional
        Maximum tokens in the bucket (burst size), by default 1.

    Attributes
    ----------
    _tokens : float
        Current number of available tokens.
    _last_refill : float
        Monotonic timestamp of the last token refill.

    Examples
    --------
    >>> limiter = TokenBucketRateLimiter(rate=1.0, capacity=1)
    >>> await limiter.acquire()  # returns immediately if bucket is full
    True
    """

    def __init__(self, rate: float = 1.0, capacity: int = 1) -> None:
        self._rate = rate
        self._capacity = capacity
        self._tokens = float(capacity)
        self._last_refill = time.monotonic()
        self._lock = asyncio.Lock()

    async def acquire(self) -> bool:
        """Acquire a token, waiting if the bucket is empty.

        If no token is immediately available, calculates the minimum
        wait time for the next refill and sleeps asynchronously.  The
        method is serialised via an ``asyncio.Lock`` to prevent race
        conditions between concurrent coroutines.

        Returns
        -------
        bool
            Always ``True`` once a token has been successfully acquired.
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
        """Refill the bucket based on elapsed monotonic time.

        Adds ``elapsed_seconds * rate`` tokens to the bucket, clamped
        to ``capacity``.  Updates ``_last_refill`` to the current
        monotonic timestamp.
        """
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self._capacity, self._tokens + elapsed * self._rate)
        self._last_refill = now
