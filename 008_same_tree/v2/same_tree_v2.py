from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def valid(p: Optional[TreeNode], q: Optional[TreeNode]):

            # If both nodes are None, they're the same
            if not p and not q:
                return True
            # If one node is None, they're not the same
            if not p or not q:
                return False
            # If the two nodes have different values, they're not the same
            return p.val == q.val

        # The queue to iterate over
        dq = deque([(p, q)])

        # While dq has any contents
        while dq:
            # Pop a pair of nodes and see if they're the same
            p, q = dq.popleft()
            if not valid(p, q):
                return False
            if p:  # If p (and therefore q, too) aren't None
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))
        return True
