a = []
for i in range(100):
    if (i % 3 == 0 and i % 5 == 0):
        a.append("FizzBuzz")
    elif (i % 3 == 0):
        a.append("Fizz")
    elif (i % 5 == 0):
        a.append("Buzz")
    else:
        a.append(i)

print(a)