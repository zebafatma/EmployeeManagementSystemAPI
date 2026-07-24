from abc import ABC, abstractmethod

from employee.infrastructure.entities.employee_entity import Employee


class GetEmployeeServiceInterface(ABC):

    @abstractmethod
    def get_employee(self, id: int, current_admin) -> Employee:
        pass
