import unittest
from acme_payroll.shift.shift import Shift


class TestShift(unittest.TestCase):
    def test_from_string_valid(self):
        shift_string = 'MO10:00-12:00'
        shift = Shift.from_string(shift_string)
        self.assertIsNotNone(shift)
        self.assertEqual(shift.day, 'MO')
        self.assertEqual(shift.start_time, '10:00')
        self.assertEqual(shift.end_time, '12:00')

    def test_from_string_invalid(self):
        shift_string = '10:00-12:00'
        shift = Shift.from_string(shift_string)
        self.assertIsNone(shift)

    def test_get_duration(self):
        shift = Shift('MO', '10:00', '12:00')
        duration = shift.get_duration()
        self.assertAlmostEqual(duration, 2.0)

    def test_is_weekday(self):
        shift_weekday = Shift('MO', '10:00', '12:00')
        self.assertTrue(shift_weekday.is_weekday())

        shift_weekend = Shift('SA', '10:00', '12:00')
        self.assertFalse(shift_weekend.is_weekday())

    def test_str(self):
        shift = Shift('MO', '10:00', '12:00')
        self.assertEqual(str(shift), 'Monday 10:00-12:00')

if __name__ == '__main__':
    unittest.main()
