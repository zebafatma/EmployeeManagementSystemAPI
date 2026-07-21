from fastapi import status

from common.exception.app_exception import AppException


class InvalidRoleException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_400_BAD_REQUEST, "Invalid Role")


class InvalidPageException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_400_BAD_REQUEST, "Invalid Page Number")


class InvalidPageSizeException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_400_BAD_REQUEST, "Invalid Page Size")


class ManagerDoesnotExistException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_400_BAD_REQUEST, "Invalid Manager Id")


class InvalidDateFromatException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_400_BAD_REQUEST, "Invalid Date Format")


class DiffrentEmailException(AppException):
    def __init__(self):
        super().__init__(
            status.HTTP_400_BAD_REQUEST, "Email diffrent from registered Email"
        )


class InvalidDateOfBirthException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Date of birth cannot be in the future.",
        )


class EmployeeMustBeAdultException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Employee must be at least 18 years old.",
        )


class InvalidJoiningDateException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Date of joining cannot be after today.",
        )


class InvalidPhoneNumberException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, message="Phone Number is invalid"
        )


class InvalidCurrencyException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Invalid Currency! Please choose a currency from ('INR','USD')",
        )
