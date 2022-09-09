from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def _isValidBST(root: TreeNode, lo=-math.inf, hi=math.inf) -> bool:

            # Empty = valid
            if not root:
                return True

            # This node's value must be within bounds
            if lo < root.val < hi:
                return _isValidBST(root.left, lo, root.val) and _isValidBST(root.right, root.val, hi)

            # If neither condition was met, the tree is invalid
            return False

        return _isValidBST(root)