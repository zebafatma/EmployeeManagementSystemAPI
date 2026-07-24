from abc import ABC, abstractmethod
from employee.infrastructure.entities.employee_entity import Employee
from employee.application.models.request.get_all_employee_request_model import GetAllEmployeeRequest
from pydantic import EmailStr

class EmployeeRepositoryInterface(ABC):

    @abstractmethod
    def create(self, employee:Employee)->Employee:
        pass

    @abstractmethod
    def update(self, employee:Employee)->Employee:
        pass

    @abstractmethod
    def get_employee_by_id(self, id:int)->Employee:
        pass

    @abstractmethod
    def get_employee_by_email(self, email:EmailStr)->Employee:
        pass

    @abstractmethod
    def delete(self, id:int)->None:
        pass

    @abstractmethod
    def get_employees(self, offset:int, request:GetAllEmployeeRequest)->tuple[list[Employee], int]:
        pass

    @abstractmethod
    def close(self)->None:
        pass