from __future__ import annotations

from fastapi import APIRouter

from app.services.mock_data_service import get_mock_data_service
from app.utils.responses import now_ms, success_response

router = APIRouter(prefix="/api/audit-logs", tags=["audit-logs"])


@router.get("")
def list_audit_logs():
    start_ms = now_ms()
    service = get_mock_data_service()
    audit_logs = service.list_audit_logs()
    sources = [audit_log["audit_log_id"] for audit_log in audit_logs if audit_log.get("audit_log_id")]
    return success_response(data=audit_logs, sources=sources, start_ms=start_ms)
