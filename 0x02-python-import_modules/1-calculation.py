#!/usr/bin/python3

# Import functions from calculator_1 module
from calculator_1 import add, sub, mul, div

# Check if this script is run directly
if __name__ == "__main__":
    # Define variables 'a' and 'b'
    a = 10
    b = 5
    # Perform arithmetic operations and print results
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
