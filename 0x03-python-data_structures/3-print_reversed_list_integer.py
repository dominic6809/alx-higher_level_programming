def print_reversed_list_integer(input_list=[]):
    """
    Prints all integers of a list in reverse order.

    Args:
        input_list (list): The list of integers.
    """
    # Check if the input list is not empty
    if input_list:
        # Iterate over the list in reverse order
        for num in reversed(input_list):
            # Print each integer using the specified format
            print('{:d}'.format(num))
