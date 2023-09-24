import random

game_over = False

while not game_over:
    print('The computer will flip a coin. Guess heads or tails')
    guess = input('Enter "H" for heads and "T" for tails: ').upper()

    coin_flip = random.choice(['H', 'T'])

    print(f'The coin flipped a {coin_flip}')

    if coin_flip != guess:
        print('Game over')
        game_over = True
    else:
        print('You guessed right! Try again...')


print('Thanks for playing')