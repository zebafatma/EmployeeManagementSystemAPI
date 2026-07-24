import logging

from common.exception.bad_request_exception import ManagerDoesnotExistException
from common.exception.conflict_exception import EmployeeWithEmailAlreadyExistsException
from common.utils.request_validation import RequestValidation

logger = logging.getLogger(__name__)


class EmployeeValidator:
    @staticmethod
    def validate_employee(request, repository):
        if request.role is not None:
            request.role = RequestValidation.validate_role(request.role)

        if request.name is not None:
            request.name = RequestValidation.validate_name(request.name, "name")

        if request.gender is not None:
            request.gender = RequestValidation.validate_gender(request.gender)

        if request.phone_no is not None:
            request.phone_no = RequestValidation.validate_phone(
                request.phone_no, "phone_no"
            )

        if request.address is not None:
            request.address = RequestValidation.validate_address(request.address)

        if request.pan_number is not None:
            request.pan_number = RequestValidation.validate_pan(request.pan_number)

        if request.emergency_contact_name is not None:
            request.emergency_contact_name = RequestValidation.validate_name(
                request.emergency_contact_name, "emergency_contact_name"
            )

        if request.emergency_contact_phone is not None:
            request.emergency_contact_phone = RequestValidation.validate_phone(
                request.emergency_contact_phone, "emergency_contact_phone"
            )

        if request.department is not None:
            request.department = RequestValidation.validate_department(
                request.department
            )

        if request.designation is not None:
            request.designation = RequestValidation.validate_designation(
                request.designation
            )

        if request.salary is not None:
            request.salary = RequestValidation.validate_salary(request.salary)

        if request.currency is not None:
            request.currenct = RequestValidation.validate_currency(request.currency)

        if request.email is not None:
            employee = repository.get_employee_by_email(request.email)
            if employee:
                logger.error(f"Email {employee.email} already exists.")
                raise EmployeeWithEmailAlreadyExistsException(request.email)

        if request.manager_id is not None:
            manager = repository.get_employee_by_id(request.manager_id)
            if manager is None:
                logger.error(f"Manager {request.manager_id} not found")
                raise ManagerDoesnotExistException(request.manager_id)

        return request
