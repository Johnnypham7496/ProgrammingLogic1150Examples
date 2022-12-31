def codes(class_codes):
    # if else determining whether the class codes is in between the numbers
    if class_codes < 2000 or class_codes <= 1000:
        # return function is user is a first year
        return print('You are a first year')
    else:
        # return function if user is a second year
        return print('You are a second year')


def main():
    # variable
    class_codes = int(input('Enter your four-digit class code: '))
    # calling to codes function
    grade = codes(class_codes)
    # output after calling function
    print(grade)



main()