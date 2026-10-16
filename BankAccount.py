class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ₹{amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ₹{amount:.2f}")

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ₹{self.balance:.2f}")

# Example Usage:
account = BankAccount("Nilofar", 5000)
account.display_balance()
account.deposit(2000)
account.withdraw(1500)
account.display_balance()
