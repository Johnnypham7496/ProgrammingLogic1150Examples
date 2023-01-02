def first_or_second_year(class_codes):
    if 1000 <= class_codes < 2000:
        # return function is user is a first year
        return print('You are a first year')
    else:
        # return function if user is a second year
        return print('You are a second year')


def codes_valid(class_codes):
    # if statement to determine
    if class_codes < 1000 or class_codes > 3000:
        return False
    else:
        return True


def main():
    # variable
    class_codes = int(input('Enter your four-digit class code: '))
    # calling to codes_valid function
    while not codes_valid(class_codes):
        print('Class codes are 4 digit numbers')
        # prompts the user to reenter the class code if the return is false
        class_codes = int(input('Enter your four-digit class code, should be a 4 digit number: '))
        # calls to the first_or_second_year function
    first_or_second_year(class_codes)
    # no need for output in main because the function itself has an output with the return of if else statements


main()