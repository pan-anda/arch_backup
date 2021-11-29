fruits = ['apple', 'banana', 'pear', 'orange']
print(fruits)
print(fruits[2].title())

message = "I love " + fruits[-1].title() + "."
print(message)

fruits[0] = 'dragon fruit'
print(fruits)

fruits.append('pineapple')
print(fruits) 

fruits.insert(2, 'mellon')
print(fruits)

del fruits[1]
print(fruits)


fruits = []

fruits.append('water mellon')
fruits.append('straberry')
fruits.append('blueberry')

print(fruits)

#pop()
fruits = ['apple', 'banana', 'pear', 'orange']

popped_fruit = fruits.pop()
print(fruits)
print(popped_fruit)


motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print("first owned moto is " + first_owned + ".")  
print(motorcycles)


fruits = ['apple', 'banana', 'pear', 'orange']

fruits.remove('banana')
print(fruits)


fruits = ['apple', 'banana', 'pear', 'orange']
print(fruits) 

too_sweet = 'banana'
fruits.remove(too_sweet)
print(fruits)
print("\nThe " + too_sweet + "is to sweet for me.")

#3.3
cars = ['yamaha', 'suzuki', 'bwm', 'toyota']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


print("\n") 
cars = ['yamaha', 'suzuki', 'bwm', 'toyota']
cars.reverse()
print(cars)

print("\n") 
print(len(cars))
