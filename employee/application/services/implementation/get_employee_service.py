import logging

from common.exception.not_found_exception import EmployeeWithIdNotFoundException
from employee.infrastructure.repository.interface.employee_repository_interface import EmployeeRepositoryInterface
from employee.application.services.interface.get_employee_service_interface import GetEmployeeServiceInterface

logger = logging.getLogger(__name__)


class GetEmployeeService(GetEmployeeServiceInterface):

    def __init__(self, repository:EmployeeRepositoryInterface):
        self.repository=repository
        
    def get_employee(self, id, current_admin):

        logger.info(f"Get request recieved by admin {current_admin.id}")

        try:
            employee = self.repository.get_employee_by_id(id)
            if employee is None:
                logger.error(f"Employee {id} not found")
                raise EmployeeWithIdNotFoundException(id)
            logger.info(f"Getting Employee {id} for admin {current_admin.id}")
            return employee
        finally:
            self.repository.close()
