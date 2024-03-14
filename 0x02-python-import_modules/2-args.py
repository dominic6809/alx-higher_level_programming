#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Calculate the number of arguments provided
    num_arguments = len(sys.argv) - 1

    # Print the appropriate message based on the number of arguments
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    # Print each argument along with its index
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
