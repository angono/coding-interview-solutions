'''
Write a function to compute the power of a number using recursion.

- Create a recursive function with parameters number N and power P.
- If P = 0 return 1.
- Else return N times result of the recursive call for N and P-1.

'''

def powers(N, P):
	if P == 0:
		return 1 
	return (N*powers(N, P-1))

def powers(N, P):
	if P == 0:
		return 1 
	return (N * powers(N, P - 1))

print(powers(8,0))
print(powers(5,2))
