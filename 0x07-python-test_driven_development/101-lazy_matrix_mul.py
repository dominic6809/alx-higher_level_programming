#!/usr/bin/python3
"""
matrix multiply module using numpy
"""


def lazy_matrix_mul(m_a, m_b):
    """
    function to Multiply two matrices using NumPy.

    params:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: Result of matrix multiplication.

    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is not a rectangle.
        TypeError: If either m_a or m_b contains non-integer/float elements
        ValueError: If m_a or m_b is empty or can't be multiplied.
    """
    import numpy as np

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or
        not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")

    # Check if m_a and m_b are non-empty
    if not m_a or not m_b:
        raise ValueError("m_a and m_b cannot be empty")

    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    # Check if number of columns in m_a matches number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    A = np.asmatrix(m_a)
    B = np.asmatrix(m_b)
    C = A.dot(B)
    return C
