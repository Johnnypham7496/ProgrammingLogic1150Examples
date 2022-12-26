# get the name
name = input('Please enter your name: ')
secret_password = 'kittens' # super top secret password
# get the password
password = input('Please enter your password: ')
if password == secret_password:
    print('Welcome, ' + name)

else:
    print('Sorry, wrong password.')

read_syllabus = input('Enter Y if you have read the syllabus for the class: ')
if read_syllabus != 'Y':
    print('Please read the syllabus carefully, there is important info in it. Thanks!')

else:
    print('Awesome. You are caught up for week 1')