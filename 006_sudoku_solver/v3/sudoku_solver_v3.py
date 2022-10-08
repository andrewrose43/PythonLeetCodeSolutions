from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        # Cache the digits in string form for fast access.
        # Python's fastest loop is the for-each, so this enables maximum speed later.
        tuple_1_9_s = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

        def _placeable(row, col, s):
            """Returns whether s could be placed at board[row][col]."""
            # Get the row and column of the top-left cell of each 3x3 box
            box_row = row - (row % 3)
            box_col = col - (col % 3)
            # Credit to LeetCode user ShaneTsui for this clever use of any().
            return not (
                    any(s == cell for cell in board[row])
                    or any(s == cell for cell in list(zip(*board))[col])
                    or any(s == cell for row in board[box_row: box_row + 3] for cell in row[box_col: box_col + 3]))

        def _backtrack(row, col):
            """Tries out all possible candidates to place at board[row][col], or moves on if board[row][col] is '.'. Returns True when a solution is completed."""

            # Solution found!
            if row > 8:
                return True

            # If cell is already full, move on
            if board[row][col] != '.':
                return _backtrack(row + 1 if col == 8 else row, (col + 1) % 9)

            for s in tuple_1_9_s:
                # If s can be placed in this cell
                if _placeable(row, col, s):
                    # Place the digit on the board
                    board[row][col] = s
                    if _backtrack(row + 1 if col == 8 else row, (col + 1) % 9):
                        return True
            # No candidate works; undo the last placement and return False
            board[row][col] = '.'
            return False

        # Get the party started
        _backtrack(0, 0)
