# alien_0 = {'color': 'green', 'points' : 5}
# # print(alien_0['color'])
# # print(alien_0['points'])
# print(alien_0)

# # new_points = alien_0['points']
# # print(f'You jast erned {new_points} points!')

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

#_______________________________________________________________________
#Empty dictionary

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# __________________________________________________________________________
#Change dictionary

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alian is now {alien_0['color']}.")

#_______________________________________________________________

# отслеживание позиции пришельца, который может двигаться с разной скоростью

# alien_0 = {'x_position':0, 'y_position':25, 'speed': 'medium'}

# print(f"original position:{alien_0['x_position']}")

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

#_________________________________________________________________

# Удаление пар «ключ-значение»

# alien_0 = {'color':'green', 'points' : 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)


# _____________________________________________________________________
# Словарь с однотипными объектами

# favorite_languages = {
#     'jen' : 'python',
#     'sara' : 'c',
#     'edward' : 'ryby',
#     'phil': 'python',
#      }

# language = favorite_languages['edward'].title()
# print(f"favorite language {language}")

# person_1 = {'first_name': 'Aliaksandr' ,
#             'last_name': 'Katlou',
#             'age': 4,
#             'city': 'Minsk',
#             }
# print(person_1['last_name'])
# ______________________________________________________

# Перебор словаря

# user_0 = {
#     'username':'eferni',
#     'first': 'enrico',
#     'last': 'fermi',
#      }
# for key , value in user_0.items():
    # print(f"\nKey: {key}")
    # print(f"Value: {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#      'phil': 'python',
#     }
# for name, language in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite language is {language.title()}.")

#     Result

# Jen's favorite language is Python.

# Sarah's favorite language is C.

# Edward's favorite language is Ruby.

# Phil's favorite language is Python.
#____________________________________________________________-


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#      'phil': 'python',
#     }
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()},I see you love {language}!")


#         Jen
# Sarah
#         Sarah,I see you love C!
# Edward
# Phil
#         Phil,I see you love Python!

#________________________________________________________
# Проверка

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#      'phil': 'python',
#     }
# if 'erin' not in favorite_languages.keys():
#     print('Erin , pleas take our poll!')

# _______________________________________________________

#Перебор ключей словаря в определенном порядке ---  sorted()

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# for name in sorted(favorite_languages.keys()):
#     print(f"\n{name.title()}, thank you taking the poll.")

#_______________________________________________________________
#Если вас прежде всего интересуют значения


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# print('The following languages have been mentioned:')
# for language in favorite_languages.values():
#     print(language.title())
# _____________________________________________________________

# Чтобы получить список выбранных элкментов (не повтор) методом set()

# favorite_languages = {
#     'mark':'c',
#     'jon': 'java',
#     'paul': 'php',
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# print('The following languages have been mentioned:')
# for language in set (favorite_languages.values()):
#     print(language.title())
#__________________________________________________________
#     УПРАЖНЕНИЯ

river_word = {'nile': 'egypt',
              'dunai': 'vena',
              'rain': 'swizaland',
              'luar': 'france',
              'taho': 'portugal',
              'ebro': 'spain',
              }
for river in set(river_word.values()):
    print(river.title())