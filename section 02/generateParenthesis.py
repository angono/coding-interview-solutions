"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
	Input: n = 3
	Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
	Input: n = 1
	Output: ["()"]

Constraints:
	1 <= n <= 8

"""

class Solution(object):
    def generateParenthesis(self, n):
	    """
	    Generates all combinations of well-formed parentheses.

	    Args:
	        n: The number of pairs of parentheses.

	    Returns:
	        A list of all combinations of well-formed parentheses.
	    
        :type n: int
        :rtype: List[str]
        """
        combinations = []

        def generate(left, right, s):
            if left == n and right == n:
                combinations.append(s)
                return 
            
            if left < n:
                generate(left + 1, right, s + "(") 
            
            if left > right:
                generate(left, right + 1, s + ")")
            
        generate(0, 0, "")
        return combinations 

        

# Example usage:
n = 3
result = generateParenthesis(n)
print(result)



