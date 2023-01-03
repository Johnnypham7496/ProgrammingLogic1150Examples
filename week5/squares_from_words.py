def main():

    while user_wants_to_continue('make squares from words'):
        word = input('Please enter the word to print in a square: ')
        word_square(word)

    print('Thanks for using the program!')


def word_square(word):
    for letter in range(len(word)):
        print(word)


def user_wants_to_continue(task):
    response = input(f'Do you want to {task}? Enter "Y" for yes, anything else for no: ')
    if response.upper() == 'Y':
        return True
    return False


main()