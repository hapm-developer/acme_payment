from controller import Controller
from views.console import Console

if __name__ == '__main__':
    console = Console()
    controller = Controller(console)
    controller.run()
