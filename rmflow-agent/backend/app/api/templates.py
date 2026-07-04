from __future__ import annotations

from fastapi import APIRouter, Query

from app.services.mock_data_service import get_mock_data_service
from app.utils.responses import now_ms, success_response

router = APIRouter(prefix="/api/templates", tags=["templates"])


@router.get("")
def list_templates(
    channel: str | None = Query(default=None),
    product_category: str | None = Query(default=None),
):
    start_ms = now_ms()
    service = get_mock_data_service()
    templates = service.list_templates(channel=channel, product_category=product_category)
    sources = [template["source_id"] for template in templates if template.get("source_id")]
    return success_response(data=templates, sources=sources, start_ms=start_ms)
