#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces element at specific position without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index where the element will be replaced.
        element: The new element to insert.

    Returns:
        list: newlist with element replaced(idx=valid),or copy of original list
    """
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    # Create a copy of the original list
    new_list = my_list[:]

    # Replace the element at the specified index
    new_list[idx] = element
    return new_list
