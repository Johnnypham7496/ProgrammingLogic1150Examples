# dictionaries like lists can be looped
colleges = {
    'Minneapolis College': '1501 Hennepin Avenue, Minneapolis',
    'Metro State': '100 E 7th St, St. Paul',
    'Saint Paul College': '235 Marshall Avenue, St. Paul',
    'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park',
    'Century College': '3300 Century Avenue N, White Bear Lake'
}
# can get a value key from a dictionary with using square brackets []
# an error will occur if the value does nto exist
metro_state_address = colleges['Metro State']
print(metro_state_address)

metro_state_address = colleges.get('North Hennepin Community College')
print(metro_state_address)

for college in colleges:
    print(college)

minneapolis_address = colleges.get('Saint Paul College')
if minneapolis_address:
    print(f'Saint Paul\'s College address is {minneapolis_address}')
else:
    print(f'Saint Paul College address not found')

# get() function is good to use to find keys and will not cause an error if key is not found
# get() will return nothing if there is no key found


"""classes = {
    1150: 'Programming Logic',
    1425: 'Data Communications',
    1310: 'PC Maintenance'
}# this will print the keys
for class_code in classes:
    print(class_code)
# this will print the value by using value function
for class_name in classes.values():
    print(class_name)
# this calls for both the key and value to be put into a statement
for class_code, class_name in classes.items():
    print(f'ITEC {class_code} is {class_name}')"""