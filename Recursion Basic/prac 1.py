#Write a recursive function to calculate the sum of first n natural numbers (1 to n) where n is a positive integer.

def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    return n + sum_of_natural_numbers(n-1)

n = int(input())
print(sum_of_natural_numbers(n))