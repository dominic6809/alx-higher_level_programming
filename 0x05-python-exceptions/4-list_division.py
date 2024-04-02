#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element two lists.

    :param my_list_1: First list
    :param my_list_2: Second list
    :param list_length: Length of the resulting list
    :return: A new list with all divisions
    """
    result = []
    for num in range(list_length):
        try:
            result.append(my_list_1[num] / my_list_2[num])
        except (TypeError, ZeroDivisionError, IndexError) as error:
            if isinstance(error, ZeroDivisionError):
                print("division by 0")
            elif isinstance(error, IndexError):
                print("out of range")
            elif isinstance(error, TypeError):
                print("wrong type")
            result.append(0)
    return result
