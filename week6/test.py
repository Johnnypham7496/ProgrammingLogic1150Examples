def main():
    quiz_scores = [8, 4, 10, 9, 7]
    quiz = int(input('Which quiz did you retake?: '))
    score = int(input('What was your score?: '))
    quiz_scores[quiz-1] = score
    quiz_change('continue changing quiz score')
    print(quiz_scores)



    main()

def quiz_change(task):
    response = input(f'Do you want to {task}? Enter "Y" for yes, anything else for no: ')
    if response.upper() == 'Y':
        return True
    return False

main()