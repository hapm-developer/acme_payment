import re

from typing import Dict, List, Tuple
from datetime import datetime, timedelta

from models.employee import Employee

class PaymentCalculator:
    def __init__(self,  employee: Employee):
        self.employee = employee
        
        self.rates = {
            'MO': {'00:01-09:00': 25, '09:01-18:00': 15, '18:01-00:00': 20},
            'TU': {'00:01-09:00': 25, '09:01-18:00': 15, '18:01-00:00': 20},
            'WE': {'00:01-09:00': 25, '09:01-18:00': 15, '18:01-00:00': 20},
            'TH': {'00:01-09:00': 25, '09:01-18:00': 15, '18:01-00:00': 20},
            'FR': {'00:01-09:00': 25, '09:01-18:00': 15, '18:01-00:00': 20},
            'SA': {'00:01-09:00': 30, '09:01-18:00': 20, '18:01-00:00': 25},
            'SU': {'00:01-09:00': 30, '09:01-18:00': 20, '18:01-00:00': 25}
        }

    def calculate_payment(self) -> int:
        total_payment = 0
        schedule = self.employee.schedule
        parsed_schedule = self._parse_schedule(schedule)
        for day, time in parsed_schedule.items():
            total_payment += self._calculate_day_payment(day, time)
        return total_payment

    def _parse_schedule(self, schedule: str) -> Dict[str, str]:
        parsed_schedule = {match.group(1): match.group(2)
               for match in re.finditer(r'([A-Z]{2})(\d{2}:\d{2}-\d{2}:\d{2})', schedule)}
        return parsed_schedule

    def _calculate_day_payment(self, day: str, time: str) -> int:
        rate = self.rates[day]
        str_start_time, str_end_time = time.split("-")
        start_time = datetime.strptime(str_start_time, '%H:%M')
        end_time = datetime.strptime(str_end_time, '%H:%M')
        total_payment = 0
        while start_time < end_time:
            rate_start, rate_end, rate_value = self._get_rate_for_time(rate, start_time)
            time_diff = min(rate_end, end_time) - start_time
            hours = time_diff.seconds / 3600
            total_payment += hours * rate_value
            start_time = rate_end
        return int(total_payment)
    
    def _get_rate_for_time(self, rate: dict, time: datetime) -> Tuple[datetime, datetime, int]:
        for time_frame, price in rate.items():
            start, end = time_frame.split('-')
            start_time = datetime.strptime(start, '%H:%M')
            end_time = datetime.strptime(end, '%H:%M')

            # Check if end_time is 24:00 and replace it with 00:00 of the next day
            if end_time.hour == 0 and end_time.minute == 0:
                end_time = datetime.combine(time.date() + timedelta(days=1), time.min.time())

            if start_time <= time <= end_time:
                return start_time, end_time, price

        raise ValueError(f"No rate found for time {time} in rate {rate}")




