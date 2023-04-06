import unittest

from datetime import datetime

from models.employee import Employee
from models.payment_calculator import PaymentCalculator
from tests.test_base import BaseTestCase


class TestPaymentCalculator(BaseTestCase):
    
    def test_parse_schedule(self):
        payment_calculator = PaymentCalculator(self.employee)
        parsed_schedule = payment_calculator._parse_schedule('MO10:00-12:00,TU08:00-11:00')
        self.assertEqual(parsed_schedule, {'MO': '10:00-12:00', 'TU': '08:00-11:00'})

    def test_get_rate_for_time(self):
        payment_calculator = PaymentCalculator(self.employee)
        rate = {'00:01-09:00': 25, '09:01-18:00': 15, '18:01-00:00': 20}
        time = datetime.strptime('08:00', '%H:%M')
        start_time, end_time, price = payment_calculator._get_rate_for_time(rate, time)
        self.assertEqual(start_time, datetime.strptime('00:01', '%H:%M'))
        self.assertEqual(end_time, datetime.strptime('09:00', '%H:%M'))
        self.assertEqual(price, 25)

    def test_calculate_day_payment(self):
        payment_calculator = PaymentCalculator(self.employee)
        day = 'MO'
        time = '10:00-12:00'
        payment = payment_calculator._calculate_day_payment(day, time)
        self.assertEqual(payment, 30)

    def test_calculate_payment(self):
        payment_calculator = PaymentCalculator(self.employee)
        payment = payment_calculator.calculate_payment()
        self.assertEqual(payment, 90)


if __name__ == '__main__':
    unittest.main()