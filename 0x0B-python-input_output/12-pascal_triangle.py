#!/usr/bin/python3
"""
function to define a Pascal's Triangle function.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    params:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    # Initialize a list to store the rows of Pascal's triangle
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)  # The first and last numbers are always 1
            else:
                above_row = triangle[i - 1]
                value = above_row[j - 1] + above_row[j]
                row.append(value)
        triangle.append(row)

    return triangle
