def greeting(name):
    message = f'Hello {name}!'
    return message


def main():
    username = 'Zoe'
    hello_message = greeting(username)
    print(hello_message)


main()


def main():
    print(f'The cubes of the numbers 1 through 10 are: ')
    for number in range(1, 11):
        print_cube(number)


def print_cube(x):
    number_cubed = x**3
    print(f'The cube of {x} is {number_cubed}')

main()


def main():
    string = input('Please enter a string: ')
    repeat = int(input('How many times do you want this string to repeat: '))
    result = string_repeater(string, repeat)
    print(result)


def string_repeater(text, n):
    repeat_string = text * n
    return repeat_string

main()


def is_password_long_enough(password):
    if len(password) >= 8:
        return True
    else:
        return False


def main():
    password = 'kittens'
    print(is_password_long_enough(password))

main()


"""def rectangle_area(rectangle_height, rectangle_width):
    area = rectangle_height * rectangle_width
    return area


def main():
    rectangle_height = float(input('Enter the height of the rectangle: '))
    rectangle_width = float(input('Enter the width of the rectangle: '))
    rectangle_area = rectangle_area(rectangle_height, rectangle_width)

    print(f'The are of the rectangle is {rectangle_area}')


main()"""