#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    :param my_list: List of elements to print (default empty list)
    :param x: Number of elements to print (default 0)
    :return: The real number of elements printed
    """
    try:
        count = 0
        for num in my_list:
            if count < x:
                print(num, end=" ")
                count += 1

        print()
    except TypeError:
        break:
            return count
