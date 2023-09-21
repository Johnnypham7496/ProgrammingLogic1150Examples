"""
Add up all textbook prices with a for loop
"""


# how many books does the user need to buy
numer_of_books = int(input('How many books to buy?: '))

# Create a variable for the total, set to zero
total = 0 

# Loop needs to repeat once per book
for book in range(numer_of_books):
    book_price = float(input('Enter book price: $'))
    # Price is zero, the book was free. Print a message
    if book_price == 0:
        print('Yay, free book!')

    # Add the latest book price it total 
    total = total + book_price

print(f'The total  price for all {numer_of_books} books is ${total:.2f}')