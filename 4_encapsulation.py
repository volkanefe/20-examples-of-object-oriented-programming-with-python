class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Balance can't be negative")

# Object creation
account=BankAccount(100)

# Encapsulated data access
print(account.get_balance()) # Output : 100

# Encapsulated data modification
account.set_balance(200)
print(account.get_balance()) # Output : 200