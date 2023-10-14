'''
Check if a string has all unique characters.

'''

def unique_chars(s):
	char_set = set()
	for char in s:
		if char in char_set:
			return False 
		else:
			char_set.add(char)
	return True

# Example usage:
input_string = "hello"
print(unique_chars(input_string))  # Output: False

input_string = "world"
print(unique_chars(input_string))  # Output: True

