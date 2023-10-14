"""
1099. Two Sum Less Than K

Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

Example 1:
	Input: nums = [34,23,1,24,75,33,54,8], k = 60
	Output: 58
	Explanation: We can use 34 and 24 to sum 58 which is less than 60.

Example 2:
	Input: nums = [10,20,30], k = 15
	Output: -1
	Explanation: In this case it is not possible to get a pair sum less that 15.

Constraints:
	1 <= nums.length <= 100
	1 <= nums[i] <= 1000
	1 <= k <= 2000


"""

class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        Finds the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k.

        Args:
            nums: A list of integers.
            k: An integer.

        Returns:
            The maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k, or -1 if no such sum exists.
        
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()  # Sort the array in ascending order
        left, right = 0, len(nums) - 1
        max_sum = -1  # Initialize max_sum to -1 (no valid sum found yet)
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < k:
                max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left
        
        return max_sum
