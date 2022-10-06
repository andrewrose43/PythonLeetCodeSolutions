class Solution:

    def totalNQueens(self, n: int) -> int:
        cols = set()  # Hash table tracking which columns are occupied
        diags = set()  # Hash table tracking which diagonals are occupied
        adiags = set()  # Hash table tracking which anti-diagonals are occupied
        count = 0
        return self._totalNQueens(0, cols, n, diags, adiags, count)

    def _totalNQueens(self, row, cols, n, diags, adiags, count) -> int:

        for col in range(n):
            # Check whether this square is free of attacking queens
            if not col in cols and not row - col in diags and not row + col in adiags:
                if row == n - 1:  # If this is the last row
                    return count + 1
                # else, add the column, diagonal, and anti-diagonal to their respective sets
                cols.add(col)
                diags.add(row - col)
                adiags.add(row + col)
                count = self._totalNQueens(row + 1, cols, n, diags, adiags, count)
                # Clean up the board; remove the queen
                cols.remove(col)
                diags.remove(row - col)
                adiags.remove(row + col)
        return count
