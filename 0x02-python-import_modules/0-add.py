#!/usr/bin/python3
# Assigning the add function from add_0 module to the local namespace
from add_0 import add
# Checking if the script is executed directly
if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
