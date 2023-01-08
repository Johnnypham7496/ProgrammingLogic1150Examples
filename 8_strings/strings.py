# print variable but calling out a specific spot within the string textx`
# first letter/spot always starts with 0
phone = 'Android'
print(phone[3])
print(phone[5])

for letter in phone:
    #    for x in enumerate(phone):
    print(letter, end="")

"""# there are considered as escape characters
print('Macy\'s is a department store')
print('One line\nAnother line')
print('There is a tab \t here')
print('Your file is in C:\\Users\\documents.doc')
"""
print()
print()
# for case-sensitive comparison, it is better to have the strings to be the same case before comparing
message = 'hello world'
print(message.upper())
email = 'USER@MINNESPOLIS.COM'
print(email.lower())

print()
print('Quiz program!')
print('What number system do computers use?')
answer = input('What is your answer?: ')
# by adding lower() to the answer variable, this converts the user input to lower for it statement comparison
# saves the time from having to manually change the characters yourself. Same thing applies to upper()
if answer.lower() == 'binary':
    print('That is correct!')
else:
    print('That is not correct. The correct answer is Binary')

print()
name = input('What is your name?: ')
if 'e' in name.lower():
    print('There is an \'e\' in your name')
else:
    print('There is no \'e\' in your name')

print()
email = input('What is you email?: ')
# endswith() functions will check the last part of the string to verify if - email ends with edu example
if email.endswith('.edu'):
    print('This is a student email')
else:
    print('This is not a student')

print()
# the in and out statements will be considered a boolean variable checking if the statement is true or false
# in and out inside a string is case-sensitive
hello = ('Hello' in 'Hello world')
print(hello)
print()
# there a re multiple different functions methods that can help with verifying a user input


class_code = input('Enter your class code: ')
while True:
    if class_code.upper().startswith('ITEC'):
        if len(class_code) == 9:
            print(f'You class is {class_code.upper()}')
        break

    else:
        print('The class code you entered is incorrect')
        class_code = input('Enter your class code: ')

hours_worked = {
    'Monday': 4.3,
    'Tuesday': 12,
    'Wednesday': 11.6,
    'Thursday': 3,
    'Friday': 9,
}

# table heading
print(f'{"Day":<15}{"Hours Worked":<15}')
for day, hours in hours_worked.items():
    print(f'{day:<15}{hours:<15}')

email = 'ab1234cd@go.minneapolis.edu'
# splitting the email variable string and turning into a list with splitting point "@" then printing the first list item
split_email = email.split('@')
print(f'Your Star ID is {split_email[0].upper()}')
