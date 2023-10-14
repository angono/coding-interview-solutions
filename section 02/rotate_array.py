'''
Rotate an array to the right by k steps.

'''

def rotate_array(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
