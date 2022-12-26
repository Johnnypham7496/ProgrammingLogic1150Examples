# user input nuber of credits they are taking the semester
number_of_credits = int(input('Please enter how many credits you are taking this semester: '))

# if else and elif statements to determine full-time student or not
if number_of_credits >= 12:
    print('You are a full-time student')
elif number_of_credits >= 6:
    print('You are part-time student')
else:
    print('You are less than part-time student')