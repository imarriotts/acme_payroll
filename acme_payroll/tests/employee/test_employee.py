import unittest
from datetime import datetime

from acme_payroll.shift.shift import Shift
from acme_payroll.employee.employee import Employee


class TestEmployee(unittest.TestCase):
    """
    A test class for the Employee class.
    """

    def setUp(self):
        # Create Shift objects to use in the tests
        self.shift1 = Shift('MO', '10:00', '12:00')
        self.shift2 = Shift('TU', '13:00', '16:00')
        self.shift3 = Shift('FR', '08:00', '17:00')
        self.shift4 = Shift('SA', '18:00', '23:00')

        # Create an Employee object to use in the tests
        self.employee = Employee('Ivan', [self.shift1, self.shift2, self.shift3, self.shift4])

    def test_get_shifts(self):
        expected_shifts = [self.shift1, self.shift2, self.shift3, self.shift4]
        self.assertEqual(self.employee.get_shifts(), expected_shifts, msg='Shifts should match expected')

    def test_get_total_hours_worked(self):
        # Calculate the expected total hours worked
        shift1_duration = datetime.strptime(self.shift1.end_time, '%H:%M') - datetime.strptime(self.shift1.start_time, '%H:%M')
        shift2_duration = datetime.strptime(self.shift2.end_time, '%H:%M') - datetime.strptime(self.shift2.start_time, '%H:%M')
        shift3_duration = datetime.strptime(self.shift3.end_time, '%H:%M') - datetime.strptime(self.shift3.start_time, '%H:%M')
        shift4_duration = datetime.strptime(self.shift4.end_time, '%H:%M') - datetime.strptime(self.shift4.start_time, '%H:%M')
        expected_total_hours = (shift1_duration + shift2_duration + shift3_duration + shift4_duration).total_seconds() / 3600

        # Check that the calculated total hours worked matches the expected value
        self.assertEqual(self.employee.get_total_hours_worked(), expected_total_hours, msg='Total hours should match expected')

    def test_get_name(self):
        self.assertEqual(self.employee.get_name(), 'Ivan', msg='Name should be Ivan')


if __name__ == '__main__':
    unittest.main()
