#!/usr/bin/python3
"""
Defines matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """
    function to Multiply two matrices.

    params:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
        not a rectangle, or contains non-integer/float elements.
        ValueError: If m_a or m_b is empty or can't be multiplied.
    """
    # Validate m_a
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    # Validate m_b
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(val, int) or isinstance(val, float))
               for val in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(val, int) or isinstance(val, float))
               for val in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_r = []
        for c in range(len(m_b)):
            new_r.append(m_b[c][r])
        inverted_b.append(new_r)

    new_matrix = []
    for row in m_a:
        new_r = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_r.append(prod)
        new_matrix.append(new_r)

    return new_matrix
