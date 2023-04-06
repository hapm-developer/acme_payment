import unittest

from models.employee import Employee
from tests.test_base import BaseTestCase


class TestEmployee(BaseTestCase):

    def test_from_input_string(self):
        # Test input string with valid data
        input_string = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        expected_name = "RENE"
        expected_schedule = "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        employee = Employee.from_input_string(input_string)
        self.assertEqual(employee.name, expected_name)
        self.assertEqual(employee.schedule, expected_schedule)

        # Test input string with invalid data (missing schedule)
        input_string = "ASTRID="
        with self.assertRaises(ValueError):
            Employee.from_input_string(input_string)

        # Test input string with invalid data (missing name)
        input_string = "=MO10:00-12:00,TU10:00-12:00"
        with self.assertRaises(ValueError):
            Employee.from_input_string(input_string)

if __name__ == '__main__':
    unittest.main()