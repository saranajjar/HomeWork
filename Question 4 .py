class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return interest_amount

    def print_info(self):
        print(f"Current Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate}")


# Create an instance of BankAccount
bank_acc = BankAccount("123456789", "John Doe")
print("Bank Account Operations:")
print("Initial Balance:", bank_acc.get_balance())
print("After depositing $1000:", bank_acc.deposit(1000))
print("After withdrawing $500:", bank_acc.withdraw(500))
print()

# Create an instance of SavingsAccount
savings_acc = SavingsAccount("987654321", "Jane Smith")
print("Savings Account Operations:")
print("Initial Balance:", savings_acc.get_balance())
savings_acc.deposit(2000)
print("After applying interest:", savings_acc.apply_interest())
savings_acc.print_info()