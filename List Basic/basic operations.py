# List declaration
list1 = [1, 2, 3, 4, 5]
list2 = [1.1, 2.2, 3.3, 4.4, 5.5]
list3 = ['a', 'b', 'c', 'd', 'e']
list4 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
list5 = [1, 2.2, 'c', 'date', 5]
print(list1) # [1, 2, 3, 4, 5]
print(list5) # [1, 2.2, 'c', 'date', 5]
print(type(list1)) # <class 'list'>
print(type(list5)) # <class 'list'>

# list access using index
list = [1, 2.2, 'c', 'date', 5]
print(list[0]) # 1
print(list[1]) # 2.2
print(list[len(list) - 1]) # 5

# list access using negative index
list = [1, 2.2, 'c', 'date', 5]
print(list[-1]) # 5
print(list[-2]) # date
print(list[-len(list)]) # 1

# list is mutable
list = [1, 2.2, 'c', 'date', 5]
list[0] = 10
list[1] = 20.2
list[3] = "new date"
print(list) # [10, 20.2, 'c', 'new date', 5]

# list slicing
list = [1, 2.2, 'c', 'date', 5]
print(list[1:3]) # [2.2, 'c']
print(list[:3]) # [1, 2.2, 'c']
print(list[1:]) # [2.2, 'c', 'date', 5]
print(list[:]) # [1, 2.2, 'c', 'date', 5]

# list concatenation
list1 = [1, 2.2, 'c', 'date', 5]
list2 = [6, 7.7, 'g', 'grape', 10]
list3 = list1 + list2
print(list3) # [1, 2.2, 'c', 'date', 5, 6, 7.7, 'g', 'grape', 10]

# list repetition
list = [1, 2.2, 'c', 'date', 5]
list = list * 3
print(list) # [1, 2.2, 'c', 'date', 5, 1, 2.2, 'c', 'date', 5, 1, 2.2, 'c', 'date', 5]

# list membership
list = [1, 2.2, 'c', 'date', 5]
print(2.2 in list) # True
print('z' in list) # False

# list iteration
list = [1, 2.2, 'c', 'date', 5]
for i in list:
    print(i)

# list length
list = [1, 2.2, 'c', 'date', 5]
print(len(list)) # 5

# list append
list = [1, 2.2, 'c', 'date', 5]
list.append(6)
print(list) # [1, 2.2, 'c', 'date', 5, 6]

# list insert
list = [1, 2.2, 'c', 'date', 5]
list.insert(2, 'new')
print(list) # [1, 2.2, 'new', 'c', 'date', 5]

# list remove
list = [1, 2.2, 'c', 'date', 5]
list.remove('c') # remove the first occurrence of 'c'
print(list) # [1, 2.2, 'date', 5]

# list pop
list = [1, 2.2, 'c', 'date', 5]
list.pop() # remove last element
print(list) # [1, 2.2, 'c', 'date']
list.pop(2) # remove element at index 2
print(list) # [1, 2.2, 'date']

# list clear
list = [1, 2.2, 'c', 'date', 5]
list.clear()
print(list) # []

# list index
list = [1, 2.2, 'c', 'date', 5]
print(list.index('date')) # 3

# list count
list = [1, 2.2, 'c', 'date', 5]
print(list.count('c')) # 1

# list sort
list = [5, 1, 3, 2, 4]
list.sort() # sort in ascending order
print(list) # [1, 2, 3, 4, 5]
list.sort(reverse=True) # sort in descending order
print(list) # [5, 4, 3, 2, 1]

# list reverse
list = [5, 1, 3, 2, 4]
list.reverse()
print(list) # [4, 2, 3, 1, 5]

# list copy
list = [1, 2.2, 'c', 'date', 5]
list2 = list.copy()
print(list2) # [1, 2.2, 'c', 'date', 5]

# list comprehension
list = [i for i in range(10)]
print(list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list comprehension with condition
list = [i for i in range(10) if i % 2 == 0] # even numbers
print(list) # [0, 2, 4, 6, 8]
print(type(list)) # <class 'list'>

