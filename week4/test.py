total = 0
more_books = True

while more_books:
    book_price = float(input('Enter the price of the textbook: '))
    total = total + book_price
    anymore = input('Any more books? Press "Y" for yes or "N" for no: ')
    if anymore == 'N':
        more_books = False

    print(f'The total of all the book is {total}')