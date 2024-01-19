from unittest import TestCase
from unittest.mock import MagicMock

from assertpy import assert_that

class Display:
    def print(self, text: str):
        pass

class VendingMachine(Display):
    def __init__(self, display):
        self.__display = display
        display.print("INSERT COIN")

class VendingMachineShould(TestCase):
    def test_display_insert_coin_when_it_is_started(
        self,
    ):
        display = Display()
        display.print = MagicMock()

        VendingMachine(display)

        display.print.assert_called_once_with("INSERT COIN")
        assert_that(display.print.called).is_true()

