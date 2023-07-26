# Given an array of integers, find the maximum and minimum elements.
# time complexity: O(n log n)
# space complexity: O(1)

def get_mini_max(arr):
	arr.sort()
	minimax = {"mini": arr[0], "max": arr[-1]}
	return minimax 

def get_mini_max(arr):
	arr.sort()
	minimax = {"mini":arr[0], "max":arr[-1]}
	return minimax


arr = [12, 34, 54, 20, 30, 2]

minimax = get_mini_max(arr)

print("The minimum is", minimax["mini"])
print("The maximum is", minimax["max"])
