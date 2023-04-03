import re
from datetime import datetime

from acme_payroll.constants import DAYS, REGEX_SHIFT, WEEKDAYS


class Shift:
    # Regex pattern to extract day, start time, and end time from a shift string
    SHIFT_REGEX_PATTERN = re.compile(REGEX_SHIFT)

    def __init__(self, day: str, start_time: str, end_time: str):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time

    @classmethod
    def from_string(cls, shift_string: str):
        """
        Creates a Shift object from a shift string.

        Args:
            shift_string (str): The string representing the shift.

        Returns:
            Shift: The Shift object created from the string, or None if the string is invalid.
        """
        match = cls.SHIFT_REGEX_PATTERN.search(shift_string)
        if match:
            day = match.group(1)
            start_time = match.group(2)
            end_time = match.group(3)
            return cls(day, start_time, end_time)
        else:
            return None

    def get_duration(self) -> float:
        """
        Calculates the duration of the shift in hours.

        Returns:
            float: The duration of the shift in hours.
        """
        start_datetime = datetime.strptime(self.start_time, '%H:%M')
        end_datetime = datetime.strptime(self.end_time, '%H:%M')
        duration = end_datetime - start_datetime
        return duration.total_seconds() / 3600

    def is_weekday(self) -> bool:
        """
        Returns True if the day is a weekday (Monday to Friday), False otherwise.

        Returns:
            bool: True if the day is a weekday, False otherwise.
        """
        return self.day[:2] in WEEKDAYS

    def __str__(self) -> str:
        """
        Returns a string representation of the Shift object.

        Returns:
            str: The string representation of the Shift object.
        """
        return f"{DAYS[self.day]} {self.start_time}-{self.end_time}"
