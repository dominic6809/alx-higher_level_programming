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
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    
    # Validate m_b
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    
    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication
    result = []
    for row_a in m_a:
        new_row = []
        for col_b in zip(*m_b):
            element = sum(a * b for a, b in zip(row_a, col_b))
            new_row.append(element)
        result.append(new_row)
    
    return result
