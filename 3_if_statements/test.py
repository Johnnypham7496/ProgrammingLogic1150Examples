# and/or/nesting statements
# request inputs for weight and age for eligibility to be a blood donor
weight = float(input('Please enter your weight: '))
age = float(input('Please enter your age: '))
# if else statements for blood donor eligibility
if weight >= 110 and age >= 16:
    print('Great! You are eligible to be a blood donor!')
else:
    print('Sorry, you are not eligible to be a blood donor.')

# or statement to check eligibility for taking apple mobile dev class
csharp = input('Have ou taken a C# programming class? If so type "yes": ')
java = input('Have you taken a Java programming class? If so type "yes": ')

if csharp == 'yes' or java == 'yes':
    print('You can take the Apple Mobile Development class')
else:
    print('You must take either C# or Java before you can take Apple Mobile Development')

# temperature
temperature = float(input('Enter the temperature in Fahrenheit: '))

if temperature <= 32:
    print('It is below freezing. Watch out for ice.')
# nesting if statements
    snowing = input('Enter "Y" or "N" is it is snowing today: ')
    if snowing == 'Y':
        print('Snow boots are recommended today!')
    elif snowing == 'N':
        print('Be sure to bundle up!')

else:
    print("It's above freezing today.")