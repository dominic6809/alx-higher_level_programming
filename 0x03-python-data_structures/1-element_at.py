#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return None

    # Initialize a variable to keep track of the current index
    current_idx = 0

    # Iterate through the list
    for item in my_list:
        # If current index matches the given index, return the element
        if current_idx == idx:
            return item
        current_idx += 1

    # If the loop completes without finding the element, return None
    return None
