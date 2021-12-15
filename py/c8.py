def greet_user():
    """show simple greetings"""
    print("hello")

greet_user()


def greet_user(username):
    """show simple greetings"""
    print("hello, " + username.title() + ".")

greet_user('sarah')

#8.2.1
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willy')
describe_pet(animal_type='cat', pet_name='sarah')

#8.2.3
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='doggie')
describe_pet('doggie')

#8.3.1
def get_formateed_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formateed_name('jimi', 'hengrix')
print(musician)

#8.3.2
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('harry', 'porter')
print(musician) 

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician) 

#8.3.3
def build_person(first_name, last_name, age=''):

    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person 

musician = build_person('doglas', 'cage', age=28)
print(musician) 



































































