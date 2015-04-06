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
