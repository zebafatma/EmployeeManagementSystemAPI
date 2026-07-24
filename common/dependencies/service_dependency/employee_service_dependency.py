from common.dependencies.repository_dependency.employee_repository_depencency import get_employee_repository
from employee.application.services.implementation.create_employee_service import CreateEmployeeService
from employee.application.services.implementation.patch_employee_service import PatchEmployeeService
from employee.application.services.implementation.delete_employee_service import DeleteEmployeeService
from employee.application.services.implementation.get_employee_service import GetEmployeeService
from employee.application.services.implementation.get_all_employee_service import GetAllEmployeesService
from employee.application.services.interface.create_employee_service_interface import CreateEmployeeServiceInterface
from employee.application.services.interface.patch_employee_service_interface import PatchEmployeeServiceInterface
from employee.application.services.interface.delete_employee_service_interface import DeleteEmployeeServiceInterface
from employee.application.services.interface.get_employee_service_interface import GetEmployeeServiceInterface
from employee.application.services.interface.get_all_employee_service_interface import GetAllEmployeeServiceInterface


def create_employee_service()->CreateEmployeeServiceInterface:
    return CreateEmployeeService(
        get_employee_repository()
    )

def patch_employee_service()->PatchEmployeeServiceInterface:
    return PatchEmployeeService(
        get_employee_repository()
    )

def delete_employee_service()->DeleteEmployeeServiceInterface:
    return DeleteEmployeeService(
        get_employee_repository()
    )

def get_employee_service()->GetEmployeeServiceInterface:
    return GetEmployeeService(
        get_employee_repository()
    )

def get_all_employee_service()->GetAllEmployeeServiceInterface:
    return GetAllEmployeesService(
        get_employee_repository()
    )