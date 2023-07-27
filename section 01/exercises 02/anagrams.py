'''
Check if two strings are anagrams.

'''

def anagrams(s, t):
	if len(s) != len(t):
		return False 
	else:
		s1 = sorted(s.lower())
		t1 = sorted(t.lower())

	return s1 == t1


print(anagrams("cold", "code"))
# Output: False


print(anagrams("arc", "car"))
# Output: True

