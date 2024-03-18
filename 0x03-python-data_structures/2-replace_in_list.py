#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element in the list at the specified index.

    Args:
        my_list (list): The list to modify.
        idx (int): The index where the element will be replaced.
        element: The new element to insert.

    Returns:
        list: modified list if idx is valid, otherwise returns original list
    """
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Replace the element at the specified index
    my_list[idx] = element
    return my_list
