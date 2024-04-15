#!/usr/bin/python3
"""
class MyList that inherits from list:
"""


class MyList(list):
    """
    A subclass of list with additional functionality.
    """

    def print_sorted(self):
        """
        Print the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
