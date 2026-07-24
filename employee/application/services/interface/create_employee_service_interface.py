from abc import ABC, abstractmethod

from employee.application.models.request.create_employee_model import (
    CreateEmployeeRequest,
)
from employee.infrastructure.entities.employee_entity import Employee


class CreateEmployeeServiceInterface(ABC):

    @abstractmethod
    def create(self, request: CreateEmployeeRequest, current_admin) -> Employee:
        pass
