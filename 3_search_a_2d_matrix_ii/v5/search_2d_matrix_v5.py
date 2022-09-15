from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Note: the constraints of the problem guaranteed that the input is not empty.
        # So there's no need to guard against that possibility.

        # Start at top right corner.
        row = 0
        col = len(matrix[0])-1

        # Cache this so we don't have to call len() repeatedly.
        height = len(matrix)

        # Traverse!
        while row < height and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False
