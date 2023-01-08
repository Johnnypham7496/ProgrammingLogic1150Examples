import random

import states as states

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

capital_items = list(capitals.items())

for quiz_number in range(35):
    quiz_file = open('capitals_quiz.txt'(quiz_number + 1), 'w')
    answer_key = open('capitals_quiz_answer.txt'(quiz_number + 1), 'w')

    quiz_file.write(f'Name:\n\n Date:\n\n Period:\n\n')
    quiz_file.write(f'State Capital Quiz Form\'s {quiz_number + 1}')
    quiz_file.write('\n\n')

states = list(capitals.keys())
random.shuffle(states)

for question_number in range(50):
    correct_answers = capitals[states[question_number]]
    wrong_answer = list(capitals.values())
    del wrong_answer[wrong_answer.index(correct_answers)]
    wrong_answer = random.sample(wrong_answer, 3)

    answer_options = wrong_answer + [correct_answers]
    random.shuffle(answer_options)

    quiz_file.write(f'What is the capital of {question_number + 1, states[question_number]}')
    for i in range(4):
        quiz_file.write(f'ABCD{i}, {answer_options}\n')
    quiz_file.write('\n')

    answer_key.write(f'{question_number + 1}ABCD{answer_options.idex[correct_answers]}')

    quiz_file.close()
    answer_key.close()
