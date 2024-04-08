#!/usr/bin/python3
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

def solve_n_queens_util(board, row, R):
    """
    function to solve the N queens problem recursively.

    params:
        board (list): The current state of the chessboard.
        row (int): The current row to place the queen.
        R (int): The size of the chessboard.
    """
    if row == R:
        # Print the board
        for i in range(R):
            for j in range(R):
                print("Q", end=" ") if board[i][j] == 1 else print(".", end=" ")
            print()
        print()
        return

    for col in range(R):
        if is_safe(board, row, col, R):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, R)
            board[row][col] = 0

def solve_n_queens(R):
    """
    Solve the N queens problem.

    params:
        R (int): The size of the chessboard.
    """
    if not isinstance(R, int):
        print("N must be a number")
        sys.exit(1)

    if R < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(R)] for _ in range(R)]
    solve_n_queens_util(board, 0, R)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        R = int(sys.argv[1])
        solve_n_queens(R)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
