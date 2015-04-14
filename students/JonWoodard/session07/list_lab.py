#!/usr/bin/python
# section 1

master_fruit = ["Apples", "Pears", "Oranges", "Peaches"]


def fruit_1():
    fruit = master_fruit[:]
    print(fruit)
    new_fruit = raw_input("Please enter a new fruit-->")
    new_fruit = new_fruit.capitalize()
    fruit.append(new_fruit)
    print(fruit)
    fruit_number = int(raw_input("Please enter a number-->"))
    # need to loop this until a suitable value is entered
    # this only asks once
    if fruit_number > len(fruit):
        fruit_number = int(raw_input("Try a smaller number-->"))
    else:
        print(fruit_number, fruit[fruit_number - 1])
    fruit = ["Pomegranites"] + (fruit)
    print(fruit)
    fruit.insert(0, "Pineapples")
    print(fruit)
    for item in fruit:
        if item[0] == "P":
            print(item)

# section 2
fruit = master_fruit[:]
print(fruit)
fruit.pop(-1)
print(fruit)
fruit_2 = fruit * 2
remove_fruit = raw_input("Which fruit would you like to remove? -->")
remove_fruit = remove_fruit.capitalize()
if remove_fruit not in fruit_2:
    print("We don't have that fruit, try again")
    remove_fruit = raw_input("Which fruit would you like to remove? -->")
    remove_fruit.capitalize
while remove_fruit in fruit_2:
    fruit_2.remove(remove_fruit)
print(fruit_2)

# section 3

copy = fruit[:]
for item in fruit:
    lower = item.lower()
    question = "Do you like " + str(lower) + "? \n-->"

    like_fruit = raw_input(question)
    while like_fruit != "yes" and like_fruit != "no":
        print('Please answer "yes" or "no"')
        like_fruit = raw_input(question)
    if like_fruit == "no":
        copy.remove(item)
print(copy)

# section 4


def fruit_2():
    fruit_copy = master_fruit[:]
    for item in master_fruit:
        newitem = item[::-1]
        while item in fruit_copy:
            i = fruit_copy.index(item)
            fruit_copy[i] = newitem
    fruit_copy.pop(-1)
    print(master_fruit, fruit_copy)
fruit_2()

# if __name__ == "__main__":
# add some assert statements to test
