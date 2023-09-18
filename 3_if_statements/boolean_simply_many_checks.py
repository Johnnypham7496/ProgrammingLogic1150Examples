""" Program to decide what activity and what clothes to wear based on the season. """

month = input('What month is it?: ').lower()

# Create a boolean variable to represent if it is summer or not.
# We'll say summer is June, July, or August.

if month == 'june' or month == 'july' or month == 'august':
    is_summer = True
else:
    is_summer = False

    
# Now we know if it is summer or not, based on the value of the is_summer boolean variable
# So if we need to make a decision based on summer or not, we can use the is_summer variable
# instead of having to check if month is 'June' or 'July' or 'August'


# Let's decide what type of hat to wear
if is_summer == True:
    print(f'Let\'s wear a hat!')
else:
    print(f'It\'s not summer. Wear a warm hat!')


# what if we need to make another decision based on summer or not?
if is_summer:
    print(f'It\'s summer! You can go swimming.')
else:
    print(f'It\'s not summer. You can go skiing.')