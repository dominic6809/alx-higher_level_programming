#!/usr/bin/python3

def remove_char_at(s, n):
    """
    Create a copy of the string with the character at position n removed.

    Args:
        s (str): The input string.
        n (int): The index of the character to be removed.

    Returns:
        str: modified str with char at position n removed
    """
    # Check if the index is valid
    if n < 0 or n >= len(s):
        return s  # If index is out of range, return the original string

    # Create new str by concat the substr before and after the char at index n
    return s[:n] + s[n+1:]
