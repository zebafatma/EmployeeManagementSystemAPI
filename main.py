from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from common.exception.app_exception import AppException
from common.exception.exception_handler.exception_handler import (
    app_exception_handler,
    global_exception_handler,
    validation_exception_handler,
)
from common.logger.logger import configure_logging
from data.database import Base, engine
from employee.endpoints.auth_endpoint import router as auth_router
from employee.endpoints.employee_endpoint import router as employee_router
from employee.endpoints.home_endpoint import router as home_router
from startup import lifespan

app = FastAPI(
    title="Employee Management System",
    version="1.0.0",
    description="REST API for managing Employees",
    lifespan=lifespan,
)

configure_logging()

Base.metadata.create_all(
    bind=engine
)  # creates all the tables in the database if they don't exist already

app.add_exception_handler(AppException, app_exception_handler)  # type: ignore
app.add_exception_handler(Exception, global_exception_handler)  # type: ignore
app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore

app.include_router(home_router)

app.include_router(auth_router)

app.include_router(employee_router)
