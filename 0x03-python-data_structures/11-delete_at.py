#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the item to be deleted.

    Returns:
        list: The modified list with the item at the specified position deleted
              or the same list if idx is negative or out of range.
    """
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list  # If so, return the original list without modification

    return my_list[:idx] + my_list[idx + 1:]
