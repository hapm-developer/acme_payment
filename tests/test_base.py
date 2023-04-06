import unittest
from unittest.mock import Mock
from views.console import Console
from models.employee import Employee
from models.payment_calculator import PaymentCalculator

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.console = Mock(Console)
        self.employee = Employee('Juan', 'MO10:00-12:00,TU11:00-13:00,TH12:00-14:00')
        self.payment_calculator = PaymentCalculator(self.employee)
