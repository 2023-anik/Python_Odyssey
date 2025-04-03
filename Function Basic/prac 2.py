#WAF to print the elements of a list in a single line (list is the parameter of the function)

#method 1
def elements_of_list1(lst):
    for i in lst:
        print(i, end = " ")# end=" " prevents new line
    print()

#method 2
def elements_of_list2(lst):
    print(*lst)# *lst unpacks the list

#method 3
def elements_of_list3(lst):
    s = map(str, lst)
    print(list(s))
    print(" ".join(map(str, lst))) # map() converts the elements of the list to string

lst = [1, 2, 3, 4, 5]
elements_of_list1(lst)
elements_of_list2(lst)
elements_of_list3(lst)

#map() is a object of the built-in class map
#Syntax: map(function, iterable)
#map() applies a function to each item in an iterable (like a list or tuple) and returns an iterator.
#Syntax: str.join(iterable)
#The join() method returns a string concatenated with the elements of an iterable.
