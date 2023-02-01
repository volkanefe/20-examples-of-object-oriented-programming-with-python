from abc import ABC, abstractmethod

# Abstract base class definition
class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

# Concrete class definitions
class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paying {amount} using credit card")

class MobileWalletPayment(Payment):
    def make_payment(self, amount):
        print(f"Paying {amount} using mobile wallet")

# Polymorphic behavior
payments = [CreditCardPayment(), MobileWalletPayment()]
for payment in payments:
    payment.make_payment(100)

# Output:
# Paying 100 using credit card
# Paying 100 using mobile wallet
