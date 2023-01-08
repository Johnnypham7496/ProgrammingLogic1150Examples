# variable for list
winter_months = ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May']
# empty dictionary for values
snowfall = {}
# for loop to par the entered values to the keys of the original list
for months in winter_months:
    snow = float(input(f'How many inches of snow in {months}: '))
    snowfall[months] = snow

print()
print(f'Here is all of the data you entered: ')
# printing the key and values and turning them into a string
for months, snow in snowfall.items():
    print(f'In {months}, there was {snow} inches of snow')
# adding all the number the values from the keys of months
total_snow = sum(snowfall.values())
# counting the number of list items in the list
months = len(snowfall)
"""calculate the average amount of snow per month by taking the sum of the entered value in the list divided by the
number of months"""
average = total_snow / months
# prints the sum total of snow per how many months there are
print(f'The total amount of snow in {months} month is {total_snow} inches')
print(f'The average amount of snow per month is {average:.2f} inches')