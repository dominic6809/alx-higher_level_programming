#!/usr/bin/python3

# Import arithmetic functions from calculator_1 module
from calculator_1 import add, sub, mul, div

# Import argv from sys module
from sys import argv


# Define function to perform arithmetic calculations
def calculate(a, operator, b):
    # Check the operator and perform the corresponding operation
    if operator == "+":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
    else:
        # Print error message if operator is not recognized
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


# Main function
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    else:
        # Convert command-line arguments to integers
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])

        # Call calculate function with provided arguments
        calculate(a, operator, b)
