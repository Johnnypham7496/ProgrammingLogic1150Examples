# dictionary of country codes and full names
# dictionaries, unlike lists, are unordered can store keys: value paris
# dictionaries can have any type of data paired: strings, floats, and int
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
