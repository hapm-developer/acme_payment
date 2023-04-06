import re
from typing import List


class Employee:
    def __init__(self, name: str, schedule: str) -> None:
        self.name: str = name
        self.schedule: str = schedule
    
    @classmethod
    def from_input_string(cls, input_string: str):
        # Verify that the input string has the correct format
        if not re.match(r'^\w+=(.+)$', input_string):
            raise ValueError('Invalid input string format')

        # Split the input string into name and schedules
        name, schedules_str = input_string.split('=')

        # Verify that there is at least one schedule
        if not schedules_str:
            raise ValueError('At least one schedule is required')

        # Split the schedules string by comma separator
        schedules = schedules_str.split(',')

        # Validate each schedule has the correct format
        for schedule in schedules:
            if not re.match(r'^[A-Z]{2}\d{2}:\d{2}-\d{2}:\d{2}$', schedule):
                raise ValueError('Invalid schedule format')

        # Create an instance of the Employee class
        return cls(name, schedules_str)

