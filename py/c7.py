"""
message = input("I will repeat what you type: ")
print(message)


name = input("Please enter your name: ")
print("Hello, " + name.title())


prompt = "We can personalize your message."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nhello" + name)

#7.1.2
height = input("how tall are you?")
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride.")
else:
    print("\nOh, pity.")


#7.1.3
number = input("enter a number: ")
number = int(number)

if number % 2 == 0:
    print("\nthe number " + str(number) + " is even. ")
else:
    print("odd")


#7.2
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


#7.2.2
prompt = "I will repeat what you enter:"
prompt += "\nEnter 'quit' to end this program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


prompt = "I will repeat what you enter:"
prompt += "\nEnter 'quit' to end this program. "
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)


#7.2.3
prompt = "I will repeat what you enter:"
prompt += "\nEnter 'quit' to end this program. "

active = True
while active:
    message = input(prompt) 

    if message == 'quit':
        active = False
    else:
        print(message)


#7.2.4
prompt = "\nEnter city you have been visited:"
prompt += "\n(Enter 'quit' when finished.) "

while True:
    city = input(prompt)

    if city =='quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


#7.2.5
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number )


#7.2.6
x = 1
while x <= 5:
    print(x)
    x += 1


#7.3
unconfirmed_users = ['alice', 'tom', 'david']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#7.3.2
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
"""


#7.3.3
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("which mountain you would like to climb? ")

    responses[name] = response

    repeat = input("Would you like to let another respond? (yes/no) ")
    if repeat == 'no':
        polling_active =False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + "would you like to climb " + response + ".")

















