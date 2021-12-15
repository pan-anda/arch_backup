"""
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I just love it.\n")
"""

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love using it.\n")
    file_object.write("I love going deep into it.\n")









