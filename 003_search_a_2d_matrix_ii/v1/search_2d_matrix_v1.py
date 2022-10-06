from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def _search_matrix(matrix: list[list[int]], target: int, lo_row: int, hi_row: int, lo_col: int, hi_col: int) -> bool:

            # Base case 1: not found
            if lo_col > hi_col or lo_row > hi_row:
                return False

            # Calculate pivot coordinates just once for reuse
            pivot_row = (hi_row-lo_row)//2+lo_row
            pivot_col = (hi_col-lo_col)//2+lo_col

            # Base case 2: found
            pivot = matrix[pivot_row][pivot_col]
            if target == pivot:
                return True

            # To stop infinite recursion.
            if lo_col == hi_col and lo_row == hi_row:
                return False

            # Divide and conquer
            if _search_matrix(matrix, target, lo_row, pivot_row, pivot_col+1, hi_col): # top right
                return True
            if _search_matrix(matrix, target, pivot_row+1, hi_row, lo_col, pivot_col): # bottom left
                return True
            if target > pivot:
                return _search_matrix(matrix, target, pivot_row+1, hi_row, pivot_col+1, hi_col) # bottom right
            # else target < pivot; return top-left search results
            return _search_matrix(matrix, target, lo_row, pivot_row, lo_col, pivot_col)

        return _search_matrix(matrix=matrix, target=target, lo_row=0, hi_row=len(matrix)-1, lo_col=0, hi_col=len(matrix[0])-1)
