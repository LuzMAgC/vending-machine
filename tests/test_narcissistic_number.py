from unittest import TestCase
from unittest.mock import MagicMock


class Display:
    def print(self, text: str):
        pass

class VendingMachine(Display):
    def __init__(self, display):
        self.__display = display
        display.print("INSERT COIN")

    def insert(self):
        self.__display.print("$0.05")

class VendingMachineShould(TestCase):
    def test_display_insert_coin_when_it_is_started(
        self
    ):
        display = Display()
        display.print = MagicMock()

        VendingMachine(display)

        display.print.assert_called_once_with("INSERT COIN")

    def test_display_five_cents_when_nickel_is_inserted(self):
        display = Display()
        display.print = MagicMock()

        VendingMachine(display).insert()

        display.print.assert_called_with("$0.05")

