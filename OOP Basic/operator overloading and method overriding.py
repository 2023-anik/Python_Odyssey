class Cricketer:
    def __init__(self, name, runs):
        self.name = name
        self.runs = runs
    
    # Overloading the + operator to add runs of two cricketers
    def __add__(self, other):
        return self.runs + other.runs
    # Overloading the * operator to multiply runs of two cricketers
    def __mul__(self, other):
        return self.runs * other.runs
    # Overloading the - operator to subtract runs of two cricketers
    def __sub__(self, other):
        return self.runs - other.runs



    def __str__(self):
        return f"{self.name}: Runs = {self.runs}"


class Bowler(Cricketer):
    def __init__(self, name, runs, wickets):
        super().__init__(name, runs)
        self.wickets = wickets
    
    #Overriding the __str__ method to include wickets
    def __str__(self):
        return f"{self.name}: Runs = {self.runs}, Wickets = {self.wickets}"

# Example usage
sakib = Cricketer("Sakib", 600)
mash = Cricketer("Mash", 500)

# Using the __str__ method to print the cricketers
print(sakib)  # Output: Sakib: Runs = 600
print(mash)  # Output: Mash: Runs = 500


# Using overloaded operators
print(sakib + mash)  # Output: 1100
print(sakib * mash)  # Output: 300000
print(sakib - mash)  # Output: 100

# Example usage of Bowler class
mustafiz = Bowler("Mustafiz", 300, 50)
print(mustafiz)  # Output: Mustafiz: Runs = 300, Wickets = 50