from employee.infrastructure.repository.implementation.employee_repository import (
    EmployeeRepository,
)
from employee.infrastructure.repository.interface.employee_repository_interface import (
    EmployeeRepositoryInterface,
)


def get_employee_repository() -> EmployeeRepositoryInterface:
    return EmployeeRepository()
