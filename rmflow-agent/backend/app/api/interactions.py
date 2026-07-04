from __future__ import annotations

from fastapi import APIRouter, Query

from app.services.mock_data_service import get_mock_data_service
from app.utils.responses import error_response, now_ms, success_response

router = APIRouter(prefix="/api/interactions", tags=["interactions"])


@router.get("")
def list_interactions(customer_id: str | None = Query(default=None)):
    start_ms = now_ms()
    service = get_mock_data_service()

    if customer_id and service.get_customer(customer_id=customer_id) is None:
        return error_response(
            code="NOT_FOUND",
            message="Resource not found",
            details={"customer_id": customer_id},
            start_ms=start_ms,
            status_code=404,
        )

    interactions = service.list_interactions(customer_id=customer_id)
    sources = [interaction["interaction_id"] for interaction in interactions]
    return success_response(data=interactions, sources=sources, start_ms=start_ms)
