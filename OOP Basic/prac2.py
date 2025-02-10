#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit, & printing the balance

class Account:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo

    def debit(self, amount):
        self.balance -= amount
        print(f"Debited {amount} from Account No: {self.accNo}")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount} to Account No: {self.accNo}")
    
    def printBalance(self):
        print(f"Account No: {self.accNo}\nBalance: {self.balance}")

a1 = Account(1000, 101)
a1.debit(100)
a1.credit(200)
a1.printBalance()