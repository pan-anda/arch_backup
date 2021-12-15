"""
print(5/0)


try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by 0.")

#10.3.3.
print("Give me two numbers, I'll divide them.")
print("Enter'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
"""

#10.3.4
print("Give me two numbers, I'll divide them.")
print("Enter'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0.")
    else:
        print(answer)









