"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

	1. Open brackets must be closed by the same type of brackets.
	2. Open brackets must be closed in the correct order.
	3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
	Input: s = "()"
	Output: true

Example 2:
	Input: s = "()[]{}"
	Output: true

Example 3:
	Input: s = "(]"
	Output: false

Constraints:
	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.

More challenges
	32. Longest Valid Parentheses
	1003. Check If Word Is Valid After Substitutions
	2337. Move Pieces to Obtain a String


"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            elif bracket in brackets.keys():
                if not stack or stack.pop() != brackets[bracket]: 
                    return False 
        return True if not stack else False
        
