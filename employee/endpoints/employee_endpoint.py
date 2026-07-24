import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Query

from common.dependencies import get_current_user
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
from employee.application.models.response.message_response_model import MessageResponse
from employee.application.services.create_employee_service import CreateEmployeeService
from employee.application.services.delete_employee_service import DeleteEmployeeService
from employee.application.services.get_all_employee_service import (
    GetAllEmployeesService,
)
from employee.application.services.get_employee_service import GetEmployeeService
from employee.application.services.patch_employee_service import PatchEmployeeService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/employees", tags=["Employees"])

create = CreateEmployeeService()


@router.post("/", response_model=EmployeeResponse)
def create_employee(
    request: CreateEmployeeRequest, current_admin=Depends(get_current_user)
):
    logger.info("POST /employees called")
    return create.create(request, current_admin)


get_employee = GetEmployeeService()


@router.get("/{id}", response_model=EmployeeResponse)
def get_employee_by_id(id: int, current_admin=Depends(get_current_user)):
    logger.info("GET /employees/{id} called")
    return get_employee.get_employee(id, current_admin)


get_employees = GetAllEmployeesService()


@router.get("/", response_model=EmployeeListResponse)
def get_all_employee(
    request: Annotated[GetAllEmployeeRequest, Query()],
    current_admin=Depends(get_current_user),
):
    logger.info("GET /employees called")
    return get_employees.get_all(current_admin, request)


patch = PatchEmployeeService()


@router.patch("/{id}", response_model=EmployeeResponse)
def patch_employee(
    id: int, request: PatchEmployeeRequest, current_admin=Depends(get_current_user)
):
    logger.info("PATCH /employees/{id} called")
    return patch.patch(id, request, current_admin)


delete = DeleteEmployeeService()


@router.delete("/{id}", response_model=MessageResponse)
def delete_employee(id: int, current_admin=Depends(get_current_user)):
    logger.info("DELETE /employees/{id} called")
    return delete.delete(id, current_admin)
