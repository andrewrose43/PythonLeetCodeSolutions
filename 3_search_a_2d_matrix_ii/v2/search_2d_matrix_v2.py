from typing import List

# This version DOES NOT WORK! See v3 for a working version of this concept.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def _binsearch(matrix, target, row, lo, hi) -> int:

            while lo < hi:
                curr_col = lo + (hi - lo) // 2  # Current column: halfway between extremes. It's binsearch.
                if matrix[row][curr_col] == target:  # Found!
                    return curr_col
                if matrix[row][curr_col] > target:
                    hi = curr_col - 1
                else:
                    lo = curr_col + 1

            # Return the target, the index of a value greater than the target, or, if there are neither of those in
            # this row, the rightmost column's index.
            return lo + 1 if (matrix[row][lo] < target and lo < len(matrix[row]) - 1) else lo


        def _searchMatrix(matrix: list[list[int]], target: int, lo_row: int, hi_row: int, lo_col: int,
                          hi_col: int) -> bool:

            # Not found
            if lo_row > hi_row or lo_col > hi_col:
                return False

            # if matrix[/2][binsearch_result] == target: return True
            pivot_row = lo_row + (hi_row - lo_row) // 2
            pivot_col = _binsearch(matrix, target, pivot_row, lo_col, hi_col)

            # Found!
            if target == matrix[pivot_row][pivot_col]:
                return True

            # Not found. This is the case where you're down to 1 item and it's not the target.
            if lo_row == hi_row and lo_col == hi_col:
                return False

            # return top right or bottom left results
            return (_searchMatrix(matrix, target, lo_row, pivot_row - 1, pivot_col, hi_col)
                    or
                    _searchMatrix(matrix, target, pivot_row + 1, hi_row, lo_col, pivot_col - 1))

        return _searchMatrix(matrix, target, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
