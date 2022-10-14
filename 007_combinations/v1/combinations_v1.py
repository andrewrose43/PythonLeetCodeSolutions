from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        return_list = []

        def _backtrack(k_minus: int, combo: list[int], curr_int: int):

            if k_minus == 0:
                return_list.append(combo + [curr_int])
                return

            for next_int in range(curr_int+1, n+1):
                if n - next_int + 1 >= k_minus:  # if there are at least k numbers left to choose from, try k more append operations
                    _backtrack(k_minus-1, combo + [curr_int], next_int)

        # Start backtracking on every possible starting point
        # +1 for inclusive range; +1 because k>=1; add those, and you get +2
        for i in range(1, n+2-k):
            _backtrack(k-1, [], i)  # k-1 because one has been chosen already

        return return_list
