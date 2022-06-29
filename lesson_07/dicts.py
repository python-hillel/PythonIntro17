from pprint import pprint
"""
    {
        key1: value1,
        key2: value2,
        key3: value3,
        key4: None,
    }
"""

d = {}
print(type(d), d)
d = dict()
print(type(d), d)
d = {
    1: 'one',
    2: 'two',
    4: 'four'
}
print(type(d), d)

d = dict(
    [
        ('Colorado', 'Rockies'),
        ('Boston', 'Red Sox'),
        ('Minnesota', 'Twins'),
        ('Milwaukee', 'Brewers'),
        ('Seattle', 'Mariners'),
        ('Boston', 'Red Sox 34')
    ]
)
pprint(d)

d = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

pprint(d)

print(d['Boston'])
d['Boston'] = 'Red Sox 345'
pprint(d)
d['Boston 12'] = 'Red Sox 34545'
pprint(d)

del d['Boston 12']
pprint(d)

person = {}
print(type(person))                             # <class 'dict'>
person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
pprint(person)

print(person['children'][1])
print(person['pets']['cat'])
person[(1, 2, 3)] = True
pprint(person)
# person[[1, 2, 3]] = False

# in, not in
print('fname' in person)

# len()
print(len(person))

# dict.clear()
person.clear()
print(person)

d = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners',
}

# dict.get(key, default_value)
print(d.get('Boston'))
print(d.get('Boston1'))
print(d.get('Boston1', 'String'))

# dict.keys()
# dict.values()
# dict.items()
pprint(d.keys())
pprint(d.values())
pprint(d.items())
for key, value in d.items():
    print(f'{key} : {value}')

# dict.pop(key)
print(d.pop('Boston'))
print(d)

# dict.popitem()
print(d.popitem())
print(d)

# dict1.update(dict2)
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
print(d1)
print(d2)
d1.update(d2)
print(d1)
print(d2)
