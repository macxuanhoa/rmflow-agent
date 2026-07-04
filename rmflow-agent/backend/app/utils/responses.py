from __future__ import annotations

import time
from typing import Any

from fastapi.responses import JSONResponse


CRM_MODE = "mock"
FALLBACK_STATUS = "none"


def now_ms() -> float:
    return time.perf_counter() * 1000


def elapsed_ms(start_ms: float) -> int:
    return max(0, int((time.perf_counter() * 1000) - start_ms))


def success_response(
    data: Any,
    sources: list[str],
    start_ms: float,
    status_code: int = 200,
) -> JSONResponse:
    payload = {
        "success": True,
        "data": data,
        "sources": sorted(set(sources)),
        "crm_mode": CRM_MODE,
        "fallback_status": FALLBACK_STATUS,
        "latency_ms": elapsed_ms(start_ms),
    }
    return JSONResponse(status_code=status_code, content=payload)


def error_response(
    code: str,
    message: str,
    details: dict[str, Any],
    start_ms: float,
    status_code: int,
) -> JSONResponse:
    payload = {
        "success": False,
        "error": {
            "code": code,
            "message": message,
            "details": details,
        },
        "crm_mode": CRM_MODE,
        "fallback_status": FALLBACK_STATUS,
        "latency_ms": elapsed_ms(start_ms),
    }
    return JSONResponse(status_code=status_code, content=payload)
