from fastapi import status
from pydantic import EmailStr

from common.exception.app_exception import AppException


class EmployeeWithIdNotFoundException(AppException):
    def __init__(self, id: int):
        super().__init__(status.HTTP_404_NOT_FOUND, f"Employee with Id: {id} not Found")


class EmployeeWithEmailNotFoundException(AppException):
    def __init__(self, email: EmailStr):
        super().__init__(
            status.HTTP_404_NOT_FOUND, f"Employee with email: {email} not Found"
        )
