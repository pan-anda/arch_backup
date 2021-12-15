filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  #readline() only show one line

pi_string = ''
for line in lines:
    pi_string += line.rstrip()     #line.strip() delete <space> among digits

print(pi_string)
print(len(pi_string))






