# Example 2: Check if a string is a palindrome
def isPalindrome(s):
    return s == s[:: -1]


s1 = isPalindrome("madam")
s2 = isPalindrome("derkos")
s3 = isPalindrome("racecar")
print(s1)
print(s2)
print(s3)
