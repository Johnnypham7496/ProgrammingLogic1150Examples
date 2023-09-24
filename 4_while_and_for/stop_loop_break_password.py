"""
Enter password. Stop loop using break if password is correct
"""


secret_password = 'kittens'


while True:
    password = input('Please enter your password: ')
    if secret_password == password:
        break 
    else: 
        print('Error - wrong password. Try again.')

# The only way to end the loop above is if the password is correct.
print('Welcome, authorized user')