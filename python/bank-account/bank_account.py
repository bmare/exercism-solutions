class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.closed_error = ValueError("That account is closed")
        self.insufficient =  ValueError("Insufficient funds")

    def get_balance(self):
        if self.is_open == False:
            raise ValueError("Not is_open")
        else:
            return self.balance

    def open(self):
        if self.is_open == True:
            raise ValueError("Already is_open")
        else:
            self.is_open = True
            self.balance=0

    def deposit(self, amount):
        if self.is_open == False:
            raise ValueError("That account is closed")
        elif amount < 0:
            raise ValueError("No negative amounts")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.is_open == False:
            raise ValueError("That account is closed")
        elif (self.balance - amount) < 0:
            raise ValueError("Insufficient funds")
        elif amount < 0:
            raise ValueError("No negative amounts")
        else:
            self.balance -= amount

    def close(self):
        if self.is_open == False:
            raise ValueError("Already closed")
        else:
            self.is_open = False
