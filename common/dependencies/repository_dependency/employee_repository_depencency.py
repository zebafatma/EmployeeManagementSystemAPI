from employee.infrastructure.repository.interface.employee_repository_interface import EmployeeRepositoryInterface
from employee.infrastructure.repository.implementation.employee_repository import EmployeeRepository

def get_employee_repository()->EmployeeRepositoryInterface:
    return EmployeeRepository()