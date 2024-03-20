#!/usr/bin/python3
# Function to find the key with the highest value in a dictionary
def best_score(a_dictionary):
    # Check if the dictionary is not empty
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    # Return None if the dictionary is empty
    return None
