class Dog:
    species = 'Canis familiaris'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method
    def description(self):
        return f"Description: {self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    # Magic method
    def __str__(self):
        return f"Magic method: {self.name} is {self.age} years old"
    
miles = Dog("Miles", 4)
print(miles) # <__main__.Dog object at 0self7f8b8c6b3d30>
# when we use Magic method __str__ we can get the output like this:
# Miles is 4 years old
# The name of the Magic method is __str__ and it is used to return a string representation of the object.
# The __str__ method is called when the print() or str() function is invoked on an object.
# The __str__ method should return a string.
# The __str__ method is one of Python's so-called "magic methods".
print(miles.description())
print(miles.speak("Woof Woof"))