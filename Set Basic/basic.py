# Set is a collection of unique elements. It is unordered and unindexed. It is similar to set in mathematics. It is used to perform mathematical set operations like union, intersection, symmetric difference, etc.

#Creating a set using set() constructor
my_set = set([1, 4, 3, 2, 5])
print(my_set) #output maight be: {1, 2, 3, 4, 5} or {1, 4, 3, 2, 5} (not guaranteed to be in order)

#Creating a set using curly braces
my_set = {1, 4, 3, 2, 5}

#Adding elements to a set
my_set.add(6)
print(my_set) #{1, 2, 3, 4, 5, 6}

#Removing elements from a set
my_set.remove(3)
print(my_set) #{1, 2, 4, 5, 6}

#Checking if an element is in the set
print(2 in my_set) #True

#Looping through a set
for x in my_set:
    print(x)

#pop() method removes a random element from the set
my_set.pop()
print(my_set)

#clear() method empties the set
my_set.clear()
print(my_set) #set()


#Set methods
my_set = {1, 4, 3, 2, 5}
my_set2 = {7, 8, 9, 10}
print(my_set.union(my_set2)) #{1, 2, 4, 5, 6, 7, 8, 9, 10}, returns a new set with all the elements of both sets
print(my_set.intersection(my_set2)) #set() - empty set, returns a new set with elements common to both sets

#Set operations
print(my_set | my_set2) #{1, 2, 4, 5, 6, 7, 8, 9, 10}, union of two sets
print(my_set & my_set2) #set() - empty set, intersection of two sets
print(my_set - my_set2) #{1, 2, 4, 5, 6}, elements that are only in my_set
print(my_set ^ my_set2) #{1, 2, 4, 5, 6, 7, 8, 9, 10}, symmetric difference

#Set comprehension
my_set = {x for x in range(5)}
print(my_set) #{0, 1, 2, 3, 4}

#Frozen set, meaning the elements of the set cannot be changed
my_frozen_set = frozenset([1, 2, 3, 4, 5])
print(my_frozen_set) #frozenset({1, 2, 3, 4, 5})