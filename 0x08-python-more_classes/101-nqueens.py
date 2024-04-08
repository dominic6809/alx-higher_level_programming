#!/usr/bin/python3
"""
Nqueens class module
"""


import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at position on the board.

    params:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
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
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(N):
    """
    Solve the N queens problem.

    params:
        n (int): The size of the chessboard.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []


def solve(board, row):
    """
    function to solve the N queens problem recursively.

    params:
        board (list): The current state of the chessboard.
        row (int): The current row to place the queen.
        N (int): The size of the chessboard.
    """
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
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
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(N)
