"""
if, elif, else Enrollment status at Minneapolis College is defined as the following:

Full time: 12 or more credits
Half time: 6-11 credits
Less than half time: 1-5 credits
"""

number_of_credits = int(input('Please enter a number of credits you are taking this semester: '))
if number_of_credits >= 12:
    print('You are a full-time student')
elif number_of_credits < 12 and number_of_credits > 6:
    print('You are a part-time student')
elif number_of_credits < 6:
    print('You are less than part-time student')