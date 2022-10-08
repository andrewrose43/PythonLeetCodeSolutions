from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        # Cache tuples for fast access later, using for-each loops, which are Python's fastest loops
        tuple_1_9_s = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        tuple_0_8_i = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        tuple_0_2_i = (0, 1, 2)

        # Sets in which to register which digits are already present in each row, column, and box
        rows_digits = tuple(set() for _ in tuple_0_8_i)
        cols_digits = tuple(set() for _ in tuple_0_8_i)
        boxes_digits = tuple(tuple(set() for _ in tuple_0_2_i) for _ in tuple_0_2_i)

        def _register(row, col, s):
            """Note that a digit has been added to the board."""
            rows_digits[row].add(s)
            cols_digits[col].add(s)
            boxes_digits[row // 3][col // 3].add(s)

        def _unregister(row, col, s):
            """Note that a digit has been removed from the board."""
            rows_digits[row].remove(s)
            cols_digits[col].remove(s)
            boxes_digits[row // 3][col // 3].remove(s)

        def _placeable(row, col, s):
            """Return a boolean tracking whether s can be placed at the given coordinates."""
            return \
                s not in rows_digits[row] \
                and s not in cols_digits[col] \
                and s not in boxes_digits[row // 3][col // 3]

        def _backtrack(row, col):
            """Attempt to add a digit to the board."""

            # Solution found!
            if row > 8:
                return True

            # Only operate on empty cells
            if board[row][col] == '.':
                for s in tuple_1_9_s:
                    if _placeable(row, col, s):
                        _register(row, col, s)
                        board[row][col] = s
                        if _backtrack(row + 1 if col == 8 else row, (col + 1) % 9):
                            return True
                        _unregister(row, col, s)
                # Reset the board
                board[row][col] = '.'
                return False
            return _backtrack(row + 1 if col == 8 else row, (col + 1) % 9)

        # Register the pre-existing contents of the board
        for row in tuple_0_8_i:
            for col in tuple_0_8_i:
                if board[row][col] != '.':
                    _register(row, col, board[row][col])

        _backtrack(0, 0)
