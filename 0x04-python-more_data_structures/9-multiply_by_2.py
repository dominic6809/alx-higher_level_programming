#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    multiplied_dict = {}

    for key, value in a_dictionary.items():
        multiplied_dict[key] = value * 2

    # Return the new dictionary with multiplied values
    return multiplied_dict
