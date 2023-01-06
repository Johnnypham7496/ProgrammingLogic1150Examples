# dictionary of country codes and full names
# dictionaries, unlike lists, are unordered can store keys: value paris
# always have curly brackets instead of regular
# connect the key and values with colon and comma to separate them like lists
# first part is a key and second part is value
# keys must be unique and there cannot be 2 of the same keys in a dictionary
# if the key is already in the dictionary, the existing value WILL BE OVERWRITTEN when modifying data

"""country_codes = {
    'CN': 'China',
    'FR': 'France',
    'MX': 'Mexico',
}"""

scores = {'Al': 9, 'Bettina': 7, 'Cody': 6, 'Dora':10}
al_score = scores['Al']
print(al_score)

dora_score = scores['Dora']
print(dora_score)
# value in dictionaries can be modified
scores['Cody'] = 8
print(scores)

# can also add existing new data to existing data

# dictionaries can have any type of data paired: strings, floats, and int
# more dictionary examples
# dictionaries can also be lists or other dictionaries
"""paint_colors = {
    'Kitchen': 'blue',
    'Living Room': 'green',
    'Bedroom': 'purple',
    'Bathroom': 'blue',
}

class_codes = {
    1100: 'IT Concepts',
    1150: 'Programming Logic',
    1310: 'PC Maintenance',
    1425: 'Data Communication',
               
}

rainfall_by_month = {
    'March': 1.4,
    'April': 2.5,
    'May': 0.5,
    'June': 3.1,
    'July': 2.8,
    'August': 1.0,
    'September': 0.2,
    'October': 1.9
    
# dictionary with lists for values  
quiz_score = {
    'Al': [8, 9, 5],
    'Bettina': [6, 10, 10],
    'Cody': [7, 7, 9]

# dictionary with another dictionary for value 
book = {
    'Title': 'Automate the Boring Stuff',
    'Author': 'Al Swiegart',
    'Price': 0.00,
    'Quantity': 10,
    'Year': 2018
}"""

# you can add another key value to the existing dictionary with variable(key) = value
game_and_publishers = {'Minecraft': 'Mojang', 'Overwatch': 'Blizzard', 'Fortnight': 'Epic'}
print(game_and_publishers)
game_and_publishers['Super Mario'] = 'Nintendo'
print(game_and_publishers)


