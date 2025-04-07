def wrapper_func(func):
    def inner(*args, **kwargs):
        print(f"Funciton execution starts")
        result = func(*args, **kwargs)
        # print(result)
        print(f"Function execution ends")
        return result
    return inner

@wrapper_func
def add(a, b):
    return a+b

sum = add(5, 10)
print(f"Sum is {sum}")