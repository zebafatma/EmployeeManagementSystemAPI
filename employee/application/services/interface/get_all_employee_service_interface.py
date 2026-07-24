from abc import ABC, abstractmethod
from employee.application.models.request.get_all_employee_request_model import GetAllEmployeeRequest
from employee.application.models.response.employee_list_response_model import EmployeeListResponse

class GetAllEmployeeServiceInterface(ABC):

    @abstractmethod
    def get_all(self, request:GetAllEmployeeRequest, current_admin)->EmployeeListResponse:
        pass