#Method 1
def evenNum(file):
    with open(file, "rt") as f:
        data = f.read()

    num = ""
    lst = []
    for i in data:
        if i != ",":
            num += i
        else:
            lst.append(int(num))
            num = ""
    if num:  # Append the last number if there's no trailing comma
        lst.append(int(num))
    return sum(1 for i in lst if i % 2 == 0)  # Count even numbers

#Method 2
def evenNum2(file):
    with open(file, "rt") as f:
        data = f.read()
    lst = (data.split(",")) # Convert the string to a list of integers
    return sum(1 for i in lst if int(i) % 2 == 0)  # Count even numbers

with open("numbers.txt", "wt") as f:
    f.write("1, 2, 76, 84, 90, 101")
print(evenNum2("numbers.txt"))  # Output: 4