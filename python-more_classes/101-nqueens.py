#!/usr/bin/python3
"""Module that solves the N queens puzzle using backtracking."""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col) without conflict.

    Args:
        board (list): current placement, board[i] = column of queen in row i.
        row (int): row index to check.
        col (int): column index to check.

    Returns:
        bool: True if placing a queen here is safe, False otherwise.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row, board, solutions):
    """Recursively place queens row by row, collecting all solutions.

    Args:
        n (int): size of the board.
        row (int): current row being processed.
        board (list): current partial placement of queens.
        solutions (list): accumulator for all valid solutions found.
    """
    if row == n:
        solutions.append(list(board))
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve(n, row + 1, board, solutions)
            board.pop()


def main():
    """Parse arguments, validate them, and print all N queens solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(n, 0, [], solutions)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    main()
