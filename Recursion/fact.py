# Factorial Calculation: Write a function to calculate the factorial of a number.
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1) 
