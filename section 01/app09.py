# python set 
# python set is an unordered and immutable container

# A set is created by using square brackets '{}'

pets = {'dog', 500, 'cat', 'snake', 'rabbit'}

print(pets)

for x in pets:
    print('item:',x)

pets.add('fish')
print(pets)

pets.remove(500)
print(pets)

pets.pop()
print(pets)

print('set length:',len(pets))

print('python' in pets)
print('fish' in pets)

more_animal = {'elephant', 'bird', 'bee'}

pets.update(more_animal)
print(pets)


mypets = set((pets))
print(mypets)






