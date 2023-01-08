# converting megabyts to bytes function call
def conversion(megabyte, byte):
    # formula
    conversion_to_byte = megabyte * byte
    # returning back to main function
    return conversion_to_byte

def main():
    # varibles
    byte = 1000000
    # input request for number of bytes
    megabyte = float(input('Enter a number of megabytes: '))
    # calling the conversion function to convert megabytes to bytes
    byte_conversion = conversion(megabyte, byte)
    # output
    # Original output has no commas or specific decimal places to ",.2f" will add the commas and 2 decimal places
    print(f'This {byte_conversion:,.2f} is how many bytes are in a megabyte')


main()