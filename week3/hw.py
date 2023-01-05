# pennies = int(input('How many pennies do you have?: '))
# dollars = (pennies // 100)
# if pennies < 100:
#    print(f'You have {pennies} pennies.')
# elif pennies == 100:
#    print(f'You have ${dollars}')
# elif pennies > 100:
#    print(f'You have ${dollars} dollars')

state_represent = input('What state do you want to represent?: ')
senator_age = int(input('How old are you?: '))
citizen_duration = int(input('How many years have you lived in the United States?: '))
inhabitants = input('Do you curretnly live in this state? Enter yes or no: ')
if senator_age <= 30:
    print('You must be at least 30 years old to be a senator.')

    if citizen_duration < 9:
        print('You have to have lived in the United States for 9 years to qualify.')
    else:
        print()

    if inhabitants == 'no':
        print('You need to be an inhabitant of the state to be able to represent it')
    else:
        print()
else:
    print(f'You are qualified to be a senator of {state_represent}')