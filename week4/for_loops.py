# for loop statement, will start counting from 0 first (argument - 1)
for number in range(11):
    print(number)

print()
print("Here are the numbers 7 through 14")
# can have different ranges depending on what's entered in the range function.
# range() is a function useful for a task that needs to be repeated a number of times
for number in range(7, 14):
    print(number)

print()
import random
# range() rolled the dice 5 times and printed the value. random.randint lets the computer pick from 1 through 6
for dice in range(5):
    dice_value = random.randint(1,6)
    print(dice_value)