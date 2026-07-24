from abc import ABC, abstractmethod

from employee.application.models.request.signup_model import SignupRequest
from employee.infrastructure.entities.admin_credentials_entity import AdminCredentials


class SignupServiceInterface(ABC):

    @abstractmethod
    def signup(self, request: SignupRequest) -> AdminCredentials:
        pass
