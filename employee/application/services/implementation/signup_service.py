import logging

from common.auth.hash_password import hash_password
from common.exception.bad_request_exception import DiffrentEmailException
from common.exception.conflict_exception import AdminAlreadyExistsException
from common.exception.forbidden_exception import UnauthorizedEmployeeException
from common.exception.not_found_exception import EmployeeWithIdNotFoundException
from employee.application.models.request.signup_model import SignupRequest
from employee.infrastructure.entities.admin_credentials_entity import AdminCredentials
from employee.infrastructure.repository.interface.auth_repository_interface import AuthRepositoryInterface
from employee.infrastructure.repository.interface.employee_repository_interface import EmployeeRepositoryInterface
from employee.application.services.interface.signup_service_interface import SignupServiceInterface

logger = logging.getLogger(__name__)


class SignupService(SignupServiceInterface):

    def __init__(self, auth_repository:AuthRepositoryInterface, employee_repository:EmployeeRepositoryInterface):
        self.auth_repository=auth_repository
        self.employee_repository=employee_repository

    def signup(self, request: SignupRequest):

        logger.info(f"Signup request recieved by employee {request.id}")

        try:

            employee = self.employee_repository.get_employee_by_id(request.id)

            if employee is None:
                logger.error(f"Employee {request.id} not found")
                raise EmployeeWithIdNotFoundException(request.id)
            
            if employee.email != request.email:
                logger.error(
                    f"Signup email: {request.email} diffrent from original email"
                )
                raise DiffrentEmailException()
            
            if employee.role != "admin":
                logger.error(f"Employee {request.id} not authorized to signup")
                raise UnauthorizedEmployeeException()
            
            admin_exists = self.auth_repository.get_admin_by_email(employee.email)
            if admin_exists:
                logger.error(f"Admin with {request.email} already exist")
                raise AdminAlreadyExistsException(request.email)
            
            hashed_password = hash_password(request.password)
            new_admin = AdminCredentials(
                id=request.id,
                email=request.email,
                name=request.name,
                password=hashed_password,
            )
            
            admin = self.auth_repository.create_admin(new_admin)
            logger.info(f"Signup successful for admin {request.email}")
            return admin
        finally:
            self.auth_repository.close()
            self.employee_repository.close()
