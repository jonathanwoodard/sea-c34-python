food_prefs = {"name": u"Jon",
              u"city": u"Seattle",
              u"cake": u"german chocolate",
              u"fruit": u"mango",
              u"salad": u"caprese",
              u"pasta": u"ravioli"}

new_string = (
    u"{name} is from {city}, and he likes {cake} cake, {fruit}s, "
    u"{salad} salad and {pasta}.").format(**food_prefs)

print(new_string)


list_of_numbers = [num for num in range(16)]
hex_list = [hex(num) for num in list_of_numbers]
hex_dict = dict(zip(list_of_numbers, hex_list))
print(hex_dict)

hex_dict_2 = {num: hex(num) for num in range(16)}

hex_dict_a = {key: hex_dict[key].count('a') for key in hex_dict}

s2 = {n for n in range(21) if n % 2 == 0}
s3 = {n for n in range(21) if n % 3 == 0}
s4 = {n for n in range(21) if n % 4 == 0}


def make_s(x, y=range(21)):
    s_x = {n for n in y if n % x == 0}
    print(s_x)
