# dictionary of country codes and full names
# dictionaries, unlike lists, are unordered can store keys: value paris
# always have curly brackets instead of regular
# connect the key and values with colon and comma to separate them like lists
# first part is a key and second part is value
# keys must be unique

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
}"""