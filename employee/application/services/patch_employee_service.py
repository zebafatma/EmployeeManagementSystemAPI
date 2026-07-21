import logging
from datetime import date

from common.exception.bad_request_exception import (
    EmployeeMustBeAdultException,
    InvalidCurrencyException,
    InvalidDateOfBirthException,
    InvalidJoiningDateException,
    InvalidRoleException,
    ManagerDoesnotExistException,
)
from common.exception.conflict_exception import EmployeeWithEmailAlreadyExistsException
from common.exception.not_found_exception import EmployeeWithIdNotFoundException
from common.utils.date_validator import DateValidator
from employee.application.models.request.patch_employee_model import (
    PatchEmployeeRequest,
)
from employee.infrastructure.repository.employee_repository import EmployeeRepository

logger = logging.getLogger(__name__)


class PatchEmployeeService:
    def patch(self, id: int, request: PatchEmployeeRequest, current_admin):

        logger.info(f"Update request recieved by admin {current_admin.id}")

        repository = EmployeeRepository()
        try:

            employee = repository.get_employee_by_id(id)

            if employee is None:
                logger.warning(f"Employee {id} not found")
                raise EmployeeWithIdNotFoundException()

            if request.email is not None:
                existing_emp = repository.get_employee_by_email(request.email)
                if existing_emp is not None and existing_emp.emp_id != id:
                    logger.warning(f"Employee with email {request.email} already exist")
                    raise EmployeeWithEmailAlreadyExistsException()

            if request.role is not None:
                if request.role not in ("admin", "employee"):
                    logger.warning(f"Invalid Role: {request.role}")
                    raise InvalidRoleException()

            if request.manager_id is not None:
                manager = repository.get_employee_by_id(request.manager_id)
                if manager is None:
                    logger.warning(f"Manager {request.manager_id} not found")
                    raise ManagerDoesnotExistException()

            if request.currency is not None and request.currency not in ("INR", "USD"):
                logger.warning("Invalid Currency for Salary")
                raise InvalidCurrencyException()

            update_data = request.model_dump(exclude_unset=True)

            if "date_of_birth" in update_data:
                dob = DateValidator.validate(update_data["date_of_birth"])
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
                doj = DateValidator.validate(update_data["date_of_join"])
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
            return repository.update(employee)
        finally:
            repository.close()
