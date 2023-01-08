def main():
    # user input credits count data
    credit_count = int(input('Please enter the amount of credits this semester: '))
    # loop if user enters an invalid number of credits by calling credits_valid function to validate
    while not credits_valid(credit_count):
        print('This is not the a valid number of credits.')
        credit_count = int(input('Please enter the amount of credits this semester, between 0 and 24: '))
    # calling for full_time_part_time function to confirm what type of student this is
    status_message = full_time_part_time(credit_count)
    # output
    print(f'You status is a {status_message} student.')


# function that checks to see if the int enter is between 0 and 24 otherwise return as False
def credits_valid(credit_count):
    if credit_count < 0 or credit_count > 24:
        return False
    else:
        return True


# function to determine what tye of students this is with if statement
def full_time_part_time(credit_count):
    if credit_count >= 12:
        return 'full time'
    elif credit_count >= 6:
        return 'part time'
    else:
        return 'less than part time'


main()


# indentation and spacing is important if wanting the code to run properly