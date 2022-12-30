def greeting(name):
    message = f'Hello {name}!'
    return message


def main():
    username = 'Zoe'
    hello_message = greeting(username)
    print(hello_message)


main()



print()
def rectangle_area(height, width):
    area = height * width
    return area

def main():
    rectangle_height = float(input('Enter the height of the rectangle: '))
    rectangle_width = float(input('Enter the width of the rectangle: '))
    rectangle_area = rectangle_area(rectangle_height, rectangle_width)

    print(f'The are of the rectangle is {rectangle_area}')


main()