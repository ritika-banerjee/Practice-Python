class BankAccount():

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        
        if amount <= 0:
            print("Amount must be positive")
            return
        
        self.balance += amount

        print(f"current balance: {self.balance}")

    def withdraw(self, amount):

        if amount <= 0:
            print("Amount should be positive")
            return

        if amount > self.balance:
            print("Insufficient Balance")
            return

        self.balance -= amount
        print(f"current balance: {self.balance}")

    def get_balance(self):

        print(f"current balance: {self.balance}")


a = BankAccount()
a.deposit(500)
a.get_balance()
a.withdraw(78)
a.get_balance()
a.deposit(-699)
a.withdraw(1333)


