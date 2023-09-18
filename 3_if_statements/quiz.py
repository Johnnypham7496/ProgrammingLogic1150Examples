"""
Quiz program. Asks the user a question, and checks if their answer is correct
"""


print('Quiz program!')

# user input answer
answer = input('What is the capital of Wisconsin: ').lower() # answer is Madison
# if else statements
if answer == 'madison':
    print("That's Correct!")

else:
    print("Sorry, the answer is Madison!")