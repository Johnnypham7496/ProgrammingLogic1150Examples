"""
Generate random numbers for the user
Emulate rolling a dice, until user wants to quit
"""
import secrets

want_to_quit = ''


while not want_to_quit:
    dice_value = secrets.SystemRandom().randint(1, 6)
    print(f'You rolled a {dice_value}')
    # Not typing anything and pressing enter will set want_to_quit to an empty string
    want_to_quit = input('Press enter to roll again, any other key to quit ')
