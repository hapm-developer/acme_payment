# Employee Payment System

## Overview
This project is an employee payment system that calculates the total pay for each employee based on their hours worked and hourly rate. The system can handle multiple employees, and each employee can have a different hourly rate.

## Architecture
The project is divided into four modules: `controller`, `employee`, `payment_calculator`, and `main`.

The `controller` module handles the input and output of the system. It receives input from the user, validates the input, and passes the input to the `payment_calculator` module. The `controller` module also displays the output to the user.

The `employee` module defines the `Employee` class, which contains the attributes of an employee (name and hourly rate) and the hours worked by the employee.

The `payment_calculator` module defines the `PaymentCalculator` class, which contains the methods to calculate the pay for an employee.

The `main` module is the entry point of the system. It creates an instance of the `PaymentCalculator` class and calls the appropriate methods to calculate the pay for each employee.

## Approach and Methodology
To develop this project, we followed a Test-Driven Development (TDD) approach. We started by writing unit tests for each module and then implemented the code to pass the tests. This approach helped us to ensure that the code was working correctly and to catch any issues early in the development process.

## Instructions
To run the program locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. Install the dependencies by running `pip install -r requirements.txt`.
4. Run the tests by running `python -m unittest discover -v`.
5. Run the program by running `python main.py`.
6. Follow the prompts to enter the employee information and calculate the pay.

## Requirements
The project requires the following dependencies:

- `python` (version 3.6 or higher)
- `pytest` (version 6.2.5 or higher)
- `coverage` (version 6.3 or higher)

You can install these dependencies by running `pip install -r requirements.txt`.