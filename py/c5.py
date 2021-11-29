cars = ['bwm', 'suzuki', 'yamaha', 'toyota']

for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())


print("\n")
cars = 'bwm'

if cars != 'toyota': 
    print("that is not my order")

#5.2.4
print("\n")
age =19

if age <= 18:
    print("You are less than 18 years old.")

# and
age_0 = 18
age_1 = 23

if age_0 >= 18 and age_1 >= 22:
    print("you could get married.")
else:
    print("You are not old enough.")

# or
print("\n")
age_0 = 18
age_1 = 21

if age_0 <18 or age_1 > 22:
    print("you could.")
else:
    print("You could not.")

# in / not in
print("\n")
requested_toppings = ['apple', 'banana', 'pear']

if 'orange' in requested_toppings:
    print("we could order apple")
else:
    print("we run out of it")

# if-elif-else
age = 12

if age < 6:
    print("cost $0")
elif age < 18:
    print("cost $5")
else: 
    print("cost $10")

# more elif
age = 65

if age < 6:
    price = 0
elif age <18:
    price = 5
elif age < 70:
    price = 10
else:
    price = 0

print("cost is $" + str(price) + ".")

#5.3.6
fruits = ['apple', 'banana', 'pear']

if 'apple' in fruits:
    print("you could order apple.")
if 'pear' in fruits:
    print("you could order pear.")
if 'orange' in fruits:
    print ("you could order orange.")

#5.4
print("\n")
requested_toppings =['mushrooms', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    print("adding " + requested_topping + ".")


print("\n")
requested_toppings =['mushrooms', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("we run out of green pepper")
    else:
        print("adding " + requested_topping + ".")

# 5.4.2
print("\n")
requested_toppings =[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print("adding " + requested_topping + ".")
else:
    print("are you sure you want to order?")

# 5.4.3
available_toppings = ["mush", 'olive', 'green pepper', 'extra cheese']

requested_toppings = ['mush', 'french fries', 'extra cheese']

for requested_topping in requested_toppings: 
    if requested_topping in available_toppings:
        print("adding " + requested_topping)
    else:
        print("we run out of " + requested_topping) 














































































