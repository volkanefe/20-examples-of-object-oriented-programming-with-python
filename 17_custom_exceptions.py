# Custom exception example
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= amount

# Use custom exception
account = BankAccount(100)
try:
    account.withdraw(200)
except InsufficientBalanceError as e:
    print(e)
# Output: Insufficient balance
