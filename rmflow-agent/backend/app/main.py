from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.audit_logs import router as audit_logs_router
from app.api.campaigns import router as campaigns_router
from app.api.customers import router as customers_router
from app.api.health import router as health_router
from app.api.interactions import router as interactions_router
from app.api.opportunities import router as opportunities_router
from app.api.products import router as products_router
from app.api.templates import router as templates_router
from app.utils.responses import error_response, now_ms

app = FastAPI(title="RMFlow Agent Mock Backend", version="0.1.0")

app.include_router(health_router)
app.include_router(customers_router)
app.include_router(interactions_router)
app.include_router(opportunities_router)
app.include_router(campaigns_router)
app.include_router(products_router)
app.include_router(templates_router)
app.include_router(audit_logs_router)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    start_ms = now_ms()
    return error_response(
        code="HTTP_ERROR",
        message=exc.detail if isinstance(exc.detail, str) else "HTTP error",
        details={"path": str(request.url.path), "status_code": exc.status_code},
        start_ms=start_ms,
        status_code=exc.status_code,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    start_ms = now_ms()
    return error_response(
        code="VALIDATION_ERROR",
        message="Request validation failed",
        details={"path": str(request.url.path), "errors": exc.errors()},
        start_ms=start_ms,
        status_code=422,
    )


@app.get("/")
def root():
    start_ms = now_ms()
    return error_response(
        code="NOT_FOUND",
        message="Resource not found",
        details={"path": "/"},
        start_ms=start_ms,
        status_code=404,
    )
