import random


def main():
    guest_list = []

    while True:
        names = input('Please enter the names of the guests. When you are finished press the enter key: ')
        if names:
            if names in guest_list:
                print('You already added that to your list')
            else:
                guest_list.append(names)
        else:
            break

        for number, names in enumerate(guest_list):
            print(number, names)

    while True:
        response = input('Are there any names you want to delete? Type yes or press enter: ')
        if response == 'yes':
            remove_name = input('What name would you like to remove?: ')
            if remove_name in guest_list:
                guest_list.remove(remove_name)
                print(f'{remove_name} deleted from the list')
            else:
                print('Name not found')
        else:
            break

        for number, names in enumerate(guest_list):
            print(number, names)

    prize = pick_prizes(guest_list)
    total_number_of_guests = len(guest_list)
    print(f'The total number of guests is {total_number_of_guests}')

    for number, names in enumerate(guest_list):
        print(number, names)
    print(prize)


def pick_prizes(guest_list):
    prize = ['Gopro', 'Ps5', '3090 Ti', 'Roomba', 'Car', 'Motorcycle']
    random_prize = random.choice(prize)
    winner = random.choice(guest_list)
    prize_counter = int(input('How many prizes should there be?: '))

    return f'{winner} has won a {random_prize}'


main()
