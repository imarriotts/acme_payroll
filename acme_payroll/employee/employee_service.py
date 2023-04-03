from typing import List

from acme_payroll.employee.employee import Employee
from acme_payroll.shift.shift import Shift


class EmployeeService:
    def __init__(self, shift_class: Shift):
        self.shift_class = shift_class

    def create_employee_list(self, employee_data: List[str]) -> List[Employee]:
        employees = []
        for employee_string in employee_data:
            data = employee_string.split('=')
            name = data[0]
            string_shifts = data[1].split(',')
            shifts = [self.shift_class.from_string(shift) for shift in string_shifts]
            employee = Employee(name, shifts)
            employees.append(employee)

        return employees
