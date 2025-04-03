from helpers.string import shout
from helpers.math import area

# print(shout(f"the area of a 5-by-8 rectangle is {area(5, 8)}"))
length = 5
width = 8
message = f"The area of a {length}-by-{width} rectangle is {area(length, width)}"
print(shout(message))