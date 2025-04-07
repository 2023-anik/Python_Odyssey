def wrapper_fun(func):
    def inner_fun(*agrs, **kwargs): # args and kwargs are used to pass any number of arguments and keyword arguments
        print(f"Before calling the function")
        func(*agrs, **kwargs)
        print(f"After calling the function")
    return inner_fun

@wrapper_fun
def say_hello(name):
    print(f"Hello, {name}!")

@wrapper_fun
def add(a, b):
    return a + b

@wrapper_fun
def multiply(a, b):
    print(f"{a} * {b} = {a * b}")

# Example usage
# wraped_function=say_hello("Alice")
# print(wraped_function)
say_hello("Alice")

result = add(5, 10)
print(f"Result of add function: {result}")

multiply(3, 4)