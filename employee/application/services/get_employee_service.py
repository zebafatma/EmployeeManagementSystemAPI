import logging

from common.exception.not_found_exception import EmployeeWithIdNotFoundException
from employee.infrastructure.repository.employee_repository import EmployeeRepository

logger = logging.getLogger(__name__)


class GetEmployeeService:
    def get_employee(self, id, current_admin):

        logger.info(f"Get request recieved by admin {current_admin.id}")

        repository = EmployeeRepository()
        try:
            employee = repository.get_employee_by_id(id)
            if employee is None:
                logger.error(f"Employee {id} not found")
                raise EmployeeWithIdNotFoundException(id)
            logger.info(f"Getting Employee {id} for admin {current_admin.id}")
            return employee
        finally:
            repository.close()
