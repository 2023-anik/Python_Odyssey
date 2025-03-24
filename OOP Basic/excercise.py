#!/usr/bin/env python3  # Add this if missing
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.color}.")


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # def __str__(self): # Magic method
    #     return f"The {self.color} car has {self.mileage} miles."

    def description(self): # instance method to return a string
        return f"The {self.color} car has {self.mileage} miles."
    

    def drive(self, num): # instance method to update the mileage
        self.mileage = num
    
blueCar = Car("blue", 20_000)
redCar = Car("red", 30_000)
# print(blueCar)
# print(redCar)

print(blueCar.description())
print(redCar.description())

blueCar.drive(5_000)
print(blueCar.mileage)
print(blueCar.description())