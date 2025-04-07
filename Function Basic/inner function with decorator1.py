import math

def timer(func):
    def inner(*args, **kwargs):
        print(f"Time started")
        func(*args, **kwargs)
        print(f"Time finished")
    return inner

@timer
def get_factorial(n):
    print(f"Factorial starting")
    print(f"Factorial of {n} is {math.factorial(n)}")

# Example usage
get_factorial(5)