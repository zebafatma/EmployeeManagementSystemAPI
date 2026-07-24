from common.dependencies.repository_dependency.auth_repository_dependency import (
    get_auth_repository,
)
from common.dependencies.repository_dependency.employee_repository_depencency import (
    get_employee_repository,
)
from employee.application.services.implementation.signin_service import SigninService
from employee.application.services.implementation.signup_service import SignupService
from employee.application.services.interface.signin_service_interface import (
    SigninServiceInterface,
)
from employee.application.services.interface.signup_service_interface import (
    SignupServiceInterface,
)


def get_signup_service() -> SignupServiceInterface:
    return SignupService(get_auth_repository(), get_employee_repository())


def get_signin_service() -> SigninServiceInterface:
    return SigninService(get_auth_repository())
