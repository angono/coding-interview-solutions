# python srings
# concatenating string simply means combining or adding strings together

a = 'hel'
b = 'lo'

text1 = a + b
print(text1)

x = 'der'
y = 'k'
z = 'os'

text2 = x + y + z
print(text2)

text3 = 'let\'s learn python'
print(text3)


# accessing parts of a string using index
text4 = 'tirel'
print(text4[0])
print(text4[1])
print(text4[-1])
print(text4[-2])


# slicing; accessing a range of characters using slicing. 
# slicing also uses square brackets
text5 = 'python programming'
print(text5[1:5])
print(text5[2:])

text6 = 'denaMSE ANGono'

print(text6)

# capitalizing string
print(text6.capitalize())

# converting to upper case
print(text6.upper())

# converting to lower case
print(text6.lower())

# get the length of a string
print(len(text6))


# replacing parts of string. syntax: replace(old, new)
print(text6.replace('denaMSE', 'is it you'))


# checking if a value is present in a string
x = 'tirel' not in text6
print(f'{x}, it is not text6')







