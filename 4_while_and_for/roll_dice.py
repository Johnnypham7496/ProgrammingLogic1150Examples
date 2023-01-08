import random

want_to_quit = ''     # empty strings are considered false

while not want_to_quit:
    dice_value = random.randint(1, 6)
    print(f'You rolled a {dice_value}')
    # not typing anything and pressing enter will set want_to_quit to an empty string
    want_to_quit = input('Press enter to roll again, any other key to quit')