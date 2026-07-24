import logging

from common.exception.bad_request_exception import (
    InvalidPageException,
    InvalidPageSizeException,
)
from employee.application.models.request.get_all_employee_request_model import (
    GetAllEmployeeRequest,
)
from employee.infrastructure.repository.employee_repository import EmployeeRepository

logger = logging.getLogger(__name__)


class GetAllEmployeesService:
    def get_all(self, current_admin, request: GetAllEmployeeRequest):

        logger.info(f"Get All request recieved by admin {current_admin.id}")

        repository = EmployeeRepository()
        try:

            if request.page < 1:
                logger.error(f"Invlaid Page Number: {request.page}")
                raise InvalidPageException
            if request.size < 1:
                logger.error(f"Invalid Page Size: {request.size}")
                raise InvalidPageSizeException
            offset = (request.page - 1) * request.size
            employees, total_records = repository.get_employees(
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
            repository.close()
