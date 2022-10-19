
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # If both nodes are None, they're the same
        if not p and not q:
            return True
        # If one node is None, they're not the same
        if not p or not q:
            return False
        # If the two nodes have different values, they're not the same
        if p.val != q.val:
            return False

        # Check both children of each of p and q
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
