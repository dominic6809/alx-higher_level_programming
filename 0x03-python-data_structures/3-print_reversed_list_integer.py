#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list in reverse order.

    Args:
        my_list (list): The list of integers.
    """
    # Iterate over the list in reverse order
    for num in range(len(my_list) - 1, -1, -1):
        print("{0:d}".format(my_list[num]))
