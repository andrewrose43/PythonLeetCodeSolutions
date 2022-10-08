from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:

        # Tuples cached for fast access later
        # (the for-each is Python's fastest loop)
        tuple_1_9_s = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        tuple_0_8_i = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        tuple_0_2_i = (0, 1, 2)

        def make_invalid_set(row, col):
            """Returns a set of all numbers which are invalid choices for this cell"""
            invalid_set = set()
            # Note that '.' will be added to invalid_set needlessly but harmlessly; it would be less efficient to avoid
            # doing so
            for i in tuple_0_8_i:
                invalid_set.add(board[row][i])
                invalid_set.add(board[i][col])

            # Now to invalidate contents of the 3x3 box the cell is in
            crude_row = row // 3
            crude_col = col // 3
            # If statements guard against redundant actions
            # "tmp" variables cache to prevent redundant calculations
            for box_row in tuple_0_2_i:
                tmp_row = crude_row * 3 + box_row
                if tmp_row != row:
                    for box_col in tuple_0_2_i:
                        tmp_col = crude_col * 3 + box_col
                        if tmp_col != col:
                            invalid_set.add(board[tmp_row][tmp_col])

            return invalid_set


        def backtrack(row, col):
            """Attempts to fill a cell and move on (or just moves on if the cell is already full)"""

            # If you've filled the board, you're done! Return True
            if row > 8:
                return True

            # If cell is empty
            if board[row][col] == '.':
                # add all non-possibilities to valid_set.
                invalid_set = make_invalid_set(row, col)
                for i in tuple_1_9_s:
                    if i not in invalid_set:
                        board[row][col] = i
                        # We're traversing in row-major order
                        if backtrack(row+1 if col == 8 else row, (col+1) % 9):
                            return True
                # You haven't found a solution, so clear this space
                board[row][col] = '.'
                return False
            # If this line is reached, the cell is already filled, so move on
            if backtrack(row+1 if col == 8 else row, (col+1) % 9):
                return True

        backtrack(0, 0)