from fastapi import status

from common.exception.app_exception import AppException


class InvalidRoleException(AppException):
    def __init__(self, role: str):
        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            f"Invalid Role '{role}'. Allowed roles are: 'admin' and 'employee'",
        )


class InvalidPageException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_400_BAD_REQUEST, "Invalid Page Number")


class InvalidPageSizeException(AppException):
    def __init__(self):
        super().__init__(status.HTTP_400_BAD_REQUEST, "Invalid Page Size")


class ManagerDoesnotExistException(AppException):
    def __init__(self, id: int):
        super().__init__(status.HTTP_400_BAD_REQUEST, f"Invalid Manager Id: {id}")


class InvalidDateFromatException(AppException):
    def __init__(self, field):
        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            message=f"Invalid date format for the field {field}. Please use : YYYY-MM-DD format only.",
        )


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
            message="Date of joining cannot be in the future.",
        )


class InvalidPhoneNumberException(AppException):
    def __init__(self, field):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=f"Phone Number is invalid for the field: {field}",
        )


class InvalidCurrencyException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Invalid Currency! Please choose a currency from ('INR','USD')",
        )


class SmallNameException(AppException):
    def __init__(self, field: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=f"Name length cannot be less than 3 for the field {field}",
        )


class InvalidPanNumberException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Invalid PAN Number. Please use a correct format",
        )


class InvalidGenderException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Invalid Gender. Please specify gender from: 'male','female','other'",
        )


class InvalidDepartmentException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Invalid Department. Please choose a department from: 'IT','HR','Sales','Finance','Marketing'",
        )


class InvalidDesignationException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Invalid Designation. Length of designation must be between 3 and 50.",
        )


class InvalidAddressException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Invalid Address. Address must contain atleast 10 and atmost 255 characters.",
        )


class InvalidSalaryException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Salary must be a whole number.",
        )
