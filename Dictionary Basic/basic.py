#Dictionary is a collection of key-value pairs. It is unordered, changeable and indexed. It as same as map in C++ and Java.

#Creating a dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

#Accessing items
print(my_dict["name"]) #John, using key to access the value of the key
print(my_dict.get("age")) #25, get() method is used to access the value of the key specified

#Changing values
my_dict["age"] = 26
print(my_dict) #{'name': 'John', 'age': 26, 'city': 'New York'}

#Looping through a dictionary
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

#Adding items
my_dict["email"] = "heda@gmail.com" #1st way to add
my_dict.update({"place": "Beissha Para"}) #2nd way to add
print(my_dict) #{'name': 'John', 'age': 26, 'city': 'New York', 'email': 'heda@gmail.com', 'place': 'Beissha Para'}

#Removing items
my_dict.pop("email")
print(my_dict) #{'name': 'John', 'age': 26, 'city': 'New York'}
del my_dict["name"]
print(my_dict) #{'age': 26, 'city': 'New York'}

#Dictionary methods
print(my_dict.keys()) #dict_keys(['name', 'age', 'city'])

print(my_dict.values()) #dict_values(['John', 26, 'New York'])

print(my_dict.items()) #dict_items([('name', 'John'), ('age', 26), ('city', 'New York')])

dict2 = my_dict.copy() #Copies the dictionary
print(dict2) #{'name': 'John', 'age': 26, 'city': 'New York'}

my_dict.update({"email": "heda@heda.com"}) #Adds the key-value pair to the dictionary
print(my_dict)
my_dict.clear() #Clears the dictionary
print(my_dict) #{}

#Nested dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "children": {
        "child1": {
            "name": "Tom",
            "age": 5
        },
        "child2": {
            "name": "Jack",
            "age": 3
        }
    }
}
#Accessing nested dictionary
print(my_dict["children"]["child1"]["name"]) #Tom
print(my_dict["children"]["child2"]["age"]) #3
print(my_dict) #{'name': 'John', 'age': 25, 'city': 'New York', 'children': {'child1': {'name': 'Tom', 'age': 5}, 'child2': {'name': 'Jack', 'age': 3}}}

#Dictionary comprehension
my_dict = {x: x*x for x in range(5)} # x is the key and x*x is the value
print(my_dict) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Dictionary comprehension with if condition
my_dict = {x: x*x for x in range(5) if x%2 == 0} # x is the key and x*x is the value
print(my_dict) #{0: 0, 2: 4, 4: 16}