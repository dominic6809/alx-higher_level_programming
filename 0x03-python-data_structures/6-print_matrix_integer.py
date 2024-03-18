#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists): The matrix to be printed.
    """
    # Check if the matrix is not empty
    if matrix:
        # Iterate over each row in the matrix
        for row in range(len(matrix)):
            # Check if the current row is not empty
            if matrix[row]:
                # Iterate over each element in the row
                for col in range(len(matrix[row])):
                    # Check if it's not the last element in the row
                    if col != (len(matrix[row]) - 1):
                        # Print the element followed by a space
                        print("{:d}".format(matrix[row][col]), end=" ")
                    else:
                        # Print the last element followed by a newline
                        print("{:d}".format(matrix[row][col]), end="\n")
            else:
                # Print an empty line for an empty row
                print("")
