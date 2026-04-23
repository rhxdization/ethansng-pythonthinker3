import random
num = 48 # random.randint(1,100)
number = int(input("enter a number: "))
if number < num:
    print("your number is too small")
elif number == num:
    print("your number is correct")
else:
    print("your number is too large")