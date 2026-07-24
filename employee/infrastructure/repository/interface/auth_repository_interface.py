from abc import ABC, abstractmethod
from employee.infrastructure.entities.admin_credentials_entity import AdminCredentials
from pydantic import EmailStr

class AuthRepositoryInterface(ABC):

    @abstractmethod
    def get_admin_by_email(self, email:EmailStr)->AdminCredentials:
        pass

    @abstractmethod
    def create_admin(self,admin:AdminCredentials)->AdminCredentials:
        pass

    @abstractmethod
    def update_last_login(self, admin:AdminCredentials)->AdminCredentials:
        pass

    @abstractmethod
    def close(self)->None:
        pass