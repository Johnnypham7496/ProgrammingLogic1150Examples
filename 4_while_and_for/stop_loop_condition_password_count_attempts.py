"""
Enter password. Stop loop using a condition if password is correct
User is only allowed 4 attempts to get the password right.
"""


secret_password = 'kitten'
password = input('Please enter your password: ')
attempts = 0


while secret_password != password and attempts < 4:
    print('Error - wrong password. Try again.')
    password = input('Please enter your password: ')
    attempts += 1


# Once the loop has ended, check if the password was entered correctly
if password == secret_password:
    print('Welcome, authorized user.')
else:
    print('Access denied.')