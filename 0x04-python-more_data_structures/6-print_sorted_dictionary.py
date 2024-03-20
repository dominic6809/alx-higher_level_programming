#!/usr/bin/python3

# Function to print a dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys
    for key in sorted_keys:
        # Print key-value pairs
        print("{}: {}".format(key, a_dictionary[key]))
