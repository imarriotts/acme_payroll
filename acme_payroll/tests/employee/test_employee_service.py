import unittest

from acme_payroll.employee.employee import Employee
from acme_payroll.shift.shift import Shift
from acme_payroll.employee.employee_service import EmployeeService


class TestEmployeeService(unittest.TestCase):
    """
    A test class for the EmployeeService class.
    """

    def setUp(self):
        self.shift_class = Shift
        self.employee_service = EmployeeService(self.shift_class)

    def test_create_employee_list(self):
        employee_data = ['IVAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
                         'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
                         'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']

        expected_employees = [Employee('IVAN', [Shift('MO', '10:00', '12:00'),
                                                Shift('TH', '12:00', '14:00'),
                                                Shift('SU', '20:00', '21:00')]),
                              Employee('RENE', [Shift('MO', '10:00', '12:00'),
                                                Shift('TU', '10:00', '12:00'),
                                                Shift('TH', '01:00', '03:00'),
                                                Shift('SA', '14:00', '18:00'),
                                                Shift('SU', '20:00', '21:00')]),
                              Employee('ASTRID', [Shift('MO', '10:00', '12:00'),
                                                  Shift('TH', '12:00', '14:00'),
                                                  Shift('SU', '20:00', '21:00')])]

        actual_employees = self.employee_service.create_employee_list(employee_data)
        self.assertEqual(len(actual_employees), len(expected_employees))

        for actual_employee, expected_employee in zip(actual_employees, expected_employees):
            self.assertEqual(actual_employee.name, expected_employee.name)
            self.assertEqual(len(actual_employee.shifts), len(expected_employee.shifts))
            for actual_shift, expected_shift in zip(actual_employee.shifts, expected_employee.shifts):
                self.assertEqual(actual_shift.day, expected_shift.day)
                self.assertEqual(actual_shift.start_time, expected_shift.start_time)
                self.assertEqual(actual_shift.end_time, expected_shift.end_time)


if __name__ == '__main__':
    unittest.main()
