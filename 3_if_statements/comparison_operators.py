""" Examples of using all the comparison operators """

# Using the equals operator to check if a number is equal to another number
book_price = float(input('Enter the price of the textbooks:  '))
if book_price == 0:
    print(f'Cool! Your books are free.')


# Using the equals operator to check if a string is equal to another string
college = input('Enter the college you attend: ').lower()
if college == 'minneapolis college':
    print('Great choice. Glad you are taking classes here at Minnesota College')


# Using the not equals operator != to check if a number is different to another number
answer = int(input('Quiz time. How many cents are in a dollar?: '))
if answer != 100:
    print('Sorry, that is the wrong answer. There are 100 cents in a dollar.')


# Using the not equals operator != to check if a string is different to another string
password = input('Please enter your new password. It cannot be "kittens": ').lower()
if password != 'kittens':
    print('Your new password is accepted.')


# Using the greater than > operator to check if a number is greater (larger) than another number
temperature = float(input('Enter your temperature in Fahrenheit: '))
if temperature > 32:
    print('The temperature is above freezing')


# Using the less than than < operator to check if a number is less (smaller) than another number
students = int(input('There can only be 30 studends in a class. Enter the number of students in class: '))
if students > 30:
    print('There is still room left in the class.')


# Using the greater than or equal to >= operator to check if a number is greater (larger) or equal to another number
age = int(input('To become president of the USA, you must be at least 35 years old. Please enter your age: '))
if age >= 35:
    print('You are old enough to become president')


# Using the less than or equal to <= operator to check if a number is less (smaller) or equal to another number
numbers_of_pennies = int(input('Enter the number of pennies you have: '))
if numbers_of_pennies <= 100:
    print('You have a dollar or less in pennies')