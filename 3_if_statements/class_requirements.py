"""
Using the or operator

Requirements for taking the Apple Mobile Development class is
either C# ("c-sharp") programming, or Java programming, or both.
Ask the user if they have taken C# programming,
Ask the user if they have taken Java programming,
and then print a message if they are eligible to take Apple Mobile Development.
"""


csharp = input("Have you taken C# programming? Type 'yes' if so: ").lower()
java = input("Have you taken Java programming? Type 'yes' if so: ").lower()


if csharp == 'yes' or java == 'yes':
    print('You can take the Apple Mobile Developement class.')
else:
    print('Sorry, you need to take either C# or Java programming before you can take the Apple Mobile Developement class.')