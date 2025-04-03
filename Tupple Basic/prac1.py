grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A")) # Output: 3
print(grades.index("B")) # Output: 4

lst = []
for i in range(len(grades)):
        lst.append(grades[i])
lst.sort()
for i in range(len(lst)):
    print(lst[i])


list1 = [1, 2, 3, 2, 4, 3]
list2 = []
for item in list1:
    if item not in list2:  # Check if item is already in list2
        list2.append(item)
print(list2)  # Output: [1, 2, 3, 4]

# Shorter Approach
list1 = [1, 4, 3, 2, 2, 3]
list2 = []
[list2.append(item) for item in list1 if item not in list2]
print(list2)  # Output: [1, 2, 3, 4]
list3 = []
list3 = list(set(list1)) # Convert list to set to remove duplicates and then convert back to list
print(list3)  # Output: [1, 2, 3, 4]