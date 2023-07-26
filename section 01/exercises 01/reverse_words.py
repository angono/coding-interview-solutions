'''
Reverse words in a sentence ("Hello World" -> "World Hello").

'''

# def reverse_words(string):
#     words = string.split()
#     return ' '.join(reversed(words))


def reverse_words(string): 
	words = string.split()[::-1]
	return ' '.join(words)


def reverse_words(string):
	words = string.split()[::-1]
	return ''.join(words)

s = reverse_words("Hello World")
print(s)

