from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        output = []  # The list to be returned
        j = 0  # Tracks the current position being modified in the current sublist

        curr = list(range(1, k+1)) + [n+1]  # The final item is the sentinel, which is not part of the combinations.
        # The sentinel serves to stop the inner while loop once each combination has been generated.
        # The sentinel's size is arbitrary; any number equal to or greater than n+1 would work.

        while j < k:

            j = 0
            output.append(curr[:k])  # Store the current combination; don't store the sentinel

            while j < k and curr[j+1] == curr[j]+1:  # While the next item is just one larger than the current item
                curr[j] = j+1  # Set the array to 1, 2, 3, ...
                j += 1

            curr[j] += 1  # If the next value is more than one greater than this one, increment this one

        return output
