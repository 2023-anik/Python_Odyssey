#Write a recursive function to print all elements of a list.

def print_list(lst, i):
    if i == len(lst):
        return
    print(lst[i], end = " ")
    print_list(lst, i+1)

lst = [1, 2, 3, 4, 5]
print_list(lst, 0)