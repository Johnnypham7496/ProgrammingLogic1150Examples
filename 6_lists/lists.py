# always starts counting at 0 not 1
# a list of strings
villians = ['Voldemort', 'Darth Vader', 'Sauron']

# a list of in numbers
numbers = [10, 9, 10, 8]

# a list of float numbers
rainfall = [0.8, 1.1, 1.3, 2.1, 0.6, 0.2, 7.6]

# a mixture of data types
mixture = ['Hello', 100, 5.55]                     # not very useful tho

# a lists of lists
lists_of_lists = [['a', 'b', 'c']], [['x', 'y', 'z']]


my_classes = ['Programming Logic', 'Info Tech Skills', 'Data Communications']

my_first_class = my_classes[0]
my_second_class = my_classes[1]
my_third_class = my_classes[2]
# lists can be changed partway through


# you can add an if statement to determine full-time or part-time students or other scenarios
credits_per_class = [3, 2, 2, 4]
total = 0

for credits in credits_per_class:
    total = total + credits
print(f'The total number of credits is {total}')

if total >= 12:
    print('You are a full-time student')
elif total >= 6:
    print('You are part-time student')
else:
    print('You are less than part-time student')



# you can add up all the total sum of numbers in a list
credits_per_class = [3, 2, 2, 4]
total = sum(credits_per_class)
print(f'The total number of credits is {total}.')


# can also rearrange lists to be alphabetical order
colleges = ['Minneapolis College',
            'Metro State',
            'Saint Paul College',
            'North Hennepin Community College',
            'Century College']
# this is the function to arrange lists in alphabetical order
# colleges.sort()

# this function reverse the lists from bottom to top
colleges.reverse

# for loop to print the list 1 string at a time instead of all under 1 line
for college in colleges:
    print(college)

zero = [0] * 100
print(zero)