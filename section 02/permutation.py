# Given two strings, check if one is a permutation of the other.
# Time complexity: O(n Log n)
# Space complexity: O(1)

# 1) Sort both strings 
# 2) Compare the sorted strings 

def permutation(str1, str2):

	if len(str1) != len(str2):
		return False

	a = sorted(str1)
	str1 = ''.join(a)

	b = sorted(str2)
	str2 = ''.join(b)

	for i in range(0, len(str1), 1):
		if str1[i] != str2[i]:
			return False 
		else:
			return True 


perm = permutation('pat','tap')
print(perm)

