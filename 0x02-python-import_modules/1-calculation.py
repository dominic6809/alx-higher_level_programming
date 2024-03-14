#!/usr/bin/python3
# Import functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide
if __name__ == "__main__":
    a = 10
    b = 5
    # Perform calculations and print results
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, subtract(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, muliply(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, divide(a, b)))
