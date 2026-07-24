import logging
from datetime import date

from common.exception.bad_request_exception import (
    EmployeeMustBeAdultException,
    InvalidDateOfBirthException,
    InvalidJoiningDateException,
)
from common.exception.not_found_exception import EmployeeWithIdNotFoundException
from common.utils.request_validation import RequestValidation
from employee.application.models.request.patch_employee_model import (
    PatchEmployeeRequest,
)
from employee.application.services.interface.patch_employee_service_interface import PatchEmployeeServiceInterface
from employee.application.validations.employee_validator import EmployeeValidator
from employee.infrastructure.repository.interface.employee_repository_interface import EmployeeRepositoryInterface

logger = logging.getLogger(__name__)


class PatchEmployeeService(PatchEmployeeServiceInterface):

    def __init__(self, repository:EmployeeRepositoryInterface):
        self.repository=repository

    def patch(self, id: int, request: PatchEmployeeRequest, current_admin):

        logger.info(f"Update request recieved by admin {current_admin.id}")

        try:

            employee = self.repository.get_employee_by_id(id)

            if employee is None:
                logger.warning(f"Employee {id} not found")
                raise EmployeeWithIdNotFoundException(id)

            request = EmployeeValidator.validate_employee(request, self.repository)

            update_data = request.model_dump(exclude_unset=True)

            if "date_of_birth" in update_data:
                dob = RequestValidation.validate_date(
                    update_data["date_of_birth"], "date_of_birth"
                )
                if dob > date.today():
                    logger.warning("Invalid Date of Birth")
                    raise InvalidDateOfBirthException()
                age = (
                    date.today().year
                    - dob.year
                    - ((date.today().month, date.today().day) < (dob.month, dob.day))
                )
                if age < 18:
                    logger.warning("Employee not an Adult")
                    raise EmployeeMustBeAdultException()
                update_data["date_of_birth"] = dob

            if "date_of_join" in update_data:
                doj = RequestValidation.validate_date(
                    update_data["date_of_join"], "date_of_join"
                )
                if doj > date.today():
                    logger.warning("Invalid Date of Join")
                    raise InvalidJoiningDateException()
                update_data["date_of_join"] = doj

            for key, value in update_data.items():
                setattr(employee, key, value)

            employee.updated_by = current_admin.id

            logger.info(
                f"Employee {id} updated successfully by admin {current_admin.id}"
            )
            return self.repository.update(employee)
        finally:
            self.repository.close()
