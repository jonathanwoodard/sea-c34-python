# create a dictionary and print it
dict_1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict_1)
dict_1.pop('cake')
print(dict_1)
dict_1['fruit'] = 'Mango'
print(dict_1)
keys = dict_1.keys()
print(keys)
values = dict_1.values()
print(values)
'cake' in dict_1
'Mango' in values


# section 2: create lists from 1-15 in base 10 and hex
list_1 = []
list_2 = []
for int in range(16):
    list_1.append(int)
    list_2.append(hex(int))
dict_2 = dict(zip(list_1, list_2))
print(dict_2)



