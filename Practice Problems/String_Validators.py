if __name__ == '__main__':
    s = input()

    # Use any() to check each condition
    alnum = any(char.isalnum() for char in s) # Check if any character is alphanumeric
    a = any(char.isalpha() for char in s)  # Check if any character is alphabetic
    d = any(char.isdigit() for char in s)  # Check if any character is a digit
    l = any(char.islower() for char in s)  # Check if any character is lowercase
    u = any(char.isupper() for char in s)  # Check if any character is uppercase

    print(alnum)
    print(a) 
    print(d)
    print(l)
    print(u)
