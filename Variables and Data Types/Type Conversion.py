# Type Casting (Type Conversion)
a = 2 # int
b = 3.5 # float
c = "5.5" # string
d = "6" # string
print(a+b) # 5.5
print(a+float(c)) # 7.5
print(a+int(d)) # 8

a = "222222"
b = 333333
print(int(a)+b) # 555555
print(str(a)+str(b)) # 222222333333


#decimal to binary
num = 11
binary = bin(num) # 0b1011 (0b is a prefix for binary numbers)
print(binary)
binary = bin(num)[2:] # 1011 (removing the prefix)
print(binary) # 1011 (data type: string)

#binary to decimal
binary = "1011"
decimal = int(binary, 2)
print(decimal) # 11 (data type: int)

#decimal to octal
num = 11
octal = oct(num) # 0o13 (0o is a prefix for octal numbers)
print(octal)
octal = oct(num)[2:] # 13 (removing the prefix). Here [2:] means from index 2 to the end
print(octal)

#octal to decimal
octal = "13"
decimal = int(octal, 8)
print(decimal) # 11 (data type: int)

#decimal to hexadecimal
num = 11
hexadecimal = hex(num).upper() # 0XB (0x is a prefix for hexadecimal numbers)
print(hexadecimal)
hexadecimal = hex(num)[2:].upper() # B (removing the prefix)
print(hexadecimal)

#hexadecimal to decimal
hexadecimal = "b"
decimal = int(hexadecimal, 16)
print(decimal) # 11 (data type: int)

# List to Tuple
lst = [1, 2, 3]
tup = tuple(lst)  # Output: (1, 2, 3)

# Tuple to List
tup = (4, 5, 6)
lst = list(tup)  # Output: [4, 5, 6]

# String to List
string = "hello"
char_list = list(string)  # Output: ['h', 'e', 'l', 'l', 'o']


