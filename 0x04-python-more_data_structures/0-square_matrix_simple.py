#!/usr/bin/python3
# Function to compute the square value of all integers in a matrix
def square_matrix_simple(matrix=[]):
    # Check if the matrix is not None
    if matrix is not None:
        # Create a new matrix to store squared values
        new_matrix = []
        # Iterate over each row in the matrix
        for row in matrix:
            squared_row = list(map(lambda x: x**2, row))
            # Append the squared row to the new matrix
            new_matrix.append(squared_row)
        return new_matrix
    return None
