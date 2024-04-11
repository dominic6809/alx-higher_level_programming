#!/usr/bin/python3
"""
matrix multiply module using numpy
"""


def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul function
    params:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.
    Returns:
        numpy.ndarray: Result of matrix multiplication"""

    import numpy as np

    """if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if (len(m_a) == 0 or len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if (len(m_b) == 0 or len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")"""

    # validate m_a
    for row in m_a:
        for val in row:
            if (not isinstance(val, int) and not isinstance(val, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[0]) != len(row):
                raise TypeError("each row of m_a must be of the same size")

    # validate m_b
    for row in m_b:
        for val in row:
            if (not isinstance(val, int) and not isinstance(val, float)):
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
