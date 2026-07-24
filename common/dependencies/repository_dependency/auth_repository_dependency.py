from employee.infrastructure.repository.interface.auth_repository_interface import AuthRepositoryInterface
from employee.infrastructure.repository.implementation.auth_repository import AuthRepository

def get_auth_repository()->AuthRepositoryInterface:
    return AuthRepository()