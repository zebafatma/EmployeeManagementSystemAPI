import logging

from common.auth.hash_password import verify_password
from common.auth.jwt_handler import create_access_token
from common.exception.unauthorized_exception import (
    InactiveAccountException,
    InvalidCredentialsException,
)
from employee.application.models.request.signin_model import SigninRequest
from employee.infrastructure.repository.interface.auth_repository_interface import AuthRepositoryInterface
from employee.application.services.interface.signin_service_interface import SigninServiceInterface

logger = logging.getLogger(__name__)


class SigninService(SigninServiceInterface):

    def __init__(self, repository:AuthRepositoryInterface):
        self.repository=repository

    def signin(self, request: SigninRequest):

        logger.info(f"Signin request recieved by admin {request.email}")

        try:

            admin = self.repository.get_admin_by_email(request.email)

            if admin is None:
                logger.error(f"Invalid Credentials provided by {request.email}")
                raise InvalidCredentialsException()
            
            if not verify_password(request.password, admin.password):
                logger.error(f"Invalid Creadentials provided by {request.email}")
                raise InvalidCredentialsException()
            
            if not admin.is_active:
                logger.error(f"Inactive admin: {request.email}")
                raise InactiveAccountException()
            
            self.repository.update_last_login(admin)
            access_token = create_access_token({"sub": admin.email, "id": admin.id})
            logger.info(f"Signing In admin {request.email}")
            return {"access_token": access_token, "token_type": "bearer"}
        
        finally:
            self.repository.close()
