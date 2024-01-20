"""
 Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
 
 Withdrawals may not exceed the available balance.
 
 Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, profit):
        self.balance += profit
    
    def withdraw(self, antiprofit):
        if self.balance < antiprofit:
            print("You don't have this amount of money!")
        else:
            self.balance -= antiprofit
            print("Have a nice day, sir!")


x = Account("John", 0)
x.deposit(100)
x.withdraw(101)
x.withdraw(99)
x.withdraw(2)
x.withdraw(1)