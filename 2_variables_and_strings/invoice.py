""" Program that get a string, int, and float from the user, then does math processing and prints the results, converting the numbers to a string """


# get data about the items sold from the user
item_name = input('Enter name of the item: ')
# convert numerical data to the correct type
unit_price = float(input('Enter unit price of ' + item_name + ': $ '))
items_sold = int(input('Enter quantity of ' + item_name + ' sold: '))
# calculate the total for all items sold
total = unit_price * items_sold
# originally I had created a separate string to add the 2 decimal places but now the code has been change to format strings instead to make it cleaner and easier
# print out invoice data
print()  # print a bsank line
print(item_name + ' Sales')
print(f'Quantity Sold: {items_sold}')
print(f'Unite price:   {unit_price:.2f}')
print(f'Total:         {total:.2f}')


