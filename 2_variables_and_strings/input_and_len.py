"""" Combining input and lengths - how long is the user's name? """


name = input('Please enter your name: ')
print(f'Hello, {name}')

name_length = len(name)
print(f'Your name is {name_length} letters long')