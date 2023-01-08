# open() is opening a text file and 'w' is considered "writing mode"
# use .write to write in the file and \n to create a new line in case there's another text
# when opening a directory or file always be sure to close by using close()
f = open('hello.txt', 'w')
f.write('hello\n')
f.close()

# be careful when opening a file with 'w'
# is the file that's being opened does not exist then it will create one once you run the code
# if the file exists, your current program will overwrite that file and erase all the original contents
planets = open('planets.txt', 'w')
planets.write('Hello Venus\n')
planets.write('Hello Mars\n')
planets.close()
# you can add context into a file by using 'a' = append
planets = open('planets.txt', 'a')
planets.write('Hello Jupiter\n')
planets.write('Hello Saturn\n')
planets.close()
# 'r' will read the context of the txt file and display when program is run
# use for loop to read each line of the text to display line by line
# read() will return all the data in the txt without changing the context
planets = open('planets.txt', 'r')
for line in planets:
    print(line)
planets.close()
print()
# this will read the txt file and create a variable based off the content
planets = open('planets.txt', 'r')
lines = planets.read()
planets.close()

print('All of the lines from the txt file:')
print(lines)

print('All the lines one by  one: ')
for line in lines:
    print(line, end='')
