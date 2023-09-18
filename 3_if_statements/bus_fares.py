"""
A program to calculate a bus fare.
On a city bus, the fare depends on your age.

Children 5 and younger ride free.
Children 6-16 pay $0.50
Adults, 16 and over pay $2
Seniors 65 and over pay $1.

This program uses if, elif and else to decide the correct fare based on a user's age.

"""


age = int(input(f'Please enter your age as a whole number: '))

if age <= 5:
    print(f'The bus fare for passengers 5 and under is $0.00')

elif age <= 16:
    print(f'The bus fare for passeengers between 6 and 16 is $0.50')

elif age <= 65:
    print(f'The bus fare for passengers over 16 but younger than 65 is $2.00')

else:
    print(f'The bus fare for passeengers older than 65 is $1.00')