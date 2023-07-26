'''
Given a sorted array, find the index of a target element using binary search.

'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target element not found in the array


# Example usage:
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target_element = 5
index = binary_search(sorted_array, target_element)
print(index)  # Output: 3 (index of target_element in the array)

