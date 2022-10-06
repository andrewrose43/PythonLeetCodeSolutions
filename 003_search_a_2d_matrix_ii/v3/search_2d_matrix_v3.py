from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def _searchMatrix(matrix: list[list[int]], target: int, up: int, down: int, left: int, right: int):

            # base case: this submatrix has no width and/or no length
            if up > down or left > right:
                return False

            # discard any submatrix whose values are all smaller or larger than the target
            if target > matrix[down][right] or target < matrix[up][left]:
                return False

            # divide: find a pivot that's the first in its row to be greater than the target
            # If you find the target, return True
            # Then recurse on the top-right and bottom-left submatrices
            pivot_row = up+(down-up)//2
            pivot_col = left
            # Proceed until you're out of bounds OR the pivot >= the target
            while pivot_col <= right and matrix[pivot_row][pivot_col] <= target:
                if matrix[pivot_row][pivot_col] == target:
                    return True
                pivot_col += 1  # Note that pivot_col can end the loop beyond the bounds of the matrix
                # That's intentional: we don't need to check above the rightmost item if it's smaller than target

            # return _sM(bottom left_ or _sM(top right)
            return _searchMatrix(matrix, target, pivot_row+1, down, left, pivot_col-1)\
                or\
                _searchMatrix(matrix, target, up, pivot_row-1, pivot_col, right)

        return _searchMatrix(matrix, target, 0, len(matrix)-1, 0, len(matrix[0])-1)