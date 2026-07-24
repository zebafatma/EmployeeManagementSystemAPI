from fastapi import status
from pydantic import EmailStr

from common.exception.app_exception import AppException


class EmployeeWithIdAlreadyExistsException(AppException):
    def __init__(self, id: int):
        super().__init__(
            status.HTTP_409_CONFLICT, f"Employee with Id: {id} Already Exist"
        )


class EmployeeWithEmailAlreadyExistsException(AppException):
    def __init__(self, email: EmailStr):
        super().__init__(
            status.HTTP_409_CONFLICT, f"Employee with Email: {email} Already Exist"
        )


class AdminAlreadyExistsException(AppException):
    def __init__(self, email: EmailStr):
        super().__init__(
            status.HTTP_409_CONFLICT, f"Admin with email: {email} Already Exist"
        )
