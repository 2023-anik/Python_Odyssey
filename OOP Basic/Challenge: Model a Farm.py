class Animal:

    # Class Attribute
    stuff_in_belly = 0
    position = 0
    
    # Initializer / Instance Attributes
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #Instance methods - talk, walk, run, feed, is_hungry, poop
    def talk(self, sound=None):
        """Return the string "<name> says <sound>""
        If `sound` is left out, returns "Hello, I'm <name>"
        """
        if sound is None:
            return f"Hello, I'm {self.name}!"
        return f"{self.name} says {sound}"
    
    def walk(self, walk_increment):
        """Move the animal's position by `walk_increment`"""
        self.position += walk_increment
        return self.position
    
    def run(self, run_increment):
        """Move the animal's position by `run_increment`"""
        self.position += run_increment
        return self.position

    def feed(self):
        """Feed the animal"""
        self.stuff_in_belly += 1
        if self.stuff_in_belly > 3:
            return self.poop()
        return f"{self.name} has been fed"
    
    def is_hungry(self):
        """Return True if the animal is hungry"""
        if self.stuff_in_belly < 2:
            return f"{self.name} is hungry"
        return f"{self.name} is not hungry"
    
    def poop(self):
        """Make the animal poop"""
        self.stuff_in_belly = 0
        return f"Ate too much ... need to find a batheroom"
    

class Dog(Animal):
    def talk(self, sound="Bark"):
        return super().talk(sound)
    
    def fetch(self):
        return f"{self.name} is fetching"
    
class Sheep(Animal):
    def talk(self, sound="Baaa"):
        return super().talk(sound)
    
class Pig(Animal):
    def talk(self, sound="Oink"):
        return super().talk(sound)


# Create a dog
dog = Dog("Blitzer", "yellow")

#Output the dog's attributes
print(f"Our dog's name is {dog.name}.")
print(f"And he's {dog.color}.")

#Output some behavior
print(f"Say something, {dog.name}.")
print(dog.talk())
print(f"Go fetch!")
print(dog.fetch())

#walk the dog
print(f"{dog.name} is at position {dog.walk(2)}")
print(f"{dog.name} is at position {dog.walk(3)}")
print(f"{dog.name} is at position {dog.walk(4)}")

#Run the dog
print(f"{dog.name} is now at position {dog.run(5)}")

#Feed the dog
print(dog.feed())

#Check if the dog is hungry
print(dog.is_hungry())

#Feed the dog more
print(dog.feed())
print(dog.feed())
print(dog.is_hungry())
print(dog.feed())