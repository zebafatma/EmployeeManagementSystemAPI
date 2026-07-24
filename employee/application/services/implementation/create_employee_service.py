import logging
from datetime import date

from common.exception.bad_request_exception import (
    EmployeeMustBeAdultException,
    InvalidDateOfBirthException,
    InvalidJoiningDateException,
)
from employee.application.services.interface.create_employee_service_interface import CreateEmployeeServiceInterface
from common.utils.request_validation import RequestValidation
from employee.application.models.request.create_employee_model import (
    CreateEmployeeRequest,
)
from employee.application.validations.employee_validator import EmployeeValidator
from employee.infrastructure.entities.employee_entity import Employee
from employee.infrastructure.repository.interface.employee_repository_interface import EmployeeRepositoryInterface

logger = logging.getLogger(__name__)


class CreateEmployeeService(CreateEmployeeServiceInterface):

    def __init__(self, repository:EmployeeRepositoryInterface):
        self.repository=repository

    def create(self, request: CreateEmployeeRequest, current_admin):

        logger.info(f"Create request recieved by admin {current_admin.id}")

        try:
            request = EmployeeValidator.validate_employee(request, self.repository)

            dob = RequestValidation.validate_date(
                request.date_of_birth, "date_of_birth"
            )
            doj = RequestValidation.validate_date(request.date_of_join, "date_of_join")

            if dob > date.today():
                logger.error("Invalid Date of Birth")
                raise InvalidDateOfBirthException()

            if doj > date.today():
                logger.error("Invalid Date of Join")
                raise InvalidJoiningDateException()

            age = (
                date.today().year
                - dob.year
                - ((date.today().month, date.today().day) < (dob.month, dob.day))
            )
            if age < 18:
                logger.error("Employee not an Adult")
                raise EmployeeMustBeAdultException()

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

            created_employee = self.repository.create(employee)
            logger.info(
                f"Employee {created_employee.id} created successfully by admin {current_admin.id}"
            )
            return created_employee
        finally:
            self.repository.close()
