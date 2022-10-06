class Solution:
    def totalNQueens(self, n: int) -> int:

        def _totalNQueens(row, cols, diags, adiags):

            # Variable to track added queens
            count = 0
            for col in range(n):
                # Cache the diagonal and anti-diagonal for speed.
                diag = row-col
                adiag = row+col

                if col not in cols and diag not in diags and adiag not in adiags:

                    # Last row?
                    if row == n-1:
                        return 1
                    # Not last row.
                    cols.add(col)
                    diags.add(diag)
                    adiags.add(adiag)
                    count += _totalNQueens(row+1, cols, diags, adiags)
                    cols.remove(col)
                    diags.remove(diag)
                    adiags.remove(adiag)

            return count

        return _totalNQueens(0, set(), set(), set())