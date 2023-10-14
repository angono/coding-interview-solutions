# python list 
# python list in an ordered container

# A list is created by using square brackets '[]'

pets = ['dog', 500, 'cat', 210, 'rabbit']

print(pets)
print(pets[0])
print(pets[1])
print(pets[2])
print(pets[-1])
print(pets[-2])
print(pets[1:4])
print(pets[:3])
print(pets[2:])

pets.append('derkos')
pets.append('angono')
print(pets)

pets.insert(3, 'maria')
print(pets)

pets.pop()
print(pets)

pets.remove('cat')
print(pets)


print('length of items in the list: ',len(pets))

pets[-1]='Ango1'
print(pets)

print('derkos' in pets)

# for loop
for x in pets:
    print('item:',x)


# using list
mypets = list((pets))
print(mypets)









