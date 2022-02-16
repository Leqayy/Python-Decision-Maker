import random

number = random.randrange(1, 3)


thing1 = input("what is the first thing you want to decide on: ")
thing2 = input("what is the second thing you want to decide on: ")

result = number
if result == 1:
    print("your result is " + thing1)
elif result == 2:
    print("your result is " + thing2)
