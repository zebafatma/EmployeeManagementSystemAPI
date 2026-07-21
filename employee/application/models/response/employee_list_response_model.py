from pydantic import BaseModel

from employee.application.models.response.employee_response_model import (
    EmployeeResponse,
)


class EmployeeListResponse(BaseModel):
    page: int
    size: int
    total_records: int
    total_pages: int
    employees: list[EmployeeResponse]
