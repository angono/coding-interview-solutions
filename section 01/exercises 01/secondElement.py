'''
# Find the second largest element in an array.

# sort the list   
list1.sort()
     
# print second maximum element
print("Second largest element is:", list1[-2])
 

Time Complexity: O(NlogN) where N is the number of elements in the Array.
Space Complexity: O(1)

'''
def secondElement(N):
	second_largest = sorted(N)[-2]
	return second_largest

def secondElement(N):
	n = sorted(N)[-2]
	return n 

list1 = [10, 20, 4, 45, 99]
n = secondElement(list1)

print(n)


'''

# List of numbers
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
 
# Removing duplicates from the list
list2 = list(set(list1))
 
# Sorting the  list
list2.sort()
 
# Printing the second last element
print("Second largest element is:", list2[-2])

'''

def secondElement(N):
	list1 = list(set(N))
	list1.sort()
	return list1[-2]

def secondElement(N):
	list1 = list(set(N))
	list1.sort()
	return list1[-2]

list1 = [10, 45, 20, 4, 45, 99, 99]
n = secondElement(list1)

print(n)














