from abc import  ABC,abstractmethod

# payment strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# concrete implementation
class DebitCardPayment(PaymentStrategy):
    def __init__(self,card_number):
        self.card_no = card_number

    def pay(self,amount):
        print(f"Paid {amount} via debit card - {self.card_no}")

class CreditCardPayment(PaymentStrategy):
    def __init__(self,card_number):
        self.card_no = card_number

    def pay(self, amount):
        print(f"Paid {amount} via credit card - {self.card_no}")

class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"paid  {amount} via UPI")

class PaymentService:

    def __init__(self, strategy : PaymentStrategy):
        self.strategy = strategy

    def set_payment_strategy(self, pay_strategy : PaymentStrategy):
        self.strategy = pay_strategy

    def checkout(self, amount):
        self.strategy.pay(amount)

if __name__ == "__main__":
    payment = PaymentService(UPIPayment("sundarmax15"))
    payment.checkout("500")

    payment.set_payment_strategy(DebitCardPayment("7883O3O-03I3-03"))
    payment.checkout("1000")

