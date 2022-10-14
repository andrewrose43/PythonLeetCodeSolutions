from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def _backtrack(combo: list, start: int):

            if len(combo) == k:
                return_list.append(combo[:])
                return

            for i in range(start, n+1):
                combo.append(i)
                _backtrack(combo, i+1)
                combo.pop()

        return_list = []
        _backtrack([], 1)
        return return_list
