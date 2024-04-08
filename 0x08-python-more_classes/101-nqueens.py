#!/usr/bin/python3
"""
Nqueens class module
"""


import sys


def is_safe(board, row, col, R):
    """
    Check if it's safe to place a queen at position

    params:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
        R (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False elsewhere.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, R)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, row):
    """
    function to solve the N queens problem recursively.

    params:
        board (list): The current state of the chessboard.
        row (int): The current row to place the queen.
        R (int): The size of the chessboard.
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

def solve_n_queens(R):
    """
    Solve the N queens problem.

    params:
        R (int): The size of the chessboard.
    """
    if R < 4:
        print("R must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(R)] for _ in range(R)]
    solutions = []

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
