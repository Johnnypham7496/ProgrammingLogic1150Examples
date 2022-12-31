def codes(class_codes):
    if class_codes < 2000 or class_codes <= 1000:
        return print('You are a first year')
    else:
        return print('You are a second year')


def main():
    class_codes = int(input('Enter your four-digit class code: '))
    grade = codes(class_codes)
    print(grade)



main()