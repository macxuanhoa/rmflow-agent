from __future__ import annotations

from fastapi import APIRouter, Query

from app.services.mock_data_service import get_mock_data_service
from app.utils.responses import now_ms, success_response

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("")
def list_products(product_category: str | None = Query(default=None)):
    start_ms = now_ms()
    service = get_mock_data_service()
    products = service.list_products(product_category=product_category)
    sources = [product["product_id"] for product in products]
    return success_response(data=products, sources=sources, start_ms=start_ms)
