import logging

from common.exception.bad_request_exception import (
    InvalidPageException,
    InvalidPageSizeException,
)
from employee.application.models.request.get_all_employee_request_model import (
    GetAllEmployeeRequest,
)
from employee.application.services.interface.get_all_employee_service_interface import (
    GetAllEmployeeServiceInterface,
)
from employee.infrastructure.repository.interface.employee_repository_interface import (
    EmployeeRepositoryInterface,
)

logger = logging.getLogger(__name__)


class GetAllEmployeesService(GetAllEmployeeServiceInterface):

    def __init__(self, repository: EmployeeRepositoryInterface):
        self.repository = repository

    def get_all(self, request: GetAllEmployeeRequest, current_admin):

        logger.info(f"Get All request recieved by admin {current_admin.id}")

        try:

            if request.page < 1:
                logger.error(f"Invlaid Page Number: {request.page}")
                raise InvalidPageException
            if request.size < 1:
                logger.error(f"Invalid Page Size: {request.size}")
                raise InvalidPageSizeException
            offset = (request.page - 1) * request.size
            logger.info(type(self.repository))
            logger.info(self.repository)
            employees, total_records = self.repository.get_employees(
                offset=offset, request=request
            )
            total_pages = (total_records + request.size - 1) // request.size
            if request.page > total_pages and total_records > 0:
                logger.error("Invalid Page Number")
                raise InvalidPageException()
            logger.info(f"Getting all employees for admin {current_admin.id}")
            return {
                "page": request.page,
                "size": request.size,
                "total_records": total_records,
                "total_pages": total_pages,
                "employees": employees,
            }
        finally:
            self.repository.close()
