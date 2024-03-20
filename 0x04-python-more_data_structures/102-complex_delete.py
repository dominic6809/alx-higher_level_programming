#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a list of keys from the dictionary
    keys_to_delete = list(a_dictionary.keys())

    # Iterate over the keys to delete
    for key in keys_to_delete:
        # Check if the value of the current key matches the specified value
        if value == a_dictionary.get(key):
            # Delete the key-value pair from the dictionary
            del a_dictionary[key]

    return a_dictionary
