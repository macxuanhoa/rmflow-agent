from __future__ import annotations

from fastapi import APIRouter, Query

from app.services.mock_data_service import get_mock_data_service
from app.utils.responses import error_response, now_ms, success_response

router = APIRouter(prefix="/api/customers", tags=["customers"])


@router.get("")
def list_customers(rm_id: str | None = Query(default=None)):
    start_ms = now_ms()
    service = get_mock_data_service()
    customers = service.list_customers(rm_id=rm_id)
    sources = [customer["customer_id"] for customer in customers]
    return success_response(data=customers, sources=sources, start_ms=start_ms)


@router.get("/{customer_id}")
def get_customer(customer_id: str):
    start_ms = now_ms()
    service = get_mock_data_service()
    customer = service.get_customer(customer_id=customer_id)

    if customer is None:
        return error_response(
            code="NOT_FOUND",
            message="Resource not found",
            details={"customer_id": customer_id},
            start_ms=start_ms,
            status_code=404,
        )

    return success_response(data=customer, sources=[customer_id], start_ms=start_ms)
