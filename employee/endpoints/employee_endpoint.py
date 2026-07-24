import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Query

from common.dependencies.auth_dependency.get_current_user_dependency import get_current_user
from employee.application.models.request.create_employee_model import (
    CreateEmployeeRequest,
)
from employee.application.models.request.get_all_employee_request_model import (
    GetAllEmployeeRequest,
)
from employee.application.models.request.patch_employee_model import (
    PatchEmployeeRequest,
)
from employee.application.models.response.employee_list_response_model import (
    EmployeeListResponse,
)
from employee.application.models.response.employee_response_model import (
    EmployeeResponse,
)
from common.dependencies.service_dependency.employee_service_dependency import get_all_employee_service, get_employee_service, create_employee_service, patch_employee_service, delete_employee_service
from employee.application.models.response.message_response_model import MessageResponse
from employee.application.services.interface.create_employee_service_interface import CreateEmployeeServiceInterface
from employee.application.services.interface.delete_employee_service_interface import DeleteEmployeeServiceInterface
from employee.application.services.interface.get_all_employee_service_interface import (
    GetAllEmployeeServiceInterface,
)
from employee.application.services.interface.get_employee_service_interface import GetEmployeeServiceInterface
from employee.application.services.interface.patch_employee_service_interface import PatchEmployeeServiceInterface

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=EmployeeResponse)
def create_employee(
    request: CreateEmployeeRequest, 
    current_admin=Depends(get_current_user),
    service:CreateEmployeeServiceInterface=Depends(create_employee_service)
):
    logger.info("POST /employees called")
    return service.create(request, current_admin)


@router.get("/{id}", response_model=EmployeeResponse)
def get_employee_by_id(
    id: int, 
    current_admin=Depends(get_current_user),
    service:GetEmployeeServiceInterface=Depends(get_employee_service)
):
    logger.info("GET /employees/{id} called")
    return service.get_employee(id, current_admin)


@router.get("/", response_model=EmployeeListResponse)
def get_all_employee(
    request: Annotated[GetAllEmployeeRequest, Query()],
    current_admin=Depends(get_current_user),
    service:GetAllEmployeeServiceInterface=Depends(get_all_employee_service)
):
    logger.info("GET /employees called")
    return service.get_all(current_admin, request)


@router.patch("/{id}", response_model=EmployeeResponse)
def patch_employee(
    id: int, 
    request: PatchEmployeeRequest, 
    current_admin=Depends(get_current_user),
    service:PatchEmployeeServiceInterface=Depends(patch_employee_service)
):
    logger.info("PATCH /employees/{id} called")
    return service.patch(id, request, current_admin)


@router.delete("/{id}", response_model=MessageResponse)
def delete_employee(
    id: int, 
    current_admin=Depends(get_current_user),
    service:DeleteEmployeeServiceInterface=Depends(delete_employee_service)):
    logger.info("DELETE /employees/{id} called")
    return service.delete(id, current_admin)
