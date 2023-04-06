import unittest

from controller import Controller
from tests.test_base import BaseTestCase
from views.console import Console

class TestController(BaseTestCase):
    def test_run(self):
        mock_console = self.console
        controller = Controller(mock_console)
        controller.run()
        mock_console.run.assert_called_once()