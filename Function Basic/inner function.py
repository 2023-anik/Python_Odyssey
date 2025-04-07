#inner function 1
def double_decker():
    print(f"Starting the double_decker function")
    def inner_fun():
        print(f"Inside the inner function")
        return 3000
    return inner_fun

#inner function with arguments
def do_something(work):
    print(f"Work started")
    work()
    print(f"Work finished")

def coding():
    print(f"Coding started")

#Example usage of inner function
print(double_decker())
print(double_decker()()) # This will call the inner function and return 3000

#Example usage of inner function with arguments
do_something(coding) # This will call the coding function