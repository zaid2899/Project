# This project demonstrates the working of a bank with single account holder
class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self,depositAmount):
        self.depositAmount = depositAmount
        if self.depositAmount < 0:
            print("Enter valid amount")
        else:
            self.balance = self.balance + self.depositAmount
    
    def withdraw(self,withdrawAmount):
        self.withdrawAmount = withdrawAmount
        if self.withdrawAmount > self.balance:
            print("Enter valid amount")
        else:
            self.balance = self.balance - self.withdrawAmount
        
    def display(self):
        print(f"Balance : {self.balance} Rs")
        


