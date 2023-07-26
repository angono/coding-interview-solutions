'''
Reverse a string in-place.
'''
'''
def reverse_string_in_place(s):
    # Convert the string to a list since strings are immutable in Python
    s_list = list(s)

    # Reverse the list using slicing
    s_list = s_list[::-1]

    # Convert the list back to a string
    reversed_string = ''.join(s_list)
    return reversed_string

'''

def reverse_string_in_place(s):
    if len(s) <= 1:
        return s
    return s[::-1]

# Example usage:
input_string = "hello, world!"
reversed_string = reverse_string_in_place(input_string)
print(reversed_string)  # Output: "!dlrow ,olleh"
