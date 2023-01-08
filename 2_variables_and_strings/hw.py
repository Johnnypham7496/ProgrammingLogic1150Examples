# name =  input('What is you name?: ')
# credits = input('How many credits are you taking this semester?: ')
# print(f'{name} is taking {credits} credits this semester')

number_of_times_traveled = int(input('How many times have you rde the bus last month?: '))
cost = float(input('What is the cost of one bus ride?: '))
total_cost_last_month = number_of_times_traveled * cost
print(f'You have rode the bus {number_of_times_traveled} times last month, the cost for each bus ride is {cost},'
      f'and the total cost you spent last month is {total_cost_last_month:.2f}')