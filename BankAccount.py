import random

# how to randomly generate an 8 digit number 

# Bank Class
class BankAccount: 
    def __init__(self, full_name, account_number, balance=0): 
        self.full_name = full_name
        self.account_number = random.randrange(10000000, 99999999)
        self.balance = balance 


    # Deposit 
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount}. New balance ${self.balance}')

    # Withdraw 
    def withdraw(self, amount):
        if self.balance > 0: 
            self.balance -= amount
            print(f'Amount withdrawn: ${amount}. New balance: ${self.balance}')
        else: 
            self.balance -= 10
            print('Insuffient Funds')

    # Get Balance 
    def get_balance(self): 
        print(f'Hey there! Your balance is: ${self.balance}')
        return self.balance

    # Add Interest 
    def add_interest(self): 
        interest = round(self.balance * 0.00083, 2)
        self.balance += interest
        print(f'With interesed added. Balance: ${self.balance}')

    # how to sensitized the bank account number 
    # Print Statement 
    def print_statment(self):
        # hide first four digits 
        hidden = str(self.account_number)[4:8]
        hidden = "****" + hidden
        print(f"{self.full_name} Account No.: {hidden} Balance: ${round(self.balance, 2)}")


# why is it printing insuffient funds and why is it not rounding 
# mitchell_hudson = BankAccount("Mitchell Hudson", "1", 0)
# mitchell_hudson.deposit(400000)
# mitchell_hudson.print_statment()
# mitchell_hudson.add_interest()
# mitchell_hudson.withdraw(150)
# mitchell_hudson.print_statment()

# jennifer_carrneo = BankAccount("Jennifer Carreno", "2", 0)
# jennifer_carrneo.deposit(500)
# jennifer_carrneo.add_interest()
# jennifer_carrneo.print_statment()
# jennifer_carrneo.withdraw(550)
# jennifer_carrneo.print_statment()

stella_collins = BankAccount('Stella Collins', "3", 0)
stella_collins.deposit(300)
stella_collins.print_statment()
stella_collins.add_interest()
stella_collins.withdraw(200)
stella_collins.print_statment()














