#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

dict = {}
for i in range(3):
    key = input()#subject name
    value = int(input())#marks
    dict[key] = value

print(dict)
for key in dict:
    print(f"{key}: {dict[key]}")