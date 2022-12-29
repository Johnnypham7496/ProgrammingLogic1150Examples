# try to print a name horizontally, vertically, triangle
name = 'Johnny'
for letter in name:
    print(letter)

print()
square_size = 10
square_character = input('Enter your name: ')
name_length = len(square_character)
for y in range(square_size):
    line = ''
    for x in range(name_length):
        line = line + square_character
        print(line)

