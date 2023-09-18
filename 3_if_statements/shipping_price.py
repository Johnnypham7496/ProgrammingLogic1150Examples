"""

A shipping company charges different rates per pound, based on how heavy the package is.

If the package is 10 lbs or less, it will cost $2 per pound
If the package is 20 lbs or less, it will cost $1.50 per pound
If the package is 30 lbs or less, it will cost $1.15 per pound

The company does not ship package that weigh over 30 lbs.

Ask the user for the weight of the package. Print a message with the shipping cost if
it can be shipped, or a message saying the package can't be shipped otherwise.

"""


weight = float(input('Enter the weight of the package, in lbs: '))

if weight > 30:
    print('This package is too heavy to be shipped.')
elif weight <= 0:
    print('Your package can\'negative weight!')
else: 
    if weight <= 10:
        price_per_pound = 2 
    elif weight <= 20:
        price_per_pound = 1.5
    elif weight <= 30:
        price_per_pound = 1.15


shipping_cost = price_per_pound * weight

# added :.2f to only include 2 numbers after the decimal point
print(f'Your {weight} lb package costs ${shipping_cost:.2f} to ship.')