days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
t_shirts_sold = {}
up_arrow = chr(8593)
down_arrow = chr(8595)

for day in days_of_the_week:
    quantity_sold = int(input(f'How many shirts were sold that {day}?: '))
    t_shirts_sold[day] = quantity_sold

print()
print(f'Here is all the data you entered:')

for day, sale in t_shirts_sold.items():
    print(f'{sale} shirts sold on {day}')

total_revenue = sum(t_shirts_sold.values())
day = len(t_shirts_sold)
average = total_revenue / day

print(f'The total shirts that have been sold this week is {total_revenue}. The average shirts sold per day is {average}'
      f'')
for day in range(0, 7):
    if t_shirts_sold[day] == average or t_shirts_sold[day] > average:
        print(f'{days_of_the_week} sales : {t_shirts_sold.values()} {up_arrow}')
    if t_shirts_sold[day] < average:
        print(f'{days_of_the_week} sales : {t_shirts_sold.values()} {down_arrow}')


