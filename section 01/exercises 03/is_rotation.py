'''
Check if a string is a rotation of another string ("abcde" and "deabc" are rotations).
'''

def is_rotation(str1, str2):
    # Check if the lengths of the two strings are equal
    if len(str1) != len(str2):
        return False

    # Concatenate the first string with itself
    concatenated_str = str1 + str1
    print(concatenated_str)

    # Check if the second string is a substring of the concatenated string
    return str2 in concatenated_str


# Example usage:
string1 = "abcde"
string2 = "deabc"
print(is_rotation(string1, string2))  # Output: True

string1 = "hello"
string2 = "world"
print(is_rotation(string1, string2))  # Output: False
