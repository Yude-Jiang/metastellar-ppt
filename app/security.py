"""Access control, rate limiting, and safe error messages."""
from __future__ import annotations

import asyncio
import logging
import time
from collections import defaultdict

from fastapi import Request

from . import config

logger = logging.getLogger(__name__)
_hits: dict[str, list[float]] = defaultdict(list)


def client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return "unknown"


def check_rate_limit(request: Request) -> str | None:
    ip = client_ip(request)
    now = time.time()
    window = 60.0
    hits = [t for t in _hits[ip] if now - t < window]
    if len(hits) >= config.RATE_LIMIT_PER_MINUTE:
        return "Too many requests. Please wait a minute and try again."
    hits.append(now)
    _hits[ip] = hits
    return None


def _extract_token(request: Request) -> str:
    token = request.headers.get("x-access-token", "").strip()
    if token:
        return token
    auth = request.headers.get("authorization", "")
    if auth.lower().startswith("bearer "):
        return auth[7:].strip()
    # img/a tags cannot send custom headers; file previews/downloads use query param.
    return request.query_params.get("access_token", "").strip()


def verify_access(request: Request) -> str | None:
    if not config.ACCESS_TOKEN:
        return None
    if _extract_token(request) != config.ACCESS_TOKEN:
        return "Unauthorized. Provide a valid access token."
    return None


def guard_request(request: Request) -> str | None:
    err = verify_access(request)
    if err:
        return err
    return check_rate_limit(request)


def user_facing_error(exc: BaseException) -> str:
    logger.exception("request failed")
    if isinstance(exc, asyncio.TimeoutError):
        return "The request timed out. Try fewer pages or a simpler brief."
    msg = str(exc).lower()
    if "timeout" in msg:
        return "The request timed out. Try fewer pages or a simpler brief."
    if "api_key" in msg or "cursor" in msg:
        return "Agent service is temporarily unavailable. Contact the tool owner."
    return "Something went wrong. Please try again or simplify your request."
