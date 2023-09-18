""" Play rock - paper - scissors against a computer """

# rock paper scissors if else thing
# this allows python to use code to do things like choosing a random option or number
import random

# this line will have the computer choose randomly for rock paper scissors
computer_choice = random.choice(['rock', 'paper', 'scissors'])
# human choice
human_choice = input('Enter "rock", "paper" or "scissors": ')
if human_choice != 'rock' and human_choice != 'paper' and human_choice != 'scissors':
    print('You can only pick one. Game Over')

else:
    print('The computer chooses ' + computer_choice)
# situations where the human and computer tie
    if human_choice == computer_choice:
        print('You both chose ' + human_choice + ' so the game is tied.')
    elif human_choice == 'rock' and computer_choice == 'scissors':
        print('Rock bests scissors. You win!')
    elif human_choice == 'scissors' and computer_choice == 'paper':
        print('Scissors beat paper. You win!')
    elif human_choice == 'paper' and computer_choice == 'rock':
        print('Paper beat rock. You win!')

    else:
        print('Sorry, ' + computer_choice + ' beats ' + human_choice + '. Computer wins.')