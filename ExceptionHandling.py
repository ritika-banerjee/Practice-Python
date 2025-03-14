def division():

    while True:

        try:
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))

            div = num1 / num2
            print(f"Division = {div}")
            break

        except ValueError:
            print("💀 The entered Value is not an integer")

        except ZeroDivisionError:
            print("💀 You can't divide a number by zero")

        except Exception as e:
            print(f"💀 unexpected error: {e}")

        finally:
            print("😑 Try again")

def list_indexing():

    list1 = []
    inp = "y"
    try:
        while inp == "y":

            num = int(input("Enter number: "))
            list1.append(num)

            inp = input("do you want to add more numbers? y/n: ").strip().lower()

        ind = int(input("enter the index: "))

        print(f"Number at index {ind} = {list1[ind]}")
        
    except IndexError:
        print("Invalid Index! Try Again")

    except ValueError:
        print("Please enter an Integer")


# custom exception class
class InsufficientFundsError(Exception):
    def __init__(self, message="😒 you don't even have that much money in your account"):
        super().__init__(message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        
        if amount > self.balance:
            raise InsufficientFundsError(f"❌ Cannot withdraw {amount}. Available balance: {self.balance}") # manually triggers an exception
        self.balance -= amount
        print(f"✅ Withdrawn {amount}. New balance: {self.balance}")



if __name__=="__main__":

    try:
        acc = BankAccount(500)
        acc.deposit(200) 
        acc.withdraw(800)  
    except InsufficientFundsError as e:
        print(e)