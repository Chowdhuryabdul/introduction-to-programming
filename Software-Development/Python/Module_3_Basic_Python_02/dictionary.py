
# to declare dictionary--
# key value pari
person = {'name': 'kala Pakhi', 'address': 'Kalipur', 'age': 23, 'job': 'bekar'}
print(person)
print(person['job'])
# to print the keys
print(person.keys())
# to print value
print(person.values())

# to add new key av value
person['langiage'] = 'python'
print(person)

# modification of existing values
person['name'] = 'sada pakhhi'
print(person)

# to runn loop to print key and values
for key, values in person.items():
    print(key, values)

# for k, v in enumerate(['tic', 'tac', 'toe']):
#     print(k, v)

# to delete 
del person['age']
print(person)