# all ariables related to the code
college = 'Minneapolis College'
department = 'ITEC'
sd_program = 'Software Development'
sd_program_credits = 60
sd_student = 291
total_students = 572
# getting the percentage of students that are in the sd program
percent_sd_students = sd_student / total_students * 100

print(f'The {sd_program} in the {department} at {college} requires {sd_program_credits}')
# the percentage has more than 2 decimals places which is why .2f is there to make the percentage more readable
print(f'{percent_sd_students:.2f}% of students in the {department} are in the {sd_program}')
# doing quick math to calculate the remaining students with other majors and writing it in a formatted string
print(f'The {total_students - sd_student} students in the {department} have other majors')

