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
