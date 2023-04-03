import unittest

from acme_payroll.employee.employee_io import EmployeeIO, EmployeeInputSingle


class TestEmployeeIO(unittest.TestCase):
    """
    A test class for the EmployeeIO class.
    """

    def setUp(self):
        # Create an EmployeeIO object to use in the tests
        self.employee_io = EmployeeIO('acme_payroll/tests/data/employee_data.txt')

    def test_read_employee_data(self):
        expected_employee_data = (['IVAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
                                   'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
                                   'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'], [])
        self.assertEqual(self.employee_io.read_employee_data(), expected_employee_data)

class TestEmployeeInputSingle(unittest.TestCase):
    """
    A test class for the EmployeeIO class.
    """

    def setUp(self):
        # Create an EmployeeIO object to use in the tests
        self.employee_io = EmployeeInputSingle('IVAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')

    def test_parse_employee_data(self):
        expected_employee_data = (['IVAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'], [])
        self.assertEqual(self.employee_io.parse_employee_data(), expected_employee_data)

if __name__ == '__main__':
    unittest.main()
