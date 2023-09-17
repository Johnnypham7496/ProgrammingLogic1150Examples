"""
Check to see if a user's password is long enough
"""

password = input('Please enter your password to check if it is long enough: ')

passwqord_min_length = 8 # Passwords must be at least 8 characters

if len(password) < passwqord_min_length:
    print('Sorry, your password is not long enough, it must be at least 8 characters')
else:
    print('Well done, your password if long enough')