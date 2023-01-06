"""def greeting(name):
    message = f'Hello {name}!!!'
    return message


def main():
    username = 'Johnny'
    hello_message = greeting(username).upper()
    print(hello_message)


main()"""

"""def main():
    moon_landing = int(input('What year did Apollo 11 land on the moon?: '))
    who_painted = input('Who painted the Mona Lisa? :')
    landing_answer(moon_landing)
    artist(who_painted)

def artist(painter):
    if painter == 'Leonardo Da Vinci':
        print('Correct')
    else:
        print('That is incorrect. The answer is Leonardo Da Vinci')

def landing_answer(landing):
    if landing == 1969:
        print('Correct')
    else:
        print('That is incorrect. The answer is 1969')

main()"""

def main():
    computer_memory = int(input('How many gigabytes of memory does your computer have?: '))
    processor_speed = float(input('What is the current speed of you processor?: '))
    operating_system = input('What is the name of your current OS?: ')
    upgrade = specs_check(computer_memory, processor_speed, operating_system)
    print(upgrade)

def specs_check(ram, ps, os):
    if ram >= 1:
        return 'You meet the minimum requirements to upgrade to Windows 10'
    elif ps >= 1:
        return 'You meet the minimum requirements to upgrade to Windows 10'

    elif os == 'Windows 8' or 'Windows 7':
        return 'You meet the minimum requirements to upgrade to Windows 10'

    else:
        return 'You do not meet the minimum requirements to upgrade your computer.'


main()