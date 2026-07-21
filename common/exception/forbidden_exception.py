from fastapi import status

from common.exception.app_exception import AppException


class UnauthorizedEmployeeException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_403_FORBIDDEN, "Unauthorized Employee")
