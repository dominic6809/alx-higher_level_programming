#!/usr/bin/python3
"""
Nqueens class module
"""


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position on the board.

    params:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the same diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_nqueens(N, board, row=0):
    """
    Solve the N queens problem.

    Args:
        n (int): The size of the chessboard.
    """
    if row == N:
        # Found a solution, print it
        print([[i, board[i]] for i in range(N)])
        return

<<<<<<< HEAD
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n)
            board[row][col] = 0


def solve_n_queens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0, n)

=======
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row+1)
>>>>>>> refs/remotes/origin/master

if __name__ == "__main__":
    # Check the command-line arguments
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

    board = [-1] * N
    solve_nqueens(N, board)
