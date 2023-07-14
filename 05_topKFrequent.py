# 1 - Contains Duplicate
class Solution(object):
    def topKFrequent(self, nums, k):
        
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        '''
        we use the sorted() function to sort the elements 
        based on their frequencies in descending order. 
        
        The key=lambda x: frequency[x] parameter specifies that 
        the sorting should be based on the values in the 
        frequency dictionary.
        '''
        sorted_nums = sorted(frequency, lambda: x, frequency[x], reverse=True)
        return sorted_nums[:k]

