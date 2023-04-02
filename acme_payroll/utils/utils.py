import os
import re
from typing import List, Tuple

from acme_payroll.constants import AVAILABLE_DAYS, INVALID_DATE_FORMAT, INVALID_DAY_CODE, INVALID_EMPLOYEE_DATA, REGEX_EMPLOYEE


class Utils:
    @staticmethod
    def validate_time_format(time_str: str) -> bool:
        """
        Validates whether the input string is a valid time in the format 'HH:MM'
        """
        try:
            hours, minutes = time_str.split(':')
            hours = int(hours)
            minutes = int(minutes)
            if not (0 <= hours < 24 and 0 <= minutes < 60):
                raise ValueError
        except ValueError:
            return False
        return True

    @staticmethod
    def validate_employee_data(employee_data: List[str]) -> List[str]:
        """
        Validates the employee data for correct formatting.
        Returns a list of validation errors.
        """
        validation_errors = []
        for line_num, line in enumerate(employee_data):
            if not re.match(REGEX_EMPLOYEE, line):
                validation_errors.append(
                    f"{INVALID_EMPLOYEE_DATA} at line {line_num+1}")
                continue
            entries = line.split('=')
            employee_name = entries[0]
            schedules = entries[1].split(',')
            for schedule in schedules:
                schedule_parts = schedule.split('-')
                day = schedule_parts[0][:2]
                if day not in AVAILABLE_DAYS:
                    validation_errors.append(
                        f"{INVALID_DAY_CODE} at line {line_num+1} for employee {employee_name}")
                    break
                start_time, end_time = schedule_parts[0][2:], schedule_parts[1]
                if not all([Utils.validate_time_format(time_str) for time_str in [start_time, end_time]]):
                    validation_errors.append(
                        f"{INVALID_DATE_FORMAT} at line {line_num+1} for employee {employee_name}")
                    break
        return validation_errors

    @staticmethod
    def get_file_path(relative_path: str) -> str:
        """
        Return the path to a file relative to the current working directory.
        """
        current_dir = os.getcwd()
        new_path: str = os.path.join(current_dir, relative_path)
        return new_path

    @staticmethod
    def file_exists(file_path: str) -> str:
        """
        Checks if a file exists relative to the current working directory.
        """
        return os.path.exists(file_path)