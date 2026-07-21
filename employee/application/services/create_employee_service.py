import logging
from datetime import date

from common.exception.bad_request_exception import (
    EmployeeMustBeAdultException,
    InvalidDateOfBirthException,
    InvalidJoiningDateException,
    InvalidPhoneNumberException,
    InvalidRoleException,
    ManagerDoesnotExistException,
)
from common.exception.conflict_exception import EmployeeWithEmailAlreadyExistsException
from common.utils.date_validator import DateValidator
from employee.application.models.request.create_employee_model import (
    CreateEmployeeRequest,
)
from employee.infrastructure.entities.employee_entity import Employee
from employee.infrastructure.repository.employee_repository import EmployeeRepository

logger = logging.getLogger(__name__)


class CreateEmployeeService:
    def create(self, request: CreateEmployeeRequest, current_admin):

        logger.info(f"Create request recieved by admin {current_admin.id}")

        repository = EmployeeRepository()
        try:
            dob = DateValidator.validate(request.date_of_birth)
            doj = DateValidator.validate(request.date_of_join)

            employee = repository.get_employee_by_email(request.email)

            if employee:
                logger.warning(f"Email {employee.email} already exists.")
                raise EmployeeWithEmailAlreadyExistsException()

            if request.role not in ("admin", "employee"):
                logger.warning(f"Invalid role {request.role}")
                raise InvalidRoleException()

            if request.manager_id is not None:
                manager = repository.get_employee_by_id(request.manager_id)
                if manager is None:
                    logger.warning(
                        f"Manager with id: {request.manager_id} doesnot exist."
                    )
                    raise ManagerDoesnotExistException()

            if dob > date.today():
                logger.warning("Invalid Date of Birth")
                raise InvalidDateOfBirthException()

            if doj > date.today():
                logger.warning("Invalid Date of Join")
                raise InvalidJoiningDateException()

            age = (
                date.today().year
                - dob.year
                - ((date.today().month, date.today().day) < (dob.month, dob.day))
            )
            if age < 18:
                logger.warning("Employee not an Adult")
                raise EmployeeMustBeAdultException()

            if not request.phone_no.isdigit() or len(request.phone_no) != 10:
                logger.warning(
                    f"Invalid Phone Number request for Employee {request.email}"
                )
                raise InvalidPhoneNumberException()

            employee = Employee(
                role=request.role,
                name=request.name,
                date_of_birth=dob,
                gender=request.gender,
                email=request.email,
                phone_no=request.phone_no,
                address=request.address,
                pan_number=request.pan_number,
                emergency_contact_name=request.emergency_contact_name,
                emergency_contact_phone=request.emergency_contact_phone,
                department=request.department,
                designation=request.designation,
                date_of_join=doj,
                manager_id=request.manager_id,
                salary=request.salary,
                created_by=current_admin.id,
                updated_by=current_admin.id,
            )

            created_employee = repository.create(employee)
            logger.info(
                f"Employee {created_employee.id} created successfully by admin {current_admin.id}"
            )
            return created_employee
        finally:
            repository.close()
