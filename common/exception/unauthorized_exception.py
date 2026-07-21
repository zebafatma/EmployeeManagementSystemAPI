from fastapi import status

from common.exception.app_exception import AppException


class InvalidCredentialsException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_401_UNAUTHORIZED, "Invalid Credentials")


class InvalidTokenException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_401_UNAUTHORIZED, "Invalid Token")


class InactiveAccountException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_401_UNAUTHORIZED, "Inactive Account")
