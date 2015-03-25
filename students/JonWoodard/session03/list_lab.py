#!/usr/bin/python

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
new_fruit = raw_input("Please enter a new fruit-->")
fruit.append(new_fruit)
print(fruit)
fruit_number = int(raw_input("Please enter a number-->"))
# need to loop this until a suitable value is entered
# this does not seem to work - asks all the time
# if IndexError:
#     fruit_number = int(raw_input("Try a smaller number-->"))
print(fruit_number, fruit[fruit_number - 1])
fruit = ["Pomegranites"] + fruit
print(fruit)
fruit.insert(0, "Pineapples")
print(fruit)
for item in fruit:
    if item[0] == "P":
        print(item)

print(fruit)
fruit.pop(-1)
print(fruit)
remove_fruit = raw_input("Which fruit would you like to remove? -->")
fruit.remove(remove_fruit)

