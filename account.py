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
            return self.balance
    
    def withdraw(self,withdrawAmount):
        self.withdrawAmount = withdrawAmount  # amount withdrawn should be subtracted from the balance of the account
        if self.withdrawAmount > self.balance:
            print("Enter valid amount")
        elif self.withdrawAmount < 0 :
            print("Amount cannot be negative")
        else:
            self.balance -= self.withdrawAmount
            return self.balance
        
    def display(self):
        print(f"Account number : {self.account_number}")
        print(f"Account holder : {self.account_holder}")
        print(f"Balance        : {self.balance} Rs")
        


class SavingAccount(BankAccount):
    def __init__(self,account_number,account_holder,balance,interest_rate):
        super().__init__(account_number,account_holder,balance)
        self.interest_rate = interest_rate
        
    def Interest(self,days):
        self.balance += self.balance*self.interest_rate/365*days
        return self.balance
        



