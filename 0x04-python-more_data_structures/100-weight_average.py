#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0

    # Calculate the weighted sum and total weight
    weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    # Calculate and return the weighted average
    return weighted_sum / total_weight
