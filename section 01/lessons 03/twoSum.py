'''
# Example 1: Two Sum - Find two elements that sum up to a target value

'''

def twoSum(nums, target):
    mapping = {}
    for i, num in enumerate(nums):
        diff = target - num 
        if diff in mapping:
            return [mapping[diff], i]
        else:
            mapping[diff] = i
    return None
