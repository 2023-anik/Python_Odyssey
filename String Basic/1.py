a = "Tur"
b = "Heda"

# concatenation
str = a + b
print(str) # TurHeda
str = a + " " + b
print(str) # Tur Heda

#length
print(len(a)) # 3
print(len(b)) # 4
print(len(str)) # 7; including space


# accessing elements, changing a character of a string is not allowed in python
print(a[0]) # T
print(a[1]) # u
print(a[2]) # r
print(b[0]) # H

# slicing
print(str[0:3]) # Tur
print(str[4:8]) # Heda
print(str[:3]) # Tur
print(str[4:]) # Heda
print(str[4: len(str)]) # Heda
print(str[:]) # Tur Heda

# negative indexing

# T = -8
# u = -7
# r = -6
# space = -5
# H = -4
# e = -3
# d = -2
# a = -1

print(str[-1]) # a
print(str[-2]) # d
print(str[-3:]) # eda
print(str[:-3]) # Tur H
print(str[-7:-2]) # ur He

