import unittest
from acme_payroll.utils.utils import Utils

class TestUtils(unittest.TestCase):

    def test_validate_time_format(self):
        self.assertTrue(Utils.validate_time_format("10:30"))
        self.assertFalse(Utils.validate_time_format("25:00"))
        self.assertFalse(Utils.validate_time_format("10:60"))
        self.assertFalse(Utils.validate_time_format("10"))
        self.assertFalse(Utils.validate_time_format("10:30:00"))

    def test_validate_employee_data(self):
        invalid_employee_data = [
            "Ivan=MD0900-1700, TUE0830-1530, WED0930-1700",
            "Luke=MD0900-1700, XYZ0830-1530, WED0930-1700",
            "Leia=MON0830-1700, TUE08301530, WED0930-1700",
            "Han=MO98:30-17:00,TU08:30-15:30,WE09:30-17:00",
            "Anakin=MO08:30-17:00,TU08:30-15:30,WE09:30-17:00",
            "Mando=MO08:30-17:00,TU08:30-15:30,WE09:30-17:00",
            "Quigon=MO08:30-17:00,TU08:30-15:30,WE09:30-17:00"
        ]

        validation_errors = Utils.validate_employee_data(invalid_employee_data)
        self.assertEqual(len(validation_errors), 4)
        self.assertIn("Invalid employee data provided at line 1", validation_errors[0])
        self.assertIn("Invalid employee data provided at line 2", validation_errors[1])
        self.assertIn("Invalid employee data provided at line 3", validation_errors[2])
        self.assertIn("Invalid date format provided at line 4 for employee Han", validation_errors[3])

    def test_get_file_path(self):
        file_path = Utils.get_file_path("test_data.txt")
        self.assertTrue(file_path.endswith("test_data.txt"))

    def test_file_exists(self):
        self.assertTrue(Utils.file_exists("acme_payroll/tests/data/employee_data.txt"))
        self.assertFalse(Utils.file_exists("employee_data.txt"))

if __name__ == '__main__':
    unittest.main()