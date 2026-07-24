import logging
import re
from datetime import datetime

from common.exception.bad_request_exception import (
    InvalidAddressException,
    InvalidCurrencyException,
    InvalidDateFromatException,
    InvalidDepartmentException,
    InvalidDesignationException,
    InvalidGenderException,
    InvalidPanNumberException,
    InvalidPhoneNumberException,
    InvalidRoleException,
    InvalidSalaryException,
    SmallNameException,
)

logger = logging.getLogger(__name__)


class RequestValidation:
    @staticmethod
    def validate_phone(phone: str, field):
        phone = phone.strip()
        if not phone.isdigit():
            logger.error("Invalid Phone number for %s", field)
            raise InvalidPhoneNumberException(field)
        if len(phone) != 10:
            logger.error("Invalid Phone number for %s", field)
            raise InvalidPhoneNumberException(field)
        return phone

    @staticmethod
    def validate_date(date_string: str, field: str):
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            logger.error("Invalid format of date for %s", field)
            raise InvalidDateFromatException(field)

    @staticmethod
    def validate_name(name: str, field: str):
        name = name.strip()
        if len(name) < 3:
            logger.error("Name is too small for %s", field)
            raise SmallNameException(field)
        return name

    @staticmethod
    def validate_pan(pan: str):
        pan = str(pan).strip().upper()
        if len(pan) != 10:
            logger.error("Invalid PAN number")
            raise InvalidPanNumberException()
        regex_pattern = r"^[A-Z]{3}[ABCFGHLJPTK][A-Z][0-9]{4}[A-Z]$"
        if not re.match(regex_pattern, pan):
            logger.error("Invalid PAN number")
            raise InvalidPanNumberException()
        return pan

    @staticmethod
    def validate_role(role: str):
        allowed_roles = {"admin", "employee"}
        role = role.strip().lower()
        if role not in allowed_roles:
            logger.error("Invalid Role: %s", role)
            raise InvalidRoleException(role)
        return role

    @staticmethod
    def validate_gender(gender: str):
        allowed_genders = {"male", "female", "other"}
        gender = gender.strip().lower()
        if gender not in allowed_genders:
            logger.error("Invalid Gender: %s", gender)
            raise InvalidGenderException()
        return gender

    @staticmethod
    def validate_department(department: str):
        department = department.strip()
        allowed_departments = {"IT", "HR", "Finance", "Sales", "Marketing"}
        if department not in allowed_departments:
            logger.error("Invalid department: %s", department)
            raise InvalidDepartmentException()
        return department

    @staticmethod
    def validate_designation(designation: str):
        designation = designation.strip()
        if len(designation) <= 2 or len(designation) > 50:
            logger.error("Invalid designation: %s", designation)
            raise InvalidDesignationException()
        return designation

    @staticmethod
    def validate_address(address: str):
        address = address.strip()
        if len(address) < 10 or len(address) > 255:
            logger.error("Invalid address: %s", address)
            raise InvalidAddressException()
        return address

    @staticmethod
    def validate_salary(salary: int):
        if salary <= 0:
            logger.error("Invalid Salary: %s", salary)
            raise InvalidSalaryException()
        return salary

    @staticmethod
    def validate_currency(currency: str):
        allowed_currency = {"USD", "INR"}
        currency = currency.strip().upper()
        if currency not in allowed_currency:
            logger.error("Invalid Currency: %s", currency)
            raise InvalidCurrencyException()
        return currency
