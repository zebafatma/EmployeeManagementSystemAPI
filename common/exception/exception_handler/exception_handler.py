import logging

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from common.exception.app_exception import AppException

logger = logging.getLogger(__name__)


async def app_exception_handler(request: Request, exc: AppException):
    logger.error(f"{request.method} {request.url.path} - {exc.message}")
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled exception at {request.method} {request.url.path}")
    return JSONResponse(
        status_code=500, content={"success": False, "message": "Internal Server Error"}
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.exception(f"Request validation failed: {exc.errors()}")
    return JSONResponse(
        status_code=400,
        content={"message": "Validation failed", "errors": exc.errors()},
    )
