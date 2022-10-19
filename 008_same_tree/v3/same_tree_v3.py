from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # The queue to iterate over
        dq = deque([(p, q)])

        # While dq has any contents
        while dq:
            # Pop a pair of nodes and see if they're the same
            p, q = dq.popleft()
            if bool(p) ^ bool(q):  # If one of these exists and the other doesn't
                return False
            if p and q and p.val != q.val:  # If the two have different values
                return False
            if p:  # If p (and therefore q, too) aren't None
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))
        return True
