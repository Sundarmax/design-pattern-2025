
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

# concrete states
class NoCardState(ATMState):
    def insert_card(self, atm):
        print("Card inserted")
        atm.change_state(HasCardState())
    def enter_pin(self, atm, pin):
        print("Insert card first")

    def withdraw_cash(self):
        print("Insert card first")

class HasCardState(ATMState):
    def insert_card(self, atm):
        print("Card already inserted")

    def enter_pin(self, atm, pin):
        if pin == 1234:
            print("PIN correct")
            atm.change_state(CorrectPinState())
        else:
            print("Incorrect PIN, card ejected")
            atm.change_state(NoCardState())
    def withdraw_cash(self, atm, amount):
        print("Enter PIN first")


class CorrectPinState(ATMState):
    def insert_card(self, atm):
        print("Transaction in progress. !")

    def enter_pin(self, atm, pin):
        print("PIN already entered")
    
    def withdraw_cash(self, atm, amount):
        if atm.cash < amount:
            print("Not enough cash in ATM")
            atm.change_state(NoCashState)
        else:
            print(f"Withdrawing {amount}")
            atm.cash-=amount
            print("Card rejected")
            atm.change_state(NoCardState)

class NoCashState(ATMState):
    
    def insert_card(self, atm):
        print("ATM out of Cash")
    
    def enter_pin(self, atm, pin):
        print("ATM out of Cash")

    def withdraw_cash(self, atm, amount):
        print("ATM out of Cash")
    
class ATM:
    def __init__(self, cash):
        self.cash = cash
        self.state = NoCardState() # initial state

    def change_state(self, state):
        self.state = state

    def insert_card(self):
        self.state.insert_card(self)

    def enter_pin(self, pin):
        self.state.enter_pin(self, pin)

    def withdraw_cash(self, amount):
        self.state.withdraw_cash(self, amount)

if __name__ == "__main__":
    
    atm = ATM(1000)
    atm.insert_card()
    atm.enter_pin(1234)
    atm.withdraw_cash(90)
