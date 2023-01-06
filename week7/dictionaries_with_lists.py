quiz_scores = {
    'Al': [8, 9, 0],
    'Bettina': [6, 10, 10],
    'Cody': [7, 7, 9]
}
# for loop will loop through all keys and values
for students, list_of_scores in quiz_scores.items():
    print(f'Student {students} scores are {list_of_scores}')

# calling the key 'Cody' to attach the value to cody_scores variable
cody_scores = quiz_scores['Cody']
# for loop to print out cody's scores line by line
# when listing the numbered spot in the list always use '+1' so it doesn't start counting from 0
for i, score in enumerate(cody_scores):
    print(f'On quiz {i + 1} Cody scored {score}')

# max() will pick the max scores from the list
cody_max = max(cody_scores)
print(f'Cody\'s best score was {cody_max}')