import random

# how to randomly generate an 8 digit number 

# Bank Class
class BankAccount: 
    def __init__(self, full_name, account_number, balance=0): 
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance 


# Deposit 
def deposit(self, amount):
    self.balance += amount
    print(f'Amount deposited:{amount}. New balance {self.balance}')

# Withdraw 
def withdraw(self, amount):
    self.balance -= amount
    if self.balance < amount: 
        self.balance -= 10 
        print ('Insuffient Funds')
    else: 
        print(f'Amount withdrawn:{amount}. New balance: {self.balance}')

# Get Balance 
def get_balance(self): 
    print(f'Your balance is: {self.balance}')
    return balance

# Add Interest 
def add_interest(self): 
    interest = balance * 0.00083

# Print Statement 
def print_statment(self):
    print(f"{self.name} Account Number: {self.account} Balance: {self.balance}")





# Instatiation 
# number = random.randint(0,9)



mitchell_hudson = BankAccount("Mitchell Hudson", "03141592", 0)
mitchell_hudson.print_statment()


