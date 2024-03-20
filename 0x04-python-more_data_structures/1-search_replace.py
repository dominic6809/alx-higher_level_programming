#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list using list comprehension with ternary operator
    new = list(map(lambda x: replace if x == search else x, my_list))
    return (new)
