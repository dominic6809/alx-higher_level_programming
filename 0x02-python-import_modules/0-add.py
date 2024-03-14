#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    """
    Assigning the add function from add_0 module to the local namespace
    Checking if the script is executed directly
    Prints the result of two added numbers
    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
