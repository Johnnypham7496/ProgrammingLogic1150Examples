"""shelve are similar to dictionaries but data is stored in the value not the keys
shelves store variable data so that it can be used at a later time compared to when running a regualr program and the
data is erased after the program ends"""
import shelve

filename = 'hours_worked.data'
hours_key = 'hours_worked'

shelf = shelve.open(filename)
hours_worked = shelf.get(hours_key)
shelf.close()

if not hours_worked:
    hours_worked = {}

day = input('What day is it?')
hours = float(input('How many hours did you work?: '))

hours_worked[day] = hours
print('Thank you. Here is all of your data: ')

for day, hours in hours_worked.items():
    print(f'On {day}, you worked {hours} hours')

shelf = shelve.open(filename)
hours_worked = shelf.get(hours_key)
shelf.close()