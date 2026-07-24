from abc import ABC, abstractmethod
from employee.application.models.request.signin_model import SigninRequest
from employee.application.models.response.token_response_model import TokenResponse

class SigninServiceInterface(ABC):

    @abstractmethod
    def signin(self, request:SigninRequest)->TokenResponse:
        pass