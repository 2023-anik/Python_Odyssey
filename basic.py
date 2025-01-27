print("*","\n**","\n***","\n****","\n*****")
print(5,5)
print(8)
print(13, end=" ")
print(21)
for i in range(5):
    print(i, end=" ") #end=" " is used to print the next print statement in the same line
print()
for i in range(5):
    print(i)

print(7, "\n", 5)
print(7, "\n5")
print("Python","Programming")
print("Hello", "World", 5, "endl", 2)
print(1,2,3,4,5)

s = "I love CodeChef"
s = s.split()
for i in range(len(s)):
    print(s[i])

for i in range(1, 6):
    print(f"{i}-{i**2}")

for i in range(4):
    for j in range(4):
        print("*", end="")
    print()

x, y = 20, 6
print(x//y)

c = 25.5
print(f"Celsius-{c}\nKelvin-{c+273}")

l = 4.5
print(f"{4.5**2}\n{4*4.5}")