# Example 3: Fibonacci using dynamic programming

'''

the fibonacci sequence is a series of numbers where 
the next number is found by adding up the two numbers 
just before. 

0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

default fib = [0, 1]

For example: 
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3 
2 + 3 = 5 
3 + 5 = 8 
5 + 8 = 13


'''

# Time complexity : O(n)
# Auxiliary Space: O(n)
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


n1 = fibonacci(2)
n2 = fibonacci(3)
n3 = fibonacci(4)
n4 = fibonacci(5)

print(f"{n1}\n{n2}\n{n3}\n{n4}")





