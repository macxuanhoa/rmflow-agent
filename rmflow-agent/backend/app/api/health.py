from __future__ import annotations

from fastapi import APIRouter

from app.utils.responses import now_ms, success_response

router = APIRouter(prefix="/api", tags=["health"])


@router.get("/health")
def health_check():
    start_ms = now_ms()
    data = {
        "status": "healthy",
        "service": "rmflow-agent-backend",
    }
    return success_response(data=data, sources=[], start_ms=start_ms)
