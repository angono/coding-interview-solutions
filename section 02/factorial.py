# Example 1: Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1 
    return n * factorial(n - 1)


n1 = factorial(6)
n2 = factorial(10)
n3 = factorial(9)


print("Factorial of 6 is", n1)
print("Factorial of 10 is", n2)
print("Factorial of 9 is", n3)
