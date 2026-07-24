from employee.infrastructure.repository.implementation.auth_repository import (
    AuthRepository,
)
from employee.infrastructure.repository.interface.auth_repository_interface import (
    AuthRepositoryInterface,
)


def get_auth_repository() -> AuthRepositoryInterface:
    return AuthRepository()
