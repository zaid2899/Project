# This project demonstrates the working of a bank with single account holder
class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number   # Account_number should be integer
        self.account_holder = account_holder   # Account_holder should contain name of holder 
        self.balance = balance                 # Balance should contain amount contained in the account
        
    def deposit(self,depositAmount):
        self.depositAmount = depositAmount     # Amount deposited should be added to the balance of the account
        if self.depositAmount < 0:
            print("Enter valid amount")
        else:
            self.balance = self.balance + self.depositAmount
    
    def withdraw(self,withdrawAmount):
        self.withdrawAmount = withdrawAmount  # amount withdrawn should be subtracted from the balance of the account
        if self.withdrawAmount > self.balance:
            print("Enter valid amount")
        else:
            self.balance = self.balance - self.withdrawAmount
        
    def display(self):
        print(f"Balance : {self.balance} Rs")
        


