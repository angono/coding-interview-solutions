'''
Given an array of integers, find the subarray with the largest sum (Kadane's algorithm).

'''

# Example 2: Kadane's Algorithm - Maximum subarray sum
def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


list1 = [10, 20, 4, 10]
print(max_subarray_sum(list1))

# Output: 44
