#!/usr/bin/python3
"""
Nqueens class module
"""


import sys


def is_safe(board, row, col, R):
    """
    Checks If addition is safe

    Args:
        row (int): row
        col (int): col
        board (list): board
        R (int): R

    Returns:
        boolean: True if safe False if not
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, R)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(R):
    """
    Recursive function to solve NQueens

    params:
        R (int): R
    """
    if R < 4:
        print("R must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(R)] for _ in range(R)]
    solutions = []


def solve(board, row):
    """
    Add solution to results

    params:
        board (list): board
        row (list): row
    """
    if row == R:
        solutions.append(board[:])
        return
    for col in range(R):
        if is_safe(board, row, col, R):
            board[row][col] = 1
            solve(board, row + 1)
            board[row][col] = 0

    solve(board, 0)

    for solution in solutions:
        for row in solution:
            print(" ".join(["Q" if cell == 1 else "." for cell in row]))
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens R")
        sys.exit(1)

    try:
        R = int(sys.argv[1])
    except ValueError:
        print("R must be a number")
        sys.exit(1)

    if R < 4:
        print("R must be at least 4")
        sys.exit(1)

    solve_n_queens(R)
