'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 10 Assignment 3
'''

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than 0.")
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        except ValueError as error:
            print(f"Error during deposit: {error}")
    
    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than 0.")
            if amount > self.balance:
                raise ValueError("Insufficient funds for withdrawal.")
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        except ValueError as error:
            print(f"Error during withdrawal: {error}")
    
    def get_balance(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"
    
    def create_account(account_holder, starting_balance=0.0):
        try:
            starting_balance = float(starting_balance)
            if starting_balance < 0:
                raise ValueError("Starting balance cannot be negative.")
            return BankAccount(account_holder, starting_balance)
        except ValueError as error:
            print(f"Could not create account: {error}")
            return None
    
    def run_demo():
        try:
            account = create_account("Taylor", 500)
            if account is None:
                return
            
            print(account.get_balance())
            print(account.deposit(150))
            print(account.withdraw(200))
            print(account.withdraw(1000))  
            print('\n')
            print('==========Attempting to deposit a negative amount==========')
            print(account.deposit(-10))
            print('\n') 
            print(account.get_balance())

        except Exception as error:
            print(f"Unexpected error in bank account demo: {error}")

    if __name__ == "__main__":
        run_demo()
