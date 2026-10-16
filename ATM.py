class ATM:
    def __init__(self, pin, balance=0.0):
        self.__pin = pin  # Encapsulated PIN
        self.balance = balance

    def verify_pin(self, entered_pin):
        return self.__pin == entered_pin

    def check_balance(self, entered_pin):
        if self.verify_pin(entered_pin):
            print(f"Current Balance: ₹{self.balance:.2f}")
        else:
            print("Incorrect PIN. Access Denied.")

    def deposit(self, entered_pin, amount):
        if self.verify_pin(entered_pin):
            if amount > 0:
                self.balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
            else:
                print("Invalid deposit amount.")
        else:
            print("Incorrect PIN. Deposit failed.")

    def withdraw(self, entered_pin, amount):
        if self.verify_pin(entered_pin):
            if amount > self.balance:
                print("Insufficient funds!")
            elif amount <= 0:
                print("Invalid withdrawal amount.")
            else:
                self.balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
        else:
            print("Incorrect PIN. Withdrawal failed.")

# Example Usage:
atm = ATM(pin=1234, balance=10000)

atm.check_balance(1234)
atm.withdraw(1234, 3000)
atm.deposit(1234, 1500)
atm.check_balance(9999)  # Wrong PIN test
