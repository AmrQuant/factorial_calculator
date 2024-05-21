def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

factorial_of_a_number = 10
print(factorial(factorial_of_a_number))