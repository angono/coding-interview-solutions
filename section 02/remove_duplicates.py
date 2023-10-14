'''
Given an array of integers, remove all duplicates and return the new array.

'''

def remove_duplicates(nums):
	num_set = set()

	for n in nums:
		if n in num_set:
			num_set.remove(n)
		else:
			num_set.add(n)
	return num_set



list1 = [10, 45, 20, 4, 45, 99]
n = remove_duplicates(list1)

print(n)



