from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.core.logging import setup_logging, get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup / shutdown."""
    setup_logging()
    logger.info("DiLS startup — settings loaded, host=%s port=%s",
                get_settings().host, get_settings().port)
    yield
    logger.info("DiLS shutdown")


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="DiLS — Logistics System",
        version="0.1.0",
        debug=settings.debug,
        lifespan=lifespan,
    )

    # ── Health check ──────────────────────────────────────────
    @app.get("/health", tags=["system"])
    async def health():
        from app.db.session import check_connection
        db_ok = check_connection()
        status = "ok" if db_ok else "degraded"
        code = 200 if db_ok else 503
        return JSONResponse(
            content={"status": status, "database": "connected" if db_ok else "unavailable"},
            status_code=code,
        )

    # ── Exception handlers ────────────────────────────────────
    @app.exception_handler(Exception)
    async def unhandled_exception(request: Request, exc: Exception):
        logger.exception("Unhandled exception on %s %s", request.method, request.url.path)
        return JSONResponse(
            content={"detail": "Internal server error"},
            status_code=500,
        )

    return app


app = create_app()
