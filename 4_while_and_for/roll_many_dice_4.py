import random

# Ask the user how many dice to roll
number_of_dice = int(input('How many dice to roll? '))

# Using variables instead of the number 5 makes it easier to reuse
# and then if you need to roll 3 or 10 dice, you just need to
# change the variable value once, instead of changing the number everywhere
print(f'About to roll {number_of_dice} dice...')

for dice in range(number_of_dice):
    dice_value = random.randint(1, 6)
    print(f'Dice {dice + 1} value is {dice_value}')