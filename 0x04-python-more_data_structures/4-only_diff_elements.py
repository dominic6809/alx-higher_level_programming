#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use symmetric difference to find elements present in only one set
    only_diff_set = set_1.symmetric_difference(set_2)
    return only_diff_set
