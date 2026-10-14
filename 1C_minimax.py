"""
Experiment 1C - Minimax Algorithm
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement the MINIMAX algorithm (here: choosing the best move for
    player X in a Tic-Tac-Toe position).

Run:
    python 1C_minimax.py

Scores: X wins = +1, O wins = -1, draw = 0.
X is the maximising player, O is the minimising player.

NOTE: The example board below is the one given in the lab manual. It already
contains a complete X diagonal (top-left, centre, bottom-right), so the game
is over and every move scores the same; the search simply returns the first
empty square. Replace `board` with a game that is still in progress to see
Minimax choose between moves (see the commented example in main).

Output for the manual's board:
    Current Board:
    X O X
    O X .
    . O X
    Game is already won by X; the move below is not meaningful.
    Best Move: (1, 2)

    Board after best move:
    X O X
    O X X
    . O X
"""

PLAYER_X = 1    # Maximising player
PLAYER_O = -1   # Minimising player
EMPTY = 0


def evaluate(board):
    """Return +1 if X has three in a row, -1 if O has, otherwise 0."""
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return 0


def is_moves_left(board):
    """Return True if at least one square is empty."""
    return any(cell == EMPTY for row in board for cell in row)


def minimax(board, is_max):
    """Return the value of `board` assuming both players play optimally."""
    score = evaluate(board)
    if score == PLAYER_X or score == PLAYER_O:  # Someone has won
        return score
    if not is_moves_left(board):                # Draw
        return 0

    if is_max:                                  # X's turn: pick the largest value
        best = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    best = max(best, minimax(board, False))
                    board[row][col] = EMPTY     # Undo the move
        return best
    else:                                       # O's turn: pick the smallest value
        best = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    best = min(best, minimax(board, True))
                    board[row][col] = EMPTY
        return best


def find_best_move(board):
    """Try every empty square for X and return the best (row, col)."""
    best_val = -float("inf")
    best_move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                move_val = minimax(board, False)   # O replies next
                board[row][col] = EMPTY
                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val
    return best_move


def print_board(board):
    """Print the board using X, O and '.'."""
    for row in board:
        print(" ".join("X" if x == PLAYER_X else "O" if x == PLAYER_O else "." for x in row))


if __name__ == "__main__":
    # Example position from the lab manual
    board = [
        [PLAYER_X, PLAYER_O, PLAYER_X],
        [PLAYER_O, PLAYER_X, EMPTY],
        [EMPTY,    PLAYER_O, PLAYER_X],
    ]
    # A position still in progress (uncomment to try it instead):
    # board = [
    #     [PLAYER_X, PLAYER_O, EMPTY],
    #     [EMPTY,    PLAYER_X, EMPTY],
    #     [PLAYER_O, EMPTY,    EMPTY],
    # ]

    print("Current Board:")
    print_board(board)

    if evaluate(board) != 0:
        winner = "X" if evaluate(board) == PLAYER_X else "O"
        print(f"Game is already won by {winner}; the move below is not meaningful.")

    move = find_best_move(board)
    print(f"Best Move: {move}")

    board[move[0]][move[1]] = PLAYER_X
    print("\nBoard after best move:")
    print_board(board)
