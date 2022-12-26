# user input nuber of credits they are taking the semester
number_of_credits = int(input('Please enter how many credits you are taking this semester: '))

# if else and elif statements to determine full-time student or not
if number_of_credits >= 12:
    print('You are a full-time student')
elif number_of_credits >= 6:
    print('You are part-time student')
else:
    print('You are less than part-time student')

# grading quiz score and giving a grade
quiz_score = float(input('Please enter the quiz score, out of 100: '))

# if else statement to determine grace level based on quiz score
if quiz_score >= 90:
    print('Your letter grade is A')

elif quiz_score >= 80:
    print('Your letter grade is B')

elif quiz_score >= 70:
    print('Your letter grade is C')

else:
    print('You failed the test')