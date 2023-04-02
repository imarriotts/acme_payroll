import unittest

from acme_payroll.constants import RATES
from acme_payroll.employee.employee import Employee
from acme_payroll.payroll.payroll import PayrollService
from acme_payroll.shift.shift import Shift


class TestPayrollService(unittest.TestCase):
    def setUp(self):
        # Create some employees
        self.employee1 = Employee("Ivan", shifts=[
            Shift.from_string("MO10:00-22:00")
        ])

        self.employee2 = Employee("Marriott", shifts=[
            Shift.from_string("TH12:00-14:00")
        ])

        self.employee3 = Employee("Saa", shifts=[
            Shift.from_string("SA14:00-18:00")
        ])

        # Add employees to a list
        self.employees = [
            self.employee1,
            self.employee2,
            self.employee3,
        ]

    def test_calculate_payroll(self):

        # Create a payroll service
        payroll_service = PayrollService.Builder(
            self.employees).with_rates(rates=RATES).build()

        # Calculate the payroll
        payroll = payroll_service.calculate_payroll()

        # Verify the expected output
        expected_output = [
            "The amount to pay Ivan is: 199.67 USD",
            "The amount to pay Marriott is: 30.00 USD",
            "The amount to pay Saa is: 80.00 USD",
        ]
        self.assertEqual(payroll, expected_output)


if __name__ == '__main__':
    unittest.main()
