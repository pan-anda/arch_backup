alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'red'
alien_0['points'] = 10

print(alien_0)

alien_0 = {'color':'green'}
alien_0 = {'color':'yellow'}
print("the alien now is " + alien_0['color'])

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("original x-postion: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

#6.2.5
alien_0 = {'color':'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#6.2.6
fav_lang = {
    'jen':'python',
    'sarah':'c',
    'ben':'java',
    'bill':'ruby',
    }

print("Sarah's favorite language is " + 
    fav_lang['sarah'].title() + 
    ".")

for name, language in fav_lang.items():
    print(name.title() + "'s fav lang is " + language.title())



#6.3.1
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

#6.3.2
print("\n")
fav_lang = {
    'jen':'python',
    'sarah':'c',
    'ben':'java',
    'bill':'ruby',
    }

for name in fav_lang.keys():
    print(name.title())



print("\n")
fav_lang = {
    'jen':'python',
    'sarah':'c',
    'ben':'java',
    'bill':'ruby',
    }

friends = ['bill', 'sarah']
for name in fav_lang.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
                ", I see your fav lang is " + 
                fav_lang[name].title() + ".")


print("\n")
fav_lang = {
    'jen':'python',
    'sarah':'c',
    'ben':'java',
    'bill':'ruby',
    }

if 'erin' not in fav_lang.keys():
    print("Erin, please take the poll.")





















