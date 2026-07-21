from datetime import datetime

from common.exception.bad_request_exception import InvalidDateFromatException


class DateValidator:

    @staticmethod
    def validate(date_string: str):
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            raise InvalidDateFromatException()
