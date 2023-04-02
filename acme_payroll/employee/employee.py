from typing import List
from acme_payroll.shift.shift import Shift

class Employee:
    def __init__(self, name: str, shifts: List[Shift]):
        self.name = name    
        self.shifts = shifts

    def get_shifts(self) -> List[Shift]:
        """
        Returns the shifts for the employee.

        Returns:
            List[Shift]: The shifts for the employee.
        """
        return self.shifts

    def get_total_hours_worked(self) -> float:
        """
        Calculates the total hours worked by the employee based on their shifts.

        Returns:
            float: The total hours worked by the employee.
        """
        total_hours = 0
        for shift in self.shifts:
            total_hours += shift.get_duration()
        return total_hours

    def get_name(self) -> str:
        """
        Returns the name of the employee.

        Returns:
            str: The name of the employee.
        """
        return self.name