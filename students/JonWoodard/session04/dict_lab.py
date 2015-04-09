#!/usr/bin/python
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
print(dict_1)


# section 2: create lists from 1-15 in base 10 and hex
list_1 = []
list_2 = []
for int in range(16):
    list_1.append(int)
    list_2.append(hex(int))
dict_2 = dict(zip(list_1, list_2))
print(dict_2)

# section 3: create a new dictionary from 1, replace values with number of 'a's
count_a = []
for item in values:
    count_a.append(item.count('a'))

dict_3 = dict(zip(keys, count_a))
print(dict_3)


# section 4: create sets of numbers divisible by 2,3,4
s2 = set()
s3 = set()
s4 = set()
for int in range(21):
    if int % 2 == 0:
        s2.add(int)
    if int % 3 == 0:
        s3.add(int)
    if int % 4 == 0:
        s4.add(int)
print(s2)
print(s3)
print(s4)

print(s3 <= s2)
print(s4 <= s2)


# section 5: create sets from strings
s5 = set('Python')
s5.add('i')
fs1 = frozenset('marathon')
s5.union(fs1)
print(s5.intersection(fs1))
