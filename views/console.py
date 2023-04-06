from typing import Optional, Tuple
from models.payment_calculator import PaymentCalculator
from models.employee import Employee


class Console:
    def __init__(self):
        self._payment_calculator = None
        self._employee = None
    
    @property
    def payment_calculator(self) -> Optional[PaymentCalculator]:
        return self._payment_calculator
    
    @payment_calculator.setter
    def payment_calculator(self, payment_calculator: PaymentCalculator):
        self._payment_calculator = payment_calculator
        
    @property
    def employee(self) -> Optional[Employee]:
        return self._employee
    
    @employee.setter
    def employee(self, employee: Employee):
        self._employee = employee

    def run(self) -> None:
        print("Welcome to the Payment Calculator!")
        while True:
            print("\nPlease select an option:")
            print("1. Calculate employee's pay")
            print("2. Exit")
            option = input()
            if option == "1":
                print("\nPlease enter the employee's name and schedule " 
                      "(in the format 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'):")
                input_string = input()
                employee = Employee.from_input_string(input_string)
                self.employee = employee
                self.payment_calculator = PaymentCalculator(employee)
                self.show_calculated_pay(employee)
            elif option == "2":
                print("Thank you for using the Payment Calculator!")
                break
            else:
                print("Invalid option. Please try again.")

    def show_calculated_pay(self, employee: Employee) -> None:

        pay = self.payment_calculator.calculate_payment()
        print(f"The amount to pay {employee.name} is: {pay} USD")
