import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from starlette_context import context

from common.context.request_context import RequestContext
from common.dependencies.auth_dependency.get_current_user_dependency import (
    get_current_user,
)
from common.dependencies.service_dependency.employee_service_dependency import (
    create_employee_service,
    delete_employee_service,
    get_all_employee_service,
    get_employee_service,
    patch_employee_service,
)
from employee.application.models.request.create_employee_model import (
    CreateEmployeeRequest,
)
from employee.application.models.request.get_all_employee_request_model import (
    GetAllEmployeeRequest,
)
from employee.application.models.request.patch_employee_model import (
    PatchEmployeeRequest,
)
from employee.application.models.response.current_user_response_model import (
    CurrentUserResponse,
)
from employee.application.models.response.employee_list_response_model import (
    EmployeeListResponse,
)
from employee.application.models.response.employee_response_model import (
    EmployeeResponse,
)
from employee.application.models.response.message_response_model import MessageResponse
from employee.application.services.interface.create_employee_service_interface import (
    CreateEmployeeServiceInterface,
)
from employee.application.services.interface.delete_employee_service_interface import (
    DeleteEmployeeServiceInterface,
)
from employee.application.services.interface.get_all_employee_service_interface import (
    GetAllEmployeeServiceInterface,
)
from employee.application.services.interface.get_employee_service_interface import (
    GetEmployeeServiceInterface,
)
from employee.application.services.interface.patch_employee_service_interface import (
    PatchEmployeeServiceInterface,
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/employees", tags=["Employees"], dependencies=[Depends(get_current_user)]
)


@router.get("/me", response_model=CurrentUserResponse)
async def get_me():
    current_admin = RequestContext.get_current_user()
    logger.info("GET /auth/me called")
    return current_admin


@router.post("/", response_model=EmployeeResponse)
async def create_employee(
    request: CreateEmployeeRequest,
    service: CreateEmployeeServiceInterface = Depends(create_employee_service),
):
    current_admin = RequestContext.get_current_user()
    logger.info("POST /employees called")
    return service.create(request, current_admin)


@router.get("/{id}", response_model=EmployeeResponse)
async def get_employee_by_id(
    id: int, service: GetEmployeeServiceInterface = Depends(get_employee_service)
):
    current_admin = RequestContext.get_current_user()
    logger.info("GET /employees/{id} called")
    return service.get_employee(id, current_admin)


@router.get("/", response_model=EmployeeListResponse)
async def get_all_employee(
    request: Annotated[GetAllEmployeeRequest, Query()],
    service: GetAllEmployeeServiceInterface = Depends(get_all_employee_service),
):
    current_admin = RequestContext.get_current_user()
    logger.info("GET /employees called")
    return service.get_all(request, current_admin)


@router.patch("/{id}", response_model=EmployeeResponse)
async def patch_employee(
    id: int,
    request: PatchEmployeeRequest,
    service: PatchEmployeeServiceInterface = Depends(patch_employee_service),
):
    current_admin = RequestContext.get_current_user()
    logger.info("PATCH /employees/{id} called")
    return service.patch(id, request, current_admin)


@router.delete("/{id}", response_model=MessageResponse)
async def delete_employee(
    id: int, service: DeleteEmployeeServiceInterface = Depends(delete_employee_service)
):
    current_admin = RequestContext.get_current_user()
    logger.info("DELETE /employees/{id} called")
    return service.delete(id, current_admin)
