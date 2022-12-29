# variables
example_class_code = 'itec 1234'
uppercase_class_code = ''

for letter in example_class_code:
    # ord is a function that returns the number that represents the UNICODE of a letter
    # unicode is a computer language that all computers understand. what?????????????

    # converting letter to unicode value
    character_code = ord(letter)
    # see if the letters are lowercase letters by seeing if the return code is between 97 or 122
    # allegedly the simpler version to write the code below is 97 <= character_code <= 122
    if character_code >= 97 and character_code <= 122:
        # subtracting 32 will give you the unicode for the uppercase letter
        uppercase_character_code = character_code - 32
        # convert the unicode into a character
        # chr function stands for character and job is to get the character that represents the unicode
        uppercase_letter = chr(uppercase_character_code)
        # append to the output string
        uppercase_class_code = uppercase_class_code + uppercase_letter
    # not a lowercase letter. append it to the output string
    else:
        uppercase_class_code + letter
    print(f'The class code in uppercase is {uppercase_class_code}')


# you're telling me people do this everytime when they need to write something uppcase wth