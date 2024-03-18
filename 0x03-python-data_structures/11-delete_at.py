#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the item to be deleted.

    Returns:
        list: The modified list with the item at the specified position deleted
    """
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list

    del my_list[idx]
    return my_list
