'''
Count the occurrences of each character in a string.

'''

def countChar(words):
	dics = {}

	for i in words:
		if i in dics:
			dics[i] += 1 
		else:
			dics[i] = 1 
	return dics


def countChar(words):
	dics = {}
	for i in words:
		if i in dics:
			dics[i] += 1
		else:
			dics[i] = 1 
	return dics 

print(countChar("opening"))
print(countChar("sentence"))
print(countChar("derkos"))

