#!/usr/bin/python

fruit = ["apples", "pears", "oranges", "peaches"]
print(fruit)
new_fruit = raw_input("Please enter a new fruit-->")
fruit.append(new_fruit)
print(fruit)
fruit_number = int(raw_input("Please enter a number-->"))
# need to loop this until a suitable value is entered
# this does not seem to work
# if IndexError:
#     fruit_number = int(raw_input("Try a smaller number-->"))
print(fruit_number, fruit[fruit_number - 1])
fruit = ["pomegranites"] + fruit
print(fruit)
fruit.insert(0, "pineapples")
print(fruit)
