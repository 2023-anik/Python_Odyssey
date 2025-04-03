# Tuple is used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.
# Tuple is more memory-efficient than a list. It is faster to access an element in a tuple than in a list.
# Tuple initialization with values separated by commas
x = (1, 2, 3, 4, 5,)
print(x)  # Output: (1, 2, 3, 4, 5)

# Tuple initialization with a single value
x = (1,)
print(x)  # Output: (1,)

# Tuple initialization without values
x = ()
print(x)  # Output: ()

# Tuple initialization without parentheses
x = 1, 2, 3, 4, 5
print(x)  # Output: (1, 2, 3, 4, 5)

# Tuple Methods and Operations
# Tuple access using index
x = (1, 2, 3, 4, 5)
print(x[0])  # Output: 1

# Tuple access using negative index
x = (1, 2, 3, 4, 5)
print(x[-1])  # Output: 5

# Tuple slicing
x = (1, 2, 3, 4, 5)
print(x[1:3])  # Output: (2, 3)

# Tuple concatenation
x = (1, 2, 3)
y = (4, 5, 6)
z = x + y
print(z)  # Output: (1, 2, 3, 4, 5, 6)

# Tuple repetition
x = (1, 2, 3)
y = x * 3
print(y)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Tuple membership
x = (1, 2, 3)
print(2 in x)  # Output: True
print(4 in x)  # Output: False

# Tuple iteration
x = (1, 2, 3)
for i in x:
    print(i)

# Tuple length
x = (1, 2, 3)
print(len(x))  # Output: 3

# Tuple unpacking
x = (1, 2, 3)
a, b, c = x
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Tuple packing
a = 1
b = 2
c = 3
x = a, b, c
print(x)  # Output: (1, 2, 3)

# Tuple with different data types
x = (1, 2.2, 'c', 'date', 5)
print(x)  # Output: (1, 2.2, 'c', 'date', 5)

# Tuple with nested tuples
x = (1, 2, (3, 4, 5), 6, 7)
print(x)  # Output: (1, 2, (3, 4, 5), 6, 7)

# Difference between tuple and list
# Tuple is immutable (unchangeable) whereas list is mutable (changeable)
# Tuple is faster than list
# Tuple consumes less memory than list
# adding, removing, or modifying elements in a tuple is not allowed