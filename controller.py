from models.payment_calculator import PaymentCalculator
from views.console import Console


class Controller:
    def __init__(self, console: Console):
        self.console = console

    def run(self):
        self.console.run()
