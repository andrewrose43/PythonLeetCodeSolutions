class Solution:

    def __init__(self):
        self.board = []
        self.size = 0
        self.count = 0

    def totalNQueens(self, n: int) -> int:
        self.board = [[0]*n for _ in range(n)]
        self.size = n  # Cached for speed
        self._nqueens(0)
        tmp = self.count
        self.count = 0
        return tmp

    def _nqueens(self, row: int) -> int:
        for col, overlap in enumerate(self.board[row]):
            if not overlap:  # the square is available
                self._move_queen(row, col, 1)  # Add a queen!
                if row == self.size - 1:
                    self.count += 1  # add 1 to the count if we just put a queen in the last row
                else:
                    self._nqueens(row + 1)
                self._move_queen(row, col, -1)  # Clean up! Get rid of that queen before checking the next column

    def _move_queen(self, row: int, col: int, addsub: int):
        # Add or remove a queen, depending on whether addsub is 1 or -1

        # This loop handles the column and row the queen can attack.
        for index, overlap in enumerate(self.board[row]):  # The overlap count isn't used, but this style of loop is
            # faster than a for-in-range loop.
            # This redundantly covers the queen itself's square, but that doesn't matter and avoiding it would be
            # less efficient than not avoiding it
            self.board[row][index] += addsub
            self.board[index][col] += addsub

        # This handles the diagonals the queen can attack.
        # This is how far away, diagonally, any square requiring an update can be.
        for i in range(1, max(row, col, self.size - row - 1, self.size - col - 1)+1):
            if row - i >= 0:
                if col - i >= 0:  # Top left
                    self.board[row - i][col - i] += addsub
                if col + i < self.size:  # Top right
                    self.board[row - i][col + i] += addsub
            if row + i < self.size:
                if col - i >= 0:  # Bottom left
                    self.board[row + i][col - i] += addsub
                if col + i < self.size:  # Bottom right
                    self.board[row + i][col + i] += addsub
    