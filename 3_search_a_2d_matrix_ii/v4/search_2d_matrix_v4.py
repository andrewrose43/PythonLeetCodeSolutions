from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def _binsearch(matrix: list[list[int]], target: int, row: int, left: int, right: int):
            curr = left+(right-left)//2
            while left <= right and matrix[row][curr] != target:
                if target < matrix[row][curr]:
                    right = curr-1
                else:
                    left = curr+1
                curr = left+(right-left)//2 if left <= right else left  # Weird logic ensures correct out-of-bounds
                # behaviour on the right side
            pass
            return max(curr, 0) # max function because curr could be -1, which would break the logic
            # note that curr can be out of bounds to the right of the matrix; this is intentional

        def _searchMatrix(matrix: list[list[int]], target: int, up: int, down: int, left: int, right: int):

            # base case: matrix has no length and/or width
            if up > down or left > right:
                return False

            # discard any submatrix with all its values less than or greater than the target
            if matrix[up][left] > target or matrix[down][right] < target:
                return False

            # Find pivot!
            pivot_row = down+(up-down)//2
            pivot_col = _binsearch(matrix, target, pivot_row, left, right)
            if pivot_col < len(matrix[0]) and matrix[pivot_row][pivot_col] == target:
                return True

            # recurse!
            # 1) top right; 2) bottom left
            return _searchMatrix(matrix, target, up, pivot_row-1, pivot_col, right)\
                or\
                _searchMatrix(matrix, target, pivot_row+1, down, left, pivot_col-1)

        return _searchMatrix(matrix, target, 0, len(matrix)-1, 0, len(matrix[0])-1)
