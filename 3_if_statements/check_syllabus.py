""" Using != operator to see if a student has read the syllabus yet """

read_syllabus = input(f'Enter Y if you read the syllabus for the class: ').lower()

if read_syllabus != 'y':
    print('Please read the syllabus for the class carefully, there is important info on it. Thanks!')