# get data about the items sold from the user
item_name = input('Enter name of the item: ')
# convert numerical data to the correct type
unit_price = float(input('Enter unit price of ' + item_name + ': $'))
items_sold = int(input('Enter quantity of ' + item_name + ' sold: '))
# calculate the total for all items sold
total = unit_price * items_sold
# adjusting format to have the total prices list have 2 digits after the decimal
format_float = "{:.2f}".format(float)
float = total
format_float_unit_price = "{:.2f}".format(unit_price)
float_unit_price = unit_price
# print out invoice data
print()  # print a bsank line
print(item_name + ' Sales')
print('Quantity Sold: ' + str(items_sold))
print('Unit price:  $' + str(format_float_unit_price))
print('Total:       $' + str(format_float))


