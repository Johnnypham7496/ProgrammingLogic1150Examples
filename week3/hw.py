# pennies = int(input('How many pennies do you have?: '))
# dollars = (pennies // 100)
# if pennies < 100:
#    print(f'You have {pennies} pennies.')
# elif pennies == 100:
#    print(f'You have ${dollars}')
# elif pennies > 100:
#    print(f'You have ${dollars} dollars')


senator_age = int(input('How old are you?: '))
citizen_duration = int(input('How many years have you lived in the United States?: '))
inhabitants = input('Do you have inhabitants within the state to help represent? Enter yes or no: ')
if senator_age < 30:
    print('You must be at least 30 years old to be a senator.')

    if citizen_duration < 9:
        print('You have to have lived in the United States for 9 years to qualify.')
    else:
        print()

    if inhabitants == 'no':
        print('You need inhabitants of the state to help represent you.')
    else:
        print()
else:
    print('You are qualified to be a senator!')