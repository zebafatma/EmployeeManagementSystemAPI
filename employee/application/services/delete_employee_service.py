import logging

from common.exception.not_found_exception import EmployeeWithIdNotFoundException
from employee.infrastructure.repository.employee_repository import EmployeeRepository

logger = logging.getLogger(__name__)


class DeleteEmployeeService:
    def delete(self, id: int, current_admin):

        logger.info(f"Delete request recieved by admin {current_admin.id}")

        repository = EmployeeRepository()
        try:
            employee = repository.get_employee_by_id(id)
            if employee is None:
                logger.error(f"Employee {id} not found")
                raise EmployeeWithIdNotFoundException(id)
            repository.delete(employee)
            logger.info(
                f"Employee {id} deleted successfully by admin {current_admin.id}"
            )
            return {"message": "Employee deleted successfully!"}
        finally:
            repository.close()
