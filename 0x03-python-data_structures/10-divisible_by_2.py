#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        list: new list with True or False.
    """
    return [True if num % 2 == 0 else False for num in my_list]
