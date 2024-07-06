# practice - Abstruction, Encapsulation and Methods

# Task: Create Account class with 2 attributes - balance and account no. Create methods for debit, credit and printing the balance.

# Credit: Shraddha Didi (youtube)

class Account: 
    def __init__(self, balance, account):
        self.balance = balance
        self.acc_number = account

    # debit method
    def debit(self, amount):
        self.balance = self.balance - amount
        print(amount, "tk is debited. Total Balance =", self.balance)
    # credit method
    def credit(self, amount):
        self.balance = self.balance + amount
        print(amount, "tk is credited. Total Balance =", self.balance)

    # get method
    def get_balance(self):
        print("Your current balance =",self.balance)
acc1 = Account(12000, "AH00132")
print(acc1.balance)
print(acc1.acc_number)

acc1.debit(1200)

acc1.credit(20)

acc1.get_balance()

