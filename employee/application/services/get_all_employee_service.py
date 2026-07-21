import logging

from common.exception.bad_request_exception import (
    InvalidPageException,
    InvalidPageSizeException,
)
from employee.infrastructure.repository.employee_repository import EmployeeRepository

logger = logging.getLogger(__name__)


class GetAllEmployeesService:
    def get_all(
        self,
        current_admin,
        page: int,
        size: int,
        name: str | None = None,
        department: str | None = None,
        role: str | None = None,
        is_active: bool | None = None,
        manager_id: int | None = None,
    ):

        logger.info(f"Get All request recieved by admin {current_admin.id}")

        repository = EmployeeRepository()
        try:

            if page < 1:
                logger.warning(f"Invlaid Page Number: {page}")
                raise InvalidPageException
            if size < 1:
                logger.warning(f"Invalid Page Size: {size}")
                raise InvalidPageSizeException
            offset = (page - 1) * size
            employees, total_records = repository.get_employees(
                offset=offset,
                limit=size,
                name=name,
                department=department,
                role=role,
                is_active=is_active,
                manager_id=manager_id,
            )
            total_pages = (total_records + size - 1) // size
            if page > total_pages and total_records > 0:
                logger.warning("Invalid Page Number")
                raise InvalidPageException()
            logger.info(f"Getting all employees for admin {current_admin.id}")
            return {
                "page": page,
                "size": size,
                "total_records": total_records,
                "total_pages": total_pages,
                "employees": employees,
            }
        finally:
            repository.close()
