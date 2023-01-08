"""When requesting the program to create a new directory, the program sees that the 'quotes' directory already exits"""
import os
"""'try' will try making the directory and if it exists then the program does nothing except printing the 
following statement"""
try:
    os.makedirs('quotes')
except FileExistsError:
    print('The quotes directory already exists.')
