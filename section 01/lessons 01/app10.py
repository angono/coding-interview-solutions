 # python dictionary 
# python dictionary is an unordered and mutable collection of items

# A dictionary is created by using square brackets '{}'

person = {
    'name':'derkos',
    'job':'web developer',
    'salary':7500
}

print(person)
print('dictionary length:',len(person))

for key in person:
    print(person[key])

if 'job' in person:
    print('yes, the "job" is in it')

print('Getting an item:',person.get('job'))
print('Getting an item:',person.get('age'))

print('name:',person['name'])
print('job:',person['job'])
print('salary:',person['salary'])


person['name'] = 'derkos tirel'
print(person)


person.pop('name')
print(person)


del person['job']
print(person)


all_persons = {
    'ceo':{
        'name':'derkos',
        'job':'web developer',
        'salary':7500,
    },
    
    'marketing':{
        'name':'maria',
        'job':'manager',
        'salary':6500,
    },
    
    'design':{
        'name':'tijah',
        'job':'researcher',
        'salary':5000,
    },
}


print('CEO:',all_persons['ceo']['name'])
print('Marketing:',all_persons['marketing']['name'])
print('Design:',all_persons['design']['name'])


for key in all_persons:
    print('Name:',all_persons[key]['name'])
    print('Job:',all_persons[key]['job'])



