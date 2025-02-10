import random # Importing the random module to generate random numbers
import string # Importing the string module to use the ascii_letters and digits constants

# print(string.ascii_letters) # Printing the ascii_letters constant
# print(string.digits) # Printing the digits constant
# print(string.ascii_lowercase) # Printing the ascii_lowercase constant
# print(string.ascii_uppercase) # Printing the ascii_uppercase constant
# print(string.punctuation) # Printing the punctuation constant

characters = string.ascii_letters + string.digits + string.punctuation # Concatenating the ascii_letters, digits, and punctuation constants

passLen = 8 # Length of the password
randomPass = " " # Initializing an empty string to store the random password
for i in range(passLen):
    randomPass += random.choice(characters) # Appending a random character from the characters string to the randomPass string

print(f"Random Password: {randomPass}") # Printing the random password