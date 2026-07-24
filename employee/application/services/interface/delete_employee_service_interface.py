from abc import ABC, abstractmethod
from employee.application.models.response.message_response_model import MessageResponse

class DeleteEmployeeServiceInterface(ABC):

    @abstractmethod
    def delete(self, id:int, current_admin)->MessageResponse:
        pass