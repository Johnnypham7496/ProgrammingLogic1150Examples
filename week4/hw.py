"""import random

want_to_quit = ''     # empty strings are considered false

while not want_to_quit:
    dice_value = random.randint(1, 6)
    dice_value_number_two = random.randint(1, 6)
    print(f'You rolled a {dice_value}, {dice_value_number_two}')
    # not typing anything and pressing enter will set want_to_quit to an empty string
    want_to_quit = input('Press enter to roll again, any other key to quit')"""

""" capital_wisconsin = input('What is the capital of Wisconsin?: ')
while not capital_wisconsin == 'Madison':
    print(f'That is not correct!')
    capital_wisconsin = input('What is the capital of Wisconsin?: ')

else:
    print(f'That is correct!') """

"""number_of_books = int(input('How many books did you buy?: '))
total = 0
for book in range(number_of_books):
    book_price = float(input('Enter the price of the book: $'))
    if book_price == 0:
        print('Nice you got a free book!')

    total = total + book_price

print(f'The total price for all {number_of_books} books is ${total:.2f}')"""


number_of_semester = int(input('How many semesters did you teach Programming Logic this year?: '))
total = 0
for semester in range(number_of_semester):
    students_per_semester = int(input('How many students registered for Programming Logic this semester?: '))

    total = total + students_per_semester
print(f'The total number of students that registered for Programming Logic {total}')

total = total / 4
print(f'The average numbers of students registers is {total}')