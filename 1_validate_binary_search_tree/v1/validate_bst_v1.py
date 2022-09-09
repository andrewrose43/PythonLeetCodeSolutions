from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def _isValidBST(root: Optional[TreeNode], lo: int, hi: int):
            if root is None:
                return True
            if (
                (root.left is None or lo < root.left.val < root.val)
                and
                (root.right is None or root.val < root.right.val < hi)
            ):
                return _isValidBST(root.left, lo, root.val) and _isValidBST(root.right, root.val, hi)

            return False

        return _isValidBST(root, -2147483648-1, 2147483648+1)
