from abc import ABC, abstractmethod
from employee.application.models.request.patch_employee_model import PatchEmployeeRequest
from employee.infrastructure.entities.employee_entity import Employee

class PatchEmployeeServiceInterface(ABC):

    @abstractmethod
    def patch(self, id:int, request:PatchEmployeeRequest, current_admin)->Employee:
        pass