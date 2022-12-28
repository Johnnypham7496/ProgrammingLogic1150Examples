# try to print a name horizontally, vertically, triangle
name = 'Johnny'
for letter in name:
    print(letter)

print()
square_size = 10
square_character = 'Johnny'

for y in range(square_size):
    line = ''
    for x in range(square_size):
        line = line + square_character
        print(line)
