import logging

from common.exception.not_found_exception import EmployeeWithIdNotFoundException
from employee.infrastructure.repository.interface.employee_repository_interface import EmployeeRepositoryInterface
from employee.application.services.interface.delete_employee_service_interface import DeleteEmployeeServiceInterface
logger = logging.getLogger(__name__)


class DeleteEmployeeService(DeleteEmployeeServiceInterface):

    def __init__(self, repository:EmployeeRepositoryInterface):
        self.repository=repository

    def delete(self, id: int, current_admin):

        logger.info(f"Delete request recieved by admin {current_admin.id}")

        try:
            employee = self.repository.get_employee_by_id(id)
            if employee is None:
                logger.error(f"Employee {id} not found")
                raise EmployeeWithIdNotFoundException(id)
            self.repository.delete(employee)
            logger.info(
                f"Employee {id} deleted successfully by admin {current_admin.id}"
            )
            return {"message": "Employee deleted successfully!"}
        finally:
            self.repository.close()
