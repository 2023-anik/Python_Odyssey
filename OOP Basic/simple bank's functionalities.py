class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdrow = 100
        self.max_withdrom = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount < self.min_withdrow:
            print(f"Fokir. You can't withdraw below {self.min_withdrow}")
        elif amount > self.max_withdrom:
            print(
                f"Bank fokir hoye jabe\n"
                f"You can not withdraw more than {self.max_withdrom}"
            )
        else:
            self.balance -= amount
            print(
                f"Here is your money {amount}\n"
                f"Your balance after withdraw: {self.get_balance()}"
            )


brac = Bank(15000)
brac.withdraw(25)
brac.withdraw(50000000)
brac.withdraw(1000)

brac.deposit(2000)
brac.deposit(3000)

print(brac.get_balance())