# input function is used to take input from the user
# input function always returns a string

# a = input() # "2"
# b = input() # "3"
# print(type(a+b), a+b) # <class 'str'> 23

# a = int(input()) # 2
# b = int(input()) # 3
# print(type(a+b), a+b) # 5

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Name:", name)
print("Age:", age)
print("Marks:", marks)