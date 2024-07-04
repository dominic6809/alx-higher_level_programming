#!/usr/bin/python3
"""Module containing the find_peak function."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    A peak is an element that is greater than or equal to its neighbors.
    For elements at the edge of the list, only one neighbor is considered.

    :param list_of_integers: List of unsorted integers
    :return: A peak element
    """
    if not list_of_integers:
        return None

    lw, high = 0, len(list_of_integers) - 1

    while lw < high:
        mid = (lw + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            lw = mid + 1

    return list_of_integers[lw]
