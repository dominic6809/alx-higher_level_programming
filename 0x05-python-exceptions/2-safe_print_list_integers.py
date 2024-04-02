#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list that are integers.

    :param my_list: List of elements to print (default empty list)
    :param x: Number of elements to access in my_list (default 0)
    :return: The real number of integers printed
    """
    count = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
