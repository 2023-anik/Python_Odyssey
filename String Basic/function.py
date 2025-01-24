# len() -> returns the length of a string
s = "Python"
print(len(s))  # Output: 6

# lower() -> converts all the characters of a string to lowercase
s = "Python"
print(s.lower())  # Output: python

# upper() -> converts all the characters of a string to uppercase
s = "Python"
print(s.upper())  # Output: PYTHON

# title() -> converts the first character of each word to uppercase
s = "python programming"
print(s.title())  # Output: Python Programming

# capitalize() -> converts the first character of a string to uppercase
s = "python programming"
print(s.capitalize())  # Output: Python programming

# count() -> returns the number of occurrences of a substring in a string
s = "Python is easy to learn. Python is open-source."
print(s.count("Python"))  # Output: 2

# find() -> returns the index of the first occurrence of a substring in a string
s = "Python is easy to learn. Python is open-source."
print(s.find("Python"))  # Output: 0

# rfind() -> returns the index of the last occurrence of a substring in a string
s = "Python is easy to learn. Python is open-source."
print(s.rfind("Python"))  # Output: 26

# index() -> returns the index of the first occurrence of a substring in a string
s = "Python is easy to learn. Python is open-source."
print(s.index("Python"))  # Output: 0

# rindex() -> returns the index of the last occurrence of a substring in a string
s = "Python is easy to learn. Python is open-source."
print(s.rindex("Python"))  # Output: 26

# replace() -> replaces a substring with another substring in a string
s = "Python is easy to learn. Python is open-source."
print(s.replace("Python", "Java"))  # Output: Java is easy to learn. Java is open-source.

# split() -> splits a string into a list of substrings
s = "Python is easy to learn. Python is open-source."
print(s.split())  # Output: ['Python', 'is', 'easy', 'to', 'learn.', 'Python', 'is', 'open-source.']

# strip() -> removes leading and trailing whitespaces from a string
s = "  Python  "
print(s.strip())  # Output: "Python"

# lstrip() -> removes leading whitespaces from a string
s = "  Python  "
print(s.lstrip())  # Output: "Python  "

# rstrip() -> removes trailing whitespaces from a string
s = "  Python  "
print(s.rstrip())  # Output: "  Python"

# isalnum() -> returns True if all the characters of a string are alphanumeric
s = "Python123"
print(s.isalnum())  # Output: True

# isalpha() -> returns True if all the characters of a string are alphabetic
s = "Python"
print(s.isalpha())  # Output: True

# isdigit() -> returns True if all the characters of a string are digits
s = "123"
print(s.isdigit())  # Output: True

# islower() -> returns True if all the characters of a string are lowercase
s = "python"
print(s.islower())  # Output: True

# isupper() -> returns True if all the characters of a string are uppercase
s = "PYTHON"
print(s.isupper())  # Output: True

# istitle() -> returns True if the first character of each word is uppercase and the rest are lowercase
# Note: The first character of the string should be uppercase
s = "Python Programming"
print(s.istitle())  # Output: True

# isspace() -> returns True if all the characters of a string are whitespaces
s = "   "
print(s.isspace())  # Output: True

# startswith() -> returns True if a string starts with a specified substring
s = "Python is easy to learn."
print(s.startswith("Python"))  # Output: True

# endswith() -> returns True if a string ends with a specified substring
s = "Python is easy to learn."
print(s.endswith("learn."))  # Output: True

# join() -> joins the elements of an iterable with a specified separator
s = ["Python", "is", "easy", "to", "learn."]
print("".join(s))  # Output: Pythoniseasytolearn.
print(" ".join(s))  # Output: Python is easy to learn.
print(" BhodA ".join(s).title())  # Output: Python Bhoda Is Bhoda Easy Bhoda To Bhoda Learn.

# center() -> returns a centered string
s = "Python"
print(s.center(8, "*"))  # Output: *Python*
print(s.center(9, "*"))  # Output: **Python*
print(s.center(10, "*"))  # Output: **Python**

# ljust() -> returns a left-justified string
s = "Python"
print(s.ljust(8, "*"))  # Output: Python**
print(s.ljust(9, "*"))  # Output: Python***
print(s.ljust(10, "*"))  # Output: Python****

# rjust() -> returns a right-justified string
s = "Python"
print(s.rjust(8, "*"))  # Output: **Python
print(s.rjust(9, "*"))  # Output: ***Python
print(s.rjust(10, "*"))  # Output: ****Python

# zfill() -> returns a string with zeros filled to the left
s = "123"
print(s.zfill(5))  # Output: 00123
print(s.zfill(6))  # Output: 000123

# partition() -> returns a tuple containing three elements: the substring before the first occurrence of a separator, the separator itself, and the substring after the first occurrence of the separator
s = "Python is easy to learn."
print(s.partition("easy"))  # Output: ('Python is ', 'easy', ' to learn.')

# rpartition() -> returns a tuple containing three elements: the substring before the last occurrence of a separator, the separator itself, and the substring after the last occurrence of the separator
s = "Python is easy to learn."
print(s.rpartition("Python"))  # Output: ('', 'Python', ' is easy to learn.')