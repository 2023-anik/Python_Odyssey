import random

target = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess: "))
    if guess == target:
        print("Congratulations! You guessed it right!")
        break
    elif guess < target:
        print("Try a higher number")
    else:
        print("Try a lower number")

print("-----Game Over!-----")