def codes(class_codes):
    # if else determining whether the class codes is in between the numbers
    for number in range(1000, 2000):
        # trying to create a statement where it makes the user enter in at least 4 digits numbers: unsuccessful
        if len(class_codes) != 4:
            if 1000 <= class_codes < 2000:
                # return function is user is a first year
                return print('You are a first year')
            else:
                # return function if user is a second year
                return print('You are a second year')
        else:
            return print('Class codes are 4 digit numbers')


def main():
    # variable
    class_codes = int(input('Enter your four-digit class code: '))
    # calling to codes function
    codes(class_codes)
    # original: output after calling function print()
    # no need for output in main because the function itself has an output with the return of if else statements


main()