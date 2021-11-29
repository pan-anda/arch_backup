magicians = ['alice', 'tom', 'david']
for magician in magicians:
    print(magician)


magicians = ['alice', 'tom', 'david']
for magician in magicians:
    print("Thank you " + magician.title() +".")

print("it's a very good show.")


for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)


even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)



squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


#4.3.4
squares = [value**2 for value in range(1,11)]
print(squares)

#4.4
simpsons = ['homer', 'marge', 'bart','lisa', 'maggie']
print(simpsons[2:5])
print(simpsons[-3:])


simpsons = ['homer', 'marge', 'bart','lisa', 'maggie']

print("here are the first three members in the Simpsons:")
for simpson in simpsons[:3]:
    print(simpson.title())


my_fruits = ['apple', 'banana', 'pear']
friend_fruits = my_fruits[:]

my_fruits.append('mango')
friend_fruits.append('pineapple')

print("I like:")
print(my_fruits)

print("She likes:")
print(friend_fruits)

#4.5
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (400,100)
print(dimensions[0])
print(dimensions[1])


dimensions = (10,20,30,40,50,60)
for dimension in dimensions:
    print(dimension)






























