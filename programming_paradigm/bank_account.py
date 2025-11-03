class BankAccount:
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.account_balance:
            print("Insufficient funds.")
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True

    def display_balance(self):
         print(f"Current Balance: ${self.account_balance:.2f}")    


    # def deposit(self, amount):
    #     amount += BankAccount.account_balance
    
    # def withdraw(self, amount):
    #     amount = BankAccount.account_balance - amount
    
    # def display_balance(self):
    #     print(f"Current Balance: ${BankAccount.account_balance}")     


# Account1 = BankAccount(account_balance= 100000000)
# Account1.debit = 1000
# print(f"Initial balance was {Account1.initial_balance} Account balance is ${Account1.account_balance} and debited amount is {Account1.debit}")

# Task Description:
# You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

# bank_account.py:
# Class Definition:

# Define a class named BankAccount.
# Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
# Encapsulation and Behaviors:

# Implement deposit(amount), withdraw(amount), and display_balance() methods.
# deposit should add the specified amount to account_balance.
# withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
# display_balance should print the current balance in a user-friendly format.
# main-0.py for Command Line Interaction:
# This script utilizes BankAccount through command line arguments for banking operations.