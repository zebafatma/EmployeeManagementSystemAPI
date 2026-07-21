from fastapi import status

from common.exception.app_exception import AppException


class EmployeeWithIdNotFoundException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_404_NOT_FOUND, "Employee with Id not Found")


class EmployeeWithEmailNotFoundException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_404_NOT_FOUND, "Employee with email not Found")
