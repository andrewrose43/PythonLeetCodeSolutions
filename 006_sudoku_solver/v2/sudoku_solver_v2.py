from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        # Iterables cached for fast for-each access later.
        # (The for-each is Python's fastest loop.)
        tuple_1_9_s = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        tuple_0_8_i = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        tuple_0_2_i = (0, 1, 2)

        # 9 rows, 9 cols, 9 boxes.
        rows = [set() for _ in tuple_0_8_i]
        cols = [set() for _ in tuple_0_8_i]
        boxes = [[set() for _ in tuple_0_2_i] for _ in tuple_0_2_i]

        def _register(row, col, s):
            """Note that a digit has been added to the board."""
            rows[row].add(s)
            cols[col].add(s)
            boxes[row//3][col//3].add(s)

        def _placeable(row, col, s):
            """Return a boolean tracking whether s can be placed at the given coordinates."""
            return \
                s not in rows[row] \
                and s not in cols[col] \
                and s not in boxes[row//3][col//3]

        def _unregister(row, col, s):
            """Note that a digit has been removed from the board."""
            rows[row].remove(s)
            cols[col].remove(s)
            boxes[row//3][col//3].remove(s)

        def _backtrack(row, col):
            """Attempt to add a digit to the board."""

            # Solution found!
            if row > 8:
                return True

            # If there's a space to fill
            if board[row][col] == '.':
                # For all possible digits
                for s in tuple_1_9_s:
                    if _placeable(row, col, s):
                        board[row][col] = s
                        _register(row, col, s)
                        if _backtrack(row+1 if col == 8 else row, (col+1) % 9):
                            return True
                        _unregister(row, col, s)
                board[row][col] = '.'  # The reset goes here to avoid redundantly doing this multiple times
                return False

            return _backtrack(row+1 if col == 8 else row, (col+1) % 9)

        # Register all the provided digits
        for row in tuple_0_8_i:
            for col in tuple_0_8_i:
                if board[row][col] != '.':
                    _register(row, col, board[row][col])

        _backtrack(0, 0)
