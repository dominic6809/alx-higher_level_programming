#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: tuple containing addition of corresponding elements
    """
    # Extract first and second elements from each tuple
    a_first = tuple_a[0] if len(tuple_a) >= 1 else 0
    a_second = tuple_a[1] if len(tuple_a) >= 2 else 0
    b_first = tuple_b[0] if len(tuple_b) >= 1 else 0
    b_second = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Perform add of corresponding elements and return the result as a tuple
    return (a_first + b_first, a_second + b_second)
