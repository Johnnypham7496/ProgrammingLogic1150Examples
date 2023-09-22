"""
Printing a word in a square, both vertically and horizontally.
"""


name = input('Please enter your name: ')

print('Your name, horizontal square')
for letter in range(len(name)):
    print(name)


print('You name, vertical square')
for letter in name:
    line = ''
    for count in range(len(name)):
        line = line + letter
    print(line)


print('Your name, vertical square, alternative method')
for letter in name:
    line = letter * len(name)
    print(line)


print('You name, as a triangle')
counter = 1
for letter in name:
    line = ''
    for count in range(counter):
        line += letter
    print(line)
    counter = counter + 1