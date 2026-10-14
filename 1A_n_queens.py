"""
Experiment 1A - Eight Queens Problem
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement the Eight Queens problem using backtracking.

Run:
    python 1A_n_queens.py

Example output (first solution found by the search):
    One of the possible solutions is:
    Q . . . . . . .
    . . . . Q . . .
    . . . . . . . Q
    . . . . . Q . .
    . . Q . . . . .
    . . . . . . Q .
    . Q . . . . . .
    . . . Q . . . .
"""

N = 8  # Size of the chessboard (N x N) and number of queens


def print_solution(board):
    """Print the board: 'Q' marks a queen, '.' an empty square."""
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


def is_safe(board, row, col):
    """Return True if a queen can be placed at board[row][col].

    Queens are placed one row at a time, so only the rows above need checking.
    """
    # Same column
    for i in range(row):
        if board[i][col]:
            return False

    # Upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    # Upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False

    return True


def solve(board, row):
    """Place queens row by row using backtracking.

    Returns True as soon as ONE complete solution is found.
    (The lab-manual version kept searching and printed all 92 solutions,
    which did not match its "One of the possible solutions" message.)
    """
    if row == N:  # All N queens placed
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1          # Place queen
            if solve(board, row + 1):    # Try to place the rest
                return True
            board[row][col] = 0          # Backtrack (remove queen)
    return False


def eight_queens():
    """Create an empty board, solve it and print the result."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve(board, 0):
        print("One of the possible solutions is:")
        print_solution(board)
    else:
        print("Solution does not exist")


if __name__ == "__main__":
    eight_queens()
