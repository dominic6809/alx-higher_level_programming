#!/usr/bin/python3
"""
matrix multiply module using numpy
"""


import numpy as np


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
    # Validate m_a
    for row in m_a:
        for obj in row:
            if (not isinstance(obj, int) and not isinstance(obj, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[0]) != len(row):
                raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    for row in m_b:
        for obj in row:
            if (not isinstance(obj, int) and not isinstance(obj, float)):
                raise TypeError("m_b should contain only integers or floats")
            if len(m_b[0]) != len(row):
                raise TypeError("each row of m_b must be of the same size")

    """if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    """
    A = np.asmatrix(m_a)
    B = np.asmatrix(m_b)
    C = A.dot(B)
    return C
