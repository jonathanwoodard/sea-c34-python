#!/usr/bin/python
# section 1

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
new_fruit = raw_input("Please enter a new fruit-->")
fruit.append(new_fruit)
print(fruit)
fruit_number = int(raw_input("Please enter a number-->"))
# need to loop this until a suitable value is entered
# this only asks once
if fruit_number > len(fruit):
    fruit_number = int(raw_input("Try a smaller number-->"))
else:
    print(fruit_number, fruit[fruit_number - 1])
fruit = ["Pomegranites"] + fruit
print(fruit)
fruit.insert(0, "Pineapples")
print(fruit)
for item in fruit:
    if item[0] == "P":
        print(item)

# section 2

print(fruit)
fruit.pop(-1)
print(fruit)
fruit_2 = fruit * 2
remove_fruit = raw_input("Which fruit would you like to remove? -->")
if remove_fruit not in fruit_2:
    print("We don't have that fruit, try again")
    remove_fruit = raw_input("Which fruit would you like to remove? -->")
while remove_fruit in fruit_2:
    fruit_2.remove(remove_fruit)
print(fruit_2)

# section 3

for item in fruit:
    like_fruit = raw_input("Do you like " + item.lower + "? -->")
    while like_fruit != "yes" or "no":
        print('Please answer "yes" or "no"')
        like_fruit = raw_input("Do you like " + item.lower + "? -->")
    if like_fruit == "no":
        fruit.remove(item)
print(fruit)

# section 4

fruit_copy = fruit[:]
for item in fruit_copy:
    item.reverse
fruit.pop(-1)
print(fruit, fruit_copy)

# if __name__ == "__main__":
# add some assert statements to test
