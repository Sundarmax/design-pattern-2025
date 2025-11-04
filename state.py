
from abc import ABC,abstractmethod
# state interface

class ATMState(ABC):
    
    @abstractmethod
    def insert_card(self, atm):
        pass
    @abstractmethod
    def enter_pin(self, atm, pin):
        pass
    @abstractmethod
    def withdraw_cash(self, atm, amount):
        pass


class ATM:
    def __init__(self, cash):
        self.cash = cash
        self.state = ""

    def change_state(self, state):
        self.state = state

    def insert_card(self):
        pass

    def enter_pin(self):
        pass

    def withdraw_cash(self):
        pass