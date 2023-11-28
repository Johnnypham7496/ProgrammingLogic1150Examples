import secrets

for dice in range(5):
    dice_value = secrets.SystemRandom().randint(1, 6)
    print(dice_value)
