import random

capitals_dict = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield"
}

# state = random.choice(list(capitals_dict.keys()))
# capital = capitals_dict[state]

state, capital = random.choice(list(capitals_dict.items())) 

print(f"What is the capital of {state}?")

while 1:
    if(input('To exit type "Exit" to skip "any charecter": ').lower() == "exit"):
        print(f"The capital of {state} is {capital}.")
        print(f"Goodbye!")
        break
    if input("Guess the answer: ").lower() == capital.lower():
        print("Correct!")
        break
    else:
        print("Incorrect! Try again.")