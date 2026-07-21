from fastapi import status

from common.exception.app_exception import AppException


class EmployeeWithIdAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_409_CONFLICT, "Employee with Id Already Exist")


class EmployeeWithEmailAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_409_CONFLICT, "Employee with Email Already Exist")


class AdminAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_409_CONFLICT, "Admin Already Exist")
